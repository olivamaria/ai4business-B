# Prompt V3 — Processo de precificação (Criativo → Atendimento), versão revisada após crítica

## Contexto

Terceira iteração do prompt recorrente semanal (ver [promptV2.md](promptV2.md)). Mesmo objetivo de fundo — conectar o conceito criativo a uma estimativa inicial de custo, reduzindo o vai-e-volta entre Criativo e Atendimento depois que a Samba ganha uma concorrência — mas desta vez o briefing V2 foi submetido a uma crítica como revisor exigente antes de ser reescrito, para virar um prompt reutilizável semanalmente sem depender de ajuste manual a cada uso.

## Crítica do briefing (V2)

**Ambíguo ou pouco claro**
- "Estimativa inicial de custo" nunca era definida em termos de granularidade (faixa simbólica? valor aproximado? categoria?), o que podia mudar de formato a cada execução semanal.
- O limite entre onde o Criativo termina e Atendimento/Produção começa não era explícito, especialmente na etapa de classificar o que é cobrável ou não.
- "Reduzir o vai-e-volta" não tinha unidade de medida nem linha de base.
- Não ficava claro se o resultado esperado era um documento vivo para uso diário, material de treinamento, ou um template por projeto.

**Faltando**
- Nenhuma instrução para consultar o contexto já existente do projeto ([negocio.md](../contexto/negocio.md), [cliente.md](../contexto/cliente.md), [processo-precificacao.md](../contexto/processo-precificacao.md)) — lacuna crítica para um prompt de uso semanal, que corre o risco de reinventar (ou contradizer) decisões já validadas em rodadas anteriores.
- Nenhuma instrução sobre o que fazer com a versão da semana anterior: comparar, refinar, ou gerar do zero.
- Faltava indicar quando exatamente a Produção entra no fluxo.
- Sem orientação de profundidade/tamanho, a resposta podia crescer indefinidamente a cada rodada.

**Sobrando ou simplificável**
- O objetivo principal (reduzir o tempo entre ganhar a concorrência e liberar o orçamento) estava escondido dentro do bloco LIMITE, misturado a restrições negativas, em vez de ter destaque próprio como critério de sucesso.
- AMOSTRA e o item 1 do FORMATO pediam essencialmente a mesma coisa (um fluxo em etapas).

**Conflitante ou difícil de executar**
- FORMATO pedia um exemplo prático de estimativa de custo, enquanto LIMITE proibia inventar valores reais — sem uma ponte explícita (faixas simbólicas), a IA precisava resolver essa tensão sozinha.
- AMOSTRA colocava "classificação do que é cobrável ou não" como etapa do Criativo, enquanto LIMITE pedia para não transformar o Criativo em equipe financeira — o briefing pedia e proibia a mesma coisa ao mesmo tempo, sem esclarecer o grau de envolvimento aceitável do Criativo.

**Objetivo e resultado esperado**
O objetivo geral já estava claro. O que faltava era a forma do entregável e como ele deveria se relacionar com o processo já documentado — o ponto que mais atrapalha o uso semanal e cumulativo deste prompt.

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

Prompt V3 executado: [contexto/processo-precificacao.md](../contexto/processo-precificacao.md) foi revisado (não recriado do zero) a partir da versão vigente. Três ajustes principais:

- Papel do Criativo na classificação cobrável/institucional deixado explícito: ele só aponta blocos do catálogo, não julga custo — a etiqueta cobrável/institucional já vem definida no catálogo por Atendimento/Produção. Atendimento confirma e só decide de fato em caso de exceção ao padrão.
- Momento de entrada da Produção destacado como nota própria logo após o fluxo: uma única vez, na etapa 6 (checkpoint), nunca antes.
- Nova seção "5. O que mudou em relação à versão anterior" adicionada ao documento, como pedido no item 5 do FORMATO.

Fluxo, tabela de etapas, exemplo prático com faixas simbólicas e os três indicadores já existentes na versão anterior foram mantidos sem alteração de conteúdo.
