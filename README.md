# Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte

## Visão geral

Este repositório contém a estrutura, documentação e futura implementação do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

desenvolvido no contexto de um trabalho de Laboratório de Estatística.

O objetivo é construir um processo estatístico e multicritério:

```text
transparente
reproduzível
auditável
interpretável
rastreável
```

para comparar e classificar fluidos de corte a partir dos dados experimentais disponíveis.

O projeto utiliza:

```text
R
+
Quarto
+
LaTeX
+
Git
+
Docker
+
renv
+
targets
+
testthat
```

como arquitetura planejada de análise, reprodutibilidade e documentação.

---

# Estado atual

O projeto encontra-se na fase de:

```text
PREPARAÇÃO DA BASE E DA ARQUITETURA
```

Situação atual:

```text
PROJECT_STATUS = BASE_PREPARED

ARCHITECTURE_STATUS = BASE_PREPARED

MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

SCIENTIFIC_EXECUTION = NOT_STARTED

SCIENTIFIC_R_CODE = NOT_IMPLEMENTED

DATA_AUDIT = NOT_EXECUTED

CANONICAL_DATASET = NOT_CREATED

CRITERIA = NOT_FINALIZED

CRITIC = NOT_EXECUTED

TOPSIS = NOT_EXECUTED

ROBUSTNESS = NOT_EXECUTED

FINAL_RANKING = NOT_GENERATED
```

Nesta fase estão sendo preparados:

```text
documentação
configurações
templates
instruções
cadernos analíticos
handoffs
arquitetura dos agentes
protocolo de revisão
estrutura de diretórios
```

Ainda não estão sendo produzidos resultados científicos.

---

# Objetivo geral

O projeto pretende responder de maneira estruturada à questão:

```text
como comparar e ordenar os fluidos de corte
considerando simultaneamente diferentes
dimensões de desempenho?
```

A classificação não será construída apenas com um cálculo isolado.

Ela dependerá de uma cadeia completa de análise.

---

# Fluxo científico

O fluxo principal planejado é:

```text
dados brutos
↓
inventário
↓
auditoria
↓
reconciliação
↓
base canônica
↓
ADA inicial
↓
ADA bivariada
↓
ADA multivariada
↓
conformidade
↓
critérios
↓
matriz de decisão
↓
normalização
↓
CRITIC
↓
TOPSIS
↓
ranking principal
↓
cenários
↓
Pareto
↓
sensibilidade
↓
robustez
↓
integração
↓
relatório
↓
apresentação
```

---

# Princípio central

O objetivo não é apenas obter:

```text
1º
2º
3º
...
```

O projeto deve permitir explicar:

```text
de onde vieram os dados
como foram auditados
quais critérios foram utilizados
como foram normalizados
como os pesos foram obtidos
como o ranking foi calculado
quanto o ranking é estável
quais limitações existem
```

---

# Equipe

O projeto é dividido entre quatro integrantes.

---

## Pacheco

Responsável principalmente por:

```text
inventário
auditoria
reconciliação
base canônica
ADA inicial
```

---

## Benjamin

Responsável principalmente por:

```text
ADA bivariada
ADA multivariada
conformidade
critérios
matriz de decisão
normalização
CRITIC
```

---

## Vitor

Responsável principalmente por:

```text
TOPSIS
ranking principal
cenários
Pareto
sensibilidade
LOCO
LOAO
rank reversal
robustez
```

---

## Marco

Responsável principalmente por:

```text
integração
relatório final
tabelas
figuras
apresentação
conclusões
limitações
```

---

## Todos

Responsáveis conjuntamente por:

```text
infraestrutura
revisão cruzada
controle de versão
checkpoints
ensaio
revisão final
entrega
```

---

# Arquitetura multiagente

O projeto utiliza cinco agentes especializados para auxiliar os integrantes.

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

Os agentes não substituem os integrantes.

Eles funcionam como:

```text
assistentes especializados
+
revisores
+
mecanismo de organização
```

---

# Roteador central

O arquivo:

```text
AGENTS.md
```

funciona como roteador central.

Ele identifica:

```text
qual tarefa foi solicitada
↓
qual etapa está envolvida
↓
qual agente deve atuar
↓
quais arquivos precisam ser consultados
↓
quando o AGENTE_BOSS deve revisar
```

---

# Pasta `agents/`

A arquitetura completa está em:

```text
agents/
├── README.md
├── AGENTE_PACHECO.md
├── AGENTE_BENJAMIN.md
├── AGENTE_VITOR.md
├── AGENTE_MARCO.md
├── AGENTE_BOSS.md
└── REVIEW_PROTOCOL.md
```

---

# AGENTE_PACHECO

Agente pessoal de Pacheco.

Especialidade:

```text
dados
inventário
auditoria
reconciliação
base canônica
ADA inicial
```

Escopo científico principal:

```text
analysis/01_PACHECO_inventario.qmd
analysis/02_PACHECO_auditoria.qmd
analysis/03_PACHECO_reconciliacao.qmd
analysis/04_PACHECO_base_canonica.qmd
analysis/05_PACHECO_ada_inicial.qmd
```

---

# AGENTE_BENJAMIN

Agente pessoal de Benjamin.

Especialidade:

```text
ADA bivariada
ADA multivariada
correlação
redundância
conformidade
critérios
normalização
CRITIC
```

Escopo científico principal:

```text
analysis/06_BENJAMIN_ada_bivariada.qmd
analysis/07_BENJAMIN_ada_multivariada.qmd
analysis/08_BENJAMIN_conformidade.qmd
analysis/09_BENJAMIN_critic.qmd
```

---

# AGENTE_VITOR

Agente pessoal de Vitor.

Especialidade:

```text
TOPSIS
ranking
cenários
Pareto
sensibilidade
LOCO
LOAO
rank reversal
robustez
```

Escopo científico principal:

```text
analysis/10_VITOR_topsis.qmd
analysis/11_VITOR_cenarios_pareto.qmd
analysis/12_VITOR_robustez.qmd
```

---

# AGENTE_MARCO

Agente pessoal de Marco.

Especialidade:

```text
integração
relatório
tabelas
figuras
apresentação
conclusões
limitações
```

Áreas principais:

```text
report/
presentation/
```

---

# AGENTE_BOSS

O `AGENTE_BOSS` supervisiona os quatro agentes especializados.

Sua função é:

```text
revisar
auditar
verificar consistência
verificar dependências
verificar handoffs
detectar erros
solicitar correções
aprovar
bloquear
realizar revisão global
```

O Boss não deve corrigir silenciosamente resultados científicos produzidos por outro agente.

---

# Protocolo do Boss

O protocolo formal está em:

```text
agents/REVIEW_PROTOCOL.md
```

Toda revisão formal utiliza, quando aplicável:

```text
PRECHECK
↓
INPUT REVIEW
↓
METHOD REVIEW
↓
OUTPUT REVIEW
↓
HANDOFF REVIEW
```

---

# Resultados possíveis da revisão

O Boss poderá emitir:

```text
APPROVED
```

ou:

```text
CHANGES_REQUESTED
```

ou:

```text
BLOCKED
```

---

# Severidade de problemas

Issues de revisão podem ser classificadas como:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

---

# Regra de autoria

A autoridade científica principal continua sendo:

```text
dados
→ Pacheco

critérios / normalização / CRITIC
→ Benjamin

TOPSIS / Pareto / robustez
→ Vitor

relatório / apresentação
→ Marco

revisão integrada
→ Boss
```

---

# Erros devem ser corrigidos na origem

Princípio fundamental:

```text
ERRO UPSTREAM
↓
CORRIGIR UPSTREAM
↓
NOVA VERSÃO
↓
REEXECUTAR DOWNSTREAM
↓
NOVA REVISÃO
```

Nunca:

```text
ERRO UPSTREAM
↓
CORRIGIR MANUALMENTE NO RELATÓRIO
```

---

# Exemplo

Se Vitor detectar problema nos pesos:

```text
AGENTE_VITOR
↓
registra o problema
↓
AGENTE_BENJAMIN
↓
investiga
↓
corrige o CRITIC
↓
gera nova versão
↓
AGENTE_BOSS
↓
revisa novamente
```

Vitor não deve alterar os pesos silenciosamente.

---

# Estrutura do repositório

```text
PROJETO1/
│
├── .github/
├── agents/
├── analysis/
├── config/
├── data/
├── decisions/
├── handoffs/
├── instructions/
├── presentation/
├── R/
├── report/
├── results/
├── scripts/
├── templates/
├── tests/
│
├── AGENTS.md
├── CHANGELOG.md
├── compose.yaml
├── Dockerfile
├── FLUIDOS_CORTE.Rproj
├── Makefile
├── PROJECT_MAP.md
├── README.md
├── renv.lock
├── STATUS.md
└── _targets.R
```

