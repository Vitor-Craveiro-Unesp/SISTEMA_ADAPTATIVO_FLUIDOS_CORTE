import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.cwd();
const dir = path.join(root, "data", "processed", "divisao");
const output = path.join(dir, "caracteristicas_unificadas_v1.xlsx");
const sourceConfig = [
  { file: "desempenho_usinagem_v1.xlsx", tab: "Desempenho usinagem", end: "O" },
  { file: "qualidade_peca_processo_v1.xlsx", tab: "Qualidade peça processo", end: "W" },
  { file: "propriedades_estabilidade_fluido_v1.xlsx", tab: "Propriedades fluido", end: "BO" },
  { file: "economico_v1.xlsx", tab: "Econômico", end: "BA" },
];
const specialMarks = {
  "desempenho_usinagem_v1.xlsx": {
    orange: ["C3", "D3", "L3", "M3", "C4", "D4", "L4", "M4", "C5", "L5", "B10", "K10"],
  },
  "qualidade_peca_processo_v1.xlsx": {},
  "propriedades_estabilidade_fluido_v1.xlsx": {
    orange: ["K3", "U4", "N5", "N6", "U6", "N7", "N9", "C10", "R10", "C11", "R11"],
  },
  "economico_v1.xlsx": {
    blue: ["I10", "N10", "AA10", "I11", "N11", "AA11"],
    green: ["E10", "F10", "G10", "K10", "L10", "M10", "E11", "F11", "M11"],
    pink: ["B10", "D10", "P10", "Q10", "U10", "B11", "D11", "P11", "Q11"],
  },
};
const markColors = { orange: "#FFC000", blue: "#A9DCEB", green: "#00B050", pink: "#FFB6C1" };
const fluids = "ABCDEFGHJKM".split("");

function columnLetter(index) {
  let out = "";
  while (index > 0) {
    index--;
    out = String.fromCharCode(65 + (index % 26)) + out;
    index = Math.floor(index / 26);
  }
  return out;
}
function columnIndex(letters) {
  return [...letters].reduce((n, char) => n * 26 + char.charCodeAt(0) - 64, 0);
}
function physicalSourceCell(sheetName, recorded) {
  if (!recorded) return null;
  const match = /^([A-Z]+)(\d+)$/.exec(String(recorded));
  if (!match) throw new Error(`Endereço inesperado: ${sheetName}!${recorded}`);
  const row = Number(match[2]) + (sheetName === "COMPARATIVO" ? 6 : 0);
  return `${match[1]}${row}`;
}
function plainHeader(header) {
  return String(header).replace(/ \[POSSÍVEL DUPLICATA\]$/, "");
}

async function render(wb, sheetName, range, suffix) {
  const blob = await wb.render({ sheetName, range, scale: 1.15, format: "png" });
  const imagePath = path.join(os.tmpdir(), `pacheco_unificada_${suffix}.png`);
  await fs.writeFile(imagePath, new Uint8Array(await blob.arrayBuffer()));
  console.log(`Prévia: ${imagePath}`);
}

const sources = [];
for (const cfg of sourceConfig) {
  const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(dir, cfg.file)));
  sources.push({ ...cfg, wb });
}

if (process.argv.includes("--preview-input")) {
  for (let i = 0; i < sources.length; i++) {
    const src = sources[i];
    await render(src.wb, "Dados", "A1:F4", `entrada_${i + 1}`);
    console.log(`${src.file}: B1 fill=${JSON.stringify(src.wb.worksheets.getItem("Dados").getRange("B1").format.fill)}; B2 fill=${JSON.stringify(src.wb.worksheets.getItem("Dados").getRange("B2").format.fill)}`);
  }
  process.exit(0);
}
if (process.argv.includes("--preview-output")) {
  const saved = await SpreadsheetFile.importXlsx(await FileBlob.load(output));
  await render(saved, "Econômico", "H9:Q11", "economico_marcacoes");
  await render(saved, "Econômico", "Z9:AA11", "economico_vida");
  await render(saved, "Origem das colunas", "I1:K5", "origem_detalhe");
  process.exit(0);
}
if (process.argv.includes("--preview-current-lineage")) {
  const saved = await SpreadsheetFile.importXlsx(await FileBlob.load(output));
  await render(saved, "Origem das colunas", "G1:K6", "origem_antes_ajuste");
  process.exit(0);
}

