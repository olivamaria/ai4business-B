---
name: revisa-repo
description: Revisa o conteúdo Markdown deste repositório (problema.md, contexto/, prompts/, e qualquer pasta nova) em busca de trechos vagos, conteúdo incompleto, informação desatualizada, nomes de arquivo fora do padrão e links internos quebrados, produzindo um relatório organizado por arquivo com severidade (bloqueante vs. sugestão). Use esta skill sempre que a Maria pedir para revisar, conferir, validar, "dar uma olhada geral" ou preparar o repositório antes de qualquer entrega — frases como "revisa o repo antes de entregar", "roda a revisão", "confere se tá tudo certo antes de mandar", "tá pronto pra entregar?", ou o comando /revisa-repo. Dispare esta skill proativamente também quando você mesmo estiver prestes a declarar concluída uma tarefa de edição de conteúdo neste repo (nova versão de processo-precificacao.md, novo prompt, novo arquivo de contexto) — a revisão faz parte do fluxo de entrega, não é opcional.
---

# Revisar o repositório antes de qualquer entrega

## Por que essa skill existe

Este repositório é conteúdo, não código: não há build, lint ou teste automatizado para pegar um erro antes que ele vá para o professor, para a Samba, ou para a próxima rodada de iteração da própria Maria. A única rede de segurança é uma leitura atenta e sistemática antes de qualquer entrega — é isso que esta skill faz.

## Antes de começar: releia o terreno, não confie na memória

A estrutura e o conteúdo deste repo mudam entre conversas. Antes de apontar qualquer problema:

1. Releia o `CLAUDE.md` da raiz — é a fonte da verdade sobre estrutura e convenções esperadas.
2. Releia todo o conteúdo real: `problema.md`, tudo em `contexto/`, tudo em `prompts/`, e qualquer pasta que exista no repo mas não esteja descrita no `CLAUDE.md` (isso, por si só, já é um achado a reportar — estrutura documentada desatualizada).
3. Rode `git status` para ver o que está sujo, não commitado, ou solto na raiz — arquivos como `.DS_Store` não deveriam compor uma entrega.

## O que procurar

As categorias abaixo mapeiam direto para as convenções do `CLAUDE.md`, então ao achar um problema você já sabe qual regra ele quebra e consegue explicar o "por quê" no relatório, não só o "o quê".

### 1. Vago ou ambíguo
Frases que soam completas mas não geram ação: "melhorar o processo", "otimizar a comunicação", afirmações sem sujeito claro ("deve ser revisado" — por quem, quando?), listas de "pontos a considerar" sem nenhuma decisão de fato. Teste prático: se a frase não vira uma ação com um responsável, ela é vaga.

### 2. Incompleto
Placeholders explícitos ("ainda pode ser refinado", "TODO", "a definir"), seções com título mas sem conteúdo, frases cortadas, listas onde o padrão dos outros itens sugere que falta algo (ex: uma tabela de etapas numeradas que pula um número). Nem todo placeholder é um problema: um parêntese deliberado convidando revisão futura (como existe hoje em `contexto/sobre-mim.md`) é transparência, não descuido — reporte como sugestão, não como bloqueante, e diga por quê você não elevou a severidade.

### 3. Desatualizado
O sinal mais forte é inconsistência entre arquivos que deveriam concordar entre si: um arquivo em `contexto/` afirma algo que outro já não sustenta mais; um prompt em `prompts/` referencia uma versão do processo que não é mais a vigente; a lista de estrutura do repo no `CLAUDE.md` não bate com o que existe fisicamente (pasta nova sem menção, arquivo citado que não existe mais). Para `contexto/processo-precificacao.md` especificamente: se o conteúdo foi revisado mas a seção "O que mudou em relação à versão anterior" não reflete essa mudança, isso é desatualização por omissão — o arquivo existe para ser revisado em camadas, não reescrito do zero, e essa seção é o registro desse histórico.

### 4. Nomes fora do padrão
O padrão predominante em `contexto/` é kebab-case em português (`sobre-mim.md`, `processo-precificacao.md`). Note que `prompts/` já foge disso hoje (`promptFinal.md`, `promptV1.md`, em camelCase) — isso é uma inconsistência real do repo atual e vale reportar mesmo já existindo há um tempo; "já é assim faz tempo" não equivale a "está certo". Da mesma forma, sinalize qualquer pasta ou arquivo cujo conteúdo esteja em inglês ou fora do padrão de idioma do restante do repo, já que a convenção declarada é português do Brasil em tudo.

### 5. Links quebrados
Rode o script abaixo a partir da raiz do repo. Ele varre todo `.md` fora de `.git`/`.claude`, extrai os links relativos e confere se o destino existe de verdade (não valida âncoras dentro do arquivo, só a existência do arquivo):

```bash
python3 .claude/skills/revisa-repo/scripts/check_links.py
```

Trate qualquer link quebrado como bloqueante — um link morto numa entrega mina a confiança em tudo o resto do documento, mesmo que o conteúdo em volta esteja ótimo.

### 6. Convenções específicas deste repo

Estas quebras são fáceis de deixar passar porque o texto ao redor "lê bem" — só ficam visíveis se você souber a regra combinada:

- **"Não confirmado internamente"**: qualquer afirmação sobre números, decisões ou critérios internos da Samba que não seria de conhecimento público, e que não está marcada como não confirmada, é suspeita — pode ser que a marcação tenha sumido numa edição, ou que a frase tenha sido escrita como fato desde o início. Reporte também o inverso: hipóteses marcadas "não confirmado" que soam como se já tivessem sido validadas em conversa mas a marcação ficou esquecida — pergunte à Maria em vez de assumir de qualquer lado.
- **Valores simbólicos**: qualquer número que pareça custo/preço real da Samba (R$, percentual de margem, etc.) é bloqueante — o combinado é usar só faixas `$` a `$$$$`. Preste atenção a exemplos "ilustrativos" que fujam da própria escala de 4 níveis que o repo define (por exemplo, uma soma informal virando uma sequência de `$` fora do padrão `$`/`$$`/`$$$`/`$$$$`) — não é um valor real, mas deixou de ser um tier reconhecível, o que é uma inconsistência a reportar mesmo assim.
- **Escopo**: qualquer revisão que comece a empurrar o Criativo para julgamento financeiro, ou que proponha ferramenta/sistema complexo em vez de processo simples com o que a Samba já tem, contradiz o princípio central do processo. Reporte isso como bloqueante conceitual, não como questão de redação.

## Formato do relatório

Não entregue uma lista corrida de reclamações — organize por arquivo, com severidade, para a Maria conseguir agir rápido sem reler tudo sozinha:

```markdown
# Revisão do repo — [data]

## Resumo
[1–2 frases: está pronto para entregar? quantos bloqueantes?]

## 🔴 Bloqueante (resolver antes de entregar)
### [arquivo.md]
- **[categoria]** (linha X): [o que está errado, citando o trecho exato] — [por que importa / qual convenção quebra]

## 🟡 Sugestão (não impede a entrega, mas vale considerar)
### [arquivo.md]
- **[categoria]** (linha X): [...]

## Achados fora dos arquivos de conteúdo
[ex: .DS_Store não commitado, pasta nova sem menção no CLAUDE.md, etc.]
```

Sempre cite a linha e o trecho exato — "tem um problema em processo-precificacao.md" não dá para agir em cima. E sempre feche com um veredito direto: pronto para entregar ou não, e por quê. Essa clareza final é o objetivo real da skill — não gerar uma lista de observações, e sim uma resposta que a Maria possa usar para decidir "mando ou não mando" sem precisar reconferir tudo sozinha.
