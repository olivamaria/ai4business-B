---
name: gera-briefing
description: Antes de uma conversa importante da Maria (reunião com a Samba, orientador da LSB, banca, cliente, etc.), lê o contexto vigente deste repositório e monta um briefing com pauta, perguntas críticas e uma checklist do que não esquecer — adotando postura cética, crítica e detalhista em vez de só resumir o que já está escrito. Use esta skill sempre que a Maria pedir para preparar uma reunião, montar uma pauta, levantar perguntas para uma conversa, ou disser algo como "tenho uma reunião importante", "preciso me preparar para falar com a Samba", "monta um briefing", "quais perguntas eu deveria fazer", ou o comando /gera-briefing. Não use para revisar o conteúdo do repo em si (isso é a skill revisa-repo) nem para gerar o processo de precificação (isso segue o fluxo de prompts/).
---

# Gerar briefing antes de uma conversa importante

## Por que essa skill existe

O valor real de uma reunião não vem de "ter uma pauta" — vem de sair dela com as perguntas certas respondidas e nenhuma decisão adiada por falta de coragem de perguntar. Este repositório já documenta, de forma explícita, tudo que ainda é hipótese ("não confirmado internamente") e tudo que ainda está em aberto. Essa é a matéria-prima mais valiosa para um briefing: não é genérico, é específico ao estado real do projeto agora.

Esta skill não deve produzir um resumo educado do que já se sabe. Deve produzir o material que uma pessoa cética, crítica e detalhista levaria para a sala — alguém que desconfia de afirmações não sustentadas, testa hipóteses em vez de aceitá-las, e não sai da sala sem uma resposta concreta para o que estava em aberto.

## Passo 0: entender a conversa antes de escrever qualquer coisa

Um briefing genérico não serve. Antes de montar qualquer coisa, você precisa saber — pergunte à Maria diretamente no chat se ela não tiver dito isso já:

1. **Com quem é a conversa** — liderança da Samba, time Criativo, time Account, orientador(a) da LSB, banca, cliente, outro. O papel da audiência muda o que vale perguntar (o Criativo não vai saber responder sobre modelo de negócio; a liderança pode não saber o detalhe operacional do handoff).
2. **Qual é o objetivo dela** — validar uma hipótese, apresentar um resultado, pedir aprovação/decisão, levantar dados que faltam, resolver um impasse. Sem objetivo claro, a pauta vira uma lista de tópicos soltos.
3. **Quanto tempo dura e se já existe pauta enviada pelo outro lado** — isso define quantos itens cabem e se algo já está fora de escopo para essa conversa específica.
4. **Algum tema específico que a Maria já sabe que precisa entrar** — não deixe de perguntar isso; ela pode ter contexto de bastidor que não está em nenhum arquivo do repo.

Não assuma essas respostas para economizar uma pergunta — o custo de um briefing errado (perguntas para a audiência errada, tempo mal calculado) é maior que o custo de perguntar antes.

## Passo 1: releia o terreno, não confie na memória

Antes de escrever qualquer pergunta, releia o estado real e atual do repositório (ele muda entre conversas):

1. [`problema.md`](../../../problema.md) — o problema âncora: quem sofre, estado atual, mudança desejada, critérios de sucesso.
2. [`contexto/sobre-mim.md`](../../../contexto/sobre-mim.md), [`contexto/negocio.md`](../../../contexto/negocio.md), [`contexto/cliente.md`](../../../contexto/cliente.md) — fundação de negócio e as perguntas em aberto que cada um já registra explicitamente.
3. [`contexto/processo-precificacao.md`](../../../contexto/processo-precificacao.md) — a versão vigente do processo, incluindo a seção "O que mudou em relação à versão anterior" (mostra o que foi decidido recentemente e pode precisar de validação).
4. Qualquer arquivo novo no repo que não esteja descrito acima (ex: pastas como `institucional/`) — se for relevante para a audiência da conversa, releia também.

Durante essa leitura, mantenha duas listas à parte:
- **Fatos e decisões já fechadas** (não vale gastar tempo de reunião perguntando sobre isso — mas vale mencionar como contexto rápido).
- **Toda ocorrência de "não confirmado internamente"** ou equivalente, e toda frase que soa como afirmação mas não tem lastro (isso é a lista de candidatos a pergunta).

## Passo 2: adote a postura cética, crítica e detalhista

