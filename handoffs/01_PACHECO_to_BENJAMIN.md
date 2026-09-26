# 01_PACHECO_to_BENJAMIN.md — Handoff da Auditoria e Base Canônica para ADA e Critérios

## Responsabilidade e estado

| Campo | Valor |
|---|---|
| Entrega | AGENTE_PACHECO |
| Recebimento | AGENTE_BENJAMIN |
| Versão | v1, 2026-09-25 |
| Status | `READY_FOR_BOSS_REVIEW` |
| Aprovação Boss | `NOT_YET_REVIEWED` |
| Elegibilidade para critérios/ranking | **não liberada** |

## Entradas auditadas

- `data/raw/ensaio_bancada_alunos (2).xlsx`, SHA-256 `30c5655a777c69db369b4e719b77e38bc47e152b6bd684f7c104d7c10226e4c6`.
- Cópia verificada: `data/interim/ensaio_bancada_alunos__working_copy_v1.xlsx`.
- Metadados e inventário: `results/audit/raw_file_inventory_v1.csv`, `sheet_inventory_v1.csv`, `variable_inventory_v1.csv`, `formula_inventory_v1.csv`.

## Saídas disponibilizadas sob revisão

- Base canônica com linhagem: `data/processed/base_canonica_v1.rds` e `.csv`.
- Dicionário de variáveis: `data/processed/dicionario_variaveis_v1.csv`.
- Auditoria: `results/audit/missing_summary_v1.csv`, `unit_summary_v1.csv`, `duplicate_source_cell_audit_v1.csv`, `outlier_assessment_v1.csv` e `issue_log_v1.csv`.
- Reconciliação: `results/audit/reconciliation_checks_v1.csv`.
- ADA inicial descritiva: `results/eda/eda_numeric_summary_v1.csv`, `eda_missingness_v1.csv` e `fig_missingness_v1.png`.

## Contratos e limitações

1. `data/raw/` permanece imutável; a cópia de trabalho possui hash idêntico à fonte.
2. Cada registro canônico tem `source_sheet` e `source_cell`; valores ausentes continuam `NA` e zeros não foram convertidos.
3. A extração contém 11 fluidos identificados: A, B, C, D, E, F, G, H, J, K e M.
4. A planilha não contém fórmulas OOXML detectáveis: resultados derivados são valores armazenados e carecem de memória de cálculo rastreável.
5. Existem divergências de soma de vida de ferramenta em B e J; não foi aplicada tolerância porque ela não está definida em configuração.
6. Há medidas de acidez marcadas como `repetir` e lacunas na avaliação econômica de J e K. Elas não podem sustentar análise numérica sem resolução documentada.

## Ação requerida antes do uso downstream

O AGENTE_BOSS deve revisar as pendências PCH-002 a PCH-006 em `results/audit/issue_log_v1.csv`. Até uma decisão explícita, o conteúdo é **UNDER_REVIEW** e não deve alimentar seleção de critérios, conformidade, CRITIC ou ranking.
