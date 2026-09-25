# CHANGELOG

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Este arquivo registra mudanças relevantes realizadas no projeto ao longo de seu desenvolvimento.

O objetivo é permitir identificar:

```text
o que mudou
quando mudou
por que mudou
qual parte do projeto foi afetada
```

---

# Convenção

Este projeto utiliza as seguintes categorias:

```text
Added
Changed
Fixed
Deprecated
Removed
Security
```

Interpretação:

```text
Added
→ novo arquivo, estrutura, funcionalidade ou componente

Changed
→ alteração importante em algo já existente

Fixed
→ correção de erro

Deprecated
→ item ainda existente, mas que deverá deixar de ser utilizado

Removed
→ item removido

Security
→ alteração relacionada a segurança, privacidade ou exposição de dados
```

---

# Política

O `CHANGELOG.md` deve registrar mudanças relevantes.

Não é necessário registrar:

```text
cada pequena edição textual
cada correção ortográfica
cada espaço removido
cada alteração temporária
```

Deve registrar mudanças como:

```text
nova arquitetura
nova etapa
mudança metodológica
alteração de responsabilidade
mudança de estrutura de diretórios
mudança na pipeline
mudança nos critérios aprovados
mudança de normalização
mudança em metodologia CRITIC/TOPSIS
mudança em artefato oficial
```

---

# [Unreleased]

## Added

- Preparada a arquitetura multiagente com cinco agentes especializados:
  - `AGENTE_PACHECO`
  - `AGENTE_BENJAMIN`
  - `AGENTE_VITOR`
  - `AGENTE_MARCO`
  - `AGENTE_BOSS`

- Criada a pasta:

```text
agents/
```

com a estrutura:

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

- Redefinido `AGENTS.md` como roteador central da arquitetura multiagente.

- Definido o `AGENTE_BOSS` como responsável pela revisão integrada do trabalho produzido pelos demais agentes.

- Definido o princípio:

```text
agente responsável
↓
execução
↓
documentação
↓
handoff
↓
AGENTE_BOSS
↓
APPROVED / CHANGES_REQUESTED / BLOCKED
```

---

## Changed

- A arquitetura de agentes foi alterada de um modelo genérico para uma arquitetura com agentes especializados por integrante.

- A responsabilidade científica permanece associada ao integrante correspondente, mesmo quando seu agente fornece suporte à execução.

- O `AGENTE_BOSS` não substitui silenciosamente o agente responsável por uma etapa.

- Correções científicas ou metodológicas detectadas pelo `AGENTE_BOSS` deverão retornar ao agente proprietário da etapa.

---

# [0.1.0] — 2026-09-25

## Added

### Estrutura geral

- Criada a arquitetura-base do projeto.

- Definida a linguagem analítica principal:

```text
R
```

- Planejada a utilização de:

```text
renv
targets
testthat
Docker
Git
GitHub
Quarto
LaTeX
Beamer
```

- Criado projeto R:

```text
FLUIDOS_CORTE.Rproj
```

com configuração destinada a evitar dependência de workspace local.

---

### Documentação principal

Preparados os arquivos estruturais:

```text
README.md
PROJECT_MAP.md
STATUS.md
AGENTS.md
CHANGELOG.md
```

O objetivo desses arquivos é fornecer:

```text
contexto
navegação
status
governança
rastreabilidade
```

para integrantes e agentes.

---

### Configuração

Criada a estrutura:

```text
config/
├── criterios.yml
├── project.yml
├── regras_validacao.yml
└── tolerancias.yml
```

#### `config/project.yml`

Preparado para centralizar:

```text
identidade do projeto
responsáveis
etapas
dependências
diretórios
políticas gerais
metodologia planejada
estado das etapas
```

#### `config/criterios.yml`

Preparado para futura definição de:

```text
critérios candidatos
critérios aprovados
critérios excluídos
direções
TARGET
restrições
variáveis diagnósticas
```

Nenhum critério científico final foi antecipado.

#### `config/regras_validacao.yml`

Preparado para centralizar regras futuras de validação relacionadas a:

```text
dados
auditoria
base canônica
ADA
correlação
PCA
conformidade
CRITIC
TOPSIS
Pareto
cenários
LOCO
LOAO
rank reversal
robustez
```

#### `config/tolerancias.yml`

Preparado para distinguir:

