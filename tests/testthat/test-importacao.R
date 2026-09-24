testthat::test_that("Arquivo bruto existe", {
  testthat::expect_true(file.exists("data/raw/ensaio_bancada_alunos.xlsx"))
})