const unified = Workbook.create();
const lineageRows = [];
const groups = [];
for (const src of sources) {
  const data = src.wb.worksheets.getItem("Dados");
  const sourceMatrix = data.getRange(`A1:${src.end}12`).values;
  const ncol = columnIndex(src.end);
  if (sourceMatrix.length !== 12 || sourceMatrix[0].length !== ncol) throw new Error(`Dimensão inesperada: ${src.file}`);
  for (let r = 1; r <= 11; r++) if (sourceMatrix[r][0] !== fluids[r - 1]) throw new Error(`Ordem de fluidos inesperada em ${src.file}, linha ${r + 1}`);

  const dictionary = new Map();
  for (const row of src.wb.worksheets.getItem("Dicionário").getRange("A2:L100").values) {
    if (row[0]) dictionary.set(String(row[0]), row);
  }
  const trace = new Map();
  for (const row of src.wb.worksheets.getItem("Rastreabilidade").getRange("A2:I400").values) {
    if (!row[0] || !row[1]) continue;
    const key = `${row[0]}\u0000${row[1]}`;
    if (trace.has(key)) throw new Error(`Rastreabilidade duplicada: ${src.file} ${key}`);
    trace.set(key, row);
  }

  const target = unified.worksheets.add(src.tab);
  target.getRange(`A1:${src.end}12`).values = sourceMatrix;
  target.getRange(`A1:${src.end}12`).format.font = { name: "Arial", size: 10, color: "#17212D" };
  target.getRange(`A1:${src.end}1`).format.fill = "#23517C";
  target.getRange(`A1:${src.end}1`).format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
  target.getRange(`A1:${src.end}1`).format.wrapText = true;
  target.getRange(`A1:${src.end}1`).format.rowHeight = 100;
  target.getRange(`A1:${src.end}1`).format.verticalAlignment = "center";
  target.getRange(`A1:${src.end}1`).format.horizontalAlignment = "center";
  target.getRange("A:A").format.columnWidth = 12;
  target.getRange(`B:${src.end}`).format.columnWidth = 30;
  target.getRange("A2:A12").format.font = { name: "Arial", size: 10, bold: true, color: "#17212D" };
  target.getRange(`A2:${src.end}12`).format.rowHeight = 22;
  target.freezePanes.freezeRows(1);
  target.showGridLines = false;

  let originalCount = 0;
  let pendingCount = 0;
  for (let c = 1; c <= ncol; c++) {
    const letter = columnLetter(c);
    const header = sourceMatrix[0][c - 1];
    if (!header) throw new Error(`Cabeçalho vazio em ${src.file}, ${letter}1`);
    if (c === 1) {
      lineageRows.push([src.tab, "A", "Fluido", src.file, "A", "Identificador", "—", "—", "A, B, C, D, E, F, G, H, J, K, M; mesma ordem nas quatro projeções", "Chave de alinhamento; não é medida experimental.", ""]);
      continue;
    }
    const isPending = String(header).startsWith("RESUMO PENDENTE");
    if (isPending) {
      pendingCount++;
      target.getRange(`${letter}1`).format.fill = "#9A6400";
      target.getRange(`${letter}2:${letter}12`).format.fill = "#FFF5DE";
      for (let r = 1; r <= 11; r++) if (sourceMatrix[r][c - 1] != null) throw new Error(`Resumo preenchido inesperadamente: ${src.file} ${letter}${r + 1}`);
      lineageRows.push([src.tab, letter, header, src.file, letter, "Resumo pendente", "—", "—", "—", "Intencionalmente vazio; regra de síntese ainda não definida.", "creme: resumo pendente"]);
      continue;
    }
    originalCount++;
    const key = plainHeader(header);
    const dict = dictionary.get(key);
    if (!dict) throw new Error(`Campo não encontrado no Dicionário: ${src.file} ${letter} ${key}`);
    if (String(header).includes("[POSSÍVEL DUPLICATA]")) target.getRange(`${letter}1`).format.fill = "#B78019";
    const rows = fluids.map((fluid) => {
      const rec = trace.get(`${fluid}\u0000${key}`);
      if (!rec) throw new Error(`Origem ausente: ${src.file} ${key} ${fluid}`);
      if (rec[2] !== dict[3]) throw new Error(`Aba de origem divergente: ${src.file} ${key} ${fluid}`);
      return rec;
    });
    const rawSheet = rows[0][2];
    const cells = rows.map((row) => physicalSourceCell(row[2], row[3]));
    const rawCols = [...new Set(cells.map((addr) => /^[A-Z]+/.exec(addr)[0]))].join(", ");
    const cellsByFluid = fluids.map((fluid, i) => `${fluid}=${cells[i]}`).join("; ");
    const marked = Object.entries(specialMarks[src.file]).flatMap(([kind, addresses]) => addresses.filter((address) => new RegExp(`^${letter}\\d+$`).test(address)).map((address) => `${kind}: ${address}`));
    const notes = [];
    if (rawSheet === "COMPARATIVO") notes.push("Endereço físico = registro de rastreabilidade + 6 linhas; extração upstream ainda requer correção.");
    if (String(header).includes("[POSSÍVEL DUPLICATA]")) notes.push("Possível duplicata; não excluída.");
    if (src.file === "economico_v1.xlsx" && ["I", "N", "AA"].includes(letter)) notes.push("J/K: valores reconstruídos deterministicamente na projeção; a célula bruta correspondente está vazia ou contém fórmula com erro. Custo total anual não foi reconstruído.");
    if (src.file === "propriedades_estabilidade_fluido_v1.xlsx" && ["C", "R"].includes(letter)) notes.push("Fluido B: 7.3 está armazenado como texto na fonte bruta e como número na projeção; sem alteração do valor.");
    if (marked.some((m) => m.startsWith("orange"))) notes.push("Há valores não reconciliados; ver auditoria Pacheco.");
    if (marked.some((m) => m.startsWith("green"))) notes.push("Zero original suspeito mantido.");
    if (marked.some((m) => m.startsWith("pink"))) notes.push("NA não resolvido.");
    const markedText = marked.map((m) => m.replace("orange", "laranja").replace("blue", "azul-claro").replace("green", "verde").replace("pink", "rosa")).join("; ");
    const typeLabel = marked.some((m) => m.startsWith("blue")) ? "Original + reconstrução J/K" : "Original";
    lineageRows.push([src.tab, letter, header, src.file, letter, typeLabel, rawSheet, rawCols, cellsByFluid, notes.join(" ") || "Cópia dos valores em Dados da projeção, sob revisão.", markedText]);
  }
  for (const [kind, addresses] of Object.entries(specialMarks[src.file])) {
    for (const address of addresses) target.getRange(address).format.fill = markColors[kind];
  }
  groups.push({ tab: src.tab, columns: ncol, originalCount, pendingCount });
}

