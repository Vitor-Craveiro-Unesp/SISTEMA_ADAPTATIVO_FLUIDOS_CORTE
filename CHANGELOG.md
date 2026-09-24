# CHANGELOG.md — Histórico de Mudanças do Projeto

Este arquivo registra alterações relevantes na estrutura, metodologia,
dados e resultados do projeto.

Não deve ser utilizado para registrar pequenas mudanças de código.
Essas alterações permanecem registradas no histórico do Git.

---

# [Unreleased]

Alterações em andamento que ainda não fazem parte de uma versão ou marco
oficial do projeto.

---

## Adicionado

- Estrutura inicial do projeto.
- README.md.
- AGENTS.md.
- PROJECT_MAP.md.
- STATUS.md.
- CHANGELOG.md.
- Estrutura de dados `raw`, `interim` e `processed`.
- Estrutura de instruções por responsável.
- Estrutura de relatórios intermediários.
- Estrutura para registro de decisões metodológicas.
- Estrutura para handoffs entre integrantes.
- Estrutura de resultados computacionais.
- Estrutura para relatório final em LaTeX.
- Estrutura para apresentação em LaTeX/Beamer.
- Estrutura para Docker.
- Estrutura para renv.
- Estrutura para targets.
- Estrutura para testes com testthat.

---

## Definido

### Linguagem principal

R.

### Metodologia principal

CRITIC + TOPSIS.

### Metodologia geral

Dados brutos
→ auditoria
→ reconciliação
→ base canônica
→ ADA
→ conformidade
→ critérios
→ normalização
→ CRITIC
→ TOPSIS
→ cenários
→ Pareto
→ sensibilidade
→ robustez
→ ranking
→ relatório
→ apresentação.

### Responsáveis

- Pacheco — auditoria, preparação dos dados, base canônica e ADA inicial.
- Benjamin — ADA aprofundada, critérios, conformidade, normalização e CRITIC.
- Vitor — TOPSIS, ranking, cenários, Pareto e robustez.
- Marco — integração científica, relatório e apresentação.

---

# Como utilizar este arquivo

Registrar somente alterações importantes.

Exemplos:

- nova versão da base canônica;
- correção importante nos dados;
- mudança de critério;
- mudança na metodologia;
- alteração dos pesos;
- alteração na estratégia de normalização;
- nova versão do ranking;
- mudança na estrutura do projeto;
- conclusão de uma grande etapa.

---

# Exemplo de registro futuro

## [0.2.0] - 2026-09-XX

### Adicionado

- Auditoria automática entre abas.
- Validação independente de somas e médias.
- Registro automático de inconsistências.

### Corrigido

- Divergência identificada no fluido B.
- Erro de cálculo em determinado total.

### Alterado

- Base canônica atualizada da versão v1 para v2.

---

# Convenção de versões

Sugestão:

## `0.x.x`

Projeto em desenvolvimento.

Exemplo:

`0.1.0`

Estrutura inicial.

`0.2.0`

Auditoria concluída.

`0.3.0`

Base canônica aprovada.

`0.4.0`

ADA concluída.

`0.5.0`

Matriz de decisão e CRITIC concluídos.

`0.6.0`

TOPSIS e ranking concluídos.

`0.7.0`

Robustez concluída.

---

## `1.0.0`

Versão final entregue.

Deve corresponder a:

- base final validada;
- análises finalizadas;
- ranking aprovado;
- relatório final;
- apresentação final;
- código reproduzível;
- testes aprovados.

---

# Regra

Nunca apagar registros históricos importantes.

Se uma decisão ou resultado for posteriormente alterado, registrar a nova
mudança em vez de apagar o histórico anterior.