# 03_reconciliacao.md — Reconciliação Numérica e Semântica Entre Abas

## 1. Responsável

**Pacheco**

---

## 2. Objetivo

Comparar formalmente informações equivalentes que aparecem em mais de uma
aba da planilha, identificar divergências, rastrear possíveis erros
propagados e definir quais valores poderão ser utilizados na base canônica.

A reconciliação deve responder:

- a mesma variável aparece em mais de uma aba?
- os valores coincidem?
- a diferença é apenas arredondamento?
- existe divergência relevante?
- existe erro propagado de uma aba para outra?
- qual aba parece conter a informação primária?
- qual valor deve ser adotado?
- a decisão pode ser automática ou precisa de julgamento humano?

Nenhuma divergência relevante deve ser resolvida silenciosamente.

---

# 3. Entradas

Utilizar:

```text
data/raw/ensaio_bancada_alunos.xlsx