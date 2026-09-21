# Biblioteca de prompts

Pedidos que funcionam, prontos para reusar. Cada entrada guarda a versão vencedora completa e o que se aprendeu chegando nela.

O histórico das iterações fica em [prompts/](prompts/) — V1, V2, V3 e a crítica que gerou cada uma. Este arquivo é a prateleira; a pasta é o rascunho.

---

## Refinar o processo de precificação (Criativo → Atendimento)

**Atualizado em:** 18/09/2026 · trabalhado originalmente em 24/08/2026
**Frequência de uso:** semanal
**Versão vencedora:** V3 ([promptV3.md](prompts/promptV3.md), consolidada em [promptFinal.md](prompts/promptFinal.md))
**Roda sobre:** [problema.md](problema.md), [contexto/](contexto/) e a versão vigente de [contexto/processo-precificacao.md](contexto/processo-precificacao.md)

### O pedido que funciona

**OBJETIVO**
Reduzir o tempo entre a Samba ganhar uma concorrência e ter o orçamento aprovado e liberado para o cliente, padronizando a passagem do conceito criativo para uma estimativa inicial de custo. Esse é o critério principal de sucesso do processo — todas as etapas abaixo devem ser desenhadas em função dele.

**CONTEXTO DE REFERÊNCIA**
Antes de propor ou revisar o processo, considere o que já está documentado no projeto: negocio.md, cliente.md e a versão vigente do processo em processo-precificacao.md. Trate a versão vigente como ponto de partida: refine, ajuste ou questione o que já existe em vez de recomeçar do zero. Ao final, destaque em poucas linhas o que mudou em relação à versão anterior e por quê.

**TAREFA**
Crie (ou refine) um processo simples e prático para padronizar a precificação de projetos da Agência Samba depois que a agência ganha uma concorrência, conectando o conceito criativo a uma estimativa inicial de custo e reduzindo o vai-e-volta entre Criativo e Atendimento.

**AMOSTRA**
Um bom resultado funciona como um fluxo que o time aplica no dia a dia. Exemplo:
Briefing do cliente → conceito criativo → identificação dos elementos do projeto → estimativa inicial de custo → classificação do que é cobrável ou não → validação com Atendimento/Produção → orçamento final.
Deixe claro:
- Quem participa de cada etapa, incluindo em que ponto exato a Produção entra (só na validação final, ou antes).
- Qual informação precisa ser definida em cada etapa.
- Em quais momentos específicos o orçamento deve ser revisado.
- Qual é o papel do Criativo na classificação cobrável/institucional — ele sinaliza a partir de categorias pré-definidas, ou faz julgamento financeiro? (O Criativo não deve fazer julgamento financeiro do zero — apenas apontar elementos dentro de categorias já definidas por Atendimento/Produção.)

**FORMATO**
1. Um fluxo com as etapas do processo em ordem.
2. Uma tabela mostrando, para cada etapa: responsável, o que deve ser feito, resultado esperado.
3. Um exemplo prático de conceito criativo transformado em estimativa inicial de custo, usando faixas simbólicas (ex.: $ a $$$$) — nunca valores reais.
4. Três indicadores simples para acompanhar se o processo está funcionando, ligados diretamente ao objetivo (tempo até orçamento liberado, número de idas e voltas Criativo↔Atendimento, e um terceiro à escolha).
5. Um resumo curto do que mudou em relação à versão anterior do processo, se houver.

**LIMITE**
Não crie um sistema tecnológico complexo nem transforme o time criativo em uma equipe financeira. Não invente valores reais de custos ou preços da Samba — use apenas faixas simbólicas ilustrativas. Proponha algo aplicável com as ferramentas e equipes que a agência já possui. Considere que a Samba pode ter vários projetos simultâneos (ex.: os seis projetos atuais do Rock in Rio). Não invente informações sobre a empresa que não estejam neste briefing ou nos arquivos de contexto já existentes do projeto.

### O que aprendi

**Em uma linha:** o meta-prompt valeu mais que o formato — foi a crítica da IA ao próprio briefing que achou a contradição que eu não tinha visto.

O detalhe: a V2 pedia, na AMOSTRA, que a classificação cobrável/institucional fosse etapa do Criativo, e proibia, no LIMITE, transformar o Criativo em equipe financeira. O briefing pedia e proibia a mesma coisa. Eu não enxerguei isso relendo — a IA enxergou quando pedi que criticasse como revisor exigente. A V3 resolve dizendo exatamente o grau de envolvimento aceitável: o Criativo aponta blocos, a etiqueta já vem do catálogo, e a exceção é do Atendimento.

**O segundo aprendizado, que só aparece no uso repetido:** nenhuma das duas primeiras versões mandava ler o contexto que já existe no repositório. Sem o bloco CONTEXTO DE REFERÊNCIA, cada execução semanal recomeçava do zero e podia contradizer o que já tinha sido decidido na semana anterior. Um prompt recorrente sem instrução de partir da versão vigente não acumula — ele regenera, e regenerar é perder trabalho.

### O caminho até aqui

| Versão | O que era | O que faltava |
|---|---|---|
| V1 | uma frase: "me entregue um processo simples para conectar conceito criativo a custo" | formato, limite, amostra — a resposta veio genérica e sem forma de aplicar |
| V2 | briefing completo: tarefa, amostra, formato, limite | contradição interna não vista, e nenhuma instrução de ler o contexto existente |
| V3 | V2 reescrita pela IA depois da crítica | — é a vencedora |

**Técnicas usadas:** amostra (one-shot) e briefing de quatro partes na V2; meta-prompting na V3. Não usei papel (role prompting) — vale testar numa próxima rodada, com o papel de controller cético revisando as faixas de custo.
