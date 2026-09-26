# Entrada reprodutível do inventário inicial da auditoria Pacheco.
source("R/pacheco/importacao.R")
source("R/pacheco/inventario.R")
source("R/pacheco/missing.R")
source("R/pacheco/unidades.R")
source("R/pacheco/reconciliacao.R")
source("R/pacheco/base_canonica.R")
source("R/pacheco/ada_inicial.R")

project_root <- find_project_root()
setwd(project_root)

raw_dir <- file.path("data", "raw")
raw_files <- list.files(raw_dir, full.names = TRUE, all.files = FALSE, no.. = TRUE)
raw_files <- raw_files[file.info(raw_files)$isdir %in% FALSE]
raw_files <- raw_files[!grepl("^\\\\.gitkeep$", basename(raw_files))]

dir.create(file.path("results", "audit"), recursive = TRUE, showWarnings = FALSE)

metadata <- do.call(rbind, lapply(raw_files, raw_file_metadata, project_root = project_root))
utils::write.csv(metadata, file.path("results", "audit", "raw_file_inventory_v1.csv"), row.names = FALSE, na = "")

xlsx_files <- raw_files[tolower(tools::file_ext(raw_files)) == "xlsx"]
if (length(xlsx_files) != 1L) {
  stop("A auditoria inicial exige exatamente um XLSX em data/raw/.", call. = FALSE)
}

raw_xlsx <- xlsx_files[[1]]
working_xlsx <- file.path("data", "interim", "ensaio_bancada_alunos__working_copy_v1.xlsx")
copy_hashes <- copy_working_xlsx(raw_xlsx, working_xlsx)
copy_record <- data.frame(
  raw_relative_path = relative_project_path(raw_xlsx, project_root),
  interim_relative_path = relative_project_path(working_xlsx, project_root),
  raw_sha256 = copy_hashes$raw_sha256,
  interim_sha256 = copy_hashes$interim_sha256,
  hashes_match = identical(copy_hashes$raw_sha256, copy_hashes$interim_sha256),
  stringsAsFactors = FALSE
)
utils::write.csv(copy_record, file.path("results", "audit", "working_copy_verification_v1.csv"), row.names = FALSE)

workbook <- load_xlsx_readonly(working_xlsx)
file_label <- relative_project_path(raw_xlsx, project_root)
utils::write.csv(sheet_inventory(workbook, file_label), file.path("results", "audit", "sheet_inventory_v1.csv"), row.names = FALSE, na = "")
utils::write.csv(variable_inventory(workbook, file_label), file.path("results", "audit", "variable_inventory_v1.csv"), row.names = FALSE, na = "")
utils::write.csv(formula_inventory(working_xlsx, file_label), file.path("results", "audit", "formula_inventory_v1.csv"), row.names = FALSE, na = "")

# A base canônica preserva o valor original, a célula e a aba; não altera dados brutos.
canonical <- build_canonical_data(workbook, file_label)
dir.create(file.path("data", "processed"), recursive = TRUE, showWarnings = FALSE)
saveRDS(canonical, file.path("data", "processed", "base_canonica_v1.rds"))
utils::write.csv(canonical, file.path("data", "processed", "base_canonica_v1.csv"), row.names = FALSE, na = "")

dictionary <- unique(canonical[, c("data_domain", "metric", "condition", "unit", "requirement"), drop = FALSE])
dictionary$observations <- vapply(seq_len(nrow(dictionary)), function(index) {
  sum(canonical$data_domain == dictionary$data_domain[[index]] &
        canonical$metric == dictionary$metric[[index]] &
        (is.na(dictionary$condition[[index]]) & is.na(canonical$condition) |
          !is.na(dictionary$condition[[index]]) & canonical$condition == dictionary$condition[[index]]))
}, integer(1))
utils::write.csv(dictionary, file.path("data", "processed", "dicionario_variaveis_v1.csv"), row.names = FALSE, na = "")

missing_report <- missing_summary(canonical)
utils::write.csv(missing_report, file.path("results", "audit", "missing_summary_v1.csv"), row.names = FALSE, na = "")
utils::write.csv(unit_summary(canonical), file.path("results", "audit", "unit_summary_v1.csv"), row.names = FALSE, na = "")

source_cell_duplicates <- aggregate(canonical$source_cell,
  by = list(source_sheet = canonical$source_sheet, source_cell = canonical$source_cell), FUN = length)
names(source_cell_duplicates)[3] <- "records_with_same_source_cell"
source_cell_duplicates$duplicate_flag <- source_cell_duplicates$records_with_same_source_cell > 1L
utils::write.csv(source_cell_duplicates, file.path("results", "audit", "duplicate_source_cell_audit_v1.csv"), row.names = FALSE)

reconciliation <- reconciliation_checks(canonical)
utils::write.csv(reconciliation, file.path("results", "audit", "reconciliation_checks_v1.csv"), row.names = FALSE, na = "")