```text
tolerâncias computacionais
tolerâncias técnicas
tolerâncias de auditoria
arredondamento de apresentação
```

Valores ainda dependentes da execução permaneceram não definidos.

---

### Dados

Criada a estrutura:

```text
data/
├── raw/
├── interim/
└── processed/
```

Definida a política:

```text
data/raw/ = IMUTÁVEL
```

A pasta `data/raw/` contém atualmente material-fonte do projeto, incluindo:

```text
ensaio_bancada_alunos (2).xlsx
linkacessodrive.txt
```

Criado `data/raw/README.md` para documentar a política de preservação dos dados originais.

---

### Análises

Preparados os seguintes cadernos analíticos:

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

Esses arquivos foram preparados apenas como estruturas de análise.

Estado:

```text
ANALYSIS_EXECUTION_STATUS = NOT_EXECUTED
```

---

### Responsabilidades científicas

Definida a divisão principal do projeto.

#### Pacheco

```text
inventário
auditoria
reconciliação
base canônica
ADA inicial
```

#### Benjamin

```text
ADA bivariada
ADA multivariada
conformidade
critérios
matriz de decisão
normalização
CRITIC
```

#### Vitor

```text
TOPSIS
ranking
cenários
Pareto
sensibilidade
robustez
```

#### Marco

```text
integração
relatório final
figuras
tabelas
apresentação
conclusões
limitações
```

#### Todos

```text
revisão cruzada
infraestrutura
controle de versão
checkpoints
ensaio
entrega final
```

---

### Handoffs

Preparada a estrutura:

```text
handoffs/
├── README.md
├── 01_PACHECO_to_BENJAMIN.md
├── 02_BENJAMIN_to_VITOR.md
├── 03_VITOR_to_MARCO.md
└── 04_MARCO_to_TODOS.md
```

Os handoffs foram definidos como contratos formais entre etapas.

---

### Decisões

Preparada a estrutura:

```text
decisions/
├── README.md
└── DEC-000-EXEMPLO.md
```

Definido que:

```text
DEC-000
```

é apenas modelo.

A primeira decisão metodológica real deverá utilizar:

```text
DEC-001
```

quando uma decisão efetivamente ocorrer.

---

### Relatórios internos

Preparados:

```text
report/stages/01_pacheco/
report/stages/02_benjamin/
report/stages/03_vitor/
report/stages/04_marco/
```

com modelos de relatório técnico por etapa.

---

### Relatório final

Preparada a estrutura:

```text
report/final/
├── chapters/
├── figures/
├── output/
├── tables/
├── main.tex
└── references.bib
```

O `main.tex` foi estruturado de acordo com o modelo fornecido pela professora.

Regras registradas:

```text
A4
10 pt
margens de 1,5 cm
duas colunas
máximo de 4 páginas incluindo referências
resumo com até 1200 caracteres com espaços
3 a 5 palavras-chave
```

Estrutura:

```text
1. Introdução
2. Material e Método
3. Resultados e Discussão
4. Conclusões
5. Referências
```

Nenhum resultado científico foi inserido antecipadamente.

---

### Apresentação

Preparados templates em:

```text
templates/presentation/
```

e estrutura futura em:

```text
presentation/
```

Definido o uso planejado de:

```text
LaTeX
Beamer
```

A apresentação deverá utilizar somente resultados aprovados.

---

### Templates

Preparados modelos para:

```text
figuras
tabelas
relatórios
apresentação
etapas
```

Incluindo:

```text
templates/stage/EXEMPLO_BASE/
├── README.md
├── checklist.md
├── analysis.qmd
└── script.R
```

O `script.R` permanece apenas como esqueleto e não contém implementação científica.

---

### Testes

Criada a estrutura futura:

```text
tests/testthat/
```

com arquivos destinados posteriormente a testes de:

```text
importação
somas
médias
unidades
reconciliação
CRITIC
TOPSIS
```

Estado:

```text
TESTS_STATUS = NOT_IMPLEMENTED
```

Os testes serão implementados somente depois das funções reais existirem.

---

### Scripts

Criada a estrutura:

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

Esses arquivos deverão ser desenvolvidos durante a execução real do projeto.

---

### CI

Preparada:

```text
.github/workflows/ci.yml
```

com escopo inicial de validação estrutural do repositório.

Estado:

```text
CI_STATUS = BASE_STRUCTURE_ONLY
```

