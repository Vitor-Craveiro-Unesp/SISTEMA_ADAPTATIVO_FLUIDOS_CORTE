# Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte

## 1. Descrição do projeto

Este projeto tem como objetivo desenvolver uma metodologia estatística
reprodutível para avaliar e classificar fluidos de corte do melhor para o
pior a partir de dados experimentais fornecidos pela disciplina.

A análise será realizada em etapas, iniciando por uma auditoria completa
da base de dados antes da aplicação de qualquer método estatístico de
classificação.

O projeto não pressupõe que os dados fornecidos estejam completamente
corretos. Por esse motivo, serão verificadas inconsistências estruturais,
dados ausentes, diferenças numéricas entre abas, unidades, fórmulas,
somas, médias e demais cálculos existentes na planilha original.

Após a construção de uma base canônica validada, será realizada uma
Análise de Dados (ADA) completa e, posteriormente, será desenvolvido um
Sistema Adaptativo de Classificação Multicritério baseado principalmente
nos métodos CRITIC e TOPSIS.

---

## 2. Objetivo geral

Construir um sistema estatístico capaz de classificar os fluidos de corte
do melhor para o pior considerando simultaneamente desempenho técnico,
qualidade, características operacionais e aspectos econômicos.

---

## 3. Objetivos específicos

- preservar integralmente os dados brutos fornecidos;
- realizar auditoria estrutural da planilha;
- identificar dados ausentes e registros incompletos;
- identificar erros de soma, média e demais cálculos;
- detectar diferenças numéricas entre abas;
- verificar unidades e tipos de dados;
- documentar todas as inconsistências encontradas;
- construir uma base canônica validada;
- realizar ADA univariada, bivariada e multivariada;
- avaliar correlação e redundância entre critérios;
- verificar conformidade com especificações técnicas;
- construir a matriz de decisão multicritério;
- determinar pesos objetivos utilizando CRITIC;
- gerar o ranking dos fluidos utilizando TOPSIS;
- avaliar diferentes cenários de decisão;
- estudar fronteiras de Pareto;
- realizar análise de sensibilidade e robustez;
- produzir um ranking final explicável e reproduzível;
- elaborar relatório técnico e apresentação final.

---

## 4. Fluxo metodológico

O fluxo geral do projeto será:

Dados brutos
→ Auditoria
→ Reconciliação entre abas
→ Validação dos cálculos
→ Base canônica
→ ADA
→ Conformidade
→ Seleção dos critérios
→ Correlação e redundância
→ Matriz de decisão
→ Normalização
→ CRITIC
→ TOPSIS
→ Cenários
→ Pareto
→ Sensibilidade e robustez
→ Ranking final
→ Relatório
→ Apresentação

Nenhum ranking será produzido antes da conclusão e validação da etapa de
qualidade dos dados.

---

## 5. Metodologia multicritério

A metodologia principal prevista é:

### CRITIC

O método CRITIC será utilizado para determinar pesos objetivos dos
critérios considerando:

- variabilidade;
- poder discriminante;
- correlação;
- redundância entre variáveis.

### TOPSIS

O TOPSIS será utilizado para classificar os fluidos considerando a
distância de cada alternativa em relação a:

- solução ideal;
- solução anti-ideal.

### Análises complementares

Também poderão ser utilizadas:

- análise de conformidade;
- análise de correlação;
- PCA, quando estatisticamente justificável;
- agrupamento exploratório;
- fronteira de Pareto;
- análise de cenários;
- análise de sensibilidade;
- avaliação de robustez do ranking.

---

## 6. Equipe

O projeto será desenvolvido por quatro integrantes.

### Pacheco

Responsável principal por:

- importação dos dados;
- inventário da planilha;
- auditoria estrutural;
- identificação de dados ausentes;
- identificação de duplicidades;
- verificação de unidades;
- auditoria de somas e médias;
- validação de fórmulas;
- reconciliação entre abas;
- registro de inconsistências;
- construção da base canônica;
- ADA inicial.

Entregável principal:

`Base canônica v1 + relatório de auditoria`

---

### Benjamin

Responsável principal por:

- ADA bivariada;
- ADA multivariada;
- análise de correlação;
- análise de redundância;
- análise de conformidade;
- classificação dos critérios;
- definição da matriz de decisão;
- normalização;
- aplicação do método CRITIC.

Entregável principal:

`Matriz de decisão v2 + pesos CRITIC`

---

### Vitor

Responsável principal por:

- aplicação do TOPSIS;
- construção do ranking;
- análise de cenários;
- análise de Pareto;
- análise de sensibilidade;
- avaliação de robustez;
- interpretação estatística do ranking.

Entregável principal:

`Ranking + cenários + robustez`

---

### Marco

Responsável principal por:

- integração dos resultados;
- organização do relatório técnico;
- padronização do LaTeX;
- integração de tabelas e figuras;
- desenvolvimento da apresentação;
- aplicação do layout visual;
- conclusão e limitações.

Entregável principal:

`Relatório final + apresentação final`

---

## 7. Handoffs

O projeto seguirá uma estrutura sequencial:

Pacheco
→ Checkpoint coletivo
→ Benjamin
→ Checkpoint coletivo
→ Vitor
→ Checkpoint coletivo
→ Marco
→ Revisão coletiva
→ Entrega

Cada responsável deverá entregar uma versão validada antes da etapa
seguinte.

Nenhum integrante deverá alterar silenciosamente os resultados produzidos
por uma etapa anterior.

Caso seja identificado um erro, a correção deverá retornar à etapa de
origem e ser registrada.

---

## 8. Tecnologias

### Linguagem

- R

### Reprodutibilidade

- Docker
- renv
- targets

### Validação

- testthat
- validate

### Manipulação e análise

- tidyverse
- readxl
- openxlsx2
- janitor
- naniar
- skimr

### Visualização

- ggplot2

### Relatórios

- Quarto
- LaTeX

### Apresentação

- LaTeX / Beamer
- PDF

### Versionamento

- Git
- GitHub

---

## 9. Estrutura principal

```text
PROJETO1/
│
├── AGENTS.md
├── PROJECT_MAP.md
├── STATUS.md
├── CHANGELOG.md
├── README.md
│
├── Dockerfile
├── compose.yaml
├── renv.lock
├── _targets.R
│
├── config/
├── instructions/
├── templates/
├── decisions/
├── handoffs/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── R/
├── analysis/
├── scripts/
├── tests/
├── results/
│
├── report/
└── presentation/