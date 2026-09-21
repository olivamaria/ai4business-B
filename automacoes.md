# Automações, acessos e execuções

Registro do que está ligado neste projeto, o que cada coisa faz e o que já rodou. Existe porque daqui a um mês ninguém lembra o que configurou — e automação que roda no escuro quebra em silêncio.

## Acessos e conectores

| O que | Estado | Para que serve neste projeto |
|---|---|---|
| **FakeERP** (API sem conector) | ativo, documentado em [fake-erp.md](fake-erp.md) | fonte de dado de pedidos para as regras. Login JWT, token de 1 hora |
| **Notion** (conector da conta) | conectado na conta Claude | nenhum uso definido neste projeto até agora |
| **Gmail** (conector) | não conectado | — |
| Rotina agendada | nenhuma | as regras rodam à mão, ver seção Execuções |

## Auditoria — manter, consertar, matar

Feita em 18/09/2026.

**MANTER**

- **Acesso ao FakeERP.** Dono: Maria. É a única fonte de dado ligada ao projeto, e é dela que as regras dependem. Devolve tempo no sentido de tornar possível o que antes exigiria pedir relatório a alguém. Saída lida pela própria Maria, ao rodar as regras.

**CONSERTAR**

- **Conector do Notion.** Está conectado na conta, mas nenhum fluxo deste projeto usa. Não está quebrado — está sem função declarada, que é pior, porque parece um ativo e não é. O que falta: decidir se o Notion vira o lugar onde os alertas aparecem (a pessoa já abre o Notion?) ou se o alerta fica em arquivo no repositório. Enquanto essa decisão não for tomada, ele conta como acesso aberto sem dono.

**MATAR**

- Nada. Não há automação abandonada porque ainda não há automação rodando sozinha — o que é uma posição mais honesta do que doze rotinas que ninguém lê.

**Nota sobre a ausência de rotina agendada.** Nenhuma rotina foi agendada neste projeto. As regras rodam à mão e cada execução fica registrada abaixo. Isso é decisão, não pendência: uma regra cuja condição ainda não foi calibrada não deveria rodar sozinha todo dia — ela viraria ruído antes de virar alerta.

## Como eu decido onde gastar esforço

Régua 70-20-10, aplicada a este projeto no estado atual:

- **70% — manter vivo o que a operação usa:** hoje é zero, porque nada está em produção na Samba. À medida que o catálogo de blocos entrar em uso real, é aqui que o esforço migra.
- **20% — melhorar o que já provou valor:** o acesso ao FakeERP e as regras escritas sobre ele.
- **10% — experimento:** o resto.

A leitura desconfortável: um projeto onde 100% do esforço ainda é experimento é um projeto que ainda não entregou nada para a operação. É verdade agora e deixa de ser quando o primeiro experimento do [problema.md](problema.md) rodar.

## Regras ligadas

Arquivo das regras: [regras.md](regras.md) — 3 regras.

| Regra | Fonte | Condição |
|---|---|---|
| 1 — Projeto que cai depois de fechado | FakeERP, relatório do mês | cancelado acima de R$ 200,00 |
| 2 — Fatia do mês parada aguardando aprovação | FakeERP, relatório do mês | pendente acima de 25% do `totalAmount` |
| 3 — Receita reconhecida abaixo do piso | FakeERP, relatório do mês | receita paga abaixo de R$ 2.000,00 |

**Como roda:** à mão, toda segunda-feira. Não há rotina agendada — ver a justificativa na auditoria acima.

**Onde a ação aparece:** arquivo em `alertas/AAAA-MM-DD.md`, no repositório.

## Execuções

| Data | Regra | Fonte | Pedidos olhados | Disparou? | Número que decidiu |
|---|---|---|---|---|---|
| 18/09 | 1 — cancelado | FakeERP 01/2026 | 4 | **sim** | maior cancelado R$ 225,00 |
| 18/09 | 2 — pendente | FakeERP 01/2026 | 4 | **sim** | 42,0% (R$ 1.200,00 de R$ 2.855,00) |
| 18/09 | 3 — receita paga | FakeERP 01/2026 | 4 | **sim** | receita paga R$ 1.430,00 |
| 18/09 | 1 — cancelado | FakeERP 03/2026 | 3 | **sim** | maior cancelado R$ 1.500,00 |
| 18/09 | 2 — pendente | FakeERP 03/2026 | 3 | não | 17,9% (R$ 500,00 de R$ 2.800,00) |
| 18/09 | 3 — receita paga | FakeERP 03/2026 | 3 | **sim** | receita paga R$ 800,00 |
| 18/09 | 1 — cancelado | FakeERP 05/2026 | 0 | não | sem dado |
| 18/09 | 2 — pendente | FakeERP 05/2026 | 0 | não | sem dado |
| 18/09 | 3 — receita paga | FakeERP 05/2026 | 0 | não | sem dado |

Alertas gerados: [alertas/2026-09-18.md](alertas/2026-09-18.md).

### Os dois silêncios não são iguais

A regra 2 ficou calada duas vezes, e pelos motivos opostos:

- **Março:** 3 pedidos olhados, pendente real de R$ 500,00, fatia de 17,9%. A condição foi avaliada e não bateu. Está tudo bem.
- **Maio:** 0 pedidos olhados. A condição não chegou a ser avaliada. Não se sabe se está tudo bem.

Vistos de fora, os dois silêncios são idênticos — é por isso que a coluna "pedidos olhados" existe nesta tabela. Sem ela, uma regra que parou de funcionar pareceria uma regra que não tinha nada a reportar.

## Painel

Arquivo: [painel.html](painel.html), na raiz. Abre com dois cliques, sem servidor e sem internet.

| | |
|---|---|
| **Fonte** | [dados/amostra.csv](dados/amostra.csv), 12 linhas, definições em [dados/fonte.md](dados/fonte.md) |
| **Como é atualizado** | à mão. Reextrair do FakeERP via [fake-erp.md](fake-erp.md), regravar o CSV e regravar o bloco de dados embutido no `painel.html` |
| **Com que frequência** | sob demanda. Não há rotina agendada |
| **Como percebo que envelheceu** | o rodapé do painel mostra a data da extração. Acima de 30 dias, reextrair antes de confiar no número |

**Por que os dados são embutidos no HTML.** O painel carrega o CSV como texto dentro do próprio arquivo, em vez de ler `dados/amostra.csv` em tempo de execução. É deliberado: um arquivo aberto por `file://` não consegue buscar outro arquivo do disco, então ler o CSV exigiria subir um servidor — e um painel que precisa de servidor para abrir é um painel que ninguém abre.

O custo dessa escolha: o CSV e o painel podem divergir. Reextrair o CSV sem regravar o painel deixa o painel mentindo com cara de atualizado. É a primeira coisa a testar no [testes.md](testes.md).

**O que o painel mostra:** os três números de [dados/fonte.md](dados/fonte.md) — pedidos no mês, receita paga, fatia parada aguardando aprovação — com seletor de mês e um alternador entre visão do financeiro e visão do comercial. As duas visões saem do mesmo CSV e chegam a números diferentes de propósito: em janeiro de 2026, R$ 1.430,00 contra R$ 2.855,00.
