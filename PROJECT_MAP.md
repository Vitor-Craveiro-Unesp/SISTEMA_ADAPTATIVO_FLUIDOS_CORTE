# PROJECT MAP

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Este arquivo funciona como o mapa estrutural do projeto.

Seu objetivo é permitir que:

```text
integrantes
agentes
revisores
```

entendam rapidamente:

```text
onde cada coisa está
qual é a função de cada pasta
quem é responsável por cada etapa
como as etapas se conectam
quais arquivos são fontes de verdade
```

---

# 1. Visão geral do projeto

O objetivo do projeto é construir um sistema estatístico e multicritério para comparação e classificação de fluidos de corte.

O fluxo científico planejado é:

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

# 2. Princípio estrutural

O repositório separa explicitamente:

```text
dados
código
configuração
análise
resultados
decisões
documentação
relatório
apresentação
```

A regra geral é:

```text
cada tipo de informação
→ possui um local principal
```

Isso reduz:

```text
duplicação
ambiguidade
resultados contraditórios
edições manuais escondidas
```

---

# 3. Estrutura principal

```text
PROJETO1/
│
├── .github/
│
├── agents/
│
├── analysis/
│
├── config/
│
├── data/
│
├── decisions/
│
├── handoffs/
│
├── instructions/
│
├── presentation/
│
├── R/
│
├── report/
│
├── results/
│
├── scripts/
│
├── templates/
│
├── tests/
│
├── .dockerignore
├── .gitignore
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

---

# 4. Arquivos principais da raiz

## `README.md`

Documento principal de apresentação do projeto.

Deve explicar:

```text
objetivo
metodologia
equipe
estrutura
reprodutibilidade
situação atual
```

---

## `AGENTS.md`

Roteador central da arquitetura multiagente.

Sua função é identificar:

```text
qual tarefa foi solicitada
↓
qual etapa está envolvida
↓
qual agente deve atuar
↓
quais arquivos devem ser consultados
↓
quando o AGENTE_BOSS deve revisar
```

Os cinco agentes são:

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

As definições individuais estão em:

```text
agents/
```

---

## `PROJECT_MAP.md`

Este arquivo.

Serve como mapa de navegação do repositório.

---

## `STATUS.md`

Registra o estado atual das etapas e artefatos.

Estados utilizados podem incluir:

```text
NOT_STARTED
NOT_EXECUTED
NOT_CREATED
NOT_GENERATED
BASE_PREPARED
DRAFT
UNDER_REVIEW
APPROVED
BLOCKED
SUPERSEDED
```

---

## `CHANGELOG.md`

Registra mudanças importantes na arquitetura, metodologia e organização do projeto.

Exemplos:

```text
mudança de arquitetura
mudança de responsabilidade
alteração metodológica
nova etapa
nova estrutura de agentes
```

---

## `FLUIDOS_CORTE.Rproj`

Configuração do projeto R/RStudio.

Deve evitar dependência de:

```text
workspace antigo
.RData
configuração local escondida
```

---

## `_targets.R`

Futura definição da pipeline reproduzível com:

```text
targets
```

Estado atual:

```text
NOT_IMPLEMENTED
```

Não deve receber lógica científica fictícia apenas para completar a estrutura.

---

## `renv.lock`

Arquivo que deverá registrar as versões reais dos pacotes utilizados por meio do:

```text
renv
```

Não deve ser preenchido manualmente com versões inventadas.

---

## `Makefile`

Arquivo destinado à futura automação de comandos.

Poderá futuramente coordenar:

```text
testes
pipeline
relatório
apresentação
renderização
```

Estado atual:

```text
NOT_IMPLEMENTED
```

---

## `Dockerfile`

Arquivo destinado à definição do ambiente containerizado do projeto.

---

## `compose.yaml`

Configuração para execução do ambiente via Docker Compose.

---

# 5. Arquitetura multiagente

O projeto utiliza cinco agentes especializados.

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

A pasta responsável por essa arquitetura é:

```text
agents/
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

