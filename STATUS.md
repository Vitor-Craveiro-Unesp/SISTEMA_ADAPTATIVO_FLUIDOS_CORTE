# STATUS

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Este arquivo registra o estado operacional atual do projeto.

Ele deve responder rapidamente:

```text
em que fase estamos?
o que já está preparado?
o que ainda não foi executado?
quem é responsável?
qual agente atua?
o que está bloqueado?
qual é a próxima etapa?
```

---

# 1. Estado geral

```text
PROJECT_STATUS = PACHECO_UNDER_REVIEW

ARCHITECTURE_STATUS = BASE_PREPARED

MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

IMPLEMENTATION_STATUS = PACHECO_IMPLEMENTED

SCIENTIFIC_EXECUTION_STATUS = PACHECO_EXECUTED_UNDER_REVIEW

SCIENTIFIC_RESULTS_STATUS = PACHECO_RESULTS_UNDER_REVIEW

FINAL_RANKING_STATUS = NOT_GENERATED

FINAL_REPORT_STATUS = NOT_READY

FINAL_PRESENTATION_STATUS = NOT_READY

FINAL_REVIEW_STATUS = NOT_READY

DELIVERY_STATUS = NOT_READY
```

---

# 2. Fase atual

O projeto encontra-se em:

```text
FASE = EXECUÇÃO PACHECO E REVISÃO BOSS
```

Nesta fase estão sendo preparados:

```text
estrutura do repositório
documentação
configurações-base
templates
instruções
cadernos analíticos
handoffs
arquitetura multiagente
protocolo de revisão
```

Ainda não estão sendo executados:

```text
inventário científico
auditoria
reconciliação
ADA
CRITIC
TOPSIS
Pareto
robustez
ranking final
```

---

# 3. Convenção de status

Os principais estados utilizados são:

```text
NOT_STARTED
NOT_EXECUTED
NOT_CREATED
NOT_GENERATED
NOT_READY
NOT_IMPLEMENTED
NOT_FINALIZED

AVAILABLE
BASE_PREPARED
DRAFT
UNDER_REVIEW
APPROVED
CHANGES_REQUESTED
BLOCKED
SUPERSEDED
```

---

# 4. Significado dos estados

## `NOT_STARTED`

A atividade ainda não começou.

---

## `NOT_EXECUTED`

A estrutura da etapa pode existir, mas a análise ainda não foi executada.

---

## `NOT_CREATED`

O artefato ainda não foi criado.

Exemplo:

```text
base canônica
```

---

## `NOT_GENERATED`

O artefato depende de execução científica e ainda não foi produzido.

Exemplos:

```text
ranking
tabela
figura
peso
```

---

## `NOT_READY`

O artefato ou handoff ainda não está pronto para utilização downstream.

---

## `NOT_IMPLEMENTED`

Existe previsão estrutural, mas a implementação real ainda não foi realizada.

---

## `NOT_FINALIZED`

A estrutura existe, mas a decisão científica ainda não foi concluída.

---

## `AVAILABLE`

O material existe e está disponível como entrada.

Não significa que tenha sido auditado ou aprovado.

---

## `BASE_PREPARED`

O esqueleto, template, documentação ou configuração-base está preparado.

Não significa execução científica.

---

## `DRAFT`

Conteúdo em construção.

---

## `UNDER_REVIEW`

Conteúdo executado e atualmente sob revisão.

---

## `APPROVED`

Conteúdo revisado e formalmente liberado.

---

## `CHANGES_REQUESTED`

A revisão identificou problemas corrigíveis antes da aprovação.

---

## `BLOCKED`

Existe problema que impede avanço confiável.

---

## `SUPERSEDED`

Uma versão posterior substituiu aquela versão.

---

# 5. Equipe

```text
Pacheco
→ inventário
→ auditoria
→ reconciliação
→ base canônica
→ ADA inicial

Benjamin
→ ADA bivariada
→ ADA multivariada
→ conformidade
→ critérios
→ matriz de decisão
→ normalização
→ CRITIC

Vitor
→ TOPSIS
→ ranking principal
→ cenários
→ Pareto
→ sensibilidade
→ robustez

Marco
→ integração
→ relatório
→ tabelas
→ figuras
→ apresentação
→ conclusões
→ limitações

Todos
→ infraestrutura
→ revisão cruzada
→ checkpoints
→ ensaio
→ revisão final
→ entrega
```

