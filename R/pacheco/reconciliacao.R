# Reconciliação numérica entre abas, sem tolerância inventada.

reconcile_pairs <- function(left, right, relation) {
  merged <- merge(left, right, by = "fluid_id", all = TRUE, suffixes = c("_left", "_right"))
  merged$relation <- relation
  merged$difference <- merged$value_numeric_left - merged$value_numeric_right
  machine_precision <- sqrt(.Machine$double.eps) * pmax(1, abs(merged$value_numeric_left), abs(merged$value_numeric_right))
  merged$status <- ifelse(
    is.na(merged$value_numeric_left) | is.na(merged$value_numeric_right), "MISSING_INPUT",
    ifelse(merged$difference == 0, "MATCH_EXACT",
      ifelse(abs(merged$difference) <= machine_precision, "MATCH_MACHINE_PRECISION", "REVIEW_REQUIRED_TOLERANCE_UNDEFINED"))
  )
  merged[, c("relation", "fluid_id", "value_numeric_left", "value_numeric_right", "difference", "status"), drop = FALSE]
}

reconciliation_checks <- function(canonical_data) {
  usinability <- canonical_data[canonical_data$data_domain == "usinabilidade" &
                                  canonical_data$metric == "vida_ferramenta_volume_removido", , drop = FALSE]
  calculated_sum <- aggregate(usinability$value_numeric, by = list(fluid_id = usinability$fluid_id), FUN = sum)
  names(calculated_sum)[2] <- "value_numeric"
  comparative_total <- canonical_data[canonical_data$data_domain == "comparativo" &
                                      canonical_data$metric == "vida_ferramenta_volume_removido" &
                                      canonical_data$condition == "somatorio", c("fluid_id", "value_numeric")]
  life_total <- reconcile_pairs(calculated_sum, comparative_total, "soma_da_vida_de_ferramenta")

  economic <- canonical_data[canonical_data$data_domain == "economico", , drop = FALSE]
  pick_source_row <- function(row_number) {
    rows <- suppressWarnings(as.integer(gsub("[^0-9]", "", economic$source_cell))) == row_number
    economic[rows, c("fluid_id", "value_numeric")]
  }
  annual_fluid <- pick_source_row(29L)
  annual_operation <- pick_source_row(41L)
  reported_total <- pick_source_row(43L)
  expected_total <- merge(annual_fluid, annual_operation, by = "fluid_id", all = TRUE, suffixes = c("_fluid", "_operation"))
  expected_total$value_numeric <- expected_total$value_numeric_fluid + expected_total$value_numeric_operation
  cost_total <- reconcile_pairs(expected_total[, c("fluid_id", "value_numeric")], reported_total, "custo_total_anual_economico")
  rbind(life_total, cost_total)
}
