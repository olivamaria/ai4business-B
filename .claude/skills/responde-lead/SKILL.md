---
name: responde-lead
description: Monta uma resposta para um lead/interessado nos serviços da Samba (contato recebido por e-mail, WhatsApp, formulário do site, indicação, etc.), no tom da empresa, usando contexto/cliente.md como base de quem é esse comprador e por que ele procura a Samba. Use esta skill sempre que a Maria colar a mensagem de um interessado e pedir para responder, ou disser algo como "responde esse lead", "chegou um contato querendo saber mais", "monta uma resposta pra esse cliente em potencial", "como eu respondo isso", ou o comando /responde-lead. Não use para comunicação interna entre times da Samba (isso é internal-comms) nem para preparar reuniões já confirmadas (isso é gera-briefing) — é especificamente para o primeiro contato ou troca com alguém de fora ainda avaliando contratar a Samba.
---

# Responder um lead interessado nos serviços da Samba

## Por que essa skill existe

O primeiro contato com um interessado é a primeira prova real do posicionamento da Samba — estratégia + criatividade + execução para grandes marcas (ver [negocio.md](../../../contexto/negocio.md)). Uma resposta genérica, de agência qualquer, desperdiça esse contato. Uma resposta que promete prazo ou preço que a própria Samba hoje não consegue cumprir de forma padronizada (ver [problema.md](../../../problema.md) — o ciclo de orçamento varia de semanas a quatro meses) cria expectativa que o processo interno ainda não sustenta. Esta skill existe para produzir uma resposta que soa como a Samba, fala com quem realmente decide do lado do cliente, e não promete o que o processo interno ainda não entrega.

## Passo 0: entender o lead antes de escrever qualquer coisa

Não dá para responder bem sem a mensagem real. Se a Maria ainda não colou o contato, peça:

1. **A mensagem do lead**, na íntegra (e-mail, print de WhatsApp, texto do formulário — como veio).
2. **O canal** — isso muda o registro (e-mail formal vs. WhatsApp mais direto).
3. **O que já se sabe sobre o lead**, se souber: empresa, tipo de projeto que tem em mente, se é um pitch/concorrência formal ou uma conversa exploratória, se já existe alguma relação anterior com a Samba.
4. **Se é a primeira resposta ou a continuação de uma troca já em andamento** — se for continuação, peça também as mensagens anteriores para manter consistência de tom e de informação já passada.

Não invente esses detalhes para economizar uma pergunta.

## Passo 1: releia o terreno

1. [`contexto/cliente.md`](../../../contexto/cliente.md) — quem compra, por que compra, e principalmente as seções marcadas "não confirmado internamente": são hipóteses, não fatos que a resposta pode assumir como verdade sobre o lead à sua frente.
2. [`contexto/negocio.md`](../../../contexto/negocio.md) — o que a Samba vende e como se posiciona (estratégia + criatividade + execução, cases com grandes marcas, projetos altamente customizados). É a matéria-prima da voz da marca.
3. [`problema.md`](../../../problema.md) — para não prometer o que o processo interno de precificação ainda não sustenta (ver Regras abaixo).

## Passo 2: tom de voz — isso ainda não está documentado como fato

Não existe hoje, neste repositório, um arquivo de "tom de voz" ou brand voice confirmado pela Samba. O tom abaixo é **inferido** a partir da linguagem que `negocio.md` já usa para se posicionar — trate como hipótese de estilo, não como regra fechada:

- **Consultivo, não vendedor.** A Samba se vende pela combinação de estratégia + criatividade + execução, não por agressividade comercial. Evite linguagem de venda direta ("aproveite", "oferta", excesso de exclamação).
- **Confiante sem alardear.** Cases com marcas como Coca-Cola, Bradesco, Sephora, Renault falam por si — cite o tipo de trabalho ou a natureza do projeto, não uma lista de nomes como troféu, a menos que a Maria confirme que é apropriado citar aquele cliente específico para aquele lead.
- **Específico ao briefing do lead, não genérico.** Refletir de volta o que o lead pediu (tipo de projeto, marca, ocasião) mostra que a mensagem foi lida de verdade — evite modelo de resposta que serviria para qualquer agência.
- **Direto sobre próximos passos**, sem prometer prazo ou valor que a Samba ainda não consegue padronizar internamente.

Se esta for a primeira vez rodando a skill, pergunte à Maria se esse tom bate com o que a Samba realmente usa — se ela confirmar ou corrigir algo de forma consistente, vale sugerir (não criar sem pedir) um `contexto/tom-de-voz.md` para não precisar reinferir isso toda vez.

## Passo 3: monte a resposta

Adapte o formato ao canal (e-mail pede saudação/fechamento mais formais; WhatsApp é mais direto), mas a lógica é sempre:

```
[Saudação personalizada — nome do lead/empresa se souber]

[Reconhecimento específico do que foi pedido — não um "obrigado pelo contato" genérico]

[Ponte curta para o que a Samba faz que é relevante para ESSE pedido — sem listar todo o portfólio]

[Próximo passo concreto: o que a Samba precisa saber para avançar (briefing, escopo, data, orçamento de referência do lead) e/ou proposta de call — sem prometer prazo fechado de proposta/orçamento]

[Fechamento e assinatura]
```

## Regras a manter

- **Nunca prometa prazo específico de proposta/orçamento.** O próprio processo interno da Samba hoje varia de semanas a quatro meses e não tem padrão claro ainda (ver [problema.md](../../../problema.md)) — prometer "em 3 dias você tem a proposta" cria uma expectativa que a Samba pode não sustentar. Se o lead perguntar prazo, responda com o próximo passo real (ex: "assim que tivermos o briefing completo, te dizemos o prazo") em vez de um número inventado.
- **Nunca invente valores reais** (preço, orçamento mínimo, exemplos de custo). Se for necessário mencionar faixa, use os tiers simbólicos (`$` a `$$$$`) só como referência interna para a Maria decidir a linguagem — não os exponha ao lead assim.
- **Nunca converta uma hipótese de `cliente.md` em fato** ao descrever de volta por que o lead está procurando a Samba — se `cliente.md` diz que não está confirmado o que pesa na decisão do cliente, a resposta não deve afirmar isso como se soubesse.
- **Nunca cite case de cliente específico sem confirmar com a Maria** se aquele nome pode ser mencionado para aquele lead (pode haver conflito de categoria/concorrência, ou o case pode ser confidencial).
- Isto é uma mensagem que vai sair da Samba para alguém de fora — a skill deve produzir o rascunho para a Maria revisar; **não envie a mensagem automaticamente** mesmo que haja uma ferramenta de e-mail disponível. Mostre o rascunho e peça confirmação antes de qualquer envio.
- Escreva em português do Brasil, no registro do canal usado pelo lead.

Depois de montar a resposta, feche com uma pergunta objetiva à Maria: falta alguma informação sobre o lead ou o projeto que mudaria o conteúdo (não o tom) da resposta antes de considerar pronta para enviar?