---

# 6. Arquitetura multiagente

O projeto utiliza:

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

Estrutura:

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

# 7. Status dos agentes

```text
MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

AGENTS_ROUTER = BASE_PREPARED

AGENTS_README = BASE_PREPARED

AGENTE_PACHECO = BASE_PREPARED

AGENTE_BENJAMIN = BASE_PREPARED

AGENTE_VITOR = BASE_PREPARED

AGENTE_MARCO = BASE_PREPARED

AGENTE_BOSS = BASE_PREPARED

REVIEW_PROTOCOL = BASE_PREPARED
```

---

# 8. Roteador central

Arquivo:

```text
AGENTS.md
```

Status:

```text
AGENTS_ROUTER = BASE_PREPARED
```

Função:

```text
tarefa
↓
etapa
↓
agente responsável
↓
arquivos relevantes
↓
revisão do Boss quando necessária
```

---

# 9. AGENTE_PACHECO

Arquivo:

```text
agents/AGENTE_PACHECO.md
```

Status:

```text
AGENTE_PACHECO = READY_FOR_BOSS_REVIEW
```

Escopo:

```text
01 — inventário
02 — auditoria
03 — reconciliação
04 — base canônica
05 — ADA inicial
```

---

# 10. AGENTE_BENJAMIN

Arquivo:

```text
agents/AGENTE_BENJAMIN.md
```

Status:

```text
AGENTE_BENJAMIN = BASE_PREPARED
```

Escopo:

```text
06 — ADA bivariada
07 — ADA multivariada
08 — conformidade
09 — critérios / normalização / CRITIC
```

---

# 11. AGENTE_VITOR

Arquivo:

```text
agents/AGENTE_VITOR.md
```

Status:

```text
AGENTE_VITOR = BASE_PREPARED
```

Escopo:

```text
10 — TOPSIS
11 — cenários / Pareto
12 — sensibilidade / robustez
```

---

# 12. AGENTE_MARCO

Arquivo:

```text
agents/AGENTE_MARCO.md
```

Status:

```text
AGENTE_MARCO = BASE_PREPARED
```

Escopo:

```text
integração
relatório
figuras
tabelas
apresentação
conclusões
limitações
```

---

# 13. AGENTE_BOSS

Arquivo:

```text
agents/AGENTE_BOSS.md
```

Status:

```text
AGENTE_BOSS = BASE_PREPARED
```

Função:

```text
revisão
auditoria
consistência
controle de dependências
handoffs
aprovação
bloqueio
revisão final
```

---

# 14. Protocolo de revisão

Arquivo:

```text
agents/REVIEW_PROTOCOL.md
```

Status:

```text
REVIEW_PROTOCOL = BASE_PREPARED

SCIENTIFIC_REVIEWS = NOT_STARTED

GLOBAL_REVIEW_STATUS = NOT_STARTED
```

O protocolo prevê:

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

# 15. Resultados possíveis de revisão

```text
APPROVED
CHANGES_REQUESTED
BLOCKED
```

Severidades:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

---

# 16. Regra multiagente

```text
AGENTE RESPONSÁVEL
↓
IMPLEMENTA
↓
EXECUTA
↓
VALIDA
↓
DOCUMENTA
↓
AGENTE_BOSS
↓
APPROVED
ou
CHANGES_REQUESTED
ou
BLOCKED
```

---

# 17. Regra de erro upstream

```text
ERRO UPSTREAM
↓
CORREÇÃO NA ORIGEM
↓
NOVA VERSÃO
↓
REEXECUÇÃO DOWNSTREAM
↓
NOVA REVISÃO
```

Nunca:

```text
ERRO UPSTREAM
↓
CORREÇÃO MANUAL APENAS NO RESULTADO FINAL
```

---

# 18. Infraestrutura

