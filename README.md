# Padronização da precificação na Agência Samba

Projeto da disciplina **AI for Business** (Link School of Business) sobre um gargalo real da Agência Samba: depois que a agência ganha uma concorrência, não existe passagem padronizada entre Criativo e Atendimento para transformar um conceito criativo em estimativa de custo. O ciclo entre "ganhamos" e "orçamento liberado ao cliente" varia de poucas semanas a quatro meses, sem que ninguém saiba explicar a variação.

Este repositório é conteúdo, não software: Markdown em português, construído aula a aula, em que cada arquivo acrescenta uma camada ao anterior. A única exceção é o `painel.html`, que é uma página que abre no navegador.

**Por onde começar a ler:** [`problema.md`](problema.md) → [`contexto/`](contexto/) → [`regras.md`](regras.md) → [`painel.html`](painel.html).

## O problema e o contexto

| Arquivo | O que é |
|---|---|
| [`problema.md`](problema.md) | O documento âncora. Quem sofre, como é hoje, o resultado desejado, o plano, o primeiro experimento e a seção `## Métrica` com o alvo declarado. Tudo o mais serve a este arquivo |
| [`contexto/sobre-mim.md`](contexto/sobre-mim.md) | Quem escreve, o papel dela na Samba e como prefere trabalhar |
| [`contexto/negocio.md`](contexto/negocio.md) | O que a Samba vende, para quem, e o que ainda não foi confirmado internamente |
| [`contexto/cliente.md`](contexto/cliente.md) | Quem compra, por que compra, e as perguntas em aberto sobre reclamação e churn |
| [`contexto/processo-precificacao.md`](contexto/processo-precificacao.md) | A proposta viva: o processo Criativo → Atendimento com catálogo de blocos de custo. É refinado versão a versão, nunca recriado do zero |
| [`CLAUDE.md`](CLAUDE.md) | Instruções permanentes para a IA: manda ler o contexto no início de toda conversa, e registra as convenções do repositório |

## Os pedidos

| Arquivo | O que é |
|---|---|
| [`prompts.md`](prompts.md) | A biblioteca: o pedido vencedor na íntegra e o que se aprendeu chegando nele |
| [`prompts/`](prompts/) | O rascunho: as iterações V1 → V2 → V3 → Final, com a crítica que gerou cada versão |

## A operação

| Arquivo | O que é |
|---|---|
| [`regras.md`](regras.md) | As três regras que a operação vigia, cada uma com gatilho, fonte, condição com número, ação, quem recebe e o que registrar quando não disparar. Começa pela Regra zero, que obriga a avisar quando a fonte falha |
| [`automacoes.md`](automacoes.md) | O que está ligado, a auditoria manter/consertar/matar, a tabela de execuções das regras e como o painel é atualizado |
| [`alertas/`](alertas/) | Os alertas que as regras produziram, um arquivo por data de execução |
| [`testes.md`](testes.md) | Os três cenários de falha, quebrados de propósito: fonte fora do ar, dado sujo e condição que nunca dispara. Com o antes e o depois de cada conserto |

## Os dados

| Arquivo | O que é |
|---|---|
| [`dados/fonte.md`](dados/fonte.md) | A fonte canônica declarada: de onde vem o dado, quem atualiza, e os três números com a regra de cálculo de cada um escrita por extenso |
| [`dados/amostra.csv`](dados/amostra.csv) | A amostra, 12 linhas. Base de treino da disciplina, **não é dado da Samba** |
| [`fake-erp.md`](fake-erp.md) | O manual da API de treino, escrito para a IA usar sozinha: endereço, autenticação, endpoints, erros comuns e a armadilha do `totalAmount` |
| [`painel.html`](painel.html) | O painel dos três números. Arquivo único, abre no navegador sem servidor e sem internet |

## O radar

| Arquivo | O que é |
|---|---|
| [`radar/comentarios.md`](radar/comentarios.md) | 82 comentários públicos coletados de 8 posts de um perfil de evento, sem identificar quem escreveu |
| [`radar/radar-tendencias.md`](radar/radar-tendencias.md) | A classificação em categorias fechadas, a tabela de relevância e a leitura de negócio |

## As skills

[`.claude/skills/`](.claude/skills/) — processos empacotados que a IA lê e executa:

- **`revisa-repo`** — revisa este repositório antes de qualquer entrega: o vago, o sem número, o desatualizado e os links quebrados
- **`gera-briefing`** — monta pauta e perguntas céticas antes de uma conversa importante, a partir do contexto vigente
- **`responde-lead`** — responde um interessado nos serviços da Samba, no tom da empresa
- **`internal-comms`** e **`canvas-design`** — instaladas do repositório oficial da Anthropic

## Convenções

- Tudo em **português brasileiro**.
- **"Não confirmado internamente"** marca o que é hipótese e ainda não foi validado com a Samba. A marcação nunca é removida em silêncio.
- **Valores simbólicos** (`$` a `$$$$`) nos exemplos de custo. Nunca números reais da Samba.
- **Refinar, não regenerar**: os documentos vivos são revisados em cima da versão anterior, registrando o que mudou.

## O que ainda não é verdade

Dois pontos que importam para quem lê pela primeira vez:

- **A operação roda sobre base de treino.** As regras e o painel usam o FakeERP da disciplina, não dados da Samba. Isso está declarado em [`dados/fonte.md`](dados/fonte.md) e em [`regras.md`](regras.md), com o mapeamento entre os dois.
- **A métrica ainda não tem linha de base.** O ciclo "ganhamos → orçamento liberado" não é medido hoje na Samba. Registrar essas duas datas por projeto é a primeira tarefa do plano, não uma pendência.
