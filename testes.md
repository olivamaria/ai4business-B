# Testes de falha

Testado em 21/09/2026, sobre a operação montada nas aulas 10 a 13: as regras de [regras.md](regras.md) rodando sobre o FakeERP, e o [painel.html](painel.html) sobre [dados/amostra.csv](dados/amostra.csv).

Os três cenários foram executados de verdade. Em todos, o que assustou não foi a falha — foi a falha não ser sinalizada.

---

## Cenário 1 · A fonte saiu do ar

**O que eu testei**

Duas variantes, porque a operação tem duas fontes.

1. Renomeei `dados/amostra.csv` para `dados/amostra_OLD.csv` e rodei a rotina que calcula os três números de [dados/fonte.md](dados/fonte.md).
2. Abri o `painel.html` com o CSV ainda ausente.

**O que aconteceu**

A rotina quebrou alto, e isso é o comportamento bom: `FileNotFoundError: dados/amostra.csv`. Impossível confundir com normalidade.

O painel foi o problema. **Abriu normalmente, mostrou os 12 pedidos e os três números de janeiro — 4 pedidos, R$ 1.430,00, 42,0% — com a fonte canônica deletada do disco.** Os dados estão embutidos no HTML, então ele não tem como perceber que a fonte sumiu. Um painel que continua exibindo número depois de a fonte morrer é pior do que um painel quebrado: ele mente com cara de atualizado.

Essa fragilidade já estava prevista em [automacoes.md](automacoes.md) antes do teste. O teste confirmou que ela é real.

**O que eu consertei**

Duas coisas, porque uma frase não conserta HTML.

- Acrescentei a **Regra zero** ao [regras.md](regras.md): *"Se a fonte não existir ou vier vazia, escreva FONTE INDISPONÍVEL e pare. Nunca invente número. Sempre me diga quantas linhas leu e quantas ignorou, e por quê."*
- Blindei o `painel.html`: sem nenhuma linha válida, ele agora mostra em vermelho **"FONTE INDISPONÍVEL — li 0 linhas e ignorei 0. Nenhum número foi estimado"**, e não renderiza número nenhum.

**Antes e depois, com o CSV vazio**

| | |
|---|---|
| **Antes** | painel abre, três cartões com "—", tabela vazia, nenhuma mensagem. Parece que está carregando |
| **Depois** | faixa vermelha no topo: "FONTE INDISPONÍVEL. Nenhuma linha válida em `dados/amostra.csv`: li 0 e ignorei 0. Nenhum número foi estimado" |

---

## Cenário 2 · Chegou dado inesperado

**O que eu testei**

Devolvi o CSV ao lugar e estraguei três linhas, uma de cada tipo:

- linha 4: **vazia**
- linha 5: pedido 1003 com `total` **negativo** (`-225.00`)
- linha 6: pedido 1004 com a data em **outro formato** (`28/01/2026` em vez de `2026-01-28`)

Rodei o painel sobre esse CSV sujo.

**O que aconteceu**

O painel **quebrou em silêncio**. A linha vazia gerou `TypeError: Cannot read properties of undefined (reading 'startsWith')`, o `render()` nunca chegou a rodar, e a tela ficou com os três cartões mostrando "—", seletor de mês vazio e **nenhuma mensagem de erro**. O erro existia, mas só no console do navegador, que ninguém abre.

Pior: se a linha vazia não existisse, as outras duas passariam caladas. O total negativo seria somado como número válido, e a linha com data em outro formato simplesmente **desapareceria** do mês sem deixar rastro — o volume cairia de 4 para 3 pedidos e ninguém saberia por quê.

**O que eu consertei**

O parser do painel agora valida cada linha antes de usar, e reporta o que descartou: número de colunas, formato de data `AAAA-MM-DD`, `total` finito e não negativo, e `status` dentro de `PAID`/`PENDING`/`CANCELLED`.

**Antes e depois, com o CSV sujo**

| | |
|---|---|
| **Antes** | três cartões com "—", sem tabela e sem aviso. O erro só no console |
| **Depois** | faixa de atenção no topo: "li 13 linhas e ignorei 3. Os números abaixo usam apenas as 10 válidas", com os três motivos listados: `linha 4: vazia` · `linha 5: total inválido ou negativo ("-225.00")` · `linha 6: data fora do formato AAAA-MM-DD ("28/01/2026")` |

---

## Cenário 3 · A condição nunca dispara

**O que eu testei**

Duas perguntas: quando cada regra disparou pela última vez, e o que acontece se eu rodar as regras exatamente como o gatilho manda — sobre o **mês corrente**.

**O que aconteceu**

Este foi o achado mais grave dos três, e não é sobre um limite mal calibrado.

Rodando sobre os meses com dado, as três regras se comportam bem: a Regra 1 dispara em 2 dos 4 meses, a Regra 2 em 1, a Regra 3 em 2. Nenhuma é morta, nenhuma é ruidosa.

Mas o gatilho de todas as três diz **"toda segunda-feira, sobre o mês corrente"**. E o FakeERP não tem nenhum pedido de setembro de 2026 em diante:

| Mês | `count` | HTTP |
|---|---|---|
| 2026-09 | 0 | 200 |
| 2026-10 | 0 | 200 |
| 2026-11 | 0 | 200 |
| 2026-12 | 0 | 200 |

Ou seja: **rodando como está escrito, as três regras ficariam caladas toda segunda-feira até o fim do ano, sem nunca dar erro.** HTTP 200, resposta bem formada, zero pedidos. Visto de fora é indistinguível de uma operação tranquila.

O silêncio não vinha de condição bem calibrada. Vinha de a fonte não ter dado para o período que o gatilho pede.

**O que eu consertei**

A Regra zero cobre exatamente isto: zero linhas lidas obriga a resposta "FONTE INDISPONÍVEL" em vez de silêncio. A tabela de execuções em [automacoes.md](automacoes.md) já registra a coluna **"pedidos olhados"** por esse motivo — foi o que permitiu, na Aula 11, separar março (3 pedidos olhados, condição avaliada, não bateu) de maio (0 pedidos olhados, condição nunca avaliada).

**O que eu não consertei, e está em aberto**

O gatilho continua dizendo "mês corrente" sobre uma base de treino que acaba em julho. A correção de verdade é a fonte da Samba passar a existir — enquanto ela não existe, a operação roda sobre um período que não tem dado, e nenhuma frase no `regras.md` resolve isso. A Regra zero garante que a operação **avise**, não que ela funcione.

---

## O que os três testes têm em comum

Em nenhum dos três a operação deu erro. Ela devolveu, nos três casos, uma resposta de aparência normal: relatório completo com a fonte deletada, traços em vez de número com dado sujo, e silêncio semanal com a base vazia.

O risco nunca foi a falha. Foi a falha não ser sinalizada.

E o conserto principal não foi técnico: foi obrigar a operação a declarar quantas linhas leu e quantas ignorou. Um número acompanhado de "li 12 linhas, ignorei 0" é uma afirmação. O mesmo número sozinho é um chute com boa aparência.