| Item | Status |
|---|---|
| Estrutura de diretórios | `BASE_PREPARED` |
| `FLUIDOS_CORTE.Rproj` | `BASE_PREPARED` |
| Documentação principal | `BASE_PREPARED` |
| Arquitetura multiagente | `BASE_PREPARED` |
| Configuração-base | `BASE_PREPARED` |
| Templates | `BASE_PREPARED` |
| Git local | `TO_BE_CONFIRMED` |
| Repositório remoto | `TO_BE_CONFIRMED` |
| CI estrutural | `BASE_PREPARED` |
| Docker | `BASE_PREPARED_OR_TO_BE_TESTED` |
| Docker Compose | `BASE_PREPARED_OR_TO_BE_TESTED` |
| renv | `NOT_IMPLEMENTED` |
| targets | `NOT_IMPLEMENTED` |
| testthat | `NOT_IMPLEMENTED` |
| Makefile | `NOT_IMPLEMENTED` |

---

# 19. Documentação principal

```text
README.md
→ BASE_PREPARED

AGENTS.md
→ BASE_PREPARED

PROJECT_MAP.md
→ BASE_PREPARED

STATUS.md
→ BASE_PREPARED

CHANGELOG.md
→ BASE_PREPARED
```

---

# 20. Dados

Estrutura:

```text
data/
├── raw/
├── interim/
└── processed/
```

Status:

```text
RAW_DATA_STATUS = AVAILABLE

INTERIM_DATA_STATUS = GENERATED_VERIFIED

PROCESSED_DATA_STATUS = GENERATED_UNDER_REVIEW

CANONICAL_DATA_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 21. Dados brutos

Material atualmente conhecido em:

```text
data/raw/
```

inclui:

```text
ensaio_bancada_alunos (2).xlsx
linkacessodrive.txt
README.md
.gitkeep
```

Status:

```text
SOURCE_DATA = AVAILABLE

SOURCE_DATA_INVENTORY = NOT_EXECUTED

SOURCE_DATA_AUDIT = NOT_EXECUTED
```

---

# 22. Política de raw

```text
RAW_DATA_POLICY = IMMUTABLE
```

Não realizar:

```text
correção manual
sobrescrita
edição direta
```

---

# 23. Pacheco — visão geral

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO
```

Status geral:

```text
PACHECO_STAGE_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 24. Etapa 01 — Inventário

Arquivo:

```text
analysis/01_PACHECO_inventario.qmd
```

Estado:

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO

TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 25. Etapa 02 — Auditoria

Arquivo:

```text
analysis/02_PACHECO_auditoria.qmd
```

Estado:

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO

TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 26. Etapa 03 — Reconciliação

Arquivo:

```text
analysis/03_PACHECO_reconciliacao.qmd
```

Estado:

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO

TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 27. Etapa 04 — Base canônica

Arquivo:

```text
analysis/04_PACHECO_base_canonica.qmd
```

Estado:

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO

TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = READY_FOR_BOSS_REVIEW

CANONICAL_DATA_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 28. Etapa 05 — ADA inicial

Arquivo:

```text
analysis/05_PACHECO_ada_inicial.qmd
```

Estado:

```text
RESPONSIBLE = Pacheco

AGENT = AGENTE_PACHECO

TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = READY_FOR_BOSS_REVIEW
```

---

# 29. Handoff Pacheco → Benjamin

Arquivo:

```text
handoffs/01_PACHECO_to_BENJAMIN.md
```

Estado:

```text
HANDOFF_STATUS = READY_FOR_BOSS_REVIEW

BOSS_REVIEW_STATUS = NOT_YET_REVIEWED
```

Só poderá ser liberado após:

```text
inventário
auditoria
reconciliação
base canônica
ADA inicial
revisão do AGENTE_BOSS
```

---

# 30. Benjamin — visão geral

```text
RESPONSIBLE = Benjamin

AGENT = AGENTE_BENJAMIN

BENJAMIN_STAGE_STATUS = NOT_STARTED
```

---

# 31. Etapa 06 — ADA bivariada

Arquivo:

```text
analysis/06_BENJAMIN_ada_bivariada.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = NOT_EXECUTED
```

---

# 32. Etapa 07 — ADA multivariada

Arquivo:

```text
analysis/07_BENJAMIN_ada_multivariada.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