# 6. `agents/README.md`

Explica a arquitetura multiagente de forma geral.

Define:

```text
papel de cada agente
limites
fluxo entre etapas
relação com handoffs
relação com o Boss
```

---

# 7. `agents/AGENTE_PACHECO.md`

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

Escopo principal:

```text
analysis/01_PACHECO_inventario.qmd
analysis/02_PACHECO_auditoria.qmd
analysis/03_PACHECO_reconciliacao.qmd
analysis/04_PACHECO_base_canonica.qmd
analysis/05_PACHECO_ada_inicial.qmd
```

Código futuro relacionado:

```text
R/pacheco/
```

Handoff principal:

```text
handoffs/01_PACHECO_to_BENJAMIN.md
```

---

# 8. `agents/AGENTE_BENJAMIN.md`

Agente pessoal de Benjamin.

Especialidade:

```text
ADA bivariada
ADA multivariada
correlação
redundância
conformidade
critérios
matriz de decisão
normalização
CRITIC
```

Escopo principal:

```text
analysis/06_BENJAMIN_ada_bivariada.qmd
analysis/07_BENJAMIN_ada_multivariada.qmd
analysis/08_BENJAMIN_conformidade.qmd
analysis/09_BENJAMIN_critic.qmd
```

Código futuro relacionado:

```text
R/benjamin/
```

Configuração especialmente relevante:

```text
config/criterios.yml
```

Handoff principal:

```text
handoffs/02_BENJAMIN_to_VITOR.md
```

---

# 9. `agents/AGENTE_VITOR.md`

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

Escopo principal:

```text
analysis/10_VITOR_topsis.qmd
analysis/11_VITOR_cenarios_pareto.qmd
analysis/12_VITOR_robustez.qmd
```

Código futuro relacionado:

```text
R/vitor/
```

Handoff principal:

```text
handoffs/03_VITOR_to_MARCO.md
```

---

# 10. `agents/AGENTE_MARCO.md`

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
R/marco/
```

Handoff principal:

```text
handoffs/04_MARCO_to_TODOS.md
```

---

# 11. `agents/AGENTE_BOSS.md`

Agente supervisor do projeto.

O Boss não substitui silenciosamente os demais agentes.

Sua função é:

```text
revisar
auditar
verificar dependências
identificar inconsistências
controlar versões científicas
verificar handoffs
solicitar correções
aprovar
bloquear
realizar revisão global
```

O Boss possui visão transversal do repositório.

---

# 12. `agents/REVIEW_PROTOCOL.md`

Define o protocolo formal de revisão do Boss.

As etapas da revisão são:

```text
PRECHECK
INPUT REVIEW
METHOD REVIEW
OUTPUT REVIEW
HANDOFF REVIEW
```

Os níveis de severidade são:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

Os resultados possíveis de uma revisão são:

```text
APPROVED
CHANGES_REQUESTED
BLOCKED
```

---

# 13. Fluxo dos agentes

O fluxo científico permanece sequencial:

```text
AGENTE_PACHECO
↓
AGENTE_BENJAMIN
↓
AGENTE_VITOR
↓
AGENTE_MARCO
```

O Boss atua transversalmente:

```text
                    AGENTE_BOSS
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ↓              ↓              ↓
 AGENTE_PACHECO   AGENTE_BENJAMIN   AGENTE_VITOR
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                   AGENTE_MARCO
                         │
                         ↓
                    AGENTE_BOSS
```

---

# 14. Propriedade científica

A responsabilidade principal é:

```text
dados
→ Pacheco

critérios / normalização / CRITIC
→ Benjamin

TOPSIS / cenários / Pareto / robustez
→ Vitor

relatório / apresentação
→ Marco

revisão integrada
→ Boss
```

---

# 15. Regra de erro upstream

A arquitetura segue:

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
CORREÇÃO MANUAL NO RESULTADO FINAL
```

---

# 16. Exemplo de comunicação entre agentes

