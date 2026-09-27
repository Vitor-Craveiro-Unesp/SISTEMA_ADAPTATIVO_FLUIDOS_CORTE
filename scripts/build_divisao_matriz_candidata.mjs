import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

// Visões da matriz candidata v1. Os nomes de resumo vêm do PDF enviado pelo usuário.
// Nenhum resumo é calculado: critérios e regras de agregação ainda dependem de revisão.
const projectRoot = process.cwd();
const processedDir = path.join(projectRoot, "data", "processed");
const outputDir = path.join(processedDir, "divisao");
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
  const [headers, ...data] = rows;
  return {
    headers,
    rows: data.map((cells) => Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]))),
  };
}

async function readCsv(fileName) {
  return parseCsv(await fs.readFile(path.join(processedDir, fileName), "utf8"));
}

function restoreUnicode(value) {
  return String(value ?? "").replace(/<U\+([0-9A-Fa-f]{4,6})>/g, (_, hex) => String.fromCodePoint(parseInt(hex, 16)));
}

function cellValue(value) {
  if (value === "NA") return "NA";
  const decoded = restoreUnicode(value);
  if (/^-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(decoded)) return Number(decoded);
  return decoded;
}

function columnName(index) {
  let number = index + 1;
  let result = "";
  while (number > 0) {
    const digit = (number - 1) % 26;
    result = String.fromCharCode(65 + digit) + result;
    number = Math.floor((number - 1) / 26);
  }
  return result;
}

function belongsToGroup(meta) {
  if (meta.data_domain === "economico") return "economico";
  if (meta.data_domain === "emulsao") return "propriedades";
  if (meta.data_domain === "usinabilidade") {
    return ["potencia_corte", "vida_ferramenta_volume_removido"].includes(meta.metric)
      ? "usinagem" : "qualidade";
  }
  if (meta.data_domain === "comparativo") {
    if (["potencia", "vida_ferramenta_volume_removido"].includes(meta.metric)) return "usinagem";
    if (["circularidade", "concentricidade", "presenca_rebarba"].includes(meta.metric)) return "qualidade";
    return "propriedades";
  }
  throw new Error(`Domínio não previsto: ${meta.data_domain}`);
}

const specs = [
  {
    id: "usinagem", fileName: "desempenho_usinagem_v1.xlsx", title: "Desempenho de usinagem",
    originalCount: 17,
    summaries: ["media_da_potencia", "media_da_vida_da_ferramenta"],
    caveat: "Potência e vida da ferramenta aparecem em duas abas; o somatório e as divergências de B, D e J exigem reconciliação antes de resumir.",
  },
  {
    id: "qualidade", fileName: "qualidade_peca_processo_v1.xlsx", title: "Qualidade da peça/processo",
    originalCount: 17,
    summaries: ["media_da_circularidade", "media_da_concentricidade", "presenca_de_rebarba", "media_da_forma_do_cavaco", "media_da_rugosidade_superficial"],
    caveat: "Forma do cavaco e presença de rebarba são campos categóricos; qualquer resumo numérico requer regra metodológica explícita.",
  },
  {
    id: "propriedades", fileName: "propriedades_estabilidade_fluido_v1.xlsx", title: "Propriedades/estabilidade do fluido",
    originalCount: 34,
    summaries: [
      "bacterias", "media_da_concentracao_media", "espuma", "fungos", "indice_refracao",
      "item_restritivo_composicao", "nevoa", "oxidacao_maquina", "ph_5_porcento",
      "resistencia_degradacao", "solidos_suspensos", "tensao_superficial", "teste_corrosao",
      "acidez", "alcalinidade", "amônia", "cloretos", "concentração média", "condutividade",
      "contagem antes mistura", "contagem final ensaio", "contagem início ensaio",
      "corrosão no fofo", "degradação", "dureza total", "estabilidade", "fósforo",
      "manchamento no fofo", "névoa", "odor na operação", "sólidos totais", "turbidez", "ph",
    ],
    caveat: "A concentração média diverge entre abas para J e K. Quatro valores de acidez estão registrados como 'repetir'. Os nomes nevoa/névoa representam campos de abas distintas.",
  },
  {
    id: "economico", fileName: "economico_v1.xlsx", title: "Econômico",
    originalCount: 26,
    summaries: null, // O PDF mantém as 26 variáveis, mas solicita a área de resumo vazia.
    caveat: "Há 15 ausências na fonte, concentradas em J e K. A concentração econômica aparece como fração (ex.: 0,079 para A), enquanto a emulsão registra 7,9%; a convenção da unidade requer revisão. Valores derivados não possuem fórmulas OOXML no XLSX bruto.",
  },
];

