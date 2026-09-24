# 04_base_canonica.md — Construção e Versionamento da Base Canônica

## 1. Responsável

**Pacheco**

---

## 2. Objetivo

Construir a primeira base oficialmente validada do projeto a partir dos dados
originais, dos resultados da auditoria, da reconciliação entre abas e das
decisões metodológicas registradas.

A base canônica deverá ser:

- reproduzível;
- rastreável;
- versionada;
- documentada;
- consistente;
- adequada para as análises estatísticas posteriores;
- independente de alterações manuais no arquivo original.

A base canônica não é uma cópia "limpa" feita manualmente.

Ela deve ser gerada por código em R.

---

# 3. Entrada oficial

Utilizar:

```text
data/raw/ensaio_bancada_alunos.xlsx