Se Vitor identificar problema nos pesos:

```text
AGENTE_VITOR
↓
registra o problema
↓
AGENTE_BENJAMIN
↓
investiga
↓
corrige na origem
↓
reexecuta CRITIC
↓
novo handoff
↓
AGENTE_BOSS
↓
nova revisão
```

Vitor não deve alterar silenciosamente os pesos de Benjamin.

---

# 17. `.github/`

Estrutura:

```text
.github/
└── workflows/
    └── ci.yml
```

A CI inicial está destinada principalmente à validação estrutural do repositório.

Estado:

```text
CI_STATUS = BASE_STRUCTURE_ONLY
```

A execução científica poderá ser adicionada quando existirem:

```text
código R
renv
tests
targets
pipeline real
```

---

# 18. `data/`

Estrutura:

```text
data/
├── raw/
├── interim/
└── processed/
```

---

# 19. `data/raw/`

Contém as fontes originais.

Regra:

```text
RAW_DATA_POLICY = IMMUTABLE
```

Não deve ocorrer:

```text
edição manual
correção direta
sobrescrita
```

---

# 20. Material atualmente conhecido em `data/raw/`

A estrutura atualmente contém material como:

```text
ensaio_bancada_alunos (2).xlsx
linkacessodrive.txt
README.md
.gitkeep
```

A planilha é uma fonte original.

Seu conteúdo científico ainda deverá ser inventariado e auditado formalmente por Pacheco.

---

# 21. `data/interim/`

Destinado a dados intermediários produzidos durante:

```text
auditoria
reconciliação
transformações
```

Estado atual:

```text
NOT_GENERATED
```

---

# 22. `data/processed/`

Destinado aos dados processados e aprovados.

A base canônica deverá futuramente ser armazenada nessa área.

Estado atual:

```text
CANONICAL_DATA_STATUS = NOT_CREATED
```

---

# 23. Regra de dados

A cadeia ideal é:

```text
raw
↓
código
↓
interim
↓
validação
↓
processed
```

Não:

```text
raw
↓
edição manual
↓
planilha corrigida
```

---

# 24. `analysis/`

Contém os cadernos analíticos reproduzíveis.

Estrutura:

```text
analysis/
├── 01_PACHECO_inventario.qmd
├── 02_PACHECO_auditoria.qmd
├── 03_PACHECO_reconciliacao.qmd
├── 04_PACHECO_base_canonica.qmd
├── 05_PACHECO_ada_inicial.qmd
├── 06_BENJAMIN_ada_bivariada.qmd
├── 07_BENJAMIN_ada_multivariada.qmd
├── 08_BENJAMIN_conformidade.qmd
├── 09_BENJAMIN_critic.qmd
├── 10_VITOR_topsis.qmd
├── 11_VITOR_cenarios_pareto.qmd
└── 12_VITOR_robustez.qmd
```

Estado atual:

```text
ANALYSIS_TEMPLATES_STATUS = BASE_PREPARED

ANALYSIS_EXECUTION_STATUS = NOT_EXECUTED
```

---

# 25. Função de `analysis/`

Os arquivos `.qmd` servem como:

```text
caderno analítico
+
documentação de execução
+
interpretação
```

Eles não devem conter resultados inventados antes da execução real.

---

# 26. `config/`

Estrutura:

```text
config/
├── criterios.yml
├── project.yml
├── regras_validacao.yml
└── tolerancias.yml
```

---

# 27. `config/project.yml`

Fonte central de configuração estrutural do projeto.

Pode centralizar:

```text
identidade
responsáveis
etapas
dependências
diretórios
metodologia planejada
status
```

---

# 28. `config/criterios.yml`

Fonte principal para definição futura dos critérios.

Deve registrar, quando implementado:

```text
critérios candidatos
critérios incluídos
critérios excluídos
direções
TARGET
papéis
restrições
```

Estado atual:

```text
CRITERIA_STATUS = NOT_FINALIZED
```

---

