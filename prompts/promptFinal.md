# Prompt Final — Processo de precificação (Criativo → Atendimento)

## Contexto

Versão final e reutilizável do prompt, depois de três rodadas de iteração ([promptV1.md](promptV1.md) → [promptV2.md](promptV2.md) → [promptV3.md](promptV3.md)). A crítica que gerou o V3 (ver [promptV3.md](promptV3.md)) resolveu as ambiguidades da V2 — granularidade da estimativa, papel do Criativo na classificação cobrável/institucional, momento de entrada da Produção, e a instrução de sempre partir do contexto e da versão vigente do processo em vez de recomeçar do zero. O V3 foi executado e gerou a versão atual de [contexto/processo-precificacao.md](../contexto/processo-precificacao.md). Este prompt é o que deve ser reaproveitado nas próximas rodadas semanais, sem precisar de ajuste manual a cada uso.

## Prompt

**OBJETIVO**
Reduzir o tempo entre a Samba ganhar uma concorrência e ter o orçamento aprovado e liberado para o cliente, padronizando a passagem do conceito criativo para uma estimativa inicial de custo. Esse é o critério principal de sucesso do processo — todas as etapas abaixo devem ser desenhadas em função dele.

**CONTEXTO DE REFERÊNCIA**
Antes de propor ou revisar o processo, considere o que já está documentado no projeto: [negocio.md](../contexto/negocio.md), [cliente.md](../contexto/cliente.md) e a versão vigente do processo em [processo-precificacao.md](../contexto/processo-precificacao.md). Trate a versão vigente como ponto de partida: refine, ajuste ou questione o que já existe em vez de recomeçar do zero. Ao final, destaque em poucas linhas o que mudou em relação à versão anterior e por quê.

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

## Resultado gerado

[contexto/processo-precificacao.md](../contexto/processo-precificacao.md) — versão final consolidada: fluxo em etapas, tabela de responsável/ação/resultado, exemplo prático com faixas simbólicas, três indicadores ligados ao objetivo, e seção própria de "o que mudou em relação à versão anterior". O papel do Criativo na classificação cobrável/institucional e o momento exato de entrada da Produção (etapa 6, checkpoint único) ficaram explícitos no documento.

## Como reusar este prompt

Nas próximas rodadas, rodar este mesmo prompt sem alteração. A instrução de "contexto de referência" já garante que a IA parte da versão vigente do processo em vez de recomeçar do zero — então repetir o prompt semanalmente serve para revisar/questionar o processo à luz de aprendizados novos, não para regenerá-lo do nada.
