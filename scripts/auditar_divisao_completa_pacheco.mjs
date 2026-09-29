import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const dir = path.join(root, "data", "processed", "divisao");
const previewOnly = process.argv.includes("--preview-only");
const repairHeader = process.argv.includes("--repair-header");
const font = "Arial";
const specs = [
  {
    key: "usinagem", file: "desempenho_usinagem_v1.xlsx", preview: "F2:R5",
    amber: ["H3", "Q3", "I3", "R3", "H4", "Q4", "I4", "R4", "H5", "Q5", "G10", "P10"],
    firstRow: 16,
    notes: [
      ["Auditoria Pacheco", "SOB REVISÃO — nenhum dado numérico foi substituído."],
      ["LARANJA", "Par de valores de vida da ferramenta divergente entre COMPARATIVO e ANÁLISE USINABILIDADE (12 células, seis pares)."],
      ["Potência", "44 de 44 pares das duas fontes coincidem; possíveis duplicatas, ainda não excluídas."],
      ["Vida da ferramenta", "Seis pares divergentes: B condições 3/4; C condições 3/4; D condição 3; J condição 2. Não reconciliar automaticamente."],
      ["Somatórios", "Os 11 somatórios do COMPARATIVO batem com as quatro condições da própria aba; isso não resolve o conflito com USINABILIDADE."],
      ["Rastreabilidade", "99 endereços COMPARATIVO estão seis linhas acima do XLSX bruto. Consultar o relatório antes de usar a coluna Célula de origem."],
      ["NA e reconstruções", "0 NA explícitos; 0 valores reconstruídos nesta planilha."],
      ["Resumos", "22 células de resumo (11 fluidos × 2 campos) continuam intencionalmente em branco."],
    ],
  },
  {
    key: "qualidade", file: "qualidade_peca_processo_v1.xlsx", preview: "J1:R4",
    amber: [], firstRow: 16,
    notes: [
      ["Auditoria Pacheco", "SOB REVISÃO — nenhum valor foi alterado em Dados."],
      ["NA e zeros", "0 NA explícitos; 0 zeros nos 17 campos originais."],
      ["Forma do cavaco", "As 44 observações são a categoria textual ruptura. Não calcular média numérica; não há variação observada nesta amostra."],
      ["Rebarba", "Campo categórico sim/não. Uma eventual codificação exige regra explícita, não foi feita aqui."],
      ["Rastreabilidade", "99 endereços COMPARATIVO estão seis linhas acima do XLSX bruto. Consultar o relatório antes de usar a coluna Célula de origem."],
      ["Resumos", "55 células de resumo (11 fluidos × 5 campos) continuam intencionalmente em branco."],
    ],
  },
  {
    key: "propriedades", file: "propriedades_estabilidade_fluido_v1.xlsx", preview: "L3:V6",
    amber: ["O5", "O6", "O7", "O9", "L3", "C10", "S10", "C11", "S11", "V4", "V6"],
    firstRow: 16,
    notes: [
      ["Auditoria Pacheco", "SOB REVISÃO — os valores originais foram preservados."],
      ["LARANJA", "11 células para revisão: quatro repetir, um 1 kg, quatro concentrações conflitantes e duas grafias *fungos."],
      ["Acidez", "D, E, F e H contêm repetir. A medição numérica está indisponível; não substituir por número."],
      ["Sólidos suspensos", "B contém 1 kg em coluna mista. Unidade e significado requerem conferência; não converter automaticamente."],
      ["Concentração", "J: 9,0% vs 8,5%; K: 9,5% vs 9,0% (COMPARATIVO vs EMULSÕES). Ambas as origens ficam preservadas."],
      ["*fungos", "C e E têm *fungos em CONTAGEM FINAL ENSAIO; o asterisco pode indicar ressalva não definida. Preservar o texto."],
      ["Zeros", "CORROSÃO NO FOFO tem 0 nos 11 fluidos. Há valor na fonte; sem evidência de NA escondido, não marcar como verde."],
      ["Rastreabilidade", "143 endereços COMPARATIVO estão seis linhas acima do XLSX bruto. Consultar o relatório antes de usar a coluna Célula de origem."],
      ["NA e resumos", "0 NA literais; quatro medições de acidez pendentes como texto; 363 células de resumo seguem vazias."],
    ],
  },
  {
    key: "economico", file: "economico_v1.xlsx", preview: "A9:Q11",
    amber: [], firstRow: 24,
    notes: [
      ["Auditoria ampliada", "SOB REVISÃO — marcações anteriores preservadas."],
      ["Fórmulas na fonte", "A aba econômica bruta tem 143 fórmulas. Seis resultados de J/K têm cache #DIV/0!; não são zeros nem células vazias."],
      ["15 ausências iniciais", "Nove células brutas vazias e seis resultados de fórmula com erro foram mapeados a NA na matriz candidata."],
      ["Custo anual total", "J/K continuam NA. O cálculo exige entradas ainda ausentes; não inferir a partir do subtotal operação/ferramenta."],
      ["Rastreabilidade", "Endereços econômicos conferidos no XLSX bruto; seis células de erro #DIV/0! aparecem como NA no campo Valor bruto da matriz."],
      ["Zeros suspeitos", "Apenas os nove zeros verdes de J/K têm dependências ausentes identificadas. Outros zeros foram preservados sem reclassificação."],
      ["Resumos", "286 células de resumo (11 fluidos × 26 campos) continuam intencionalmente em branco."],
    ],
  },
];