# 29. `config/regras_validacao.yml`

Contém regras conceituais que futuramente deverão ser transformadas em validações e testes.

Inclui temas como:

```text
raw
inventário
auditoria
reconciliação
base canônica
ADA
CRITIC
TOPSIS
Pareto
robustez
```

---

# 30. `config/tolerancias.yml`

Centraliza tolerâncias numéricas e técnicas.

Regra:

```text
valor não definido
→ permanece null / TO_BE_FILLED
```

Não inventar tolerância apenas para fazer a análise passar.

---

# 31. `instructions/`

Contém instruções operacionais detalhadas por responsável e etapa.

Conceitualmente:

```text
agents/
→ COMO o agente deve se comportar

instructions/
→ O QUE fazer em cada etapa

analysis/
→ ONDE registrar execução e interpretação

R/
→ ONDE implementar funções
```

---

# 32. `R/`

Estrutura:

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

# 33. `R/pacheco/`

Futura implementação relacionada a:

```text
inventário
auditoria
reconciliação
base canônica
ADA inicial
```

---

# 34. `R/benjamin/`

Futura implementação relacionada a:

```text
ADA bivariada
ADA multivariada
conformidade
critérios
normalização
CRITIC
```

---

# 35. `R/vitor/`

Futura implementação relacionada a:

```text
TOPSIS
ranking
cenários
Pareto
sensibilidade
robustez
```

---

# 36. `R/marco/`

Futura implementação relacionada a:

```text
integração
tabelas finais
figuras finais
comunicação científica
```

quando necessário.

---

# 37. `R/shared/`

Destinado a funções reutilizadas por mais de uma etapa.

Objetivo:

```text
evitar duplicação
```

---

# 38. `scripts/`

Estrutura atualmente conhecida:

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

Esses arquivos pertencem à execução real e serão implementados pelos integrantes.

---

# 39. `tests/`

Estrutura:

```text
tests/
├── testthat/
│   ├── test-critic.R
│   ├── test-importacao.R
│   ├── test-medias.R
│   ├── test-reconciliacao.R
│   ├── test-somas.R
│   ├── test-topsis.R
│   └── test-unidades.R
└── _targets.R
```

Estado:

```text
TESTS_STATUS = NOT_IMPLEMENTED
```

---

# 40. Regra de testes

Os testes reais só devem ser implementados depois das funções reais existirem.

Não inventar APIs apenas para preencher os arquivos de teste.

---

# 41. `results/`

Destinado exclusivamente aos resultados gerados pela execução.

Estrutura conceitual:

```text
results/
├── audit/
├── ada/
├── tables/
├── figures/
├── critic/
├── topsis/
├── scenarios/
└── robustness/
```

Estado:

```text
RESULTS_STATUS = NOT_GENERATED
```

---

# 42. Regra de `results/`

Não colocar em `results/`:

```text
dados fornecidos pela professora
templates
material de referência
resultados digitados manualmente
```

A pasta deve representar:

```text
outputs gerados
```

---

# 43. `decisions/`

Estrutura:

```text
decisions/
├── README.md
└── DEC-000-EXEMPLO.md
```

---

# 44. Função de `decisions/`

Registrar decisões metodológicas importantes.

Exemplos:

```text
fonte oficial entre valores divergentes
normalização principal
definição de TARGET
exclusão relevante de critério
mudança importante no protocolo de robustez
```

---

# 45. `DEC-000-EXEMPLO.md`

É apenas modelo.

A primeira decisão real deverá utilizar:

```text
DEC-001
```

quando existir uma decisão concreta.

---

# 46. `handoffs/`

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

# 47. Fluxo dos handoffs

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

---

# 48. Função do handoff

O handoff funciona como contrato entre etapas.

Deve informar, quando aplicável:

```text
qual versão foi entregue
qual status possui
quais resultados são oficiais
quais limitações existem
quais issues permanecem abertas
```

---

# 49. Regra de handoff

Arquivo existente não significa:

```text
handoff aprovado
```