EXECUTION_STATUS = NOT_EXECUTED
```

---

# 33. Etapa 08 — Conformidade

Arquivo:

```text
analysis/08_BENJAMIN_conformidade.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

CONFORMITY_STATUS = NOT_EXECUTED
```

---

# 34. Etapa 09 — Critérios / Normalização / CRITIC

Arquivo:

```text
analysis/09_BENJAMIN_critic.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

CRITERIA_STATUS = NOT_FINALIZED

DECISION_MATRIX_STATUS = NOT_CREATED

NORMALIZATION_STATUS = NOT_EXECUTED

CRITIC_STATUS = NOT_EXECUTED

CRITIC_WEIGHTS_STATUS = NOT_GENERATED
```

---

# 35. Handoff Benjamin → Vitor

Arquivo:

```text
handoffs/02_BENJAMIN_to_VITOR.md
```

Estado:

```text
HANDOFF_STATUS = NOT_READY

BOSS_REVIEW_STATUS = NOT_STARTED
```

Só poderá ser liberado após aprovação de:

```text
ADA aprofundada
conformidade
critérios
matriz de decisão
normalização
CRITIC
```

---

# 36. Vitor — visão geral

```text
RESPONSIBLE = Vitor

AGENT = AGENTE_VITOR

VITOR_STAGE_STATUS = NOT_STARTED
```

---

# 37. Etapa 10 — TOPSIS

Arquivo:

```text
analysis/10_VITOR_topsis.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

TOPSIS_STATUS = NOT_EXECUTED

PRIMARY_RANKING_STATUS = NOT_GENERATED
```

---

# 38. Etapa 11 — Cenários e Pareto

Arquivo:

```text
analysis/11_VITOR_cenarios_pareto.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

SCENARIO_STATUS = NOT_EXECUTED

PARETO_STATUS = NOT_EXECUTED
```

---

# 39. Etapa 12 — Robustez

Arquivo:

```text
analysis/12_VITOR_robustez.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

WEIGHT_SENSITIVITY_STATUS = NOT_EXECUTED

LOCO_STATUS = NOT_EXECUTED

NORMALIZATION_ROBUSTNESS_STATUS = NOT_EXECUTED

LOAO_STATUS = NOT_EXECUTED

RANK_REVERSAL_STATUS = NOT_EXECUTED

ROBUSTNESS_STATUS = NOT_EXECUTED

FINAL_RANKING_STATUS = NOT_GENERATED
```

---

# 40. Handoff Vitor → Marco

Arquivo:

```text
handoffs/03_VITOR_to_MARCO.md
```

Estado:

```text
HANDOFF_STATUS = NOT_READY

BOSS_REVIEW_STATUS = NOT_STARTED
```

---

# 41. Marco — visão geral

```text
RESPONSIBLE = Marco

AGENT = AGENTE_MARCO

MARCO_STAGE_STATUS = NOT_STARTED
```

---

# 42. Integração

Arquivo principal:

```text
report/stages/04_marco/relatorio_integracao.qmd
```

Estado:

```text
TEMPLATE_STATUS = BASE_PREPARED

INTEGRATION_STATUS = NOT_EXECUTED

SCIENTIFIC_CONTENT_STATUS = NOT_GENERATED
```

---

# 43. Relatório final

Arquivo principal:

```text
report/final/main.tex
```

Estado:

```text
REPORT_TEMPLATE_STATUS = BASE_PREPARED

REPORT_SCIENTIFIC_CONTENT = NOT_GENERATED

FINAL_REPORT_STATUS = NOT_READY
```

---

# 44. Referências

Arquivo:

```text
report/final/references.bib
```

Estado:

```text
REFERENCES_STATUS = EMPTY_BY_DESIGN
```

Nenhuma referência fictícia deve ser adicionada.

---

# 45. Apresentação

Estrutura:

```text
presentation/
```

Estado:

```text
PRESENTATION_BASE_STATUS = BASE_PREPARED

