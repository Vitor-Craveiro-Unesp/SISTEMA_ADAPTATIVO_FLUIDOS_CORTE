# STATUS.md — Estado Atual do Projeto

## 1. Projeto

**Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte**

Prazo oficial:

**20/10/2026**

---

## 2. Etapa atual

### ETAPA 0 — Preparação da infraestrutura e organização do projeto

Status:

**EM ANDAMENTO**

---

## 3. Responsáveis atuais

### TODOS

Responsáveis pela preparação inicial:

- Pacheco
- Benjamin
- Vitor
- Marco

---

## 4. Objetivo da etapa atual

Preparar o ambiente computacional, a estrutura do repositório e a
documentação necessária antes do início da auditoria estatística dos dados.

---

## 5. Concluído

- [x] Objetivo geral do projeto definido.
- [x] Metodologia geral definida.
- [x] CRITIC + TOPSIS definidos como metodologia multicritério principal.
- [x] Uso de R definido.
- [x] Uso de Docker definido.
- [x] Uso de renv definido.
- [x] Uso de targets definido.
- [x] Uso de testthat definido.
- [x] Uso de Quarto/LaTeX definido.
- [x] Estrutura principal do repositório criada.
- [x] Responsabilidades da equipe definidas.
- [x] README.md criado.
- [x] AGENTS.md criado.
- [x] PROJECT_MAP.md criado.

---

## 6. Em andamento

- [ ] Finalizar arquivos de configuração.
- [ ] Configurar Docker.
- [ ] Configurar renv.
- [ ] Configurar targets.
- [ ] Configurar testes iniciais.
- [ ] Preparar instruções detalhadas das etapas.
- [ ] Adicionar dados originais em `data/raw/`.
- [ ] Testar execução do ambiente completo.

---

## 7. Próxima etapa

### ETAPA 1 — Auditoria e preparação dos dados

Responsável principal:

**Pacheco**

A etapa somente deverá iniciar após a preparação e validação mínima do
ambiente computacional.

---

## 8. Objetivos da próxima etapa

Pacheco deverá:

- importar os dados sem alterar o arquivo original;
- inventariar todas as abas;
- identificar variáveis;
- identificar fluidos;
- verificar tipos;
- identificar dados faltantes;
- detectar duplicidades;
- verificar unidades;
- recalcular somas;
- recalcular médias;
- recalcular indicadores;
- procurar fórmulas quebradas;
- comparar valores repetidos entre abas;
- registrar divergências;
- identificar valores suspeitos;
- produzir o dicionário de dados;
- construir a base canônica v1;
- realizar a ADA inicial.

---

## 9. Entrada esperada da próxima etapa

Arquivo original:

`data/raw/ensaio_bancada_alunos.xlsx`

O arquivo dentro de `data/raw/` deverá permanecer imutável.

---

## 10. Saídas esperadas da próxima etapa

Principais entregáveis:

- inventário da planilha;
- dicionário de dados;
- relatório de missing;
- relatório de duplicidades;
- auditoria de unidades;
- auditoria de somas;
- auditoria de médias;
- auditoria de fórmulas;
- reconciliação entre abas;
- registro de inconsistências;
- base canônica v1;
- ADA inicial;
- relatório de auditoria;
- handoff Pacheco → Benjamin.

---

## 11. Pendências conhecidas da base

Algumas inconsistências já foram observadas preliminarmente e deverão ser
confirmadas pelo código em R.

### Divergências entre abas

Há indícios de diferenças numéricas para determinados resultados
experimentais entre abas.

Essas diferenças deverão ser detectadas automaticamente e não corrigidas
manualmente.

---

### Somatórios

Alguns totais deverão ser recalculados independentemente pelo R para
verificar possíveis erros de soma.

---

### Dados econômicos

Há indícios de cálculos incompletos ou erros de fórmula em determinados
fluidos.

Devem ser investigados durante a auditoria.

---

### Unidades

Há pelo menos uma ocorrência aparente de mistura entre valor numérico e
unidade textual.

Deve ser verificada formalmente.

---

### Dados ausentes

Há informações aparentemente ausentes ou pendentes.

Esses casos deverão ser classificados corretamente antes de qualquer
tratamento.

---

## 12. Regra para inconsistências conhecidas

As observações acima são apenas hipóteses preliminares.

Nenhuma delas deverá ser considerada oficialmente confirmada até ser
reproduzida e registrada pela auditoria em R.

Fluxo:

```text
suspeita
↓
teste em R
↓
evidência
↓
registro da inconsistência
↓
decisão metodológica
↓
eventual correção