A aprovação depende da execução e revisão.

---

# 50. `report/`

Estrutura:

```text
report/
├── final/
├── stages/
└── templates/
```

---

# 51. `report/stages/`

Estrutura:

```text
report/stages/
├── 01_pacheco/
├── 02_benjamin/
├── 03_vitor/
└── 04_marco/
```

Esses documentos podem conter detalhes técnicos maiores que o relatório final.

---

# 52. Relatório de Pacheco

```text
report/stages/01_pacheco/relatorio_auditoria.qmd
```

---

# 53. Relatório de Benjamin

```text
report/stages/02_benjamin/relatorio_ada_criterios.qmd
```

---

# 54. Relatório de Vitor

```text
report/stages/03_vitor/relatorio_ranking.qmd
```

---

# 55. Relatório de Marco

```text
report/stages/04_marco/relatorio_integracao.qmd
```

---

# 56. `report/final/`

Estrutura:

```text
report/final/
├── chapters/
├── figures/
├── output/
├── tables/
├── main.tex
└── references.bib
```

---

# 57. `report/final/main.tex`

Documento principal do relatório final.

O template oficial fornecido pela professora possui prioridade sobre modelos genéricos.

---

# 58. Regras do relatório final

Estrutura oficial:

```text
1. Introdução
2. Material e Método
3. Resultados e Discussão
4. Conclusões
5. Referências
```

---

# 59. Formatação conhecida

```text
A4
10 pt
margens de 1,5 cm
duas colunas
máximo de 4 páginas incluindo referências
```

Resumo:

```text
até 1200 caracteres com espaços
```

Palavras-chave:

```text
3 a 5
```

---

# 60. `report/final/references.bib`

Destinado apenas às referências realmente utilizadas.

Estado inicial:

```text
EMPTY_BY_DESIGN
```

Não adicionar referências fictícias.

---

# 61. `presentation/`

Estrutura atualmente utilizada:

```text
presentation/
├── figures/
└── latex/
```

---

# 62. `presentation/figures/`

Destinado a figuras validadas utilizadas na apresentação.

Enquanto não houver resultados:

```text
NOT_GENERATED
```

---

# 63. `presentation/latex/`

Área destinada à apresentação final editável em LaTeX/Beamer.

O `README.md` dessa pasta documenta seu uso.

---

# 64. `templates/`

Contém modelos reutilizáveis.

Os templates são:

```text
moldes
```

e não:

```text
resultados
```

---

# 65. `templates/stage/EXEMPLO_BASE/`

Estrutura:

```text
README.md
checklist.md
analysis.qmd
script.R
```

Serve como modelo de etapa.

Não representa uma etapa científica executada.

---

# 66. `templates/presentation/`

Estrutura de apresentação preparada como base.

Inclui área LaTeX com:

```text
assets/
figures/
sections/
commands.tex
main.tex
preamble.tex
theme.tex
```

e material de referência separado.

---

# 67. Material externo

A regra geral é:

```text
dados originais
→ data/raw/

logos / assets
→ pasta apropriada de assets

material de referência
→ pasta de referência

resultados
→ results/
```

Nunca misturar fonte externa com output da análise.

---

# 68. Ordem recomendada de leitura

Para uma pessoa que entra no projeto:

```text
1. README.md
2. AGENTS.md
3. PROJECT_MAP.md
4. STATUS.md
5. agents/README.md
6. config/project.yml
7. arquivo do agente responsável
8. instructions/ da etapa
9. handoff correspondente
10. analysis/ correspondente
```

---

# 69. Ordem de leitura — Pacheco

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
agents/AGENTE_PACHECO.md
↓
config/
↓
instructions/pacheco/
↓
data/raw/
↓
analysis/01–05
```

---

# 70. Ordem de leitura — Benjamin

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
agents/AGENTE_BENJAMIN.md
↓
handoffs/01_PACHECO_to_BENJAMIN.md
↓
config/
↓
instructions/benjamin/
↓
analysis/06–09
```