async function renderPreview(wb, spec, suffix) {
  for (const [sheetName, range, label] of [
    ["Dados", spec.preview, "dados"],
    ["Leia-me", `${spec.firstRow === 24 ? "A16:B30" : "A12:B26"}`, "leia_me"],
  ]) {
    const image = await wb.render({ sheetName, range, scale: 1.15, format: "png" });
    const target = path.join(os.tmpdir(), `auditoria_divisao_${spec.key}_${label}_${suffix}.png`);
    await fs.writeFile(target, new Uint8Array(await image.arrayBuffer()));
    console.log(`${spec.key} ${sheetName}: ${target}`);
  }
}

for (const spec of specs) {
  if (repairHeader && spec.key !== "economico") continue;
  const target = path.join(dir, spec.file);
  const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(target));
  if (previewOnly) {
    await renderPreview(wb, spec, "antes");
    continue;
  }
  const data = wb.worksheets.getItem("Dados");
  const readme = wb.worksheets.getItem("Leia-me");
  if (repairHeader) {
    readme.getRange("B24").values = [[spec.notes[0][1]]];
    wb.recalculate();
    await renderPreview(wb, spec, "reparo");
    const repaired = await SpreadsheetFile.exportXlsx(wb);
    await repaired.save(target);
    console.log(`Cabeçalho reparado ${target}`);
    continue;
  }
  const lastRow = spec.firstRow + spec.notes.length - 1;
  if (readme.getRange(`A${spec.firstRow}:B${lastRow}`).values.some((row) => row.some((v) => v !== null && v !== ""))) {
    throw new Error(`${spec.file}: área de auditoria já ocupada`);
  }
  for (const address of spec.amber) {
    const cell = data.getRange(address);
    if (cell.values[0][0] === null || cell.values[0][0] === "") throw new Error(`${spec.file}: ${address} está vazia`);
    cell.format.fill = "#FFC000";
    cell.format.font = { name: font, size: 10, bold: true, color: "#493600" };
  }
  readme.getRange(`A${spec.firstRow}:B${lastRow}`).values = spec.notes;
  readme.getRange(`A${spec.firstRow}:B${lastRow}`).format.font = { name: font, size: 10, color: "#17212D" };
  readme.getRange(`A${spec.firstRow}:B${spec.firstRow}`).format.fill = "#23517C";
  readme.getRange(`A${spec.firstRow}:B${spec.firstRow}`).format.font = { name: font, size: 10, bold: true, color: "#FFFFFF" };
  if (spec.amber.length > 0) {
    const legend = readme.getRange(`A${spec.firstRow + 1}`);
    legend.format.fill = "#FFC000";
    legend.format.font = { name: font, size: 10, bold: true, color: "#493600" };
  }
  readme.getRange(`B${spec.firstRow + 1}:B${lastRow}`).format.wrapText = true;
  readme.getRange(`A${spec.firstRow + 1}:B${lastRow}`).format.rowHeight = 45;
  wb.recalculate();
  const check = await wb.inspect({ kind: "table", range: `Leia-me!A${spec.firstRow}:B${lastRow}`, include: "values,formulas", tableMaxRows: spec.notes.length, tableMaxCols: 2, maxChars: 6000 });
  console.log(check.ndjson);
  const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, maxChars: 1500 });
  console.log(`${spec.file} errors: ${errors.ndjson}`);
  await renderPreview(wb, spec, "depois");
  const output = await SpreadsheetFile.exportXlsx(wb);
  await output.save(target);
  console.log(`Editado ${target}`);
}