const candidate = await readCsv("matriz_candidata_completa_v1.csv");
const metadata = await readCsv("matriz_candidata_completa_metadados_v1.csv");
const trace = await readCsv("matriz_candidata_completa_flags_v1.csv");
if (candidate.rows.length !== 11 || metadata.rows.length !== 94 || trace.rows.length !== 1034) {
  throw new Error("Dimensões da base candidata v1 divergem do inventário revisado.");
}
const grouped = Object.fromEntries(specs.map((spec) => [spec.id, []]));
for (const meta of metadata.rows) grouped[belongsToGroup(meta)].push(meta);
for (const spec of specs) {
  if (grouped[spec.id].length !== spec.originalCount) {
    throw new Error(`${spec.title}: esperado ${spec.originalCount}, obtido ${grouped[spec.id].length}.`);
  }
}
if (specs.reduce((sum, spec) => sum + grouped[spec.id].length, 0) !== 94) {
  throw new Error("Alguma variável foi omitida ou atribuída a mais de um grupo.");
}
const existing = await Promise.all(specs.map(async (spec) => {
  try { await fs.access(path.join(outputDir, spec.fileName)); return spec.fileName; }
  catch { return null; }
}));
if (existing.some(Boolean) && !process.argv.includes("--replace-generated")) {
  throw new Error(`Arquivos existentes não serão sobrescritos sem --replace-generated: ${existing.filter(Boolean).join(", ")}`);
}
await fs.mkdir(outputDir, { recursive: true });

