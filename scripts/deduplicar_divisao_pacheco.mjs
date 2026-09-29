import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

// Deduplicação conservadora das projeções da matriz candidata.
// Não altera data/raw nem a base canônica; a fonte e as divergências permanecem.
const root = process.cwd();
const folder = path.join(root, "data", "processed", "divisao");
const sourceFolder = path.join(folder, "backup_pre_deduplicacao");
const stage = path.join(folder, ".dedup_stage");
const suffix = " [POSSÍVEL DUPLICATA]";

const specs = [
  {
    file: "desempenho_usinagem_v1.xlsx",
    drop: (label) => label.startsWith("comparativo | potencia | condicao_") ||
      label.startsWith("comparativo | vida_ferramenta_volume_removido | condicao_1 |"),
    clearFlag: (label) => label.startsWith("usinabilidade | potencia_corte | condicao_") ||
      label.startsWith("usinabilidade | vida_ferramenta_volume_removido | condicao_1 |") ||
      label.startsWith("comparativo | vida_ferramenta_volume_removido | somatorio |"),
    expectedDrops: 5,
    noteRow: 24,
    amber: ["B10", "C3", "C4", "C5", "D3", "D4", "L3", "L4", "L5", "M3", "M4", "K10"],
    note: "Cinco colunas idênticas (44 valores de potência e 11 da vida, condição 1) foram retiradas desta projeção. Mantidas as medições da ANÁLISE USINABILIDADE; diferenças nas condições 2–4 da vida ainda exigem reconciliação.",
  },
  {
    file: "propriedades_estabilidade_fluido_v1.xlsx",
    drop: (label) => label.startsWith("comparativo | nevoa |"),
    clearFlag: () => false,
    expectedDrops: 1,
    noteRow: 25,
    amber: ["K3", "N5", "N6", "N7", "N9", "C10", "R10", "C11", "R11", "U4", "U6"],
    note: "A coluna comparativo | nevoa, idêntica nos 11 fluidos à NÉVOA de ANÁLISE EMULSÕES, foi retirada desta projeção. Bactérias/espuma e contagens em momentos distintos permanecem por representarem variáveis diferentes.",
  },
];

function base(label) {
  return String(label ?? "").replace(suffix, "");
}

function moveColumn(sheet, sourceCol, targetCol, lastRow) {
  if (sourceCol === targetCol) return;
  sheet.getRangeByIndexes(0, targetCol - 1, lastRow, 1)
    .copyFrom(sheet.getRangeByIndexes(0, sourceCol - 1, lastRow, 1), "all");
}

function compactRows(sheet, firstRow, lastRow, width, keep) {
  const snapshot = sheet.getRangeByIndexes(firstRow - 1, 0, lastRow - firstRow + 1, width).values;
  let targetRow = firstRow;
  for (let i = 0; i < snapshot.length; i++) {
    if (!keep(snapshot[i])) continue;
    const sourceRow = firstRow + i;
    if (targetRow !== sourceRow) {
      sheet.getRangeByIndexes(targetRow - 1, 0, 1, width)
        .copyFrom(sheet.getRangeByIndexes(sourceRow - 1, 0, 1, width), "all");
    }
    targetRow++;
  }
  if (targetRow <= lastRow) {
    sheet.getRangeByIndexes(targetRow - 1, 0, lastRow - targetRow + 1, width)
      .clear({ applyTo: "all" });
  }
  return targetRow - firstRow;
}

function setReadme(readme, key, value) {
  const rows = readme.getRange("A1:B30").values;
  const index = rows.findIndex((row) => row[0] === key);
  if (index < 0) throw new Error(`Leia-me: chave ausente ${key}`);
  readme.getRangeByIndexes(index, 1, 1, 1).values = [[value]];
}

