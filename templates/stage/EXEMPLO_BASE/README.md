# Exemplo Base de Etapa

## Finalidade

Esta pasta funciona como modelo estrutural para a execução de uma etapa do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Ela foi criada para orientar os integrantes sobre:

```text
como iniciar uma etapa
como organizar a análise
como documentar o trabalho
como validar os resultados
como preparar o handoff
```

Esta pasta é apenas um **template**.

Ela não representa uma etapa já executada.

---

# Estrutura do modelo

```text
EXEMPLO_BASE/
├── README.md
├── checklist.md
├── analysis.qmd
└── script.R
```

Cada arquivo possui uma finalidade diferente.

---

# `README.md`

Este arquivo explica:

```text
objetivo da etapa
estrutura do template
fluxo de trabalho
responsabilidades
regras de execução
```

Ele deve ser consultado antes do início da etapa.

---

# `checklist.md`

Arquivo utilizado para verificar se a etapa:

```text
começou corretamente
↓
foi executada corretamente
↓
foi validada
↓
foi documentada
↓
está pronta para handoff
```

O checklist não substitui os testes automatizados.

Ele funciona como controle operacional e científico.

---

# `analysis.qmd`

Documento destinado à análise e interpretação da etapa.

Poderá conter:

```text
objetivo
dados utilizados
metodologia
tabelas
figuras
resultados
interpretação
limitações
conclusões da etapa
```

Os resultados inseridos nesse arquivo devem vir da execução real da análise.

---

# `script.R`

Arquivo destinado ao código específico da etapa.

Nesta base ele deverá permanecer apenas como esqueleto.

Os integrantes serão responsáveis posteriormente por:

```text
implementar funções
carregar dados
executar análises
validar resultados
produzir outputs
```

---

# Princípio de uso

Uma etapa deve seguir, de forma geral:

```text
entrada aprovada
↓
verificação da entrada
↓
execução da análise
↓
validação
↓
interpretação
↓
documentação
↓
handoff
```

Não iniciar uma etapa sem compreender a entrada recebida.

---

# Como utilizar este template

O integrante responsável deverá utilizar esta pasta como referência para estruturar seu próprio trabalho.

A ideia conceitual é:

```text
EXEMPLO_BASE
↓
adaptar para a etapa real
↓
implementar análise
↓
executar
↓
validar
↓
documentar
```

A forma exata de reutilização dos arquivos poderá ser definida pelos integrantes durante a implementação.

---

# Não trabalhar diretamente no exemplo

A pasta:

```text
templates/stage/EXEMPLO_BASE/
```

não deverá se transformar em uma etapa oficial.

Ela serve apenas como referência.

Os resultados reais deverão permanecer nas áreas correspondentes do projeto.

---

# Identificação da etapa

Ao utilizar o modelo, a etapa deverá possuir pelo menos:

```text
nome
responsável
objetivo
entrada
saída
status
versão
```

Exemplo estrutural:

```text
STAGE_NAME = TO_BE_FILLED
RESPONSIBLE = TO_BE_FILLED
INPUT_VERSION = TO_BE_FILLED
OUTPUT_VERSION = TO_BE_FILLED
STATUS = DRAFT
```

---

# Responsável

Cada etapa deverá possuir um responsável principal.

No projeto atual:

```text
Pacheco
→ auditoria, reconciliação, base canônica e ADA inicial

Benjamin
→ ADA aprofundada, critérios, conformidade, normalização e CRITIC

Vitor
→ TOPSIS, ranking, cenários, Pareto, sensibilidade e robustez

Marco
→ integração, relatório e apresentação
```

---

# Revisão

Responsável principal não significa ausência de revisão.

Cada etapa deverá possuir revisão cruzada quando apropriado.

Fluxo:

```text
responsável executa
↓
responsável valida
↓
outro integrante revisa
↓
correções
↓
aprovação
```

---

# Entrada

Antes de executar uma etapa, registrar:

```text
INPUT = TO_BE_FILLED
INPUT_VERSION = TO_BE_FILLED
INPUT_STATUS = TO_BE_FILLED
```

A entrada deve estar aprovada quando depender de etapa anterior.

---

# Handoff de entrada

Quando existir um handoff formal, ele deverá ser lido antes da execução.

Exemplos do projeto:

```text
01_PACHECO_to_BENJAMIN.md
02_BENJAMIN_to_VITOR.md
03_VITOR_to_MARCO.md
04_MARCO_to_TODOS.md
```

---

# Dados

O integrante deverá confirmar:

```text
qual base está usando
qual versão
quantas observações
quais variáveis
quais unidades
quais limitações conhecidas
```

Não utilizar arquivos paralelos sem rastreabilidade.

---

# Dados brutos

