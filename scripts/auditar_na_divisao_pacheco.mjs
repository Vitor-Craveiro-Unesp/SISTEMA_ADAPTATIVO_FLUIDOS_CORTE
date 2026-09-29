import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const dir = path.join(root, "data", "processed", "divisao");
const file = path.join(dir, "economico_v1.xlsx");
const previewOnly = process.argv.includes("--preview-only");
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const data = wb.worksheets.getItem("Dados");

async function preview(suffix) {
  const image = await wb.render({ sheetName: "Dados", range: "A9:Q11", scale: 1.2, format: "png" });
  const target = path.join(os.tmpdir(), `auditoria_na_pacheco_${suffix}.png`);
  await fs.writeFile(target, new Uint8Array(await image.arrayBuffer()));
  console.log(`Prévia: ${target}`);
  const legend = await wb.render({ sheetName: "Leia-me", range: "A16:B22", scale: 1.2, format: "png" });
  const legendTarget = path.join(os.tmpdir(), `auditoria_na_pacheco_legenda_${suffix}.png`);
  await fs.writeFile(legendTarget, new Uint8Array(await legend.arrayBuffer()));
  console.log(`Prévia da legenda: ${legendTarget}`);
}

if (previewOnly) {
  await preview("antes");
  process.exit(0);
}

const red = [
  ["AA10", 2242.7], ["I10", 0.8918], ["N10", 117.5584],
  ["AA11", 2450.7], ["I11", 0.8161], ["N11", 117.4828],
];
const green = ["E10", "F10", "G10", "K10", "L10", "M10", "E11", "F11", "M11"];
const pink = ["B10", "D10", "P10", "Q10", "U10", "B11", "D11", "P11", "Q11"];
const expectedIds = ["J", "K"];
for (const [row, id] of [[10, expectedIds[0]], [11, expectedIds[1]]]) {
  if (data.getRange(`A${row}`).values[0][0] !== id) throw new Error(`Fluido inesperado na linha ${row}`);
}
for (const [address] of red) {
  if (data.getRange(address).values[0][0] !== "NA") throw new Error(`${address} não está NA`);
}
for (const address of green) {
  if (data.getRange(address).values[0][0] !== 0) throw new Error(`${address} não é zero`);
}
for (const address of pink) {
  if (data.getRange(address).values[0][0] !== "NA") throw new Error(`${address} não está NA`);
}

for (const [address, value] of red) {
  const cell = data.getRange(address);
  cell.values = [[value]];
  cell.format.fill = "#FF0000";
  cell.format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
  cell.setNumberFormat(address.startsWith("AA") ? "0.0" : "0.0000");
}
for (const address of green) {
  const cell = data.getRange(address);
  cell.format.fill = "#00B050";
  cell.format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
}
for (const address of pink) {
  const cell = data.getRange(address);
  cell.format.fill = "#FFB6C1";
  cell.format.font = { name: "Arial", size: 10, bold: true, color: "#7A1538" };
}

const readme = wb.worksheets.getItem("Leia-me");
readme.getRange("A16:B22").values = [
  ["Auditoria de NA", "Pacheco — sob revisão"],
  ["VERMELHO", "Valor reconstruído/preenchido com base em relação determinística e dados da matriz original."],
  ["VERDE", "Zero suspeito que pode representar NA escondido; valor original preservado."],
  ["ROSA", "NA explícito que permanece sem solução segura; valor original preservado."],
  ["Células reconstruídas", 6],
  ["Zeros suspeitos", 9],
  ["NA explícitos não resolvidos", 9],
];
readme.getRange("A16:B22").format.font = { name: "Arial", size: 10, color: "#17212D" };
readme.getRange("A16:B16").format.fill = "#23517C";
readme.getRange("A16:B16").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
readme.getRange("A17").format.fill = "#FF0000";
readme.getRange("A17").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
readme.getRange("A18").format.fill = "#00B050";
readme.getRange("A18").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
readme.getRange("A19").format.fill = "#FFB6C1";
readme.getRange("A19").format.font = { name: "Arial", size: 10, bold: true, color: "#7A1538" };
readme.getRange("B17:B19").format.wrapText = true;
readme.getRange("A17:B19").format.rowHeight = 38;

wb.recalculate();
const result = await wb.inspect({ kind: "table", range: "Leia-me!A16:B22", include: "values,formulas", tableMaxRows: 7, tableMaxCols: 2, maxChars: 4000 });
console.log(result.ndjson);
const errors = await wb.inspect({
  kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 }, maxChars: 2500,
});
console.log(`Busca de erros: ${errors.ndjson}`);
await preview("depois");
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(file);
console.log(`Arquivo editado: ${file}`);