Uma descrição detalhada da estrutura está em:

```text
PROJECT_MAP.md
```

---

# Dados

Os dados estão organizados em:

```text
data/
├── raw/
├── interim/
└── processed/
```

---

# Dados brutos

Arquivos originais ficam em:

```text
data/raw/
```

Regra:

```text
RAW DATA = IMMUTABLE
```

Os arquivos originais não devem ser:

```text
corrigidos manualmente
sobrescritos
editados
```

---

# Fonte original atualmente disponível

Atualmente existe material-fonte em:

```text
data/raw/
```

incluindo:

```text
ensaio_bancada_alunos (2).xlsx
```

O conteúdo ainda deverá ser oficialmente inventariado e auditado durante a execução de Pacheco.

---

# Dados intermediários

A pasta:

```text
data/interim/
```

será utilizada para artefatos intermediários quando necessário.

Estado atual:

```text
NOT_GENERATED
```

---

# Dados processados

A pasta:

```text
data/processed/
```

receberá futuramente dados processados e aprovados.

A base canônica deverá ser gerada por código.

Estado atual:

```text
CANONICAL_DATA_STATUS = NOT_CREATED
```

---

# Base canônica

A base canônica deverá ser:

```text
gerada por código
versionada
validada
documentada
rastreável
```

Ela se tornará a principal fonte de dados das etapas downstream.

---

# Não corrigir silenciosamente

Nenhum valor deve ser alterado apenas porque parece incorreto.

Fluxo obrigatório:

```text
detectar
↓
registrar
↓
investigar
↓
obter evidência
↓
decidir
↓
corrigir por código
```

---

# Missing

Regra importante:

```text
NA != 0
```

Ausência de informação não deve ser transformada automaticamente em zero.

---

# Outliers

Regra:

```text
OUTLIER
≠
ERRO AUTOMÁTICO
```

Valores extremos devem ser investigados antes de qualquer remoção.

---

# Configurações

A pasta:

```text
config/
```

centraliza regras estruturais e metodológicas.

Estrutura:

```text
config/
├── criterios.yml
├── project.yml
├── regras_validacao.yml
└── tolerancias.yml
```

---

# `config/project.yml`

Centraliza configurações gerais do projeto.

---

# `config/criterios.yml`

Deverá concentrar a definição dos critérios.

Estado:

```text
CRITERIA_STATUS = NOT_FINALIZED
```

---

# `config/regras_validacao.yml`

Centraliza regras que deverão ser verificadas durante a execução.

---

# `config/tolerancias.yml`

Centraliza tolerâncias numéricas e técnicas.

Valores ainda sem justificativa permanecem:

```text
null
```

ou:

```text
TO_BE_FILLED
```

---

# Instruções operacionais

A pasta:

```text
instructions/
```

contém instruções por integrante e por etapa.

Diferença conceitual:

```text
agents/
→ comportamento do agente

instructions/
→ procedimento da etapa

analysis/
→ execução e interpretação

R/
→ implementação
```

---

# Cadernos analíticos

A pasta:

```text
analysis/
```

contém:

```text
01_PACHECO_inventario.qmd
02_PACHECO_auditoria.qmd
03_PACHECO_reconciliacao.qmd
04_PACHECO_base_canonica.qmd
05_PACHECO_ada_inicial.qmd

06_BENJAMIN_ada_bivariada.qmd
07_BENJAMIN_ada_multivariada.qmd
08_BENJAMIN_conformidade.qmd
09_BENJAMIN_critic.qmd

10_VITOR_topsis.qmd
11_VITOR_cenarios_pareto.qmd
12_VITOR_robustez.qmd
```

Estado:

```text
ANALYSIS_TEMPLATES_STATUS = BASE_PREPARED

ANALYSIS_EXECUTION_STATUS = NOT_EXECUTED
```

---

# Código R

A implementação futura será organizada em:

```text
R/
├── pacheco/
├── benjamin/
├── vitor/
├── marco/
└── shared/
```

Estado atual:

```text
SCIENTIFIC_R_CODE_STATUS = NOT_IMPLEMENTED
```

---

# Código compartilhado

Funções utilizadas por mais de um integrante poderão ser colocadas em:

```text
R/shared/
```

para evitar duplicação.

---

# Scripts

A pasta:

```text
scripts/
```

possui arquivos destinados à futura orquestração.

Estado:

```text
SCRIPTS_STATUS = NOT_IMPLEMENTED
```

Eles serão implementados pelos integrantes durante a execução real.

---

# Testes

Os testes automatizados ficarão em:

```text
tests/testthat/
```

Framework planejado:

```text
testthat
```

Estado:

```text
TESTS_STATUS = NOT_IMPLEMENTED
```

Não devem ser implementados contra funções fictícias.

---

# Pipeline

O projeto prevê:

```text
targets
```

para coordenação da pipeline.

Arquivo:

```text
_targets.R
```

Estado:

```text
TARGETS_PIPELINE_STATUS = NOT_IMPLEMENTED
```

---

# Dependências R

O projeto prevê:

```text
renv
```

para gerenciamento das dependências.

O arquivo:

```text
renv.lock
```

deverá refletir os pacotes realmente utilizados.

Não deve ser preenchido manualmente com versões fictícias.

---

# Docker

A arquitetura prevê:

```text
Docker
+
Docker Compose
```

por meio de:

```text
Dockerfile
compose.yaml
```

para melhorar a reprodutibilidade do ambiente.

---

# Git

O projeto utiliza Git para controle de versão.

Uma organização planejada de branches é:

```text
pacheco/auditoria
benjamin/criterios
vitor/ranking
marco/relatorio
```

A integração deve ocorrer preferencialmente após revisão.

---

# Integração contínua

A configuração está em:

```text
.github/workflows/ci.yml
```

Estado atual:

```text
CI_STATUS = BASE_STRUCTURE_ONLY
```

A CI científica deverá ser expandida quando a implementação real existir.

---

# Handoffs

A pasta:

```text
handoffs/
```

formaliza as passagens entre os integrantes.

Estrutura:

```text
handoffs/
├── README.md
├── 01_PACHECO_to_BENJAMIN.md
├── 02_BENJAMIN_to_VITOR.md
├── 03_VITOR_to_MARCO.md
└── 04_MARCO_to_TODOS.md
```

---

# Fluxo dos handoffs

```text
Pacheco
↓
Benjamin
↓
Vitor
↓
Marco
↓
Todos
```

Um handoff deve indicar:

```text
o que está sendo entregue
qual versão
qual status
quais limitações
quais pendências
```

---

# Decisions

A pasta:

```text
decisions/
```

é utilizada para registrar decisões metodológicas relevantes.

Estrutura inicial:

```text
README.md
DEC-000-EXEMPLO.md
```

`DEC-000` é apenas um molde.

A primeira decisão real deverá começar em:

```text
DEC-001
```

---

# Resultados

Resultados gerados serão armazenados em:

```text
results/
```

podendo incluir:

```text
audit
ada
tables
figures
critic
topsis
scenarios
robustness
```

Estado atual:

```text
RESULTS_STATUS = NOT_GENERATED
```

---

# Regra de resultados

A pasta `results/` deve conter:

```text
outputs da execução
```

e não:

```text
material fornecido pela professora
templates
arquivos de referência
números digitados manualmente
```

---

# CRITIC

O projeto prevê utilização do CRITIC para obtenção de pesos informacionais.

Formulação de referência:

\[
C_j
=
\sigma_j
\sum_k(1-r_{jk})
\]

e:

\[
w_j
=
\frac{C_j}
{\sum_j C_j}
\]

---

# Regra de correlação no CRITIC

A formulação principal utiliza:

\[
1-r_{jk}
\]

e não:

\[
1-|r_{jk}|
\]

Não realizar essa substituição silenciosamente.

---

# Interpretação dos pesos CRITIC

Regra:

```text
CRITIC WEIGHT
=
INFORMATION WEIGHT
```

Não significa automaticamente:

```text
TECHNICAL IMPORTANCE
```

---

# TOPSIS

Depois da definição dos critérios, normalização e pesos, o ranking principal será calculado com TOPSIS.

Matriz ponderada:

\[
v_{ij}=w_jr_{ij}
\]

Distância ao ideal positivo:

\[
S_i^+
=
\sqrt{
\sum_j(v_{ij}-v_j^+)^2
}
\]

Distância ao ideal negativo:

\[
S_i^-
=
\sqrt{
\sum_j(v_{ij}-v_j^-)^2
}
\]

Coeficiente:

\[
C_i
=
\frac{S_i^-}
{S_i^+ + S_i^-}
\]

---

# Orientação dos critérios

