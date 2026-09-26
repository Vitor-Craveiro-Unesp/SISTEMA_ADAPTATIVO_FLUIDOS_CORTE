# Classificação de ausências. Ausência, zero e texto observacional são distintos.

is_missing_value <- function(x) {
  is.na(x) || (is.character(x) && !nzchar(trimws(x)))
}

missing_summary <- function(canonical_data) {
  groups <- unique(canonical_data[, c("data_domain", "metric"), drop = FALSE])
  output <- lapply(seq_len(nrow(groups)), function(index) {
    rows <- canonical_data[canonical_data$data_domain == groups$data_domain[[index]] &
                             canonical_data$metric == groups$metric[[index]], , drop = FALSE]
    data.frame(
      data_domain = groups$data_domain[[index]],
      metric = groups$metric[[index]],
      observations = nrow(rows),
      missing_values = sum(rows$is_missing),
      explicit_zeroes = sum(!rows$is_missing & !is.na(rows$value_numeric) & rows$value_numeric == 0),
      textual_values = sum(!rows$is_missing & !is.na(rows$value_text)),
      missing_rate = mean(rows$is_missing),
      stringsAsFactors = FALSE
    )
  })
  do.call(rbind, output)
}