PRESENTATION_RESULTS = NOT_GENERATED

FINAL_PRESENTATION_STATUS = NOT_READY
```

---

# 46. Handoff Marco → Todos

Arquivo:

```text
handoffs/04_MARCO_to_TODOS.md
```

Estado:

```text
HANDOFF_STATUS = NOT_READY

BOSS_REVIEW_STATUS = NOT_STARTED
```

---

# 47. Configuração

Estrutura:

```text
config/
├── criterios.yml
├── project.yml
├── regras_validacao.yml
└── tolerancias.yml
```

Status:

```text
CONFIG_STRUCTURE_STATUS = BASE_PREPARED
```

---

# 48. `config/project.yml`

```text
STATUS = BASE_PREPARED
```

---

# 49. `config/criterios.yml`

```text
STATUS = BASE_PREPARED

FINAL_CRITERIA_STATUS = NOT_FINALIZED
```

---

# 50. `config/regras_validacao.yml`

```text
STATUS = BASE_PREPARED

AUTOMATED_VALIDATION_STATUS = NOT_IMPLEMENTED
```

---

# 51. `config/tolerancias.yml`

```text
STATUS = BASE_PREPARED

COMPUTATIONAL_TOLERANCES = NOT_DEFINED_OR_NOT_FINALIZED

TECHNICAL_TOLERANCES = NOT_DEFINED_OR_NOT_FINALIZED
```

---

# 52. Instructions

A estrutura:

```text
instructions/
```

está preparada.

Estado:

```text
INSTRUCTIONS_STATUS = BASE_PREPARED
```

---

# 53. Analysis

Os 12 cadernos analíticos estão preparados estruturalmente.

```text
ANALYSIS_TEMPLATES_STATUS = BASE_PREPARED

ANALYSIS_EXECUTION_STATUS = NOT_EXECUTED
```

---

# 54. Templates

A estrutura:

```text
templates/
```

está preparada para:

```text
etapas
figuras
tabelas
relatório
apresentação
```

Estado:

```text
TEMPLATES_STATUS = BASE_PREPARED
```

---

# 55. Decisions

Estrutura:

```text
decisions/
```

Estado:

```text
DECISION_SYSTEM_STATUS = BASE_PREPARED

REAL_DECISIONS = NONE_OR_NOT_REGISTERED
```

O arquivo:

```text
DEC-000-EXEMPLO.md
```

é apenas modelo.

---

# 56. Handoffs

Estrutura:

```text
handoffs/
```

Estado:

```text
HANDOFF_TEMPLATES_STATUS = BASE_PREPARED

ACTIVE_HANDOFF = NONE
```

---

# 57. Código R

Estrutura:

```text
R/
```

Estado:

```text
SCIENTIFIC_R_CODE_STATUS = NOT_IMPLEMENTED
```

A implementação científica será realizada pelos integrantes durante suas etapas.

---

# 58. Scripts

Estrutura atualmente prevista:

```text
scripts/
├── build_canonical_data.R
├── render_all.R
├── run_ada.R
├── run_audit.R
└── run_ranking.R
```

Estado:

```text
SCRIPTS_STATUS = NOT_IMPLEMENTED
```

---

# 59. Testes

Estrutura:

```text
tests/testthat/
```

Estado:

```text
TESTS_STATUS = NOT_IMPLEMENTED
```

Os testes deverão ser implementados após as funções reais existirem.

---

# 60. Pipeline `targets`

Arquivo:

```text
_targets.R
```

Estado:

```text
TARGETS_PIPELINE_STATUS = NOT_IMPLEMENTED
```

---

# 61. `renv`

Arquivo:

```text
renv.lock
```

Estado:

```text
RENV_STATUS = NOT_CONFIGURED_OR_NOT_CONFIRMED
```

O lockfile deverá ser produzido pelo ambiente realmente utilizado.

---

# 62. Makefile

Arquivo:

```text
Makefile
```

Estado:

```text
MAKEFILE_STATUS = NOT_IMPLEMENTED
```

Não deve receber comandos fictícios apenas para preencher o arquivo.

---

# 63. CI

Arquivo:

```text
.github/workflows/ci.yml
```

Estado:

```text
CI_STATUS = BASE_STRUCTURE_ONLY
```

Ainda não executa a análise científica completa.

---

# 64. Docker

Arquivos:

```text
Dockerfile
compose.yaml
```

Estado:

```text
DOCKER_STRUCTURE_STATUS = BASE_PREPARED