const editLineageOnly = process.argv.includes("--edit-lineage-only");
const finalWb = editLineageOnly ? await SpreadsheetFile.importXlsx(await FileBlob.load(output)) : unified;
const lineage = editLineageOnly ? finalWb.worksheets.getItem("Origem das colunas") : finalWb.worksheets.add("Origem das colunas");
const rawWorkbook = "data/raw/ensaio_bancada_alunos (2).xlsx";
const orderedRows = lineageRows.map(([tab, col, characteristic, dividedFile, dividedCol, type, rawSheet, rawCols, cells, note, marks]) => [
  tab,
  col,
  characteristic,
  rawSheet === "—" ? "—" : rawWorkbook,
  rawSheet,
  rawCols,
  rawSheet === "—" ? cells : `${rawSheet}! ${cells}`,
  dividedFile,
  dividedCol,
  type,
  note,
  marks,
]);
const head = ["Aba unificada", "Coluna", "Característica", "Planilha original em data/raw", "Aba original", "Coluna(s) original(is)", "Células originais por fluido", "Arquivo dividido", "Coluna no dividido", "Tipo", "Observação de auditoria", "Marcações na aba"];
lineage.getRange("A1:L1").values = [head];
lineage.getRange(`A2:L${orderedRows.length + 1}`).values = orderedRows;
lineage.getRange(`A1:L${orderedRows.length + 1}`).format.font = { name: "Arial", size: 10, color: "#17212D" };
lineage.getRange("A1:L1").format.fill = "#23517C";
lineage.getRange("A1:L1").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
lineage.getRange("A1:L1").format.rowHeight = 34;
lineage.getRange("A1:L1").format.wrapText = true;
lineage.getRange("A:A").format.columnWidth = 28;
lineage.getRange("B:B").format.columnWidth = 10;
lineage.getRange("C:C").format.columnWidth = 68;
lineage.getRange("D:D").format.columnWidth = 48;
lineage.getRange("E:E").format.columnWidth = 30;
lineage.getRange("F:F").format.columnWidth = 35;
lineage.getRange("G:G").format.columnWidth = 110;
lineage.getRange("H:H").format.columnWidth = 40;
lineage.getRange("I:I").format.columnWidth = 19;
lineage.getRange("J:J").format.columnWidth = 28;
lineage.getRange("K:K").format.columnWidth = 100;
lineage.getRange("L:L").format.columnWidth = 55;
lineage.getRange(`A2:L${orderedRows.length + 1}`).format.rowHeight = 46;
lineage.getRange(`C2:C${orderedRows.length + 1}`).format.wrapText = true;
lineage.getRange(`G2:G${orderedRows.length + 1}`).format.wrapText = true;
lineage.getRange(`K2:L${orderedRows.length + 1}`).format.wrapText = true;
lineage.freezePanes.freezeRows(1);
lineage.showGridLines = false;

finalWb.recalculate();
console.log(`Grupos: ${JSON.stringify(groups)}`);
console.log(`Linhas de origem: ${orderedRows.length}`);
const check = await finalWb.inspect({ kind: "table", range: "'Origem das colunas'!D1:G5", include: "values", tableMaxRows: 5, tableMaxCols: 4, maxChars: 2500 });
console.log(check.ndjson);
if (editLineageOnly) {
  await render(finalWb, "Origem das colunas", "D1:G6", "origem_depois_ajuste");
} else {
  await render(finalWb, "Desempenho usinagem", "A1:F4", "saida_1");
  await render(finalWb, "Qualidade peça processo", "A1:F4", "saida_2");
  await render(finalWb, "Propriedades fluido", "A1:F4", "saida_3");
  await render(finalWb, "Econômico", "A1:F4", "saida_4");
  await render(finalWb, "Origem das colunas", "D1:G6", "saida_origem");
}
await (await SpreadsheetFile.exportXlsx(finalWb)).save(output);
console.log(`Arquivo criado: ${output}`);