await fs.mkdir(stage, { recursive: true });
for (const spec of specs) {
  const source = path.join(sourceFolder, spec.file);
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(source));
  const data = workbook.worksheets.getItem("Dados");
  const dictionary = workbook.worksheets.getItem("Dicionário");
  const trace = workbook.worksheets.getItem("Rastreabilidade");
  const readme = workbook.worksheets.getItem("Leia-me");
  const originalCount = Number(readme.getRange("B3").values[0][0]);
  const summaryCount = Number(readme.getRange("B4").values[0][0]);
  const totalCols = 1 + originalCount + summaryCount;
  const headings = data.getRangeByIndexes(0, 0, 1, totalCols).values[0];
  const originals = headings.slice(1, originalCount + 1).map(base);
  const dropped = originals.filter(spec.drop);
  if (dropped.length !== spec.expectedDrops) {
    throw new Error(`${spec.file}: esperadas ${spec.expectedDrops} exclusões, encontradas ${dropped.length}`);
  }
  const dropSet = new Set(dropped);
  const oldColumns = [];
  for (let col = 2; col <= totalCols; col++) {
    if (col <= originalCount + 1 && dropSet.has(base(headings[col - 1]))) continue;
    oldColumns.push(col);
  }
  const newOriginalCount = originalCount - dropped.length;
  if (oldColumns.length !== newOriginalCount + summaryCount) throw new Error("Contagem de colunas inconsistente");

  // Copia da esquerda para a direita: cada origem tem índice >= destino.
  oldColumns.forEach((oldCol, index) => moveColumn(data, oldCol, index + 2, 12));
  data.getRangeByIndexes(0, oldColumns.length + 1, 12, dropped.length).clear({ applyTo: "all" });

  const dictionaryKept = compactRows(dictionary, 2, 1 + originalCount + summaryCount, 12,
    (row) => !dropSet.has(base(row[0])));
  if (dictionaryKept !== newOriginalCount + summaryCount) throw new Error("Dicionário: contagem incorreta");
  const traceKept = compactRows(trace, 2, 1 + 11 * originalCount, 9,
    (row) => !dropSet.has(base(row[1])));
  if (traceKept !== 11 * newOriginalCount) throw new Error("Rastreabilidade: contagem incorreta");

  // Remove a sinalização de duplicata apenas onde a cópia exata saiu ou onde
  // o campo é um agregado, não outra medição. Mantém os pares divergentes.
  for (let col = 2; col <= newOriginalCount + 1; col++) {
    const cell = data.getRangeByIndexes(0, col - 1, 1, 1);
    const label = base(cell.values[0][0]);
    if (spec.clearFlag(label)) cell.values = [[label]];
    cell.format.fill = cell.values[0][0].endsWith(suffix) ? "#B78019" : "#23517C";
  }
  const lastOriginalCol = newOriginalCount + 1;
  const lastColumn = lastOriginalCol + summaryCount;
  const originalBody = data.getRangeByIndexes(1, 1, 11, newOriginalCount);
  originalBody.format.fill = null;
  originalBody.format.font = { name: "Arial", size: 10, bold: false, color: "#17212D" };
  originalBody.format.numberFormat = "0.00########";
  originalBody.format.wrapText = true;
  const summaryHeader = data.getRangeByIndexes(0, lastOriginalCol, 1, summaryCount);
  summaryHeader.format.fill = "#9A6400";
  summaryHeader.format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
  const summaryBody = data.getRangeByIndexes(1, lastOriginalCol, 11, summaryCount);
  summaryBody.format.fill = "#FFF5DE";
  summaryBody.format.font = { name: "Arial", size: 10, bold: false, color: "#17212D" };
  summaryBody.format.numberFormat = "General";
  summaryBody.format.wrapText = false;
  for (const address of spec.amber) {
    const cell = data.getRange(address);
    cell.format.fill = "#FFC000";
    cell.format.font = { name: "Arial", size: 10, bold: true, color: "#493600" };
  }
  if (lastColumn !== 1 + oldColumns.length) throw new Error("Largura calculada inconsistente");

  const dictionaryBody = dictionary.getRangeByIndexes(1, 0, newOriginalCount + summaryCount, 12);
  dictionaryBody.format.fill = null;
  dictionaryBody.format.font = { name: "Arial", size: 10, bold: false, color: "#17212D" };
  dictionaryBody.format.wrapText = true;
  dictionary.getRangeByIndexes(newOriginalCount + 1, 0, summaryCount, 12).format.fill = "#FFF5DE";
  for (let row = 2; row <= newOriginalCount + 1; row++) {
    const label = base(dictionary.getRangeByIndexes(row - 1, 0, 1, 1).values[0][0]);
    if (!spec.clearFlag(label)) continue;
    dictionary.getRangeByIndexes(row - 1, 7, 1, 2).values = [["NÃO", null]];
    dictionary.getRangeByIndexes(row - 1, 11, 1, 1).values = [[
      label.includes("somatorio")
        ? "Agregado de quatro condições no COMPARATIVO; não é duplicata de uma condição. Conferir cálculo e divergências entre fontes antes de selecionar critério."
        : "Cópia idêntica de outra aba retirada desta projeção. Valor da ANÁLISE USINABILIDADE mantido; fonte bruta preservada.",
    ]];
  }
  for (let row = 2; row <= traceKept + 1; row++) {
    const label = base(trace.getRangeByIndexes(row - 1, 1, 1, 1).values[0][0]);
    if (spec.clearFlag(label)) {
      trace.getRangeByIndexes(row - 1, 6, 1, 2).values = [["NÃO", null]];
    }
  }

  readme.getRange("B3").values = [[newOriginalCount]];
  if (spec.file.startsWith("desempenho")) {
    setReadme(readme, "Potência", "44/44 valores coincidem entre fontes. As quatro colunas do COMPARATIVO foram retiradas desta projeção; as quatro da ANÁLISE USINABILIDADE foram mantidas.");
    setReadme(readme, "Vida da ferramenta", "Condição 1 (11/11 valores iguais) mantida apenas da ANÁLISE USINABILIDADE. Condições 2–4 de ambas as fontes permanecem: seis pares divergentes exigem reconciliação.");
    setReadme(readme, "Rastreabilidade", "44 endereços restantes do COMPARATIVO estão seis linhas acima do XLSX bruto. Consultar o relatório antes de usar a coluna Célula de origem.");
    setReadme(readme, "Pendência específica", "Potência e vida da ferramenta condição 1 tiveram as cópias exatas retiradas desta projeção. Permanecem divergências na vida condições 2–4, somatório e rastreabilidade.");
  } else {
    setReadme(readme, "Rastreabilidade", "132 endereços restantes do COMPARATIVO estão seis linhas acima do XLSX bruto. Consultar o relatório antes de usar a coluna Célula de origem.");
    setReadme(readme, "Pendência específica", "A coluna repetida de névoa do COMPARATIVO foi retirada desta projeção. A concentração média ainda diverge entre abas para J/K e quatro acidezes seguem como repetir.");
  }
  const newNoteRow = spec.noteRow;
  if (readme.getRange(`A${newNoteRow}:B${newNoteRow}`).values.some((row) => row.some((value) => value !== null && value !== ""))) {
    throw new Error(`${spec.file}: linha de nota já ocupada`);
  }
  readme.getRange(`A${newNoteRow}:B${newNoteRow}`).values = [["Deduplicação exata", spec.note]];
  readme.getRange(`A${newNoteRow}:B${newNoteRow}`).format.rowHeight = 58;
  readme.getRange(`B${newNoteRow}`).format.wrapText = true;

  workbook.recalculate();
  const result = await workbook.inspect({ kind: "table", range: `Dados!A1:${spec.file.startsWith("desempenho") ? "O" : "BQ"}3`, include: "values,formulas", tableMaxRows: 3, tableMaxCols: 8, maxChars: 1800 });
  console.log(`${spec.file}: ${dropped.length} colunas retiradas; ${newOriginalCount} originais restantes; ${result.ndjson}`);
  const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!", options: { useRegex: true, maxResults: 30 }, maxChars: 1000 });
  console.log(`${spec.file}: erros ${errors.ndjson}`);
  const output = await SpreadsheetFile.exportXlsx(workbook);
  await output.save(path.join(stage, spec.file));
}
console.log(`Arquivos preparados em ${stage}; validar antes de promover.`);
