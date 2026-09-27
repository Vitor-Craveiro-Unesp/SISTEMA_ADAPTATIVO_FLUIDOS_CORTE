import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const processed = path.join(root, "data", "processed");
const font = "Arial";

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    if (quoted) {
      if (char === '"' && text[i + 1] === '"') {
        field += '"';
        i += 1;
      } else if (char === '"') {
        quoted = false;
      } else {
        field += char;
      }
    } else if (char === '"') {
      quoted = true;
    } else if (char === ",") {
      row.push(field);
      field = "";
    } else if (char === "\n") {
      row.push(field.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      field = "";
    } else {
      field += char;
    }
  }
  if (field.length > 0 || row.length > 0) {
    row.push(field.replace(/\r$/, ""));
    rows.push(row);
  }
  const [headers, ...values] = rows;
  return { headers, rows: values.map((items) => Object.fromEntries(headers.map((header, index) => [header, items[index] ?? ""]))) };
}

async function readCsv(name) {
  return parseCsv(await fs.readFile(path.join(processed, name), "utf8"));
}

function excelColumn(index) {
  let value = index + 1;
  let result = "";
  while (value > 0) {
    const remainder = (value - 1) % 26;
    result = String.fromCharCode(65 + remainder) + result;
    value = Math.floor((value - 1) / 26);
  }
  return result;
}

function coerceValue(value) {
  if (value === "NA") return "NA";
  if (/^-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(value)) return Number(value);
  return value;
}

function tableValues(data, headers = data.headers) {
  return [headers, ...data.rows.map((row) => headers.map((header) => coerceValue(row[header])))];
}

