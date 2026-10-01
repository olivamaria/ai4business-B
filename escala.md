# Pronto para escalar?

O portão da Aula 15, aplicado à operação montada nas aulas 10 a 14: as três regras de [regras.md](regras.md) rodando sobre o FakeERP, os alertas em [alertas/](alertas/), o [painel.html](painel.html) sobre [dados/amostra.csv](dados/amostra.csv) e a métrica declarada em [problema.md](problema.md).

Avaliado em 01/10/2026. A régua: evidência é arquivo e data. Onde não há arquivo, a resposta é "sem evidência", não uma suposição.

| # | Pergunta | Resposta |
|---|---|---|
| 1 | Roda sem mim? | **não** |
| 2 | Quando falha, avisa? | **em parte** |
| 3 | Alguém lê a saída? | **não** |
| 4 | Mede alguma coisa? | **não** |
| 5 | O cliente foi ouvido? | **não** |

---

## 1. Roda sem mim?

**Resposta:** não.

**Evidência:**

- [automacoes.md](automacoes.md), tabela "Acessos e conectores": `Rotina agendada | nenhuma | as regras rodam à mão`.
- [automacoes.md](automacoes.md), seção "Regras ligadas": "**Como roda:** à mão, toda segunda-feira."
- [automacoes.md](automacoes.md), tabela "Execuções": existe **uma** data de execução, 18/09/2026, com a hora "não registrada". O [alertas/](alertas/) tem um único arquivo, `2026-09-18.md`.

**O que a evidência mostra além do "não":** a rotina não roda sozinha, e também não rodou à mão no ritmo que ela mesma declara. O gatilho é "toda segunda-feira", mas 18/09/2026 foi uma sexta. As duas segundas seguintes, 21/09 e 28/09, não têm execução registrada nem arquivo de alerta. Em 21/09 houve trabalho no repositório (os testes de [testes.md](testes.md) e a Regra zero), mas a verificação semanal não foi rodada.

A decisão de não agendar está justificada em [automacoes.md](automacoes.md), na "Nota sobre a ausência de rotina agendada": a condição ainda não estava calibrada. A justificativa é razoável. Ela explica por que não há agendamento, mas não transforma o "não" em "sim".

**Se não: o que falta**

- Uma execução que aconteça sem alguém apertar nada, registrada em [automacoes.md](automacoes.md) com data e hora.
- Antes disso, cumprir o próprio gatilho à mão: rodar nas segundas e registrar cada execução, inclusive as que dão "FONTE INDISPONÍVEL".

---

## 2. Quando falha, avisa?

**Resposta:** em parte. O painel avisa, e isso foi provado. As regras estão instruídas a avisar, mas isso nunca foi provado com a regra em execução.

**Evidência do que avisa:**

- [testes.md](testes.md), Cenário 1: com a fonte apagada, o painel passou a mostrar a faixa vermelha "FONTE INDISPONÍVEL". O antes e o depois estão registrados, com teste de 21/09/2026.
- [testes.md](testes.md), Cenário 2: com o CSV sujo, o painel passou a mostrar "li 13 linhas e ignorei 3", com o motivo de cada linha descartada.
- [painel.html](painel.html), linhas 154 e 158: o código das duas mensagens está no arquivo.

**Evidência do que não está provado:**

- A Regra zero ([regras.md](regras.md)) é uma frase dentro de um prompt executado à mão. Ela foi escrita em 21/09/2026, depois da única execução das regras (18/09). Desde então as regras não rodaram nenhuma vez. Não existe um alerta ou registro de execução em que uma regra tenha escrito "FONTE INDISPONÍVEL".
- O próprio [testes.md](testes.md), Cenário 3, admite o limite: "A Regra zero garante que a operação **avise**, não que ela funcione".
- A falha mais provável da operação hoje não é a fonte cair, e sim a rotina não rodar. Essa falha não avisa ninguém. As segundas 21/09 e 28/09 passaram sem execução, e nada no repositório acusou isso. Nenhum dos três cenários de [testes.md](testes.md) cobre esse caso.

**Se não: o que falta**

- Uma execução das regras sobre o mês corrente (09/2026, que tem `count: 0`) que produza um arquivo em `alertas/` com "FONTE INDISPONÍVEL". Isso transforma a Regra zero de instrução escrita em comportamento observado.
- Um jeito de perceber a segunda-feira sem execução. Enquanto a rotina for manual, o mínimo é olhar a data da última linha de [automacoes.md](automacoes.md) e tratar "mais de 7 dias" como falha.

