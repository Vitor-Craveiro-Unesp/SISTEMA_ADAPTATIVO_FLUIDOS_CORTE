# ADA inicial: descrição exploratória sem escolha de critérios, pesos ou ranking.

initial_eda_summary <- function(canonical_data) {
  numeric_data <- canonical_data[!is.na(canonical_data$value_numeric), , drop = FALSE]
  groups <- unique(numeric_data[, c("data_domain", "metric", "unit"), drop = FALSE])
  do.call(rbind, lapply(seq_len(nrow(groups)), function(index) {
    rows <- numeric_data[numeric_data$data_domain == groups$data_domain[[index]] &
      numeric_data$metric == groups$metric[[index]] &
      ((is.na(numeric_data$unit) & is.na(groups$unit[[index]])) |
        (!is.na(numeric_data$unit) & !is.na(groups$unit[[index]]) & numeric_data$unit == groups$unit[[index]])), , drop = FALSE]
    data.frame(
      data_domain = groups$data_domain[[index]], metric = groups$metric[[index]], unit = groups$unit[[index]],
      n = nrow(rows), min = min(rows$value_numeric), median = stats::median(rows$value_numeric),
      mean = mean(rows$value_numeric), max = max(rows$value_numeric), stringsAsFactors = FALSE
    )
  }))
}
