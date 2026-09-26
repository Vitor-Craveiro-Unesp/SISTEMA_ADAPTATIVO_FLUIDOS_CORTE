# Auditoria de unidades e mistura texto/número.

normalize_unit <- function(unit) {
  if (is.na(unit) || !nzchar(trimws(unit))) return(NA_character_)
  lookup <- c(
    "cm³" = "cm3", "cm3" = "cm3", "µm" = "um", "μm" = "um",
    "μS/cm" = "uS/cm", "µS/cm" = "uS/cm", "R$/L" = "BRL/L",
    "R$" = "BRL", "UFC/ml" = "UFC/mL", "M/N" = "mN/m"
  )
  unit <- trimws(as.character(unit))
  mapped <- unname(lookup[unit])
  if (!is.na(mapped)) mapped else unit
}

unit_summary <- function(canonical_data) {
  output <- aggregate(
    canonical_data$source_cell,
    by = list(data_domain = canonical_data$data_domain, metric = canonical_data$metric, unit = canonical_data$unit),
    FUN = length
  )
  names(output)[4] <- "observations"
  output[order(output$data_domain, output$metric, output$unit), , drop = FALSE]
}