---

## 3. Alguém lê a saída?

**Resposta:** não. Há uma pessoa com nome, mas nenhum registro do que ela fez depois de ler.

**Evidência:**

- [regras.md](regras.md), campo "Quem recebe" de cada regra: Maria (Atendimento/Comercial), com a ação dos 10 minutos seguintes descrita. Para a Regra 1, por exemplo: "registra o motivo do cancelamento". Isso cumpre a primeira metade do critério: há uma pessoa com nome.
- [alertas/2026-09-18.md](alertas/2026-09-18.md) pede três próximos passos: o motivo do cancelamento do pedido 1003, em quem está a bola no pedido 1004, e a separação entre atraso e perda em janeiro. **Nenhum dos três tem resposta registrada** em nenhum arquivo do repositório. Sem evidência do que foi feito nos 10 minutos seguintes.

**Por que o "não" é estrutural, e não só falta de anotação:**

- Quem roda, quem recebe e quem lê é a mesma pessoa, a autora. A saída nunca chega a ninguém além de quem a produziu.
- A ação pedida é impossível de cumprir. O pedido 1003 é um registro da base de treino ([dados/fonte.md](dados/fonte.md): "Esta não é a base da Agência Samba"), e não existe ninguém na Samba a quem perguntar por que ele foi cancelado. Uma saída que pede uma ação sem destino não tem como ser lida no sentido que a pergunta exige.
- [automacoes.md](automacoes.md), auditoria, item CONSERTAR: a decisão sobre onde o alerta aparece (Notion ou arquivo) "ainda não foi tomada".

**Se não: o que falta**

- Para cada alerta, uma linha registrando o que a pessoa que recebeu fez com ele e quando. Pode ser no próprio arquivo de `alertas/`, numa seção "O que foi feito".
- Com dado real, um destinatário que não seja a autora: no mínimo, quem responde pelo orçamento na reunião quinzenal citada em [problema.md](problema.md).

---

## 4. Mede alguma coisa?

**Resposta:** não. A tabela existe, mas a medição nunca foi feita.

**Evidência da tabela:**

- [problema.md](problema.md), seção `## Métrica`, com a tabela Métrica / Alvo / Como confiro: dias corridos entre "ganhamos a concorrência" e "orçamento liberado ao cliente", descontadas as pausas; mediana de 21 dias e teto de 42 dias até 31/12/2026; conferência quinzenal na planilha de controle do Atendimento.

**Evidência de que nenhuma medição foi feita:**

- [problema.md](problema.md), "O que precisa existir para eu conferir": "A planilha de controle citada acima **ainda não existe**".
- [problema.md](problema.md), tabela de "O resultado que eu quero": **Linha de base**: "a medir".
- [regras.md](regras.md), "O que não está escrito aqui e deveria estar": "Nenhuma regra vigia **tempo de ciclo em dias**, que é a métrica declarada".
- [README.md](README.md), "O que ainda não é verdade": "A métrica ainda não tem linha de base".

O que a operação mede de fato são três números do FakeERP ([dados/fonte.md](dados/fonte.md)). Eles são medições reais, mas de uma base de treino, e nenhum deles é a métrica do projeto. A Regra 2 é a que mais se aproxima, e o próprio [regras.md](regras.md) diz que com dado real ela "deixa de ser percentual de valor e passa a ser dias de ciclo".

**Se não: o que falta**

- A primeira medição: data de fechamento e data de liberação do orçamento dos 6 projetos do Rock in Rio, mais as pausas com início, fim e motivo, numa planilha. Com isso a linha de base deixa de ser "a medir". Esse é o item escolhido na decisão abaixo.

---

## 5. O cliente foi ouvido?

**Resposta:** não. Sem evidência.

Aqui, "quem usa" é o time da Samba que viveria o processo: Criativo, Atendimento e Produção (ver [contexto/processo-precificacao.md](contexto/processo-precificacao.md)). Em segundo plano, o cliente da Samba, que é quem espera pelo orçamento.

**Evidência:**