---

# 71. Ordem de leitura — Vitor

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
agents/AGENTE_VITOR.md
↓
handoffs/02_BENJAMIN_to_VITOR.md
↓
config/
↓
instructions/vitor/
↓
analysis/10–12
```

---

# 72. Ordem de leitura — Marco

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
agents/AGENTE_MARCO.md
↓
handoffs/03_VITOR_to_MARCO.md
↓
report/
↓
presentation/
```

---

# 73. Ordem de leitura — Boss

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
agents/AGENTE_BOSS.md
↓
agents/REVIEW_PROTOCOL.md
↓
config/
↓
handoffs/
↓
artefatos da etapa em revisão
```

---

# 74. Ordem para agente em uma tarefa

Antes de alterar qualquer coisa:

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
agents/AGENTE_<RESPONSÁVEL>.md
↓
config/
↓
instructions da etapa
↓
handoff correspondente
↓
arquivos da etapa
```

---

# 75. Ordem de revisão formal

```text
AGENTE RESPONSÁVEL
↓
solicita revisão
↓
AGENTE_BOSS
↓
agents/AGENTE_BOSS.md
↓
agents/REVIEW_PROTOCOL.md
↓
artefatos
↓
APPROVED
ou
CHANGES_REQUESTED
ou
BLOCKED
```

---

# 76. Fonte de verdade por assunto

```text
dados brutos
→ data/raw/

configuração estrutural
→ config/

definição dos agentes
→ agents/

roteamento de agentes
→ AGENTS.md

implementação
→ R/

scripts de execução
→ scripts/

análise
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

histórico de mudanças
→ CHANGELOG.md
```

---

# 77. Dados versus resultados

```text
data/
→ dados

results/
→ outputs científicos

report/
→ comunicação escrita

presentation/
→ comunicação oral/visual
```

Essas funções não devem ser misturadas.

---

# 78. Código versus análise

```text
R/
→ funções reutilizáveis

scripts/
→ execução/orquestração

analysis/
→ cadernos analíticos

tests/
→ testes automatizados
```

---

# 79. Conformidade versus ranking

Regra metodológica fundamental:

```text
CONFORMIDADE
≠
RANKING
```

Uma alternativa pode:

```text
ter bom desempenho multicritério
```

e ainda assim:

```text
não atender determinada especificação
```

---

# 80. CRITIC

Formulação de referência:

\[
C_j
=
\sigma_j
\sum_k(1-r_{jk})
\]

\[
w_j
=
\frac{C_j}{\sum_j C_j}
\]

Regra:

```text
utilizar 1-r
```

Não substituir silenciosamente por:

```text
1-|r|
```

---

# 81. Interpretação dos pesos CRITIC

```text
peso CRITIC
=
peso informacional
```

Não significa automaticamente:

```text
importância técnica absoluta
```

---

# 82. TOPSIS

Matriz ponderada:

\[
v_{ij}=w_jr_{ij}
\]

Distâncias:

\[
S_i^+
=
\sqrt{
\sum_j(v_{ij}-v_j^+)^2
}
\]

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

# 83. Regra de orientação

Se a matriz já estiver orientada como:

```text
maior = melhor
```

não inverter novamente os critérios `COST` no TOPSIS.

---

# 84. Pareto

Regra:

```text
PARETO NÃO UTILIZA PESOS
```

Alternativa não dominada não significa automaticamente:

```text
melhor alternativa
```

---

# 85. Robustez

A análise prevista inclui, quando apropriado:

```text
cenários
sensibilidade de pesos
LOCO
normalização alternativa
LOAO
rank reversal
```

---

# 86. Frequências de robustez

Regra:

```text
frequência em cenários
≠
probabilidade real
```

---

# 87. Correlação

Regra:

```text
correlação
≠
causalidade
```

---

# 88. Mudanças upstream

Quando uma entrada aprovada for alterada:

```text
identificar mudança
↓
avaliar impacto
↓
nova versão
↓
marcar resultados afetados
↓
reexecutar downstream
↓
nova revisão
```

---

# 89. `SUPERSEDED`

Artefatos construídos sobre uma versão antiga devem ser considerados:

```text
SUPERSEDED
```

quando a alteração upstream os invalida.

---

# 90. Regra de implementação

Enquanto o projeto estiver na fase de arquitetura:

```text
documentação
templates
configuração-base
checklists
```

podem ser preparados.

Mas:

```text
resultados
cálculos
código científico
testes reais
pipeline real
```

devem ser implementados pelos integrantes durante a execução.

---

# 91. Estado atual da arquitetura

```text
PROJECT_STATUS = BASE_PREPARED

ARCHITECTURE_STATUS = BASE_PREPARED
```

---

# 92. Estado atual da arquitetura multiagente

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

# 93. Estado atual dos dados

```text
RAW_DATA_STATUS = AVAILABLE

DATA_INVENTORY = NOT_EXECUTED

DATA_AUDIT = NOT_EXECUTED

RECONCILIATION = NOT_EXECUTED

CANONICAL_DATASET = NOT_CREATED
```

---

# 94. Estado atual da análise

```text
INITIAL_ADA = NOT_EXECUTED

BIVARIATE_ADA = NOT_EXECUTED

MULTIVARIATE_ADA = NOT_EXECUTED

CONFORMITY = NOT_EXECUTED

CRITERIA = NOT_FINALIZED

DECISION_MATRIX = NOT_CREATED

NORMALIZATION = NOT_EXECUTED

CRITIC = NOT_EXECUTED

TOPSIS = NOT_EXECUTED

SCENARIOS = NOT_EXECUTED

PARETO = NOT_EXECUTED

ROBUSTNESS = NOT_EXECUTED
```

---

# 95. Estado atual dos resultados

```text
AUDIT_RESULTS = NOT_GENERATED

ADA_RESULTS = NOT_GENERATED

CRITIC_RESULTS = NOT_GENERATED

TOPSIS_RESULTS = NOT_GENERATED

SCENARIO_RESULTS = NOT_GENERATED

PARETO_RESULTS = NOT_GENERATED

ROBUSTNESS_RESULTS = NOT_GENERATED

FINAL_RANKING = NOT_GENERATED
```

---

# 96. Estado atual da implementação

```text
SCIENTIFIC_R_CODE = NOT_IMPLEMENTED

SCRIPTS = NOT_IMPLEMENTED

TESTS = NOT_IMPLEMENTED

TARGETS_PIPELINE = NOT_IMPLEMENTED

RENV = NOT_CONFIGURED_OR_NOT_CONFIRMED

MAKEFILE = NOT_IMPLEMENTED
```

---

# 97. Estado atual da comunicação final

```text
REPORT_TEMPLATE = BASE_PREPARED

REPORT_SCIENTIFIC_CONTENT = NOT_GENERATED

FINAL_REPORT = NOT_READY

PRESENTATION_TEMPLATE = BASE_PREPARED

PRESENTATION_RESULTS = NOT_GENERATED

FINAL_PRESENTATION = NOT_READY
```

---

# 98. Próxima fase científica

Quando a fase estrutural terminar, o início científico será:

```text
AGENTE_PACHECO
↓
01 — INVENTÁRIO
```

Arquivo correspondente:

```text
analysis/01_PACHECO_inventario.qmd
```

---

# 99. Regra para avanço

A existência de um arquivo não significa conclusão.

Exemplo:

```text
analysis/09_BENJAMIN_critic.qmd existe
```

não significa:

```text
CRITIC = EXECUTED
```

Conclusão exige:

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

---

# 100. Princípio final

> O PROJECT_MAP é o mapa de navegação do repositório. Ele não substitui README, AGENTS, STATUS, instructions ou handoffs. Sua função é mostrar como todas essas partes se conectam para formar uma única cadeia científica reproduzível, desde os dados brutos até a conclusão final.