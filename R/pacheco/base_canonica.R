# Construção de uma base canônica longa, com linhagem até a célula de origem.

cell_value <- function(grid, row, column) {
  if (row > nrow(grid) || column > ncol(grid)) return(NA)
  grid[row, column][[1]]
}

as_numeric_or_na <- function(value) {
  if (is.numeric(value)) return(as.numeric(value))
  suppressWarnings(as.numeric(as.character(value)))
}

as_text_or_na <- function(value) {
  if (is_missing_value(value) || is.numeric(value)) return(NA_character_)
  trimws(as.character(value))
}

canonical_record <- function(file_label, sheet, cell, domain, fluid, metric,
                             condition = NA_character_, unit = NA_character_,
                             requirement = NA_character_, value = NA,
                             fluid_type = NA_character_) {
  missing <- is_missing_value(value)
  data.frame(
    source_file = file_label,
    source_sheet = sheet,
    source_cell = cell,
    data_domain = domain,
    fluid_id = as.character(fluid),
    fluid_type = fluid_type,
    metric = trimws(as.character(metric)),
    condition = condition,
    unit = normalize_unit(unit),
    requirement = if (is_missing_value(requirement)) NA_character_ else trimws(as.character(requirement)),
    value_raw = if (missing) NA_character_ else as.character(value),
    value_numeric = if (missing) NA_real_ else as_numeric_or_na(value),
    value_text = if (missing) NA_character_ else as_text_or_na(value),
    is_missing = missing,
    stringsAsFactors = FALSE
  )
}

extract_usinability <- function(grid, file_label, sheet_name) {
  fluid_columns <- 6:16
  fluids <- vapply(fluid_columns, function(column) as.character(cell_value(grid, 3, column)), character(1))
  sections <- list(
    list(rows = 4:7, metric = "vida_ferramenta_volume_removido"),
    list(rows = 8:11, metric = "potencia_corte"),
    list(rows = 12:15, metric = "rugosidade_superficial"),
    list(rows = 16:19, metric = "forma_cavaco")
  )
  records <- list()
  record_index <- 1L
  for (section in sections) {
    for (row in section$rows) {
      for (index in seq_along(fluid_columns)) {
        column <- fluid_columns[[index]]
        records[[record_index]] <- canonical_record(
          file_label, sheet_name, paste0(excel_column_name(column), row), "usinabilidade",
          fluids[[index]], section$metric, paste0("condicao_", row - min(section$rows) + 1L),
          cell_value(grid, row, 5), cell_value(grid, row, 4), cell_value(grid, row, column)
        )
        record_index <- record_index + 1L
      }
    }
  }
  do.call(rbind, records)
}

extract_emulsions <- function(grid, file_label, sheet_name) {
  fluid_columns <- 6:16
  fluids <- vapply(fluid_columns, function(column) as.character(cell_value(grid, 3, column)), character(1))
  records <- list()
  record_index <- 1L
  for (row in 4:24) {
    for (index in seq_along(fluid_columns)) {
      column <- fluid_columns[[index]]
      records[[record_index]] <- canonical_record(
        file_label, sheet_name, paste0(excel_column_name(column), row), "emulsao",
        fluids[[index]], cell_value(grid, row, 3), NA_character_, cell_value(grid, row, 5),
        cell_value(grid, row, 4), cell_value(grid, row, column)
      )
      record_index <- record_index + 1L
    }
  }
  do.call(rbind, records)
}

extract_comparative <- function(grid, file_label, sheet_name) {
  fluids <- vapply(3:13, function(row) as.character(cell_value(grid, row, 1)), character(1))
  records <- list()
  record_index <- 1L
  add_block <- function(metric, columns, conditions, unit = NA_character_, requirement = NA_character_) {
    for (row_index in seq_along(fluids)) {
      for (column_index in seq_along(columns)) {
        column <- columns[[column_index]]
        records[[record_index <<- record_index + 1L]] <<- canonical_record(
          file_label, sheet_name, paste0(excel_column_name(column), row_index + 2L), "comparativo",
          fluids[[row_index]], metric, conditions[[column_index]], unit, requirement,
          cell_value(grid, row_index + 2L, column)
        )
      }
    }
  }
  # decremento inicial para manter a primeira posição da lista como 1
  record_index <- 0L
  add_block("vida_ferramenta_volume_removido", 2:6, c("condicao_1", "condicao_2", "condicao_3", "condicao_4", "somatorio"), "cm3")
  add_block("presenca_rebarba", 7, NA_character_, "sem_unidade")
  add_block("espuma", 8, NA_character_, "sem_unidade")
  add_block("nevoa", 9, NA_character_, "sem_unidade")
  add_block("teste_corrosao", 10, NA_character_, "sem_unidade")
  add_block("oxidacao_maquina", 11, NA_character_, "sem_unidade")
  add_block("fungos", 12, NA_character_, "sem_unidade")
  add_block("bacterias", 13, NA_character_, "sem_unidade")
  add_block("concentricidade", 14:17, paste0("condicao_", 1:4), requirement = "tolerancia declarada na fonte: +/- 0,1")
  add_block("circularidade", 18:21, paste0("condicao_", 1:4), requirement = "tolerancia declarada na fonte: +/- 0,1")
  add_block("potencia", 22:25, paste0("condicao_", 1:4), "kW")
  add_block("resistencia_degradacao", 26, NA_character_, "sem_unidade")
  add_block("item_restritivo_composicao", 27, NA_character_, "sem_unidade")
  add_block("solidos_suspensos", 28, NA_character_, "sem_unidade")
  add_block("tensao_superficial", 29, NA_character_, "sem_unidade")
  add_block("ph_5_porcento", 30, NA_character_, "sem_unidade")
  add_block("concentracao_media", 31, NA_character_, "%")
  add_block("indice_refracao", 32, NA_character_, "sem_unidade")
  do.call(rbind, records)
}

extract_economic <- function(grid, file_label, sheet_name) {
  fluid_columns <- c(5L, seq.int(8L, 35L, by = 3L))
  fluids <- vapply(fluid_columns, function(column) as.character(cell_value(grid, 16, column)), character(1))
  fluid_types <- vapply(fluid_columns, function(column) as.character(cell_value(grid, 11, column)), character(1))
  # A linha 42 é espaçadora; não é observação nem ausência de dado.
  rows <- c(14:29, 33:41, 43)
  records <- list()
  record_index <- 1L
  for (row in rows) {
    for (index in seq_along(fluid_columns)) {
      column <- fluid_columns[[index]]
      records[[record_index]] <- canonical_record(
        file_label, sheet_name, paste0(excel_column_name(column), row), "economico",
        fluids[[index]], cell_value(grid, row, 1), NA_character_, NA_character_, NA_character_,
        cell_value(grid, row, column), fluid_types[[index]]
      )
      record_index <- record_index + 1L
    }
  }
  do.call(rbind, records)
}

build_canonical_data <- function(workbook, file_label) {
  sheet_names <- openxlsx::sheets(workbook)
  usinability <- extract_usinability(read_sheet_grid(workbook, 4), file_label, sheet_names[[4]])
  emulsions <- extract_emulsions(read_sheet_grid(workbook, 5), file_label, sheet_names[[5]])
  comparative <- extract_comparative(read_sheet_grid(workbook, 6), file_label, sheet_names[[6]])
  economic <- extract_economic(read_sheet_grid(workbook, 7), file_label, sheet_names[[7]])
  canonical <- rbind(usinability, emulsions, comparative, economic)
  canonical[order(canonical$data_domain, canonical$fluid_id, canonical$metric, canonical$condition, canonical$source_cell), , drop = FALSE]
}