DOCKER_RUNTIME_VALIDATION = NOT_EXECUTED_OR_NOT_CONFIRMED
```

---

# 65. Git

Estado deverá ser atualizado conforme o repositório real.

```text
LOCAL_GIT_STATUS = TO_BE_CONFIRMED

REMOTE_REPOSITORY_STATUS = TO_BE_CONFIRMED
```

---

# 66. Resultados científicos

Atualmente:

```text
AUDIT_RESULTS = NOT_GENERATED

ADA_RESULTS = NOT_GENERATED

CONFORMITY_RESULTS = NOT_GENERATED

CRITIC_RESULTS = NOT_GENERATED

TOPSIS_RESULTS = NOT_GENERATED

SCENARIO_RESULTS = NOT_GENERATED

PARETO_RESULTS = NOT_GENERATED

ROBUSTNESS_RESULTS = NOT_GENERATED
```

---

# 67. Ranking

```text
PRIMARY_RANKING = NOT_GENERATED

FINAL_RANKING = NOT_GENERATED

TOP_1 = NOT_DEFINED

TOP_3 = NOT_DEFINED
```

Nenhum fluido deve ser apresentado como vencedor nesta fase.

---

# 68. Critérios

```text
FINAL_CRITERIA = NOT_DEFINED

CRITERION_DIRECTIONS = NOT_DEFINED

TARGET_CRITERIA = NOT_DEFINED
```

---

# 69. Pesos

```text
CRITIC_WEIGHTS = NOT_GENERATED
```

---

# 70. Conformidade

```text
TECHNICAL_CONFORMITY = NOT_EXECUTED
```

---

# 71. Pareto

```text
PARETO_FRONT = NOT_GENERATED
```

---

# 72. Robustez

```text
WEIGHT_SENSITIVITY = NOT_EXECUTED

LOCO = NOT_EXECUTED

NORMALIZATION_ROBUSTNESS = NOT_EXECUTED

LOAO = NOT_EXECUTED

RANK_REVERSAL = NOT_EXECUTED

ROBUSTNESS_CLASS = NOT_DEFINED
```

---

# 73. Estado das revisões do Boss

```text
PACHECO_REVIEW = NOT_STARTED

BENJAMIN_REVIEW = NOT_STARTED

VITOR_REVIEW = NOT_STARTED

MARCO_REVIEW = NOT_STARTED

