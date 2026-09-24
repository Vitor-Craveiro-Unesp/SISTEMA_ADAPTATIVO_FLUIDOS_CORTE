library(targets)

tar_option_set(
  packages = c(
    "dplyr", "tidyr", "readr", "readxl", "openxlsx2",
    "janitor", "ggplot2", "purrr", "stringr", "tibble", "yaml"
  )
)

list(
  tar_target(
    raw_xlsx,
    "data/raw/ensaio_bancada_alunos.xlsx",
    format = "file"
  )
  # Acrescentar targets à medida que cada etapa for implementada.
)
