# Fonte canônica

O lugar combinado onde o dado verdadeiro mora. Duas visões da mesma base são legítimas; duas bases não são.

## Qual é a fonte

**[amostra.csv](amostra.csv)** — 12 pedidos, extraídos do FakeERP em 21/09/2026, cobrindo todos os meses de 2026 que a base tem: janeiro, fevereiro, março e julho.

**Esta não é a base da Agência Samba.** É a base de treino da disciplina, documentada em [../fake-erp.md](../fake-erp.md) — o caminho C previsto na aula.

A escolha é declarada, não disfarçada. O ciclo de precificação da Samba não é medido hoje: não existe registro de quando cada projeto foi fechado nem de quando o orçamento foi liberado (ver [../problema.md](../problema.md)). Não há CSV real a exportar porque não há medição a exportar — essa ausência é o problema, não um contratempo.

O que esta fonte permite exercitar é a mecânica: declarar a regra de cálculo antes do número, e ter um lugar só de onde todo mundo lê.

### Por que esta base serve como ensaio

Os três estados de pedido mapeiam nos três estados de um projeto da Samba:

| `status` no CSV | O equivalente na Samba |
|---|---|
| `PAID` | projeto faturado |
| `PENDING` | escopo entregue, orçamento aguardando liberação — o gargalo |
| `CANCELLED` | projeto que caiu depois de ganho, com trabalho já feito |

## Onde vive e quem atualiza

| Pergunta | Resposta |
|---|---|
| **Onde vive** | CSV no repositório, em `dados/amostra.csv` |
| **Quem escreve nela** | ninguém escreve à mão. É reextraída do FakeERP via [../fake-erp.md](../fake-erp.md) |
| **Com que frequência** | sob demanda, quando as regras rodam |
| **Como eu percebo que está desatualizada** | o rodapé do [../painel.html](../painel.html) mostra a data da última extração. Acima de 30 dias, reextrair antes de confiar em qualquer número |
| **O que quebra** | a base é de treino e pode ser resetada pelos professores sem aviso. Se a contagem de linhas mudar sem extração nova, a fonte mudou embaixo do painel |

## Sanitização

Regra aplicada em 21/09/2026: **nenhuma substituição foi necessária.**

A fonte não contém nome de pessoa, telefone, e-mail, CPF, CNPJ nem endereço — as seis colunas são `pedido_id`, `data`, `valor`, `desconto`, `total` e `status`, todas não identificáveis. O `pedido_id` já é um identificador sequencial, que é exatamente o formato que a regra de sanitização pede.

Quando a fonte real da Samba entrar, a substituição será necessária: nome de cliente vira `CLI-001`, mantendo o mesmo identificador para o mesmo cliente.

---

## Os três números

Um de volume, um de dinheiro, um de qualidade. A regra de cálculo importa mais do que o nome do número.

### 1. Pedidos no mês — volume

**Definição:** contagem de linhas de `amostra.csv` cuja `data` cai no mês, **incluindo** as de status `CANCELLED` e `PENDING`.

**Por que inclui cancelado:** este número mede trabalho realizado, não dinheiro. Um projeto que caiu depois de ganho consumiu criação, cotação e conceito — some do faturamento, mas não some do esforço. Tirá-lo daqui esconderia justamente o retrabalho que o projeto quer enxergar.

### 2. Receita paga no mês — dinheiro

**Definição:** soma da coluna `total` apenas das linhas com `status == "PAID"`. Exclui `CANCELLED` e `PENDING`.

**O que este número não é:** não é o `totalAmount` que a API do FakeERP devolve. Aquele campo soma tudo, inclusive cancelado e pendente. Em janeiro de 2026 a diferença é de R$ 1.425,00 — `totalAmount` diz R$ 2.855,00, receita paga diz R$ 1.430,00.

Nenhum dos dois está errado. O comercial conta pedido fechado, o financeiro conta dinheiro que entrou. É por isso que a regra precisa estar escrita aqui e não na cabeça de quem monta a planilha.

### 3. Fatia parada aguardando aprovação — qualidade

**Definição:** soma da coluna `total` das linhas com `status == "PENDING"`, dividida pela soma de `total` de **todas** as linhas do mês, em percentual.

**Por que este é o número de qualidade e não o ticket médio:** ele mede escopo já entregue cujo dinheiro ainda não foi liberado. É o intervalo entre "ganhamos a concorrência" e "orçamento aprovado e liberado" do [../problema.md](../problema.md), expresso como proporção do mês. Ticket médio diria o tamanho do pedido; este diz o quanto da operação está travada esperando alguém assinar.

**O denominador inclui cancelado** de propósito, para bater exatamente com a Regra 2 de [../regras.md](../regras.md). Duas definições diferentes para o mesmo conceito, em dois arquivos do mesmo repositório, recriariam a briga de planilha que esta fonte existe para evitar.

---

## FALTA DEFINIR

Cada item abaixo é uma decisão de negócio da Samba que ainda não foi tomada. Enquanto estiverem em aberto, os três números só rodam sobre a base de ensaio.

- **FALTA DEFINIR** — o que conta como "projeto" na contagem de volume: um contrato assinado, uma concorrência vencida, ou uma frente dentro de um projeto grande? Os seis projetos do Rock in Rio são seis ou é um?
- **FALTA DEFINIR** — em que momento a receita de um projeto é reconhecida: na assinatura, no faturamento, no recebimento, ou por medição ao longo da produção?
- **FALTA DEFINIR** — se o relógio de "aguardando aprovação" conta dias corridos ou úteis, e como as pausas declaradas em [../problema.md](../problema.md) entram na conta.
- **FALTA DEFINIR** — qual é o valor de corte que aciona a aprovação da Holding Clube, e se esse tempo entra no número ou é medido à parte.
