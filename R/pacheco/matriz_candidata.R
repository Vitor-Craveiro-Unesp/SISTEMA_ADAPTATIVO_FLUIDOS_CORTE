# Matriz candidata completa: visualização ampla e rastreabilidade por célula.
# Não é a matriz de decisão oficial; critérios, direções e exclusões pertencem a Benjamin.

matrix_safe_id <- function(value, fallback = "sem_condicao") {
  if (is.na(value) || !nzchar(trimws(value))) value <- fallback
  value <- iconv(as.character(value), from = "", to = "ASCII//TRANSLIT")
  value <- tolower(gsub("[^A-Za-z0-9]+", "_", value))
  value <- gsub("^_+|_+$", "", value)
  value
}

matrix_column_id <- function(data_domain, metric, condition) {
  paste(
    paste0("dominio_", matrix_safe_id(data_domain)),
    paste0("metrica_", matrix_safe_id(metric)),
    paste0("condicao_", matrix_safe_id(condition)),
    sep = "__"
  )
}

matrix_display_label <- function(data_domain, metric, condition, unit) {
  parts <- c(data_domain, metric)
  if (!is.na(condition) && nzchar(trimws(condition))) parts <- c(parts, condition)
  if (!is.na(unit) && nzchar(trimws(unit))) parts <- c(parts, paste0("[", unit, "]"))
  paste(parts, collapse = " | ")
}

duplicate_mapping <- function() {
  data.frame(
    matrix_column_id = c(
      matrix_column_id("usinabilidade", "vida_ferramenta_volume_removido", "condicao_1"),
      matrix_column_id("usinabilidade", "vida_ferramenta_volume_removido", "condicao_2"),
      matrix_column_id("usinabilidade", "vida_ferramenta_volume_removido", "condicao_3"),
      matrix_column_id("usinabilidade", "vida_ferramenta_volume_removido", "condicao_4"),
      matrix_column_id("comparativo", "vida_ferramenta_volume_removido", "condicao_1"),
      matrix_column_id("comparativo", "vida_ferramenta_volume_removido", "condicao_2"),
      matrix_column_id("comparativo", "vida_ferramenta_volume_removido", "condicao_3"),
      matrix_column_id("comparativo", "vida_ferramenta_volume_removido", "condicao_4"),
      matrix_column_id("comparativo", "vida_ferramenta_volume_removido", "somatorio"),
      matrix_column_id("usinabilidade", "potencia_corte", "condicao_1"),
      matrix_column_id("usinabilidade", "potencia_corte", "condicao_2"),
      matrix_column_id("usinabilidade", "potencia_corte", "condicao_3"),
      matrix_column_id("usinabilidade", "potencia_corte", "condicao_4"),
      matrix_column_id("comparativo", "potencia", "condicao_1"),
      matrix_column_id("comparativo", "potencia", "condicao_2"),
      matrix_column_id("comparativo", "potencia", "condicao_3"),
      matrix_column_id("comparativo", "potencia", "condicao_4"),
      matrix_column_id("emulsao", "CONCENTRAÇÃO MÉDIA", NA_character_),
      matrix_column_id("comparativo", "concentracao_media", NA_character_)
    ),
    duplicate_group = c(
      rep("DUP_01_VIDA_FERRAMENTA", 9L),
      rep("DUP_02_POTENCIA", 8L),
      rep("DUP_03_CONCENTRACAO_MEDIA", 2L)
    ),
    duplicate_note = c(
      rep("Medições de vida da ferramenta aparecem na aba original e na aba consolidada; não usar ambas como critérios independentes sem reconciliação.", 9L),
      rep("Medições de potência aparecem na aba original e na aba consolidada; não usar ambas como critérios independentes sem reconciliação.", 8L),
      rep("A concentração média aparece na aba de emulsões e na aba consolidada; confirmar equivalência antes de selecionar critérios.", 2L)
    ),
    stringsAsFactors = FALSE
  )
}

build_candidate_matrix <- function(canonical_data) {
  required <- c("source_sheet", "source_cell", "data_domain", "fluid_id", "metric", "condition",
                "unit", "value_raw", "value_numeric", "value_text", "is_missing")
  missing_required <- setdiff(required, names(canonical_data))
  if (length(missing_required) > 0L) {
    stop("A base canônica não possui os campos necessários: ", paste(missing_required, collapse = ", "), call. = FALSE)
  }

  records <- canonical_data
  records$matrix_column_id <- mapply(
    matrix_column_id, records$data_domain, records$metric, records$condition,
    USE.NAMES = FALSE
  )
  records$na_flag <- records$is_missing
  records$value_for_matrix <- ifelse(records$is_missing, NA_character_, records$value_raw)

  duplicate_info <- duplicate_mapping()
  records <- merge(records, duplicate_info, by = "matrix_column_id", all.x = TRUE, sort = FALSE)
  records$possible_duplicate <- !is.na(records$duplicate_group)
  records$matrix_readiness_status <- ifelse(
    records$na_flag,
    "MISSING_VALUE_REVIEW_REQUIRED",
    ifelse(records$possible_duplicate,
      "POSSIBLE_DUPLICATE_REVIEW_REQUIRED",
      "UNDER_REVIEW_NOT_A_DECISION_CRITERION"
    )
  )
  records <- records[order(records$fluid_id, records$matrix_column_id), , drop = FALSE]

  metadata <- unique(records[, c(
    "matrix_column_id", "data_domain", "source_sheet", "metric", "condition", "unit", "requirement",
    "possible_duplicate", "duplicate_group", "duplicate_note"
  ), drop = FALSE])
  metadata$display_label <- mapply(
    matrix_display_label, metadata$data_domain, metadata$metric, metadata$condition, metadata$unit,
    USE.NAMES = FALSE
  )
  metadata$observations <- vapply(metadata$matrix_column_id, function(column_id) {
    sum(records$matrix_column_id == column_id)
  }, integer(1))
  metadata$missing_values <- vapply(metadata$matrix_column_id, function(column_id) {
    sum(records$matrix_column_id == column_id & records$na_flag)
  }, integer(1))
  metadata$missing_fluids <- vapply(metadata$matrix_column_id, function(column_id) {
    affected <- records$fluid_id[records$matrix_column_id == column_id & records$na_flag]
    if (length(affected) == 0L) "" else paste(affected, collapse = ", ")
  }, character(1))
  metadata$wide_column_name <- ifelse(
    metadata$possible_duplicate,
    paste0(metadata$matrix_column_id, "__POSSIVEL_DUPLICATA_", metadata$duplicate_group),
    metadata$matrix_column_id
  )
  metadata <- metadata[order(metadata$data_domain, metadata$metric, metadata$condition), , drop = FALSE]

  fluids <- sort(unique(records$fluid_id))
  column_ids <- metadata$matrix_column_id
  wide <- data.frame(fluid_id = fluids, stringsAsFactors = FALSE, check.names = FALSE)
  for (index in seq_along(column_ids)) {
    column_id <- column_ids[[index]]
    selected <- records[records$matrix_column_id == column_id, c("fluid_id", "value_for_matrix"), drop = FALSE]
    values <- selected$value_for_matrix[match(fluids, selected$fluid_id)]
    wide[[metadata$wide_column_name[[index]]]] <- values
  }

  list(wide = wide, metadata = metadata, flags = records)
}
