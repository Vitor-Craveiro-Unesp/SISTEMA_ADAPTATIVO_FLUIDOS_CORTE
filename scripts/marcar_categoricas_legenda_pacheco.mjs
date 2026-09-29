import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

// Edição apenas de apresentação/auditoria: não converte nem altera dados.
const base = path.join(process.cwd(), "data", "processed", "divisao");
const input = path.join(base, "caracteristicas_unificadas_v1.xlsx");
const output = path.join(base, "caracteristicas_unificadas_v1.legenda.tmp.xlsx");
const colors = {
  header: "#23517C",
  duplicate: "#B78019",
  pendingHeader: "#9A6400",
  pendingBody: "#FFF5DE",
  anomaly: "#FFC000",
  missing: "#FFB6C1",
  zero: "#00B050",
  reconstructed: "#A9DCEB",
  categorical: "#DCC8F2",
};

const categorical = [
  { tab: "Qualidade peça processo", columns: ["J", "K", "L", "M", "N"] },
  { tab: "Propriedades fluido", columns: ["B", "D", "E", "G", "H", "J", "M", "T", "U", "V", "X", "Z", "AA", "AC", "AD", "AE"] },
  { tab: "Econômico", columns: ["R", "V"] },
];
const notes = {
  "Qualidade peça processo!J": "Binária; confirmar direção e regra antes de codificar.",
  "Qualidade peça processo!K": "Constante ('ruptura'); codificação não cria informação discriminante.",
  "Qualidade peça processo!L": "Constante ('ruptura'); codificação não cria informação discriminante.",
  "Qualidade peça processo!M": "Constante ('ruptura'); codificação não cria informação discriminante.",
  "Qualidade peça processo!N": "Constante ('ruptura'); codificação não cria informação discriminante.",
  "Propriedades fluido!B": "Constante ('não'); confirmar papel como diagnóstico.",
  "Propriedades fluido!D": "Constante ('OK'); escala técnica não definida.",
  "Propriedades fluido!E": "Binária; confirmar direção e regra antes de codificar.",
  "Propriedades fluido!G": "Nominal/multicomponente; não impor distância numérica arbitrária.",
  "Propriedades fluido!H": "Binária; confirmar direção e regra antes de codificar.",
  "Propriedades fluido!J": "Possível ordem técnica; validar escala e sentido com Pacheco/Benjamin.",
  "Propriedades fluido!M": "Constante ('GRAU 0'); confirmar escala original.",
  "Propriedades fluido!T": "Texto qualitativo sob unidade UFC/mL; não inferir contagem zero.",
  "Propriedades fluido!U": "Texto qualitativo sob unidade UFC/mL; *fungos em U4/U6 mantém alerta de origem.",
  "Propriedades fluido!V": "Texto qualitativo sob unidade UFC/mL; não inferir contagem zero.",
  "Propriedades fluido!X": "Binária; uniformizar maiúsculas antes de eventual codificação.",
  "Propriedades fluido!Z": "Constante ('não'); unidade do cabeçalho pede investigação.",
  "Propriedades fluido!AA": "Revisar semântica de 'não' versus 'estavel' antes de codificar.",
  "Propriedades fluido!AC": "Binária; uniformizar maiúsculas e acentos antes de codificar.",
  "Propriedades fluido!AD": "Binária; confirmar direção e regra antes de codificar.",
  "Propriedades fluido!AE": "Qualitativa; definir se há ordem técnica e direção antes de codificar.",
  "Econômico!R": "Constante ('Broca'); contexto da operação, não critério por si só.",
  "Econômico!V": "Identificador do produto, espelha o fluido; não converter em critério numérico.",
};

function categoryValues(sheet, column) {
  const values = sheet.getRange(`${column}2:${column}12`).values.map((row) => row[0]);
  if (values.some((value) => typeof value !== "string" || !value.trim())) {
    throw new Error(`Coluna categórica mudou ou contém vazio: ${sheet.name}!${column}2:${column}12`);
  }
  return [...new Set(values)].sort((a, b) => a.localeCompare(b, "pt-BR"));
}