Os dados em:

```text
data/raw/
```

devem permanecer imutáveis.

Nunca:

```text
abrir
corrigir manualmente
salvar por cima
```

como parte da pipeline oficial.

---

# Transformações

Toda transformação relevante deverá ser feita por código e ser reproduzível.

Exemplos:

```text
renomear variável
converter unidade
agregar condições
calcular índice
normalizar
```

---

# Código

O código da etapa deverá:

```text
ler entradas
validar entradas
executar transformações
executar análises
produzir saídas
```

e não depender de procedimentos manuais ocultos.

---

# Linguagem

A linguagem analítica principal do projeto é:

```text
R
```

---

# Infraestrutura

A arquitetura prevista inclui:

```text
R
renv
targets
testthat
Docker
Git
```

Os integrantes deverão utilizar apenas os componentes efetivamente implementados no projeto.

---

# Caminhos

Não utilizar caminhos pessoais como:

```text
C:/Users/Nome/Desktop/arquivo.xlsx
```

Preferir sempre caminhos relativos ao repositório.

---

# Configuração

Parâmetros metodológicos que possam mudar deverão, quando adequado, ser centralizados em configuração em vez de espalhados pelo código.

Exemplos futuros:

```text
tolerâncias
critérios
direções
regras de validação
```

---

# Análise

A análise deve responder claramente:

```text
o que foi feito?
por que foi feito?
com quais dados?
com qual método?
com qual resultado?
com qual limitação?
```

---

# Resultados

Nenhum resultado deve ser preenchido antes da execução.

Nesta base:

```text
RESULTS_STATUS = NOT_GENERATED
```

---

# Resultados exploratórios

Resultados preliminares devem ser claramente identificados como:

```text
EXPLORATORY
```

Eles não devem ser apresentados automaticamente como conclusão oficial.

---

# Resultados aprovados

Somente resultados revisados poderão adquirir status equivalente a:

```text
APPROVED
```

---

# Tabelas

Tabelas científicas devem ser geradas a partir dos resultados reais.

Evitar redigitar números manualmente.

---

# Figuras

Figuras científicas devem ser produzidas de forma rastreável.

Fluxo:

```text
dados
↓
R
↓
resultado
↓
figura
```

---

# Interpretação

Não basta produzir um número ou gráfico.

Cada resultado importante deverá responder:

```text
o que foi observado?
↓
qual o significado?
↓
qual o impacto na próxima etapa?
```

---

# Validação

Toda etapa deverá possuir validações apropriadas ao seu conteúdo.

Exemplos:

```text
tipos
dimensões
intervalos
somas
identificadores
propriedades matemáticas
consistência
```

---

# Testes automatizados

Sempre que apropriado, testes deverão ser implementados em:

```text
tests/testthat/
```

O template de etapa não substitui essa estrutura.

---

# Cálculo independente

Resultados críticos podem exigir uma segunda forma de verificação.

Exemplos:

```text
recalcular total
verificar soma dos pesos
comparar implementação
testar caso simples
```

---

# Warnings

Warnings não devem ser ocultados apenas para deixar a execução limpa.

Eles devem ser avaliados quanto ao impacto científico.

---

# Erros

Se um erro impedir a validade da etapa:

```text
STATUS = BLOCKED
```

até sua resolução.

---

# Issues

Problemas relevantes deverão ser registrados com informações como:

```text
id
descrição
severidade
status
impacto
```

---

# Severidade

Uma classificação possível é:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

---

# Decisões metodológicas

Quando uma escolha tiver impacto relevante sobre os resultados, ela poderá exigir registro em:

```text
decisions/
```

---

# Não escolher método pelo resultado

É proibido comparar várias opções metodológicas e selecionar somente aquela que produz o fluido desejado como vencedor.

A escolha deve possuir justificativa independente do resultado final.

---

# Limitações

Cada etapa deverá documentar suas limitações reais.

Não inserir limitações genéricas apenas para completar a documentação.

---

# Dependências downstream

Antes de alterar um resultado já aprovado, verificar quais etapas dependem dele.

Exemplo:

```text
normalização
↓
CRITIC
↓
TOPSIS
↓
ranking
↓
robustez
↓
relatório
```

Uma alteração upstream pode exigir reexecução de toda a cadeia downstream.

---

# Saídas

Ao concluir a etapa, registrar:

```text
OUTPUT = TO_BE_FILLED
OUTPUT_VERSION = TO_BE_FILLED
OUTPUT_STATUS = TO_BE_FILLED
```

---

# Artefatos

Uma etapa poderá produzir:

```text
dados
tabelas
figuras
relatórios
logs
resultados
```

Somente os artefatos realmente necessários deverão ser gerados.

---

# Handoff

