# Inventário de abas, dimensões, tipos, fórmulas e fluidos.

is_blank_cell <- function(x) {
  is.na(x) || (is.character(x) && !nzchar(trimws(x)))
}

excel_column_name <- function(index) {
  letters <- ""
  while (index > 0L) {
    remainder <- (index - 1L) %% 26L
    letters <- paste0(LETTERS[remainder + 1L], letters)
    index <- (index - 1L) %/% 26L
  }
  letters
}

detect_header_row <- function(grid, max_rows = 25L) {
  if (nrow(grid) == 0L || ncol(grid) == 0L) return(NA_integer_)
  candidate_rows <- seq_len(min(nrow(grid), max_rows))
  scores <- vapply(candidate_rows, function(row_index) {
    values <- unlist(grid[row_index, , drop = FALSE], use.names = FALSE)
    values <- values[!vapply(values, is_blank_cell, logical(1))]
    if (length(values) == 0L) return(0)
    text_share <- mean(vapply(values, function(value) is.character(value) && !is.na(value), logical(1)))
    length(values) + text_share
  }, numeric(1))
  candidate_rows[which.max(scores)]
}

apparent_type <- function(values) {
  non_blank <- values[!vapply(values, is_blank_cell, logical(1))]
  if (length(non_blank) == 0L) return("all_blank")
  if (all(vapply(non_blank, is.numeric, logical(1)))) return("numeric")
  if (all(vapply(non_blank, function(x) inherits(x, "Date") || inherits(x, "POSIXt"), logical(1)))) return("date_time")
  if (all(vapply(non_blank, is.logical, logical(1)))) return("logical")
  "mixed_or_text"
}

sheet_inventory <- function(workbook, file_label) {
  sheets <- openxlsx::sheets(workbook)
  do.call(rbind, lapply(seq_along(sheets), function(index) {
    grid <- read_sheet_grid(workbook, sheets[[index]])
    non_blank <- if (nrow(grid) == 0L || ncol(grid) == 0L) 0L else sum(!is.na(as.matrix(grid)) & trimws(as.character(as.matrix(grid))) != "")
    data.frame(
      source_file = file_label,
      sheet_index = index,
      sheet_name = sheets[[index]],
      rows_read = nrow(grid),
      columns_read = ncol(grid),
      non_blank_cells = non_blank,
      provisional_header_row = detect_header_row(grid),
      stringsAsFactors = FALSE
    )
  }))
}

variable_inventory <- function(workbook, file_label) {
  sheets <- openxlsx::sheets(workbook)
  records <- lapply(sheets, function(sheet) {
    grid <- read_sheet_grid(workbook, sheet)
    header_row <- detect_header_row(grid)
    if (ncol(grid) == 0L) return(NULL)
    do.call(rbind, lapply(seq_len(ncol(grid)), function(column_index) {
      values <- unlist(grid[, column_index, drop = FALSE], use.names = FALSE)
      header <- if (!is.na(header_row) && header_row <= nrow(grid)) as.character(grid[header_row, column_index][[1]]) else NA_character_
      non_blank <- values[!vapply(values, is_blank_cell, logical(1))]
      data.frame(
        source_file = file_label,
        sheet_name = sheet,
        column_index = column_index,
        excel_column = excel_column_name(column_index),
        provisional_header = ifelse(is.na(header) || !nzchar(trimws(header)), NA_character_, trimws(header)),
        apparent_type = apparent_type(values),
        rows_non_blank = length(non_blank),
        rows_blank = sum(vapply(values, is_blank_cell, logical(1))),
        distinct_non_blank = length(unique(as.character(non_blank))),
        example_values = paste(utils::head(unique(as.character(non_blank)), 3L), collapse = " | "),
        stringsAsFactors = FALSE
      )
    }))
  })
  records <- Filter(Negate(is.null), records)
  if (length(records) == 0L) return(data.frame())
  do.call(rbind, records)
}

xml_attr <- function(tag, attribute) {
  match <- regmatches(tag, regexpr(paste0(attribute, "=\\\"[^\\\"]*\\\""), tag, perl = TRUE))
  if (length(match) == 0L || !nzchar(match)) return(NA_character_)
  sub(paste0("^", attribute, "=\\\"|\\\"$"), "", match)
}

formula_inventory <- function(xlsx_path, file_label) {
  archive_files <- utils::unzip(xlsx_path, list = TRUE)$Name
  if (!all(c("xl/workbook.xml", "xl/_rels/workbook.xml.rels") %in% archive_files)) {
    stop("O arquivo não contém a estrutura OOXML esperada para auditoria de fórmulas.", call. = FALSE)
  }
  extraction_dir <- tempfile("pacheco_xlsx_")
  dir.create(extraction_dir)
  on.exit(unlink(extraction_dir, recursive = TRUE, force = TRUE), add = TRUE)
  utils::unzip(xlsx_path, exdir = extraction_dir)

  workbook_xml <- paste(readLines(file.path(extraction_dir, "xl", "workbook.xml"), warn = FALSE, encoding = "UTF-8"), collapse = "")
  rels_xml <- paste(readLines(file.path(extraction_dir, "xl", "_rels", "workbook.xml.rels"), warn = FALSE, encoding = "UTF-8"), collapse = "")
  sheet_tags <- regmatches(workbook_xml, gregexpr("<sheet\\b[^>]*?/>", workbook_xml, perl = TRUE))[[1]]
  rel_tags <- regmatches(rels_xml, gregexpr("<Relationship\\b[^>]*?/>", rels_xml, perl = TRUE))[[1]]
  relationship_targets <- stats::setNames(
    vapply(rel_tags, xml_attr, character(1), attribute = "Target"),
    vapply(rel_tags, xml_attr, character(1), attribute = "Id")
  )

  records <- lapply(sheet_tags, function(sheet_tag) {
    sheet_name <- xml_attr(sheet_tag, "name")
    relationship_id <- xml_attr(sheet_tag, "r:id")
    target <- relationship_targets[[relationship_id]]
    if (is.null(target) || !nzchar(target)) return(NULL)
    sheet_xml_path <- file.path(extraction_dir, "xl", target)
    if (!file.exists(sheet_xml_path)) return(NULL)
    sheet_xml <- paste(readLines(sheet_xml_path, warn = FALSE, encoding = "UTF-8"), collapse = "")
    cell_tags <- regmatches(sheet_xml, gregexpr("<c\\b[^>]*>.*?<f(?:\\s[^>]*)?>(?:<!\\[CDATA\\[)?[^<]*(?:\\]\\]>)?</f>.*?</c>", sheet_xml, perl = TRUE))[[1]]
    if (length(cell_tags) == 0L) return(NULL)
    data.frame(
      source_file = file_label,
      sheet_name = sheet_name,
      cell = vapply(cell_tags, function(tag) xml_attr(sub("^<c", "<cell", tag), "r"), character(1)),
      formula = paste0("=", vapply(cell_tags, function(tag) sub("^.*?<f(?:\\s[^>]*)?>(?:<!\\[CDATA\\[)?([^<]*?)(?:\\]\\]>)?</f>.*$", "\\1", tag, perl = TRUE), character(1))),
      stringsAsFactors = FALSE
    )
  })
  records <- Filter(Negate(is.null), records)
  if (length(records) == 0L) {
    return(data.frame(source_file = character(), sheet_name = character(), cell = character(), formula = character()))
  }
  do.call(rbind, records)
}
