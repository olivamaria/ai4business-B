# Regras

As regras que a operação vigia, fora da cabeça das pessoas. Cada uma diz quando é olhada, sobre qual dado, o que precisa ser verdade para agir, o que acontece, quem abre e o que fica registrado quando está tudo bem.

## Sobre a fonte usada hoje

Estas regras rodam sobre o **FakeERP**, a base de treino da disciplina, documentada em [fake-erp.md](fake-erp.md). Não é dado da Agência Samba, e isso está declarado também em [dados/fonte.md](dados/fonte.md).

A escolha é deliberada, não um atalho. O processo de precificação da Samba **não é medido hoje** — não existe registro de quando cada projeto foi fechado nem de quando o orçamento foi liberado (ver [problema.md](problema.md), seção "O resultado que eu quero"). Escrever regra sobre um dado que não existe produziria uma regra que nunca dispara, que é o mesmo que não ter regra.

O FakeERP serve porque a tensão dele é a mesma da Samba. Três estados de pedido que mapeiam direto no problema:

| FakeERP | O equivalente na Samba |
|---|---|
| `PAID` | projeto faturado, dinheiro reconhecido |
| `PENDING` | escopo entregue, orçamento aguardando liberação — **o gargalo do [problema.md](problema.md)** |
| `CANCELLED` | projeto que caiu depois de ganho, com trabalho já feito |

Por isso cada regra abaixo tem um campo a mais que os sete: **o que ela vigia no processo da Samba**, e o que precisaria existir para ela rodar sobre dado real. Quando a fonte da Samba existir, muda a Fonte e a Condição de cada regra — o resto do arquivo continua valendo.

---

## Regra zero — vale para todas as regras abaixo

> **Se a fonte não existir ou vier vazia, escreva "FONTE INDISPONÍVEL" e pare. Nunca invente número. Sempre me diga quantas linhas leu e quantas ignorou, e por quê.**

Acrescentada em 21/09/2026, depois dos testes registrados em [testes.md](testes.md). Antes dela, as três regras ficavam caladas em mês sem dado exatamente como ficariam em mês tranquilo — e o silêncio de uma regra quebrada é idêntico ao de uma regra saudável.

Duas situações que esta frase cobre e que já foram observadas de verdade:

- O FakeERP devolve **HTTP 200 com `count: 0`** para mês sem pedido. Não é erro: é ausência de dado com aparência de normalidade.
- O gatilho das regras diz "mês corrente". De setembro de 2026 em diante a base não tem pedido nenhum, então as regras rodariam toda segunda sem nunca disparar, e sem nunca acusar.

---

## Regra 1 — Projeto que cai depois de fechado

| Campo | |
|---|---|
| **Gatilho** | tempo. Toda segunda-feira, rodada à mão (não há rotina agendada — ver [automacoes.md](automacoes.md)) |
| **Fonte** | FakeERP, `GET /report/{ano}/{mes}` do mês corrente, via [fake-erp.md](fake-erp.md) |
| **Condição** | existir no mês ao menos um pedido com `status == "CANCELLED"` cujo `total` seja **maior que R$ 200,00** |
| **Ação** | escrever alerta em `alertas/AAAA-MM-DD.md` com o `orderId`, o valor e a data do cancelamento, e quanto o mês perdeu somando todos os cancelados |
| **Quem recebe** | Maria (Atendimento/Comercial). Nos 10 minutos seguintes: abre o alerta, identifica o pedido e registra o motivo do cancelamento — é o motivo, não o valor, que diz se há padrão |
| **Se não disparar** | gravar em [automacoes.md](automacoes.md) a data, o maior cancelado do mês e quantos pedidos foram olhados |

**O que vigia no processo da Samba:** trabalho perdido depois de a agência já ter ganho a concorrência. Hoje, quando um projeto cai depois de fechado, o custo já incorrido — horas de criação, cotação, conceito — não é somado em lugar nenhum. A regra existe para esse valor parar de sumir.

**Para rodar sobre dado real:** um registro por projeto com data de fechamento, status e o esforço já gasto quando ele caiu.

**Por que R$ 200,00:** abaixo disso o cancelamento não paga o tempo de investigar. Testado sobre os quatro meses com dado na base: dispara em 2 deles.

---

## Regra 2 — Fatia do mês parada aguardando aprovação