function styleTableHeader(range) {
  range.format = {
    fill: "#1F4E78",
    font: { name: font, bold: true, color: "#FFFFFF", size: 10 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
  };
}

function formatSheetBase(sheet) {
  sheet.getRange("A1").format.font = { name: font, size: 14, bold: true, color: "#17365D" };
  sheet.getRange("A2").format.font = { name: font, size: 10, italic: true, color: "#666666" };
}

const matrix = await readCsv("matriz_candidata_completa_v1.csv");
const metadata = await readCsv("matriz_candidata_completa_metadados_v1.csv");
const flags = await readCsv("matriz_candidata_completa_flags_v1.csv");
const flaggedColumns = new Set(metadata.rows.filter((row) => row.possible_duplicate === "TRUE").map((row) => row.wide_column_name));
const naCells = flags.rows.filter((row) => row.na_flag === "TRUE");

const workbook = Workbook.create();

const summary = workbook.worksheets.add("Resumo");
formatSheetBase(summary);
summary.getRange("A1").values = [["Matriz candidata completa v1"]];
summary.getRange("A2").values = [["Base de inspeção sob revisão. Não é a matriz de decisão oficial e não possui pesos, orientação ou ranking."]];
summary.getRange("A4:B9").values = [
  ["Item", "Valor"],
  ["Fluidos", matrix.rows.length],
  ["Variáveis", matrix.headers.length - 1],
  ["Células NA", naCells.length],
  ["Colunas com possível duplicata", flaggedColumns.size],
  ["Fonte", "data/raw/ensaio_bancada_alunos (2).xlsx"],
];
styleTableHeader(summary.getRange("A4:B4"));
summary.getRange("A4:B9").format.font = { name: font, size: 10 };
summary.getRange("A4:B9").format.columnWidth = 28;
summary.getRange("A11").values = [["Como ler"]];
summary.getRange("A11").format.font = { name: font, size: 11, bold: true, color: "#17365D" };
summary.getRange("A12").values = [["Cabeçalhos com POSSÍVEL DUPLICATA indicam sobreposição possível entre abas. Não representam erro automático."]];
summary.getRange("A13").values = [["NA é ausência registrada na fonte e não deve ser interpretado como zero."]];
summary.getRange("A14").values = [["Aba Matriz candidata: valores. Aba Metadados: definição e origem. Aba Rastreabilidade: marcações por célula."]];
summary.getRange("A12:A14").format = { font: { name: font, size: 10 }, wrapText: true };
summary.getRange("A:A").format.columnWidth = 80;
summary.getRange("B:B").format.columnWidth = 32;

const candidate = workbook.worksheets.add("Matriz candidata");
formatSheetBase(candidate);
candidate.getRange("A1").values = [["Matriz candidata completa v1"]];
candidate.getRange("A2").values = [["Valores preservados da base canônica v1. NA = ausente. Cabeçalho amarelo = possível duplicata; consulte Metadados e Rastreabilidade."]];
const candidateHeaders = matrix.headers.map((header) => {
  if (header === "fluid_id") return "Fluido";
  const meta = metadata.rows.find((row) => row.wide_column_name === header);
  return meta ? `${meta.display_label}${meta.possible_duplicate === "TRUE" ? " [POSSÍVEL DUPLICATA]" : ""}` : header;
});
const candidateRows = matrix.rows.map((row) => matrix.headers.map((header) => coerceValue(row[header])));
candidate.getRangeByIndexes(3, 0, candidateRows.length + 1, candidateHeaders.length).values = [candidateHeaders, ...candidateRows];
const candidateLastColumn = excelColumn(candidateHeaders.length - 1);
styleTableHeader(candidate.getRange(`A4:${candidateLastColumn}4`));
candidate.getRange(`A4:${candidateLastColumn}${candidateRows.length + 4}`).format.font = { name: font, size: 10 };
candidate.getRange(`A4:A${candidateRows.length + 4}`).format.font = { name: font, size: 10, bold: true };
candidate.getRange(`A4:A${candidateRows.length + 4}`).format.columnWidth = 12;
candidate.getRange(`B4:${candidateLastColumn}${candidateRows.length + 4}`).format.columnWidth = 16;
candidate.getRange(`A4:${candidateLastColumn}4`).format.rowHeight = 78;
candidate.freezePanes.freezeRows(4);
candidate.freezePanes.freezeColumns(1);
candidate.tables.add(`A4:${candidateLastColumn}${candidateRows.length + 4}`, true, "MatrizCandidata");
matrix.headers.forEach((header, index) => {
  if (flaggedColumns.has(header)) {
    const column = excelColumn(index);
    candidate.getRange(`${column}4`).format.fill = "#FCE4B2";
    candidate.getRange(`${column}5:${column}${candidateRows.length + 4}`).format.fill = "#FFF8E8";
  }
});
matrix.rows.forEach((row, rowIndex) => {
  matrix.headers.forEach((header, columnIndex) => {
    if (row[header] === "NA") {
      const address = `${excelColumn(columnIndex)}${rowIndex + 5}`;
      candidate.getRange(address).format = { fill: "#FDE9E7", font: { name: font, color: "#C00000", bold: true, size: 10 } };
    }
  });
});

const metadataSheet = workbook.worksheets.add("Metadados");
formatSheetBase(metadataSheet);
metadataSheet.getRange("A1").values = [["Metadados das colunas da matriz"]];
metadataSheet.getRange("A2").values = [["Use esta aba para localizar origem, unidade, condição, ausências e motivo de possível duplicata."]];
const metadataValues = tableValues(metadata);
metadataSheet.getRangeByIndexes(3, 0, metadataValues.length, metadata.headers.length).values = metadataValues;
const metadataLastColumn = excelColumn(metadata.headers.length - 1);
styleTableHeader(metadataSheet.getRange(`A4:${metadataLastColumn}4`));
metadataSheet.getRange(`A4:${metadataLastColumn}${metadataValues.length + 3}`).format.font = { name: font, size: 10 };
metadataSheet.getRange(`A4:${metadataLastColumn}${metadataValues.length + 3}`).format.wrapText = true;
metadataSheet.getRange(`A4:${metadataLastColumn}4`).format.rowHeight = 42;
metadataSheet.getRange(`A:A`).format.columnWidth = 34;
metadataSheet.getRange(`B:F`).format.columnWidth = 18;
metadataSheet.getRange(`G:G`).format.columnWidth = 32;
metadataSheet.getRange(`H:J`).format.columnWidth = 18;
metadataSheet.getRange(`K:K`).format.columnWidth = 55;
metadataSheet.getRange(`L:O`).format.columnWidth = 18;
metadataSheet.freezePanes.freezeRows(4);
metadataSheet.tables.add(`A4:${metadataLastColumn}${metadataValues.length + 3}`, true, "MetadadosMatriz");

const trace = workbook.worksheets.add("Rastreabilidade");
formatSheetBase(trace);
trace.getRange("A1").values = [["Rastreabilidade e marcações por célula"]];
trace.getRange("A2").values = [["Cada linha reconstrói o valor até a aba e célula de origem. Filtre na_flag ou possible_duplicate para revisão."]];
const traceValues = tableValues(flags);
trace.getRangeByIndexes(3, 0, traceValues.length, flags.headers.length).values = traceValues;
const traceLastColumn = excelColumn(flags.headers.length - 1);
styleTableHeader(trace.getRange(`A4:${traceLastColumn}4`));
trace.getRange(`A4:${traceLastColumn}${traceValues.length + 3}`).format.font = { name: font, size: 10 };
trace.getRange(`A4:${traceLastColumn}${traceValues.length + 3}`).format.wrapText = true;
trace.getRange(`A4:${traceLastColumn}4`).format.rowHeight = 42;
trace.getRange(`A:A`).format.columnWidth = 34;
trace.getRange(`B:H`).format.columnWidth = 18;
trace.getRange(`I:Q`).format.columnWidth = 24;
trace.getRange(`R:R`).format.columnWidth = 58;
trace.freezePanes.freezeRows(4);
trace.tables.add(`A4:${traceLastColumn}${traceValues.length + 3}`, true, "RastreabilidadeMatriz");

workbook.recalculate();
const inspection = await workbook.inspect({
  kind: "table",
  range: "Resumo!A1:B14",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 4,
});
console.log(inspection.ndjson);
const image = await workbook.render({ sheetName: "Resumo", range: "A1:B14", scale: 1.5, format: "png" });
await fs.writeFile(path.join(processed, "matriz_candidata_completa_v1_resumo.png"), new Uint8Array(await image.arrayBuffer()));
const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(path.join(processed, "matriz_candidata_completa_v1.xlsx"));