Se a matriz entregue ao TOPSIS já estiver orientada como:

```text
maior = melhor
```

não inverter novamente critérios `COST`.

---

# Ranking principal versus ranking final

O primeiro resultado TOPSIS deverá ser considerado:

```text
PRIMARY_RANKING
```

e não automaticamente:

```text
FINAL_RANKING
```

Fluxo:

```text
TOPSIS
↓
cenários
↓
Pareto
↓
sensibilidade
↓
LOCO
↓
normalização alternativa
↓
LOAO
↓
rank reversal
↓
robustez
↓
interpretação final
```

---

# Conformidade técnica

O projeto mantém separação explícita entre:

```text
conformidade
```

e:

```text
desempenho multicritério
```

Portanto:

```text
boa posição no TOPSIS
```

não implica automaticamente:

```text
conformidade
```

---

# Pareto

A análise de Pareto será utilizada como ferramenta complementar.

Regra:

```text
PARETO NÃO UTILIZA PESOS
```

Uma alternativa não dominada não é automaticamente a vencedora.

---

# Robustez

A análise de robustez poderá incluir:

```text
cenários de pesos
sensibilidade
LOCO
normalizações alternativas
LOAO
rank reversal
```

---

# Frequências de cenários

Regra:

```text
frequência
≠
probabilidade real
```

Exemplo:

```text
uma alternativa ficou em primeiro em 80% dos cenários
```

não significa:

```text
80% de probabilidade de ser a melhor
```

---

# Correlação

Regra:

```text
CORRELAÇÃO
≠
CAUSALIDADE
```

---

# Relatório

O relatório final ficará em:

```text
report/final/
```

Arquivo principal:

```text
report/final/main.tex
```

---

# Formato do relatório

O modelo oficial fornecido pela professora possui prioridade.

A estrutura é:

```text
1. Introdução
2. Material e Método
3. Resultados e Discussão
4. Conclusões
5. Referências
```

---

# Regras formais conhecidas

```text
A4
10 pt
margens de 1,5 cm
duas colunas
máximo de 4 páginas incluindo referências
resumo de até 1200 caracteres com espaços
3 a 5 palavras-chave
```

---

# Relatórios internos

Detalhes técnicos ficam em:

```text
report/stages/
```

com áreas específicas para:

```text
Pacheco
Benjamin
Vitor
Marco
```

---

# Apresentação

A apresentação final será organizada em:

```text
presentation/
```

A arquitetura prevê:

```text
LaTeX/Beamer
```

Somente resultados aprovados deverão aparecer nos slides.

---

# Templates

A pasta:

```text
templates/
```

contém moldes reutilizáveis.

Eles não representam resultados científicos.

---

# Material fornecido pela professora

Materiais externos devem ser armazenados conforme sua função.

Exemplos:

```text
dados originais
→ data/raw/

logos
→ área de assets

material visual de referência
→ área de referência
```

Nunca tratar material externo como resultado produzido pelo grupo.

---

# Reprodutibilidade

O objetivo é permitir:

```text
clonar projeto
↓
configurar ambiente
↓
executar pipeline
↓
reproduzir resultados
```

com as mesmas entradas, configurações e versões.

---

# Evitar

```text
setwd()
caminhos absolutos pessoais
edições manuais escondidas
dependência de .RData
objetos antigos no workspace
resultados digitados manualmente
parâmetros científicos sem documentação
```

---

# Preferir

```text
caminhos relativos
funções reproduzíveis
configurações versionadas
controle de versão
pipeline
testes
revisão formal
```

---

# Mudança upstream

Se uma entrada aprovada for alterada:

```text
nova versão
↓
avaliação de impacto
↓
resultados afetados
↓
reexecução downstream
↓
nova revisão
```

Outputs antigos podem receber:

```text
SUPERSEDED
```

---

# Ordem recomendada de leitura

Para uma pessoa entrando no projeto:

```text
1. README.md
2. AGENTS.md
3. PROJECT_MAP.md
4. STATUS.md
5. agents/README.md
6. config/project.yml
7. agents/AGENTE_<RESPONSÁVEL>.md
8. instructions/ da etapa
9. handoff correspondente
10. analysis/ correspondente
```

---

# Ordem para um agente

```text
README.md
↓
AGENTS.md
↓
PROJECT_MAP.md
↓
STATUS.md
↓
agents/README.md
↓
arquivo específico do agente
↓
config/
↓
instructions/
↓
handoff
↓
artefatos da etapa
```

