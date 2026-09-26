source("R/pacheco/importacao.R")
source("R/pacheco/missing.R")
source("R/pacheco/unidades.R")

testthat::test_that("a cópia de trabalho conserva o hash do XLSX bruto", {
  comparison <- utils::read.csv("results/audit/working_copy_verification_v1.csv", check.names = FALSE)
  testthat::expect_true(comparison$hashes_match[[1]])
  testthat::expect_identical(comparison$raw_sha256[[1]], comparison$interim_sha256[[1]])
})

testthat::test_that("a base canônica preserva linhagem e ausências", {
  canonical <- readRDS("data/processed/base_canonica_v1.rds")
  testthat::expect_true(all(c("source_file", "source_sheet", "source_cell", "is_missing") %in% names(canonical)))
  testthat::expect_equal(sum(duplicated(canonical[, c("source_sheet", "source_cell")])), 0L)
  testthat::expect_true(any(canonical$is_missing))
  testthat::expect_true(any(!is.na(canonical$value_text)))
})

testthat::test_that("zero não é reclassificado como ausência", {
  canonical <- readRDS("data/processed/base_canonica_v1.rds")
  zeroes <- canonical[!canonical$is_missing & !is.na(canonical$value_numeric) & canonical$value_numeric == 0, ]
  testthat::expect_gt(nrow(zeroes), 0L)
  testthat::expect_false(any(zeroes$is_missing))
})