GLOBAL_FINAL_REVIEW = NOT_STARTED
```

---

# 74. Condição de avanço — Pacheco

Para avançar para Benjamin:

```text
PACHECO_STAGE
↓
UNDER_REVIEW
↓
AGENTE_BOSS
↓
APPROVED
↓
HANDOFF 01
```

---

# 75. Condição de avanço — Benjamin

Para avançar para Vitor:

```text
BENJAMIN_STAGE
↓
UNDER_REVIEW
↓
AGENTE_BOSS
↓
APPROVED
↓
HANDOFF 02
```

---

# 76. Condição de avanço — Vitor

Para avançar para Marco:

```text
VITOR_STAGE
↓
UNDER_REVIEW
↓
AGENTE_BOSS
↓
APPROVED
↓
HANDOFF 03
```

---

# 77. Condição de avanço — Marco

Para entrega:

```text
MARCO_INTEGRATION
↓
UNDER_REVIEW
↓
AGENTE_BOSS
↓
APPROVED
↓
TODOS
↓
REVISÃO FINAL
```

---

# 78. Regra de versões

Se uma etapa aprovada for alterada:

```text
nova versão
↓
outputs dependentes avaliados
↓
outputs antigos podem virar SUPERSEDED
↓
reexecução
↓
nova revisão
```

---

# 79. Regra de resultado obsoleto

Um output:

```text
SUPERSEDED
```

não deve alimentar:

```text
ranking atual
relatório final
apresentação final
```

---

# 80. Regra de arquivos existentes

Arquivo criado não significa etapa executada.

Exemplo:

```text
analysis/09_BENJAMIN_critic.qmd
```

pode estar:

```text
BASE_PREPARED
```

enquanto:

```text
CRITIC_STATUS = NOT_EXECUTED
```

---

# 81. Regra de conclusão de etapa

Uma etapa só deve ser considerada concluída após:

```text
implementação
+
execução
+
validação
+
documentação
+
revisão
```

Quando necessário:

```text
+
handoff
```

---

# 82. Próxima fase do projeto

Após concluir a preparação estrutural:

```text
FASE = IMPLEMENTAÇÃO E EXECUÇÃO
```

---

# 83. Próxima etapa científica

Responsável:

```text
Pacheco
```

Agente:

```text
AGENTE_PACHECO
```

Etapa:

```text
01 — INVENTÁRIO
```

Arquivo:

```text
analysis/01_PACHECO_inventario.qmd
```

Estado atual:

```text
NOT_EXECUTED
```

---

# 84. Primeiro checkpoint do Boss

O primeiro checkpoint científico acontecerá depois que Pacheco concluir o conjunto de etapas necessário ao:

```text
handoffs/01_PACHECO_to_BENJAMIN.md
```

Então:

```text
AGENTE_BOSS
↓
agents/REVIEW_PROTOCOL.md
↓
revisão
↓
APPROVED / CHANGES_REQUESTED / BLOCKED
```

---

# 85. Resumo rápido

```text
ARQUITETURA DO REPOSITÓRIO
✓ BASE_PREPARED

DOCUMENTAÇÃO PRINCIPAL
✓ BASE_PREPARED

ARQUITETURA DE 5 AGENTES
✓ BASE_PREPARED

AGENTE_PACHECO
✓ BASE_PREPARED

AGENTE_BENJAMIN
✓ BASE_PREPARED

AGENTE_VITOR
✓ BASE_PREPARED

AGENTE_MARCO
✓ BASE_PREPARED

AGENTE_BOSS
✓ BASE_PREPARED

PROTOCOLO DE REVISÃO
✓ BASE_PREPARED

DADOS ORIGINAIS
✓ AVAILABLE

IMPLEMENTAÇÃO R
✗ NOT_IMPLEMENTED

INVENTÁRIO
✗ NOT_EXECUTED

AUDITORIA
✗ NOT_EXECUTED

RECONCILIAÇÃO
✗ NOT_EXECUTED

BASE CANÔNICA
✗ NOT_CREATED

ADA
✗ NOT_EXECUTED

CRITÉRIOS
✗ NOT_FINALIZED

CONFORMIDADE
✗ NOT_EXECUTED

CRITIC
✗ NOT_EXECUTED

TOPSIS
✗ NOT_EXECUTED

PARETO
✗ NOT_EXECUTED

ROBUSTEZ
✗ NOT_EXECUTED

RANKING FINAL
✗ NOT_GENERATED

RELATÓRIO COM RESULTADOS
✗ NOT_GENERATED

APRESENTAÇÃO COM RESULTADOS
✗ NOT_GENERATED

REVISÃO CIENTÍFICA DO BOSS
✗ NOT_STARTED

ENTREGA FINAL
✗ NOT_READY
```

---

# 86. Princípios metodológicos ativos

```text
data/raw/ é imutável

NA não é zero

outlier não é erro automático

correlação não implica causalidade

conformidade não é ranking

peso CRITIC é peso informacional

CRITIC utiliza 1-r como formulação principal

Pareto não utiliza pesos

frequência de cenário não é probabilidade

ranking principal não é automaticamente ranking final

erro upstream deve ser corrigido upstream
```

---

# 87. Princípio final

> O STATUS deve refletir aquilo que foi realmente realizado. Arquitetura preparada não significa análise executada; arquivo criado não significa resultado validado; e resultado calculado não significa etapa aprovada. O avanço científico ocorre apenas após implementação, execução, validação, documentação e revisão.