A execução científica será adicionada somente depois da implementação real de:

```text
R
renv
testthat
targets
```

---

## Changed

### Metodologia

Definido o fluxo principal:

```text
dados
↓
auditoria
↓
critérios
↓
correlação/redundância
↓
condições experimentais
↓
normalização
↓
CRITIC
↓
TOPSIS
↓
cenários
↓
Pareto
↓
sensibilidade
↓
robustez
↓
ranking explicável
```

---

### CRITIC

Definida como formulação metodológica de referência:

\[
C_j
=
\sigma_j
\sum_k(1-r_{jk})
\]

\[
w_j
=
\frac{C_j}
{\sum_jC_j}
\]

Definido que:

```text
1 - r
```

é a formulação principal.

Não deverá ser substituída silenciosamente por:

```text
1 - |r|
```

---

### Interpretação do CRITIC

Definido que:

```text
peso CRITIC
=
peso informacional
```

e não:

```text
importância técnica absoluta
```

---

### TOPSIS

Definida a formulação de referência:

\[
v_{ij}=w_jr_{ij}
\]

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

\[
C_i
=
\frac{S_i^-}
{S_i^+ + S_i^-}
\]

---

### Orientação dos critérios

Definido que, se a matriz normalizada já estiver orientada como:

```text
maior = melhor
```

os critérios de custo não deverão ser invertidos novamente no TOPSIS.

---

### Conformidade

Definida a separação:

```text
conformidade técnica
≠
desempenho multicritério
```

---

### Pareto

Definido que a análise de Pareto:

```text
não utiliza pesos
```

e será utilizada como evidência complementar ao TOPSIS.

---

### Robustez

Definidas como análises planejadas:

```text
cenários
sensibilidade de pesos
LOCO
normalização alternativa
LOAO
rank reversal
```

Definido que frequências nesses experimentos:

```text
não são probabilidades reais
```

---

### Política de resultados

Definido que nenhum resultado científico deverá ser inserido antes da execução.

Estados utilizados:

```text
NOT_EXECUTED
NOT_GENERATED
NOT_CREATED
NOT_FINALIZED
```

---

### Política de dados

Definido:

```text
nenhum valor deve ser corrigido silenciosamente
```

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

### Política de métodos

Definido que métodos, critérios e tolerâncias não devem ser escolhidos depois de observar qual alternativa produz o resultado desejado.

---

## Fixed

- Nenhuma correção científica registrada nesta versão.

---

## Removed

- Nenhum componente científico removido nesta versão.

---

## Deprecated

- Nenhum componente marcado como obsoleto nesta versão.

---

## Security

- Definido que a presença de um arquivo em `data/raw/` não implica automaticamente autorização para publicação em repositório remoto.

- Antes da publicação de dados, deverão ser verificadas questões de:

```text
permissão
licença
privacidade
tamanho
necessidade de distribuição
```

---

# Estado científico na versão 0.1.0

```text
DATA_INVENTORY = NOT_EXECUTED

AUDIT = NOT_EXECUTED

RECONCILIATION = NOT_EXECUTED

CANONICAL_DATASET = NOT_CREATED

ADA = NOT_EXECUTED

CRITERIA = NOT_FINALIZED

CONFORMITY = NOT_EXECUTED

CRITIC = NOT_EXECUTED

TOPSIS = NOT_EXECUTED

SCENARIOS = NOT_EXECUTED

PARETO = NOT_EXECUTED

ROBUSTNESS = NOT_EXECUTED

FINAL_RANKING = NOT_GENERATED
```

---

# Regra para próximas versões

Quando uma mudança relevante ocorrer, adicionar uma entrada em:

```text
[Unreleased]
```

e, quando houver um marco estável, criar uma nova versão, por exemplo:

```text
[0.2.0]
[0.3.0]
[1.0.0]
```

Uma organização possível:

```text
0.1.x
→ arquitetura e preparação

0.2.x
→ implementação inicial

0.3.x
→ pipeline funcionando

0.4.x
→ resultados científicos em revisão

1.0.0
→ entrega final aprovada
```

Essa numeração é uma convenção de organização do repositório e poderá ser ajustada pelo grupo.

---

# Princípio final

> O CHANGELOG registra a evolução do projeto. Ele deve permitir compreender quando uma estrutura, método ou decisão importante mudou, sem depender apenas do histórico de commits para reconstruir o desenvolvimento científico.