- Nenhum arquivo do repositório registra uma conversa com alguém do Criativo, do Atendimento ou da Produção sobre o processo ou sobre a operação. Também não há registro de nada que tenha mudado por causa de uma conversa dessas.
- [contexto/processo-precificacao.md](contexto/processo-precificacao.md): os blocos do catálogo estão como "Exemplos prováveis de blocos (a validar, não assumir como fato)", e a seção "O que precisa ser validado com o time antes de aplicar" continua em aberto.
- [contexto/cliente.md](contexto/cliente.md): reclamações e motivos de perda de conta estão marcados como "**Não há dados públicos confiáveis**" e "a validar diretamente com atendimento e clientes".
- [contexto/sobre-mim.md](contexto/sobre-mim.md), "O que eu ainda não sei": como cada área estima custo hoje, quais critérios usa para o que é cobrável, e onde isso fica registrado. São exatamente as perguntas que só uma conversa responde.

O acesso existe ([problema.md](problema.md), "Como eu tenho acesso": "contato direto com as equipes criativa, de atendimento e de produção"). O que não existe é o registro de ter usado esse acesso.

**Se não: o que falta**

- Conversas com 3 pessoas que usariam o processo, uma de cada área (Criativo, Atendimento, Produção), e o registro do que mudou no processo ou no catálogo por causa de cada conversa. O objetivo não é saber se gostaram. É descobrir o que foi entendido errado.

---

## A decisão

**Não abre.**

Quatro "não" e um "em parte". Para uma operação com duas semanas de vida, rodando sobre base de treino, esse é o resultado esperado, e o certo. Escalar agora multiplicaria uma rotina que já não roda no ritmo combinado, aplicada a dados que não são da Samba, sem ninguém além da autora lendo o resultado.

### O UM item que vira sim primeiro

**Pergunta 4: fazer a primeira medição da métrica.**

**O que é:** registrar a data em que a Samba soube que ganhou e a data em que o orçamento foi enviado ao cliente para os 6 projetos do Rock in Rio. As pausas entram com início, fim e motivo, conforme [problema.md](problema.md). O resultado é a primeira mediana e o primeiro maior valor, comparados com o alvo de 21 e 42 dias.

**Até quando:** 15/10/2026.

**Por que este, e não os outros três:**

- **Ele destrava as outras perguntas, e as outras não destravam ele.** Com o dado real, a Regra 2 pode virar a regra de dias de ciclo que [regras.md](regras.md) já prevê (pergunta 1). O alerta passa a ter destino real e alguém na Samba a quem perguntar (pergunta 3). E levantar as datas obriga a sentar com o Atendimento, que é o começo da pergunta 5.
- **Automatizar primeiro (pergunta 1) seria escalar o vazio.** O [testes.md](testes.md), Cenário 3, mostra que o FakeERP tem `count: 0` de setembro de 2026 em diante. Uma rotina agendada hoje rodaria toda segunda para escrever "FONTE INDISPONÍVEL" até o fim do ano.
- **A pergunta 5 é a mais importante, mas não é a que mais trava.** Sem nenhum número sobre o ciclo, a conversa com o time fica no nível da opinião, como "acho que demora". Com as datas dos 6 projetos na mesa, a conversa vira "por que este levou o dobro daquele?". Por isso ela é a segunda da fila, não a primeira.

**Como fica provado:** a planilha existe, o link para ela e a data da primeira medição estão em [problema.md](problema.md), e a linha "Linha de base" deixa de dizer "a medir".

**O risco honesto:** o [problema.md](problema.md) avisa que o histórico está "espalhado" e é recuperável "por garimpo manual". Se até 15/10 só for possível reconstruir parte dos 6 projetos, a medição sai com o número de projetos que deu, declarado como "li N de 6". Ela não deve ser completada com estimativa.

---

## A sexta pergunta: se eu dobrar o volume amanhã, o que quebra primeiro?

**A execução manual, que já quebrou no volume de hoje.**

Hoje há uma pessoa, três regras, um mês de fonte e uma execução semanal prometida. Mesmo assim, duas das três segundas desde a primeira execução passaram sem rodada ([automacoes.md](automacoes.md), Execuções). Dobrar o volume significa, por exemplo, os 6 projetos do Rock in Rio virarem 12 ou as regras virarem 6. A rotina continuaria dependendo da mesma pessoa, que roda, recebe e lê. O tempo de rodar cresce com o volume, e o tempo dessa pessoa não.

**A segunda coisa a quebrar é o painel.** Ele é atualizado à mão em dois lugares que precisam bater: o CSV e o bloco de dados embutido no HTML ([automacoes.md](automacoes.md), seção "Painel"). Com mais extrações por semana, cresce a chance de atualizar um e esquecer o outro. Nesse caso o painel mostra número velho com cara de atualizado, que é a falha que o [testes.md](testes.md) já identificou como a pior.
