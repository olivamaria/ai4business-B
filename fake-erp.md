# FakeERP — como usar esta API

Arquivo de contexto escrito para ser lido pela IA antes de consultar o FakeERP, o ERP de treino da disciplina. Se este arquivo estiver na pasta, não é preciso reexplicar nada: leia daqui e faça a chamada.

## Endereço e documentação

| | |
|---|---|
| **Base** | `https://fake-erp.isilab.com.br` |
| **Documentação (OpenAPI 3.1)** | `https://fake-erp.isilab.com.br/v3/api-docs` |
| **O que a API faz** | login com JWT e relatório de pedidos por ano e mês. Só isso — não há escrita, nem clientes, nem produtos |

## Autenticação

`POST /auth/login`, corpo JSON. **O campo do usuário se chama `login`, não `username`.** É a causa mais comum de 403 aqui.

```bash
TOKEN=$(curl -s -X POST https://fake-erp.isilab.com.br/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"login":"user","password":"user"}' \
  | python3 -c 'import sys,json; print(json.load(sys.stdin)["token"])')
```

Credenciais de treino: login `user`, senha `user`.

A resposta traz `token`, `type` (`Bearer`) e `expiresInMs` — **3600000, ou seja, 1 hora**. Em sessão longa, reautentique em vez de reaproveitar um token antigo.

## Endpoint de relatório

`GET /report/{year}/{month}`, com `Authorization: Bearer <token>`. O mês vai sem zero à esquerda (`/report/2026/1`).

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  https://fake-erp.isilab.com.br/report/2026/1
```

**O que volta:**

| Campo | O que é |
|---|---|
| `count` | quantidade de pedidos no mês |
| `totalValue` | soma dos valores antes do desconto |
| `totalDiscount` | soma dos descontos |
| `totalAmount` | soma dos totais — **de todos os pedidos, inclusive cancelado e pendente** |
| `orders[]` | cada pedido com `orderId`, `orderDateTime`, `value`, `discount`, `total`, `status` |

`status` assume `PAID`, `CANCELLED` ou `PENDING`.

## A armadilha: `totalAmount` não é receita

Este é o ponto que importa mais do que qualquer endpoint.

`totalAmount` soma **tudo**, inclusive o que foi cancelado e o que ainda não foi pago. Quem perguntar "quanto vendemos" e receber `totalAmount` recebe um número que ninguém no financeiro reconhece.

**Receita paga** é uma regra de negócio que a API não conhece e que precisa ser aplicada por fora:

> receita paga = soma de `total` apenas dos pedidos com `status == "PAID"`

Em janeiro de 2026 a diferença é grande: `totalAmount` = R$ 2.855,00, receita paga = R$ 1.430,00. A diferença são um cancelado de R$ 225,00 e um pendente de R$ 1.200,00.

Sempre que a pergunta envolver dinheiro que entrou, use receita paga e diga qual regra foi usada.

## Quais meses têm dados

A base é de treino e a maior parte do ano está vazia. Levantamento feito em 18/09/2026:

| Mês | Pedidos | `totalAmount` | Receita paga | Status presentes |
|---|---|---|---|---|
| 2026-01 | 4 | 2.855,00 | 1.430,00 | 2 PAID, 1 CANCELLED, 1 PENDING |
| 2026-02 | 3 | 3.149,90 | 3.149,90 | 3 PAID |
| 2026-03 | 3 | 2.800,00 | 800,00 | 1 PAID, 1 CANCELLED, 1 PENDING |
| 2026-07 | 2 | 4.300,00 | 4.300,00 | 2 PAID |
| 04, 05, 06, 08 | 0 | 0,00 | 0,00 | — |

Mês vazio devolve HTTP 200 com `count: 0` e `orders: []`. **Não é erro** — é ausência de dado. Uma regra que fica calada nesses meses ficou calada por falta de dado, não porque a condição foi avaliada e não bateu. A distinção importa na hora de registrar execução.

## Erros comuns

Todos os erros de autenticação e autorização devolvem **HTTP 403**, sem corpo explicativo. A API não distingue as causas, então o 403 sozinho não diz o que houve. Testado em 18/09/2026:

| Situação | Resposta |
|---|---|
| Campo `username` em vez de `login` | 403 |
| Senha errada | 403 |
| Chamada sem header `Authorization` | 403 |
| Token inválido ou expirado (mais de 1 hora) | 403 |

**Ordem de verificação diante de um 403:** confira o nome do campo (`login`), depois se o header `Authorization: Bearer` foi enviado, depois a idade do token. Reautenticar resolve a maioria dos casos e custa uma chamada.

## Regras de uso

- **Nunca deduzir número.** Se a resposta da API não estiver em mãos, faça a chamada. Um valor inventado aqui contamina toda regra que depender dele.
- **Não devolver JSON cru** quando a pergunta for de negócio. Devolver a leitura, dizendo de qual mês e qual regra de cálculo.
- **Declarar a regra junto do número.** "Receita paga de janeiro: R$ 1.430,00 (soma dos PAID; exclui 1 cancelado e 1 pendente)" — e não só "R$ 1.430,00".