for (const spec of specs) {
  const sourceFields = grouped[spec.id];
  const summaryNames = spec.summaries ?? sourceFields.map((meta) => restoreUnicode(meta.metric).trim().replace(/\s+/g, " ").toLowerCase());
  if (summaryNames.length !== ({ usinagem: 2, qualidade: 5, propriedades: 33, economico: 26 })[spec.id]) {
    throw new Error(`Contagem de resumos incorreta para ${spec.id}.`);
  }
  const workbook = Workbook.create();
  const data = workbook.worksheets.add("Dados");
  data.showGridLines = false;
  data.tabColor = "#23517C";
  const dataHeaders = [
    "Fluido",
    ...sourceFields.map((meta) => `${restoreUnicode(meta.display_label)}${meta.possible_duplicate === "TRUE" ? " [POSSÍVEL DUPLICATA]" : ""}`),
    ...summaryNames.map((name) => `RESUMO PENDENTE | ${name}`),
  ];
  if (new Set(dataHeaders).size !== dataHeaders.length) throw new Error(`Cabeçalhos repetidos em ${spec.title}.`);
  const dataRows = candidate.rows.map((row) => [
    row.fluid_id,
    ...sourceFields.map((meta) => cellValue(row[meta.wide_column_name])),
    ...summaryNames.map(() => null),
  ]);
  data.getRangeByIndexes(0, 0, dataRows.length + 1, dataHeaders.length).values = [dataHeaders, ...dataRows];
  const lastDataCol = columnName(dataHeaders.length - 1);
  const lastOriginalCol = columnName(sourceFields.length);
  const firstSummaryCol = columnName(sourceFields.length + 1);
  data.getRange(`A1:${lastDataCol}${dataRows.length + 1}`).format.font = { name: font, size: 10, color: "#17212D" };
  data.getRange(`A1:${lastOriginalCol}1`).format = {
    fill: "#23517C", font: { name: font, size: 10, bold: true, color: "#FFFFFF" },
    wrapText: true, horizontalAlignment: "center", verticalAlignment: "center",
  };
  data.getRange(`${firstSummaryCol}1:${lastDataCol}1`).format = {
    fill: "#9A6400", font: { name: font, size: 10, bold: true, color: "#FFFFFF" },
    wrapText: true, horizontalAlignment: "center", verticalAlignment: "center",
  };
  data.getRange(`A1:${lastDataCol}1`).format.rowHeight = 100;
  data.getRange("A:A").format.columnWidth = 12;
  data.getRange(`B:${lastDataCol}`).format.columnWidth = 24;
  data.getRange(`${firstSummaryCol}2:${lastDataCol}${dataRows.length + 1}`).format.fill = "#FFF5DE";
  data.getRange(`B2:${lastOriginalCol}${dataRows.length + 1}`).format.numberFormat = "0.00########";
  data.getRange(`B2:${lastOriginalCol}${dataRows.length + 1}`).format.wrapText = true;
  data.getRange(`A2:${lastDataCol}${dataRows.length + 1}`).format.rowHeight = 32;
  data.freezePanes.freezeRows(1);
  data.freezePanes.freezeColumns(1);
  for (let index = 0; index < sourceFields.length; index += 1) {
    if (sourceFields[index].possible_duplicate === "TRUE") {
      data.getRange(`${columnName(index + 1)}1`).format.fill = "#B78019";
    }
  }
  let missingCount = 0;
  for (let rowIndex = 0; rowIndex < dataRows.length; rowIndex += 1) {
    for (let fieldIndex = 0; fieldIndex < sourceFields.length; fieldIndex += 1) {
      const value = dataRows[rowIndex][fieldIndex + 1];
      const address = `${columnName(fieldIndex + 1)}${rowIndex + 2}`;
      if (value === "NA") {
        missingCount += 1;
        data.getRange(address).format = { fill: "#FBE3E1", font: { name: font, size: 10, color: "#A61E1E", bold: true } };
      } else if (typeof value === "string" && value.toLowerCase() === "repetir") {
        data.getRange(address).format = { fill: "#FFF1C6", font: { name: font, size: 10, color: "#815600", bold: true } };
      }
    }
  }

  const dictionary = workbook.worksheets.add("Dicionário");
  dictionary.showGridLines = false;
  const dictHeaders = ["Coluna em Dados", "Tipo", "Domínio", "Aba de origem", "Métrica ou resumo", "Condição", "Unidade", "Possível duplicata", "Grupo de duplicidade", "NA na fonte", "Situação", "Observação"];
  const dictRows = [
    ...sourceFields.map((meta) => [
      restoreUnicode(meta.display_label), "Original", meta.data_domain, restoreUnicode(meta.source_sheet),
      restoreUnicode(meta.metric), meta.condition === "NA" ? "" : meta.condition,
      meta.unit === "NA" ? "" : restoreUnicode(meta.unit), meta.possible_duplicate === "TRUE" ? "SIM" : "NÃO",
      meta.duplicate_group === "NA" ? "" : meta.duplicate_group, Number(meta.missing_values),
      "SOB REVISÃO", meta.duplicate_note === "NA" ? "" : restoreUnicode(meta.duplicate_note),
    ]),
    ...summaryNames.map((name) => [
      `RESUMO PENDENTE | ${name}`, "Resumo", "", "PDF de agrupamento", name,
      "", "", "", "", "", "EM BRANCO", "Regra de cálculo/seleção ainda não definida; nenhuma fórmula foi aplicada.",
    ]),
  ];
  dictionary.getRangeByIndexes(0, 0, dictRows.length + 1, dictHeaders.length).values = [dictHeaders, ...dictRows];
  dictionary.getRange(`A1:L${dictRows.length + 1}`).format.font = { name: font, size: 10, color: "#17212D" };
  dictionary.getRange("A1:L1").format = {
    fill: "#23517C", font: { name: font, size: 10, bold: true, color: "#FFFFFF" },
    wrapText: true, horizontalAlignment: "center", verticalAlignment: "center",
  };
  dictionary.getRange("A1:L1").format.rowHeight = 42;
  dictionary.getRange("A:A").format.columnWidth = 64;
  dictionary.getRange("B:C").format.columnWidth = 18;
  dictionary.getRange("D:D").format.columnWidth = 28;
  dictionary.getRange("E:E").format.columnWidth = 43;
  dictionary.getRange("F:K").format.columnWidth = 22;
  dictionary.getRange("L:L").format.columnWidth = 66;
  dictionary.getRange(`A2:L${dictRows.length + 1}`).format.wrapText = true;
  dictionary.getRange(`A2:L${dictRows.length + 1}`).format.rowHeight = 32;
  dictionary.freezePanes.freezeRows(1);
  dictionary.freezePanes.freezeColumns(2);
  dictionary.getRange(`A${sourceFields.length + 2}:L${dictRows.length + 1}`).format.fill = "#FFF5DE";

  const lineage = workbook.worksheets.add("Rastreabilidade");
  lineage.showGridLines = false;
  const lineageHeaders = ["Fluido", "Coluna em Dados", "Aba de origem", "Célula de origem", "Valor bruto", "Valor ausente", "Possível duplicata", "Grupo de duplicidade", "Estado"];
  const selectedIds = new Set(sourceFields.map((meta) => meta.matrix_column_id));
  const lineageRows = trace.rows.filter((row) => selectedIds.has(row.matrix_column_id)).map((row) => {
    const meta = sourceFields.find((item) => item.matrix_column_id === row.matrix_column_id);
    return [row.fluid_id, restoreUnicode(meta.display_label), restoreUnicode(row.source_sheet), row.source_cell,
      row.is_missing === "TRUE" ? "NA" : cellValue(row.value_raw), row.is_missing === "TRUE" ? "SIM" : "NÃO",
      row.possible_duplicate === "TRUE" ? "SIM" : "NÃO", row.duplicate_group === "NA" ? "" : row.duplicate_group,
      row.matrix_readiness_status];
  });
  if (lineageRows.length !== sourceFields.length * candidate.rows.length) throw new Error(`Rastreabilidade incompleta em ${spec.title}.`);
  lineage.getRangeByIndexes(0, 0, lineageRows.length + 1, lineageHeaders.length).values = [lineageHeaders, ...lineageRows];
  lineage.getRange(`A1:I${lineageRows.length + 1}`).format.font = { name: font, size: 10, color: "#17212D" };
  lineage.getRange("A1:I1").format = {
    fill: "#23517C", font: { name: font, size: 10, bold: true, color: "#FFFFFF" },
    wrapText: true, horizontalAlignment: "center", verticalAlignment: "center",
  };
  lineage.getRange("A1:I1").format.rowHeight = 42;
  lineage.getRange("A:A").format.columnWidth = 12;
  lineage.getRange("B:B").format.columnWidth = 64;
  lineage.getRange("C:C").format.columnWidth = 28;
  lineage.getRange("D:I").format.columnWidth = 22;
  lineage.freezePanes.freezeRows(1);
  lineage.freezePanes.freezeColumns(2);

  const readme = workbook.worksheets.add("Leia-me");
  readme.showGridLines = false;
  readme.getRange("A1:B10").values = [
    ["Divisão", spec.title],
    ["Estado", "MATRIZ CANDIDATA SOB REVISÃO"],
    ["Variáveis originais", sourceFields.length],
    ["Resumos previstos", summaryNames.length],
    ["Resumos calculados", 0],
    ["NA nos dados originais", missingCount],
    ["Dados de origem", "data/processed/matriz_candidata_completa_v1.csv"],
    ["Planilha bruta", "data/raw/ensaio_bancada_alunos (2).xlsx"],
    ["Agrupamento", "tabela_resumo_variaveis_matriz_candidata.pdf, páginas 1–3, fornecido pelo usuário"],
    ["Pendência específica", spec.caveat],
  ];
  readme.getRange("A1:B10").format.font = { name: font, size: 10, color: "#17212D" };
  readme.getRange("A:A").format.columnWidth = 28;
  readme.getRange("B:B").format.columnWidth = 90;
  readme.getRange("A1:A10").format.font = { name: font, size: 10, bold: true, color: "#23517C" };
  readme.getRange("B10").format.wrapText = true;
  readme.getRange("A12").values = [["NA indica ausência na fonte; as colunas RESUMO PENDENTE estão intencionalmente vazias."]];
  readme.getRange("A13").values = [["As marcações de duplicidade sinalizam sobreposição possível. Elas não aprovam exclusão nem definição de critério."]];
  readme.getRange("A14").values = [["Consulte Dicionário e Rastreabilidade antes de usar qualquer variável nas etapas seguintes."]];

  workbook.recalculate();
  const check = await workbook.inspect({kind: "table", range: "Leia-me!A1:B10", include: "values,formulas", tableMaxRows: 10, tableMaxCols: 2});
  console.log(`${spec.fileName}: ${sourceFields.length} originais, ${summaryNames.length} resumos vazios, ${missingCount} NA`);
  console.log(check.ndjson);
  const preview = await workbook.render({sheetName: "Dados", range: `A1:${columnName(Math.min(sourceFields.length, 6))}5`, scale: 1.2, format: "png"});
  await fs.writeFile(path.join(os.tmpdir(), `divisao_${spec.id}_preview.png`), new Uint8Array(await preview.arrayBuffer()));
  const previewRanges = [
    ["Dados", `${columnName(Math.max(0, sourceFields.length - 1))}1:${columnName(Math.min(dataHeaders.length - 1, sourceFields.length + 3))}5`, "resumos"],
    ["Dicionário", "A1:F6", "dicionario"],
    ["Rastreabilidade", "A1:F6", "rastreabilidade"],
    ["Leia-me", "A1:B10", "leia_me"],
  ];
  for (const [sheetName, range, label] of previewRanges) {
    const image = await workbook.render({sheetName, range, scale: 1.2, format: "png"});
    await fs.writeFile(path.join(os.tmpdir(), `divisao_${spec.id}_${label}.png`), new Uint8Array(await image.arrayBuffer()));
  }
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(path.join(outputDir, spec.fileName));
}