Isso é o que diferencia um briefing útil de uma lista de tópicos. Para cada hipótese, decisão ou afirmação relevante à conversa, aplique este teste antes de aceitar:

- **"Como sabemos isso?"** — se a resposta é "foi inferido" ou "parece razoável", isso não é fato, é hipótese disfarçada — vira pergunta, não vira pauta informativa.
- **"O que acontece se isso estiver errado?"** — para cada hipótese com impacto real no processo (ex: modelo de cobrança, tempo médio do ciclo, causa da lentidão), pergunte-se qual decisão desmorona se a premissa cair. Essas são as perguntas de maior prioridade — priorize-as no topo.
- **Contradições entre arquivos** — se `negocio.md` e `processo-precificacao.md` sugerem coisas diferentes sobre o mesmo ponto, isso não se resolve sozinho lendo mais: vira pergunta explícita para a reunião.
- **O que foi decidido por omissão** — uma seção que não menciona um cenário óbvio (ex: o que acontece se o orçamento estourar o prazo combinado) não significa que o cenário não existe; geralmente significa que ninguém decidiu ainda. Traga isso à tona em vez de deixar por baixo do tapete.
- **Objeções prováveis da audiência** — pense do ponto de vista de quem vai ouvir: o que nessa proposta/processo eles vão questionar primeiro? Antecipe isso e prepare a Maria com a resposta ou, se não houver resposta ainda, marque como risco a admitir na reunião em vez de tentar defender algo frágil.
- **Perguntas fechadas > perguntas abertas** quando o objetivo é decisão. "O Account valida prazos com o cliente ou é o Criativo quem faz isso hoje?" gera uma resposta acionável; "como vocês veem o processo?" não gera.

Não amoleça isso para ser "gentil" com o conteúdo do repo — o objetivo da skill é proteger a Maria de entrar despreparada, não validar o que já foi escrito.

## Passo 3: monte o briefing

Organize por utilidade em sala, não por ordem de leitura dos arquivos. Use este formato:

```markdown
# Briefing — [nome da conversa] — [data]

## Com quem e por quê
[audiência, papel de cada participante se souber, objetivo declarado da conversa, tempo disponível]

## Contexto rápido (o que já é fato, não precisa reabrir)
- [fato 1, com fonte: arquivo.md]
- [fato 2, ...]

## O que ainda é hipótese (não confirmado) e por que importa
- **[hipótese]** (fonte: arquivo.md) — o que muda se isso for falso: [...]

## Pauta proposta
1. [item, com tempo estimado se relevante]
2. [...]
[a pauta deve terminar em algo que gera decisão ou próximo passo — nunca só "alinhamento"]

## Perguntas críticas
### Para validar hipóteses em aberto
- [pergunta fechada e específica]

### Para destravar decisões pendentes
- [pergunta]

### Para testar riscos/objeções prováveis
- [pergunta]

## Riscos e objeções que a Maria deve antecipar
- **[objeção provável]** — [como responder, ou "ainda não temos resposta — admitir e propor prazo para trazer"]

## O que não esquecer
- [ ] [item concreto: levar/mostrar algo, confirmar algo antes de entrar, decisão que não pode sair da sala sem dono e prazo]
- [ ] [...]

## Depois da reunião
- [ ] Atualizar `contexto/*.md` ou `processo-precificacao.md` com o que foi confirmado/decidido
- [ ] [outros follow-ups específicos]
```

## Regras a manter (herdadas das convenções do repo)

- **Nunca converta uma hipótese "não confirmada" em fato dentro do briefing** só porque ela soa plausível — o briefing existe justamente para testar essas hipóteses na conversa, não para blindá-las.
- **Nunca invente valores reais** (custos, margens, prazos exatos da Samba) que não estejam nos arquivos — se um número é necessário para uma pergunta, use as faixas simbólicas (`$` a `$$$$`) ou pergunte o valor real como parte da pauta.
- **Escopo**: não proponha, dentro do briefing, que o Criativo assuma julgamento financeiro nem sugira ferramenta complexa — isso contradiz o princípio central do processo e não deve aparecer nem como pergunta neutra ("vocês considerariam...") disfarçando uma proposta fora de escopo.
- Depois de montar o briefing, feche com uma frase direta: qual é a pergunta mais importante da lista inteira — a que, se não for feita, torna a reunião um desperdício. Isso ajuda a Maria a priorizar se o tempo apertar.