Ao final, a etapa deverá deixar claro:

```text
o que foi entregue
qual versão
quais limitações permanecem
quais problemas existem
o que a próxima etapa pode assumir
o que a próxima etapa não deve alterar
```

---

# Critério de conclusão

Uma etapa não está concluída apenas porque o código terminou sem erro.

Ela precisa ter:

```text
execução
+
validação
+
interpretação
+
documentação
+
revisão
```

---

# Status possíveis

Utilizar, quando apropriado:

```text
DRAFT
UNDER_REVIEW
APPROVED
BLOCKED
SUPERSEDED
```

---

# Git

O código e a documentação deverão ser versionados.

Cada integrante deverá trabalhar conforme a estratégia de Git definida pelo projeto.

---

# Branches

Estrutura planejada:

```text
pacheco/auditoria
benjamin/criterios
vitor/ranking
marco/relatorio
```

A implementação poderá ajustar a estratégia se o grupo decidir de forma documentada.

---

# Commits

Preferir commits:

```text
pequenos
coerentes
descritivos
```

em vez de um único commit com toda a etapa.

---

# Revisão antes de merge

Antes de integrar uma etapa:

```text
[ ] código executa
[ ] testes passam
[ ] resultados validados
[ ] documentação atualizada
[ ] handoff atualizado
[ ] nenhuma informação sensível ou temporária
```

---

# Arquivos temporários

Não versionar arquivos temporários, caches ou outputs descartáveis quando já estiverem cobertos pelo `.gitignore`.

---

# Relatório interno

O arquivo:

```text
analysis.qmd
```

pode funcionar como caderno analítico ou relatório técnico da etapa.

Ele não substitui necessariamente os relatórios formais localizados em:

```text
report/stages/
```

Os integrantes deverão evitar duplicação desnecessária de conteúdo.

---

# Relação com `report/stages/`

Uma organização recomendada é:

```text
analysis.qmd
→ análise operacional e exploratória

report/stages/
→ síntese técnica formal da etapa
```

A implementação final poderá simplificar essa relação, desde que exista uma fonte clara e não haja versões concorrentes.

---

# Uso do `script.R`

O `script.R` deste template serve apenas como exemplo estrutural.

Durante o projeto real, o código poderá ser melhor organizado em:

```text
R/pacheco/
R/benjamin/
R/vitor/
R/marco/
R/shared/
```

conforme a arquitetura do repositório.

---

# Não criar um script monolítico

Evitar colocar toda a lógica do projeto em um único arquivo com centenas ou milhares de linhas.

Preferir funções com responsabilidades claras.

---

# Funções compartilhadas

Código reutilizado por diferentes integrantes deverá, quando apropriado, ser movido para:

```text
R/shared/
```

---

# `_targets.R`

A pipeline principal poderá ser coordenada através de:

```text
_targets.R
```

quando os integrantes iniciarem a implementação.

Este template não deve antecipar a definição completa da pipeline.

---

# Reprodutibilidade

O objetivo é permitir que outro integrante consiga:

```text
clonar o projeto
↓
configurar ambiente
↓
executar a pipeline
↓
obter os mesmos resultados
```

dadas as mesmas entradas.

---

# Material fornecido pela professora

Qualquer material externo fornecido pela professora deverá ser preservado conforme sua função.

Exemplos:

```text
dados → data/raw/

template de apresentação → área de referência apropriada

logos → assets/

normas e referências → área apropriada
```

Não converter material externo em resultado do grupo.

---

# Responsabilidade dos integrantes

Nesta fase, estamos apenas montando a base do projeto.

Os integrantes serão responsáveis por:

```text
implementar
executar
testar
validar
interpretar
documentar
revisar
```

suas respectivas etapas.

---

# Checklist da etapa

O arquivo:

```text
checklist.md
```

deverá ser utilizado como apoio durante todo o ciclo da etapa.

Não deixar o checklist somente para o final.

---

# Fluxo resumido

```text
1. ler instruções
2. conferir entrada
3. planejar análise
4. implementar
5. executar
6. validar
7. interpretar
8. documentar
9. revisar
10. preparar handoff
```

---

# Estado atual do template

```text
STAGE_TEMPLATE_STATUS = BASE_PREPARED

ANALYSIS_STATUS = NOT_EXECUTED

CODE_STATUS = NOT_IMPLEMENTED

RESULTS_STATUS = NOT_GENERATED

HANDOFF_STATUS = NOT_APPLICABLE
```

---

# Princípio final

> O template existe para reduzir improvisação e tornar cada etapa compreensível, revisável e reproduzível. Ele organiza o trabalho dos integrantes, mas não substitui a implementação, a análise ou a interpretação que deverão ser realizadas por eles.