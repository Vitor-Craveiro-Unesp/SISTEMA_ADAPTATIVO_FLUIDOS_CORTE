# Importação do XLSX preservando estrutura e tipos originais.

find_project_root <- function(start = getwd()) {
  current <- normalizePath(start, winslash = "/", mustWork = TRUE)
  repeat {
    if (file.exists(file.path(current, "AGENTS.md")) &&
        dir.exists(file.path(current, "data"))) {
      return(current)
    }
    parent <- dirname(current)
    if (identical(parent, current)) {
      stop("Não foi possível localizar a raiz do projeto.", call. = FALSE)
    }
    current <- parent
  }
}

file_sha256 <- function(path) {
  if (!requireNamespace("digest", quietly = TRUE)) {
    stop("O pacote 'digest' é necessário para calcular SHA-256.", call. = FALSE)
  }
  digest::digest(file = path, algo = "sha256")
}

relative_project_path <- function(path, project_root) {
  path_norm <- normalizePath(path, winslash = "/", mustWork = TRUE)
  root_norm <- paste0(normalizePath(project_root, winslash = "/", mustWork = TRUE), "/")
  if (startsWith(path_norm, root_norm)) {
    substring(path_norm, nchar(root_norm) + 1L)
  } else {
    path_norm
  }
}

raw_file_metadata <- function(path, project_root) {
  info <- file.info(path)
  data.frame(
    relative_path = relative_project_path(path, project_root),
    file_name = basename(path),
    extension = tools::file_ext(path),
    bytes = unname(info$size),
    modified_at = format(info$mtime, tz = "UTC", usetz = TRUE),
    sha256 = file_sha256(path),
    stringsAsFactors = FALSE
  )
}

copy_working_xlsx <- function(raw_path, interim_path) {
  dir.create(dirname(interim_path), recursive = TRUE, showWarnings = FALSE)
  copied <- file.copy(raw_path, interim_path, overwrite = TRUE, copy.date = TRUE)
  if (!isTRUE(copied)) {
    stop("Não foi possível criar a cópia de trabalho do XLSX.", call. = FALSE)
  }
  raw_hash <- file_sha256(raw_path)
  interim_hash <- file_sha256(interim_path)
  if (!identical(raw_hash, interim_hash)) {
    stop("A cópia de trabalho não preservou o SHA-256 do arquivo bruto.", call. = FALSE)
  }
  invisible(list(raw_sha256 = raw_hash, interim_sha256 = interim_hash))
}

load_xlsx_readonly <- function(path) {
  if (!requireNamespace("openxlsx", quietly = TRUE)) {
    stop("O pacote 'openxlsx' é necessário para ler o XLSX.", call. = FALSE)
  }
  openxlsx::loadWorkbook(path, isUnzipped = FALSE)
}

read_sheet_grid <- function(workbook, sheet) {
  openxlsx::readWorkbook(
    workbook,
    sheet = sheet,
    colNames = FALSE,
    skipEmptyRows = FALSE,
    skipEmptyCols = FALSE,
    check.names = FALSE,
    fillMergedCells = FALSE
  )
}