| Campo | |
|---|---|
| **Gatilho** | tempo. Toda segunda-feira, rodada à mão |
| **Fonte** | FakeERP, `GET /report/{ano}/{mes}` do mês corrente, via [fake-erp.md](fake-erp.md) |
| **Condição** | a soma de `total` dos pedidos com `status == "PENDING"` representar **mais de 25% do `totalAmount` do mês** |
| **Ação** | escrever alerta em `alertas/AAAA-MM-DD.md` com o percentual, o valor parado, quantos pedidos são, e o mais antigo deles pela `orderDateTime` |
| **Quem recebe** | Maria (Atendimento/Comercial). Nos 10 minutos seguintes: pega o pedido mais antigo da lista e descobre em quem a bola está parada |
| **Se não disparar** | gravar em [automacoes.md](automacoes.md) a data, o percentual apurado e quantos pedidos foram olhados |

**O que vigia no processo da Samba:** é a regra mais importante deste arquivo. Ela mede escopo já entregue cujo dinheiro ainda não foi liberado — exatamente o intervalo entre "ganhamos a concorrência" e "orçamento aprovado e liberado" que o [problema.md](problema.md) quer encurtar. Um mês com fatia grande parada em aprovação é o sintoma numérico do gargalo que hoje só se percebe pela sensação de que "está demorando".

**Para rodar sobre dado real:** o `dados/amostra.csv` com um projeto por linha, data de fechamento, data de liberação do orçamento e o estado das pausas do relógio (ver [problema.md](problema.md), "A regra de contagem: o relógio pausa"). Com isso, a condição deixa de ser percentual de valor e passa a ser dias de ciclo acima do teto de 6 semanas.

**Por que 25%:** testado sobre os quatro meses com dado: dispara em 1 deles. Março de 2026 tem pendente de verdade, mas a 17,9% — fica calada com dado na mesa, que é o comportamento desejado. Um limite de 15% faria a regra disparar quase sempre e virar ruído.

---

## Regra 3 — Receita reconhecida abaixo do piso

| Campo | |
|---|---|
| **Gatilho** | tempo. Toda segunda-feira, rodada à mão |
| **Fonte** | FakeERP, `GET /report/{ano}/{mes}` do mês corrente, via [fake-erp.md](fake-erp.md) |
| **Condição** | a **receita paga** do mês ficar **abaixo de R$ 2.000,00**. Receita paga soma o `total` apenas dos pedidos com `status == "PAID"` — ignora cancelado e pendente, e **não** é o `totalAmount` que a API devolve |
| **Ação** | escrever alerta em `alertas/AAAA-MM-DD.md` com a receita paga, o `totalAmount` ao lado, e a diferença entre os dois explicada por status |
| **Quem recebe** | Maria (Atendimento/Comercial). Nos 10 minutos seguintes: confere se a diferença vem de cancelamento (perda) ou de pendência (atraso) — são dois problemas diferentes com donos diferentes |
| **Se não disparar** | gravar em [automacoes.md](automacoes.md) a data, a receita paga apurada e quantos pedidos foram olhados |

**O que vigia no processo da Samba:** a distância entre o número do comercial e o número do financeiro. A API entrega R$ 2.855,00 para janeiro; a receita reconhecida é R$ 1.430,00. Nenhum dos dois está errado — eles respondem perguntas diferentes, e é por isso que a reunião começa discutindo planilha. A regra só funciona porque a definição de "receita paga" está escrita neste arquivo. A API não a conhece.

**Para rodar sobre dado real:** a definição equivalente na Samba — o que conta como receita reconhecida de um projeto, e em que momento — escrita em [dados/fonte.md](dados/fonte.md) antes de virar condição.

**Por que R$ 2.000,00:** testado sobre os quatro meses com dado: dispara em 2 deles.

---

## O que não está escrito aqui e deveria estar

- Nenhuma regra vigia **tempo de ciclo em dias**, que é a métrica declarada no [problema.md](problema.md). Não dá para escrever: a fonte não tem data de fechamento nem de liberação. É a primeira regra a nascer quando a amostra da Samba existir.
- Nenhuma regra distingue **mês sem dado** de **mês que não bateu a condição**. As duas situações produzem silêncio idêntico visto de fora, e por isso o campo "Se não disparar" registra sempre quantos pedidos foram olhados — zero pedidos olhados é ausência de dado, não é tudo bem.