async function render(wb, sheetName, range, suffix) {
  const blob = await wb.render({ sheetName, range, scale: 1.1, format: "png" });
  const file = path.join(os.tmpdir(), `pacheco_${suffix}.png`);
  await fs.writeFile(file, new Uint8Array(await blob.arrayBuffer()));
  console.log(`Prévia: ${file}`);
}

const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
if (process.argv.includes("--preview-before")) {
  await render(wb, "Qualidade peça processo", "I1:O5", "categoricas_antes_qualidade");
  await render(wb, "Propriedades fluido", "T1:V7", "categoricas_antes_fluido");
  process.exit(0);
}
if (wb.worksheets.items.some((sheet) => sheet.name === "Legenda das cores")) {
  throw new Error("A aba 'Legenda das cores' já existe; não duplicar nem sobrescrever.");
}

const catalog = [];
let painted = 0;
for (const group of categorical) {
  const sheet = wb.worksheets.getItem(group.tab);
  for (const column of group.columns) {
    const categories = categoryValues(sheet, column);
    const heading = sheet.getRange(`${column}1`).values[0][0];
    sheet.getRange(`${column}2:${column}12`).format.fill = colors.categorical;
    painted += 11;
    catalog.push([group.tab, column, heading, categories.join(" · "), notes[`${group.tab}!${column}`]]);
  }
}
// As duas anotações '*fungos' eram laranja: preservar o alerta em borda.
for (const address of ["U4", "U6"]) {
  wb.worksheets.getItem("Propriedades fluido").getRange(address).format.borders = {
    preset: "outside", style: "medium", color: colors.anomaly,
  };
}

const legend = wb.worksheets.add("Legenda das cores");
legend.showGridLines = false;
legend.tabColor = colors.categorical;
legend.getRange("A1:E1").merge();
legend.getRange("A1").values = [["Legenda das cores e variáveis categóricas"]];
legend.getRange("A1:E1").format = {
  fill: colors.header,
  font: { name: "Arial", size: 16, bold: true, color: "#FFFFFF" },
};
legend.getRange("A1:E1").format.rowHeight = 36;
legend.getRange("A2:E2").merge();
legend.getRange("A2").values = [["Base candidata / sob revisão. Cores são alertas visuais; não significam validação, aprovação ou conversão já realizada."]];
legend.getRange("A2:E2").format.font = { name: "Arial", size: 11, color: "#17212D" };
legend.getRange("A2:E2").format.rowHeight = 30;
legend.getRange("A2:E2").format.wrapText = true;
legend.getRange("A4:E4").values = [["Amostra", "Cor (hex)", "Onde aparece", "Significado", "O que fazer"]];
legend.getRange("A4:E4").format = {
  fill: colors.header,
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
};