---

# Ordem de revisão do Boss

```text
agents/AGENTE_BOSS.md
↓
agents/REVIEW_PROTOCOL.md
↓
STATUS.md
↓
handoffs/
↓
config/
↓
artefatos da etapa
```

---

# Fontes de verdade

```text
dados brutos
→ data/raw/

configuração
→ config/

agentes
→ agents/

roteamento dos agentes
→ AGENTS.md

implementação
→ R/

análises
→ analysis/

resultados
→ results/

decisões
→ decisions/

handoffs
→ handoffs/

relatório
→ report/

apresentação
→ presentation/

estado atual
→ STATUS.md

histórico
→ CHANGELOG.md
```

---

# Estado atual dos agentes

```text
MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

AGENTS_ROUTER = BASE_PREPARED

AGENTE_PACHECO = BASE_PREPARED

AGENTE_BENJAMIN = BASE_PREPARED

AGENTE_VITOR = BASE_PREPARED

AGENTE_MARCO = BASE_PREPARED

AGENTE_BOSS = BASE_PREPARED

REVIEW_PROTOCOL = BASE_PREPARED
```

---

# Estado científico atual

```text
DATA_INVENTORY = NOT_EXECUTED

DATA_AUDIT = NOT_EXECUTED

RECONCILIATION = NOT_EXECUTED

CANONICAL_DATASET = NOT_CREATED

INITIAL_ADA = NOT_EXECUTED

BIVARIATE_ADA = NOT_EXECUTED

MULTIVARIATE_ADA = NOT_EXECUTED

CONFORMITY = NOT_EXECUTED

CRITERIA = NOT_FINALIZED

NORMALIZATION = NOT_EXECUTED

CRITIC = NOT_EXECUTED

TOPSIS = NOT_EXECUTED

SCENARIOS = NOT_EXECUTED

PARETO = NOT_EXECUTED

ROBUSTNESS = NOT_EXECUTED

FINAL_RANKING = NOT_GENERATED
```

---

# Estado da implementação

```text
SCIENTIFIC_R_CODE = NOT_IMPLEMENTED

SCRIPTS = NOT_IMPLEMENTED

TESTS = NOT_IMPLEMENTED

TARGETS_PIPELINE = NOT_IMPLEMENTED

MAKEFILE = NOT_IMPLEMENTED
```

---

# Próxima etapa científica

Depois da preparação estrutural:

```text
AGENTE_PACHECO
↓
ETAPA 01
↓
INVENTÁRIO
```

Arquivo:

```text
analysis/01_PACHECO_inventario.qmd
```

---

# Regra para início da execução

A partir da execução real:

```text
integrante
+
seu agente
```

passam a implementar e executar sua etapa.

O `AGENTE_BOSS` entra nos checkpoints de revisão.

---

# Regra para avanço entre integrantes

```text
Pacheco executa
↓
Boss revisa
↓
APPROVED
↓
Benjamin executa
↓
Boss revisa
↓
APPROVED
↓
Vitor executa
↓
Boss revisa
↓
APPROVED
↓
Marco integra
↓
Boss revisa
↓
revisão de todos
```

---

# O que não está definido ainda

Nesta fase ainda não estão definidos:

```text
critérios finais
TARGETs finais
pesos CRITIC
matriz de decisão final
ranking TOPSIS
top 1
top 3
fronteira de Pareto
estabilidade
conclusão científica
```

Essas informações dependerão da execução real.

---

# Princípios do projeto

```text
dados brutos são preservados

nenhuma correção é silenciosa

NA não é zero

outlier não é erro automático

correlação não implica causalidade

conformidade não é ranking

peso CRITIC não é importância técnica absoluta

Pareto não é ranking

frequência de cenários não é probabilidade

ranking principal não é automaticamente ranking final

erros devem ser corrigidos na origem

resultados precisam ser executados, validados e revisados
```

---

# Critério de sucesso

O projeto deverá permitir reconstruir:

```text
conclusão
↓
ranking
↓
TOPSIS
↓
CRITIC
↓
critérios
↓
base canônica
↓
reconciliação
↓
auditoria
↓
dados brutos
```

---

# Princípio final

> O objetivo deste repositório não é apenas produzir um ranking de fluidos de corte. O objetivo é construir uma cadeia científica em que dados, decisões, cálculos, revisões, resultados e conclusões possam ser compreendidos, auditados e reproduzidos pela equipe.