# 05_normalizacao.md — Normalização dos Critérios

## 1. Responsável

**Benjamin**

---

## 2. Objetivo

Definir e aplicar, futuramente por código em R, uma estratégia de normalização
adequada para tornar os critérios comparáveis antes do cálculo dos pesos CRITIC
e da aplicação do TOPSIS.

A normalização deve respeitar:

- natureza do critério;
- direção de preferência;
- escala original;
- presença de valores negativos;
- existência de critérios de alvo;
- interpretação técnica;
- compatibilidade com CRITIC e TOPSIS.

A normalização não deve alterar arbitrariamente a estrutura de preferência dos
dados.

---

# 3. Princípio fundamental

Critérios como:

```text
vida da ferramenta
potência
rugosidade
custo