const rows = [
  [null, "Sem preenchimento", "Dados sem alerta de cor", "Célula sem marcação especial; isso não prova que esteja validada.", "Conferir origem, tipo e unidade normalmente."],
  [colors.header, colors.header, "Cabeçalhos", "Identificação da coluna ou seção.", "Não interpretar como resultado analítico."],
  [colors.duplicate, colors.duplicate, "Cabeçalhos de variáveis", "Possível duplicata, ainda não confirmada.", "Comparar origem, definição e valores antes de excluir qualquer campo."],
  [colors.pendingHeader, colors.pendingHeader, "Cabeçalhos RESUMO PENDENTE", "Síntese ainda sem regra aprovada.", "Definir método antes de calcular; manter células vazias por enquanto."],
  [colors.pendingBody, colors.pendingBody, "Corpo de RESUMO PENDENTE", "Vazio intencional, diferente de NA observado na fonte.", "Não imputar nem tratar como ausência experimental."],
  [colors.anomaly, colors.anomaly, "Corpo dos dados", "Divergência, texto em campo numérico ou anotação de origem a investigar.", "Investigar a fonte; preservar valor original e decisão rastreável."],
  [colors.missing, colors.missing, "Corpo dos dados", "NA explícito ainda sem resolução.", "Não transformar NA em zero; investigar mecanismo da ausência."],
  [colors.zero, colors.zero, "Corpo dos dados", "Zero registrado, porém suspeito.", "Verificar fórmula/semântica antes de usar em análise."],
  [colors.reconstructed, colors.reconstructed, "Corpo dos dados", "Valor reconstruído deterministicamente por regra auditada.", "Confirmar rastreabilidade e regra antes de promover a base."],
  [colors.categorical, colors.categorical, "Corpo de variáveis textuais", "Valor categórico; ainda não está numericamente codificado.", "Se selecionado para análise numérica, definir tipo, sentido e codificação; preservar texto original."],
  [colors.categorical, "Lilás + borda laranja", "Propriedades fluido!U4 e U6", "Categoria textual com alerta de origem simultâneo (*fungos).", "Investigar a anotação; a borda mantém a pendência mesmo com fundo lilás."],
];
legend.getRange("A5:E15").values = rows.map((r) => ["", ...r.slice(1)]);
for (let i = 0; i < rows.length; i++) {
  const [fill] = rows[i];
  if (fill) legend.getRange(`A${i + 5}`).format.fill = fill;
}
legend.getRange("A15").format.borders = { preset: "outside", style: "medium", color: colors.anomaly };
legend.getRange("A5:E15").format.font = { name: "Arial", size: 10, color: "#17212D" };
legend.getRange("A6").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
legend.getRange("A5:E15").format.wrapText = true;
legend.getRange("A5:E15").format.rowHeight = 48;

legend.getRange("A17:E17").merge();
legend.getRange("A17").values = [[`Inventário: ${catalog.length} colunas textuais; ${painted} células lilás (incluindo U4 e U6)`]];
legend.getRange("A17:E17").format = {
  fill: colors.header,
  font: { name: "Arial", size: 12, bold: true, color: "#FFFFFF" },
};
legend.getRange("A18:E18").values = [["Aba", "Coluna", "Variável", "Categorias observadas", "Cuidado antes de usar numericamente"]];
legend.getRange("A18:E18").format = {
  fill: colors.header,
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
};
const last = 18 + catalog.length;
legend.getRange(`A19:E${last}`).values = catalog;
legend.getRange(`A19:E${last}`).format.font = { name: "Arial", size: 10, color: "#17212D" };
legend.getRange(`A19:E${last}`).format.wrapText = true;
legend.getRange(`A19:E${last}`).format.rowHeight = 44;
legend.getRange(`B19:B${last}`).format.fill = colors.categorical;

legend.getRange("A:A").format.columnWidth = 26;
legend.getRange("B:B").format.columnWidth = 22;
legend.getRange("C:C").format.columnWidth = 56;
legend.getRange("D:D").format.columnWidth = 72;
legend.getRange("E:E").format.columnWidth = 76;
legend.freezePanes.freezeRows(4);

const warningRow = last + 2;
legend.getRange(`A${warningRow}:E${warningRow}`).merge();
legend.getRange(`A${warningRow}`).values = [["Fluido (coluna A) é identificador, não critério; campos 'repetir', '1 kg' e 'NA' em medidas numéricas não foram coloridos como categorias. Resumos vazios continuam creme. Benjamin só deve codificar após definição metodológica."]];
legend.getRange(`A${warningRow}:E${warningRow}`).format.wrapText = true;
legend.getRange(`A${warningRow}:E${warningRow}`).format.rowHeight = 45;
legend.getRange(`A${warningRow}:E${warningRow}`).format.font = { name: "Arial", size: 10, color: "#17212D" };

wb.recalculate();
await render(wb, "Legenda das cores", "A1:E10", "legenda_apos");
await render(wb, "Propriedades fluido", "T1:V7", "categoricas_apos_fluido");
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(output);
console.log(`Gerado para validação: ${output}`);
