# Execução Pacheco v1 — inventário, auditoria e base canônica

**Status:** `READY_FOR_BOSS_REVIEW`  
**Responsável:** AGENTE_PACHECO  
**Data de execução:** 2026-09-25  
**Escopo:** etapas 01–05; sem seleção de critérios, conformidade final, pesos ou ranking.

## Fonte e reprodutibilidade

- Fonte imutável auditada: `data/raw/ensaio_bancada_alunos (2).xlsx`.
- SHA-256 da fonte: `30c5655a777c69db369b4e719b77e38bc47e152b6bd684f7c104d7c10226e4c6`.
- Cópia de trabalho: `data/interim/ensaio_bancada_alunos__working_copy_v1.xlsx`.
- Os hashes são idênticos; a verificação está em `results/audit/working_copy_verification_v1.csv`.
- A execução reprodutível é `Rscript scripts/run_audit.R` a partir da raiz do projeto.

## Inventário

O XLSX contém sete abas: `SPEC FLUIDOS`, `CAVACOS`, `EQUA-USN`, `ANÁLISE USINABILIDADE`, `ANÁLISE EMULSÕES`, `COMPARATIVO` e `AVALIAÇÃO ECONÔMICA`. O inventário de dimensões, tipos aparentes, cabeçalhos provisórios e fórmulas está em `results/audit/`.

Não foi detectada fórmula OOXML. Portanto, resultados calculados no arquivo estão presentes como valores armazenados e não possuem trilha de fórmula recuperável pelo XLSX.

## Auditoria e reconciliação

- As ausências foram preservadas como `NA`; zeros observados permanecem zeros.
- O texto `repetir` em três observações de acidez foi preservado como texto, não convertido em valor numérico.
- A planilha `CAVACOS` só contém uma célula de identificação e requer confirmação de finalidade.
- A reconciliação de soma de vida de ferramenta mostra divergências que requerem revisão em B e J. Diferenças somente de precisão de máquina foram marcadas separadamente.
- A identidade de custo anual fecha para os fluidos com entradas completas; J e K têm insumos econômicos ausentes e não foram imputados.
- Como `config/tolerancias.yml` não define limites numéricos, não houve descarte, correção ou classificação automática de outliers.

## Base canônica e ADA inicial

Foi criada uma base longa com `source_file`, `source_sheet`, `source_cell`, domínio, fluido, métrica, condição, unidade, requisito, valor original, valor numérico/textual e marcador de ausência. Ela permite rastrear cada observação ao XLSX.

- `data/processed/base_canonica_v1.rds`
- `data/processed/base_canonica_v1.csv`
- `data/processed/dicionario_variaveis_v1.csv`
- `results/eda/eda_numeric_summary_v1.csv`
- `results/eda/eda_missingness_v1.csv`
- `results/eda/fig_missingness_v1.png`

A ADA inicial é somente descritiva. Não foram produzidos critérios finais, matriz de decisão, normalização, pesos ou ranking.

## Pendências para revisão Boss

1. Definir como tratar as divergências de reconciliação B e J e a precisão/arre­dondamento de valores derivados.
2. Esclarecer a finalidade e/ou o conteúdo ausente da aba `CAVACOS`.
3. Obter medições de acidez marcadas como `repetir`.
4. Completar ou justificar campos econômicos ausentes de J e K.
5. Registrar origem/memória de cálculo para valores armazenados sem fórmulas OOXML.