numeric_summary <- initial_eda_summary(canonical)
dir.create(file.path("results", "eda"), recursive = TRUE, showWarnings = FALSE)
utils::write.csv(numeric_summary, file.path("results", "eda", "eda_numeric_summary_v1.csv"), row.names = FALSE, na = "")
utils::write.csv(missing_report, file.path("results", "eda", "eda_missingness_v1.csv"), row.names = FALSE, na = "")

if (requireNamespace("ggplot2", quietly = TRUE)) {
  figure_data <- aggregate(canonical$is_missing, by = list(data_domain = canonical$data_domain), FUN = mean)
  names(figure_data)[2] <- "missing_rate"
  grDevices::png(file.path("results", "eda", "fig_missingness_v1.png"), width = 1120, height = 640, res = 160)
  graphics::barplot(figure_data$missing_rate, names.arg = figure_data$data_domain, ylim = c(0, 1),
    col = "#2C7FB8", ylab = "Taxa de ausência", main = "Ausências por domínio da base canônica")
  graphics::abline(h = seq(0, 1, by = 0.25), col = "grey85", lty = 3)
  grDevices::dev.off()
}

issues <- data.frame(
  issue_id = character(), severity = character(), domain = character(), location = character(),
  description = character(), evidence = character(), required_action = character(), status = character(),
  stringsAsFactors = FALSE
)
add_issue <- function(id, severity, domain, location, description, evidence, action, status = "OPEN") {
  issues[nrow(issues) + 1L, ] <<- list(id, severity, domain, location, description, evidence, action, status)
}
add_issue("PCH-001", "INFO", "documentation", "instructions/01_PACHECO_AUDITORIA_BASE",
  "O nome do XLSX referido na instrução difere do arquivo bruto efetivamente recebido.",
  paste0("Arquivo auditado: ", basename(raw_xlsx)), "Atualizar a referência documental sem renomear o arquivo bruto.")
if (nrow(formula_inventory(working_xlsx, file_label)) == 0L) {
  add_issue("PCH-002", "MEDIUM", "traceability", "workbook", "Não foram encontradas fórmulas OOXML no XLSX.",
    "formula_inventory_v1.csv não contém linhas; resultados calculados estão armazenados como valores.",
    "Registrar a origem ou a memória de cálculo antes de tratar valores derivados como plenamente rastreáveis.")
}
add_issue("PCH-003", "MEDIUM", "structure", "CAVACOS!B1", "A aba CAVACOS contém apenas uma identificação de produto.",
  "Inventário: 1 linha, 2 colunas e 1 célula não vazia.", "Confirmar se a aba deveria conter dados de cavaco ou se é somente uma referência.")
repeated_acidity <- canonical[canonical$data_domain == "emulsao" & canonical$metric == "ACIDEZ" & canonical$value_text == "repetir", ]
if (nrow(repeated_acidity) > 0L) {
  add_issue("PCH-004", "HIGH", "emulsao", paste(repeated_acidity$source_cell, collapse = ", "),
    "O campo ACIDEZ contém o texto 'repetir' em vez de uma medida numérica.",
    paste0(nrow(repeated_acidity), " observações mantidas como texto, não convertidas para zero ou NA."),
    "Obter/reexecutar a medição e versionar a atualização antes de qualquer análise numérica dessa métrica.")
}
economic_missing <- canonical[canonical$data_domain == "economico" & canonical$is_missing, ]
if (nrow(economic_missing) > 0L) {
  affected_fluids <- paste(sort(unique(economic_missing$fluid_id)), collapse = ", ")
  add_issue("PCH-005", "HIGH", "economico", "AVALIAÇÃO ECONÔMICA",
    "Há campos econômicos ausentes na fonte; eles foram preservados como NA.",
    paste0(nrow(economic_missing), " células ausentes; fluidos afetados: ", affected_fluids, "."),
    "Completar ou justificar as ausências antes de análise econômica comparativa.")
}
review_rows <- reconciliation[reconciliation$status == "REVIEW_REQUIRED_TOLERANCE_UNDEFINED", ]
if (nrow(review_rows) > 0L) {
  add_issue("PCH-006", "MEDIUM", "reconciliation", "comparativo/economico",
    "Há diferenças entre valores reconciliados que não podem ser classificadas com tolerância não definida.",
    paste0(nrow(review_rows), " comparação(ões) requer(em) decisão de tolerância."),
    "Definir tolerâncias metodológicas ou confirmar correções na origem; não aplicar ajuste automático.")
}
utils::write.csv(issues, file.path("results", "audit", "issue_log_v1.csv"), row.names = FALSE, na = "")

outlier_audit <- unique(canonical[!is.na(canonical$value_numeric), c("data_domain", "metric", "unit"), drop = FALSE])
outlier_audit$assessment <- "NOT_ASSESSED_TOLERANCE_UNDEFINED"
outlier_audit$note <- "config/tolerancias.yml não define limites numéricos; nenhum valor foi removido ou corrigido."
utils::write.csv(outlier_audit, file.path("results", "audit", "outlier_assessment_v1.csv"), row.names = FALSE, na = "")

message("Inventário inicial concluído. Resultados: results/audit/")
