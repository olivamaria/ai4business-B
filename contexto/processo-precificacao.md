# Processo: do conceito criativo à estimativa inicial de custo

## Princípio central

O time criativo não vira time financeiro. Em vez disso, ganha uma **linguagem de custo compartilhada**: um catálogo padronizado de blocos recorrentes de projeto, cada um com uma faixa de custo aproximada e uma sinalização de cobrável/não. Ao montar um conceito, o criativo já o descreve nesses blocos — e o atendimento tem, na hora, uma faixa estimada, sem esperar cotação detalhada de fornecedor.

A ideia não é prever o custo exato. É dar ao criativo um sinal de custo cedo o suficiente pra ele poder ajustar o conceito *antes* de ele virar proposta formal — em vez de descobrir o estouro de orçamento só depois, quando já é retrabalho.

## Pré-requisito: o catálogo de blocos de custo

Levantar com atendimento e produção, usando os projetos em andamento (ex: os 6 do Rock in Rio) como amostra, os elementos recorrentes que aparecem projeto após projeto. Para cada bloco: nome, faixa de custo histórica (pode ser algo simples como $ / $$ / $$$ / $$$$) e se costuma ser cobrável do cliente ou institucional.

Exemplos prováveis de blocos (a validar, não assumir como fato):
- Estrutura física / cenografia
- Tecnologia / interatividade
- Conteúdo e produção audiovisual
- Talent / curadoria musical
- Logística e operação no local
- Staff e equipe de ativação
- Licenciamento / direitos de uso

**Não confirmado internamente:**
- Se já existe alguma base histórica de custos por projeto (ver [negocio.md](negocio.md)) ou se isso precisa ser levantado do zero.
- Se as faixas de custo variam tanto entre projetos (ex: convenção corporativa vs. ativação em festival) que um catálogo único não seria suficiente, exigindo variações por tipo de projeto.

O catálogo pode (e deve) começar pequeno — algo como 8 a 12 blocos — e ser refinado com o uso real, não construído de uma vez de forma exaustiva.

## O processo passo a passo

**Etapa 0 — Samba ganha o cliente** (ponto de partida, como já acontece hoje)

**Etapa 1 — Rascunho do conceito com blocos (Criativo)**
Ao propor o conceito, o criativo o descreve em termos dos blocos do catálogo — não precisa de valor exato, só marcar quais blocos o conceito usa e, por elemento, se é cobrável do cliente ou institucional (ex: "ativação física média + conteúdo audiovisual + tech interativa leve + talent, tudo cobrável do cliente").
→ Resultado: uma **Ficha de Conceito com Estimativa**, simples o bastante pra ser preenchida em minutos, não em reunião.

**Etapa 2 — Faixa automática (Atendimento)**
Atendimento soma as faixas dos blocos escolhidos e tem, no mesmo dia, uma estimativa aproximada (ex: "R$ X a R$ Y"). Isso já permite alinhar expectativa com o cliente cedo, ou levantar a bandeira internamente se o conceito estourou o budget esperado — antes de qualquer trabalho de detalhamento.

**Etapa 3 — Um único checkpoint de validação (Atendimento + Produção)**
Em vez de múltiplas idas e voltas ao longo de semanas, um encontro único entre atendimento e produção valida a faixa com dados reais de fornecedor, ajusta o que for necessário e fecha o orçamento formal.

**Etapa 4 — Orçamento aprovado internamente e liberado pro cliente**

## Por que isso reduz o vai-e-volta

Hoje (ver [problema.md](../problema.md)) o custo só aparece depois que o conceito já foi todo desenhado — o retrabalho acontece porque ninguém sabia, na hora de propor, se aquilo cabia no orçamento. Com o catálogo, o sinal de custo chega junto com a primeira versão do conceito, então o ajuste acontece *antes* de formalizar, e não depois.

Isso também resolve, de forma implícita, o segundo ponto do problema: como cada bloco já é marcado como cobrável ou institucional desde a Etapa 1, essa distinção passa a ficar registrada em algum lugar, em vez de existir só na cabeça de quem está no projeto.

## O que precisa ser validado com o time antes de aplicar

- Quais são, de fato, os blocos recorrentes de custo nos projetos da Samba — levantar com produção, usando os 6 projetos do Rock in Rio como amostra real.
- Se dá pra estabelecer faixas de custo confiáveis com os dados que já existem hoje, ou se é preciso organizar histórico primeiro.
- Quem teria autoridade/conhecimento pra validar as faixas de cada bloco (provavelmente produção + atendimento sênior).
- Se o critério de cobrável/institucional é o mesmo em todo tipo de projeto ou varia por cliente/contrato.

## Próximo passo sugerido

Testar esse processo manualmente em 1–2 dos projetos do Rock in Rio em andamento — mesmo que só com uma planilha simples, sem nenhuma ferramenta nova — pra validar se os blocos e as faixas fazem sentido antes de pensar em qualquer software. Esse teste manual também é o que vai gerar os dados reais pra alimentar o MVP depois.
