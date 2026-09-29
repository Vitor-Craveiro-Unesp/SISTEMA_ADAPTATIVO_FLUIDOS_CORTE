import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const source = path.join(root, "data", "raw", "ensaio_bancada_alunos (2).xlsx");
const output = path.join(root, "data", "processed", "divisao", "ensaio_bancada_alunos_copia_auditada.xlsx");
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(source));

async function render(name, sheetName, range) {
  const img = await wb.render({ sheetName, range, scale: 1.1, format: "png" });
  const target = path.join(os.tmpdir(), `pacheco_original_${name}.png`);
  await fs.writeFile(target, new Uint8Array(await img.arrayBuffer()));
  console.log(`Prévia: ${target}`);
}

if (process.argv.includes("--preview-only")) {
  await render("comparativo_antes", "COMPARATIVO", "A8:F12");
  await render("economico_antes", "AVALIAÇÃO ECONÔMICA", "AE36:AJ43");
  process.exit(0);
}

if (process.argv.includes("--roundtrip-test")) {
  const roundtrip = path.join(os.tmpdir(), "pacheco_original_roundtrip.xlsx");
  await (await SpreadsheetFile.exportXlsx(wb)).save(roundtrip);
  console.log(`Teste de exportação: ${roundtrip}`);
  process.exit(0);
}

const marked = [];
function mark(sheetName, addresses, color, label) {
  const sheet = wb.worksheets.getItem(sheetName);
  for (const address of addresses) {
    sheet.getRange(address).format.fill = color;
    marked.push([sheetName, address, label]);
  }
}

// Pares conflitantes entre duas abas: ambos os lados preservados.
mark("COMPARATIVO", ["D10", "E10", "D11", "E11", "D12", "C17"], "#FFC000", "vida divergente");
mark("ANÁLISE USINABILIDADE", ["G6", "G7", "H6", "H7", "I6", "N5"], "#FFC000", "vida divergente");
mark("COMPARATIVO", ["AE17", "AE18", "AB10"], "#FFC000", "concentração/unidade pendente");
mark("ANÁLISE EMULSÕES", ["N13", "O13", "I14", "J14", "K14", "M14", "H24", "J24"], "#FFC000", "concentração/repetir/*fungos pendente");

// O zero continua zero; a ausência continua em branco; fórmulas com erro não são substituídas.
mark("AVALIAÇÃO ECONÔMICA", ["AF23", "AF24", "AF29", "AF28", "AF27", "AF20", "AI23", "AI24", "AI20"], "#00B050", "zero suspeito");
mark("AVALIAÇÃO ECONÔMICA", ["AF15", "AF18", "AF17", "AF19", "AI15", "AI18", "AI17", "AF38", "AI38", "AF40", "AF41", "AF43", "AI40", "AI41", "AI43"], "#FFB6C1", "ausência/erro de fórmula");

const legend = wb.worksheets.add("LEGENDA AUDITORIA");
legend.getRange("A1:D1").values = [["CÓPIA AUDITADA DA FONTE ORIGINAL", "Estado: UNDER_REVIEW", "Data: 2026-09-29", "Responsável: Pacheco"]];
legend.getRange("A2:D2").values = [["A fonte em data/raw/ permanece imutável.", "As abas originais mantêm seus números e fórmulas.", "Correções determinísticas ficam em aba própria.", "Não liberar a Benjamin."]];
legend.getRange("A4:C4").values = [["COR", "SIGNIFICADO", "AÇÃO"]];
legend.getRange("A5:C9").values = [
  ["LARANJA", "Conflito entre fontes ou texto/unidade ambíguos.", "Investigar origem, protocolo e precisão; não escolher por conveniência."],
  ["VERDE", "Zero original suspeito; valor não foi trocado.", "Conferir entradas e distinguir zero real de ausência."],
  ["ROSA", "Célula vazia ou fórmula com erro ainda sem solução segura.", "Obter insumos ou manter ausência documentada."],
  ["AZUL-CLARO", "Valor reconstruído deterministicamente na aba CORREÇÕES AUDITADAS.", "Usar somente como proposta rastreável; revisar dependências."],
  ["SEM COR", "Sem marcação nesta auditoria.", "Não implica aprovação científica."],
];
for (const [row, color] of [[5, "#FFC000"], [6, "#00B050"], [7, "#FFB6C1"], [8, "#A9DCEB"]]) legend.getRange(`A${row}`).format.fill = color;
legend.getRange("A11:C11").values = [["PENDÊNCIA CRÍTICA", "341 endereços COMPARATIVO em planilhas derivadas estão 6 linhas acima da fonte física.", "Corrigir extração upstream e regenerar derivados; não alterar a fonte bruta."]];
legend.getRange("A12:C12").values = [["FONTE DE VIDA", "Seis pares de condições B/C/D/J divergem entre abas.", "A origem oficial deve ser confirmada antes da base canônica."]];
legend.getRange("A13:C13").values = [["TOTAL ECONÔMICO", "CUSTO TOTAL ANUAL de J/K não foi reconstruído.", "Faltam insumos; zeros intermediários são suspeitos."]];
legend.getRange("A1:D1").format.fill = "#23517C";
legend.getRange("A1:D1").format.font = { name: "Arial", size: 11, bold: true, color: "#FFFFFF" };
legend.getRange("A4:C4").format.fill = "#23517C";
legend.getRange("A4:C4").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
legend.getRange("A1:D13").format.wrapText = true;
legend.getRange("A:A").format.columnWidth = 24;
legend.getRange("B:B").format.columnWidth = 68;
legend.getRange("C:C").format.columnWidth = 70;
legend.getRange("D:D").format.columnWidth = 24;
legend.getRange("A1:D13").format.rowHeight = 32;

const corrections = wb.worksheets.add("CORREÇÕES AUDITADAS");
corrections.getRange("A1:F1").values = [["Fluido", "Campo", "Valor reconstruído", "Unidade", "Fonte e cálculo", "Estado"]];
corrections.getRange("A2:F7").values = [
  ["J", "Vida da ferramenta", 2242.7, "cm³", "COMPARATIVO!F17 = 2242,7136; arredondado a 1 casa", "DETERMINÍSTICO / UNDER_REVIEW"],
  ["K", "Vida da ferramenta", 2450.7, "cm³", "COMPARATIVO!F18 = 2450,7072; arredondado a 1 casa", "DETERMINÍSTICO / UNDER_REVIEW"],
  ["J", "Custo da ferramenta para o lote", 0.8918, "R$", "20 / 2242,7 × 100; arredondado a 4 casas", "DETERMINÍSTICO / UNDER_REVIEW"],
  ["K", "Custo da ferramenta para o lote", 0.8161, "R$", "20 / 2450,7 × 100; arredondado a 4 casas", "DETERMINÍSTICO / UNDER_REVIEW"],
  ["J", "Custo total anual operação/ferramenta", 117.5584, "R$", "116,6666667 + (20 / 2242,7 × 100); arredondado a 4 casas", "DETERMINÍSTICO / UNDER_REVIEW"],
  ["K", "Custo total anual operação/ferramenta", 117.4828, "R$", "116,6666667 + (20 / 2450,7 × 100); arredondado a 4 casas", "DETERMINÍSTICO / UNDER_REVIEW"],
];
corrections.getRange("C2:C7").format.fill = "#A9DCEB";
corrections.getRange("C2:C7").format.font = { name: "Arial", size: 10, color: "#17212D" };
corrections.getRange("C2:C3").setNumberFormat("0.0");
corrections.getRange("C4:C7").setNumberFormat("0.0000");
corrections.getRange("A1:F1").format.fill = "#23517C";
corrections.getRange("A1:F1").format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
corrections.getRange("A:A").format.columnWidth = 12;
corrections.getRange("B:B").format.columnWidth = 46;
corrections.getRange("C:C").format.columnWidth = 20;
corrections.getRange("D:D").format.columnWidth = 12;
corrections.getRange("E:E").format.columnWidth = 70;
corrections.getRange("F:F").format.columnWidth = 34;
corrections.getRange("A1:F7").format.rowHeight = 28;
corrections.getRange("E1:F7").format.wrapText = true;
corrections.getRange("A9:F9").values = [["ATENÇÃO", "Estes são os 6 valores já reconstruídos em economico_v1.xlsx.", "", "", "Não preencher automaticamente AF38/AI38 ou total anual na aba original; há dependências econômicas pendentes.", "UNDER_REVIEW"]];
corrections.getRange("A9:F9").format.fill = "#FFF5DE";
corrections.getRange("A9:F9").format.rowHeight = 48;
corrections.getRange("A9:F9").format.wrapText = true;

await render("comparativo_depois", "COMPARATIVO", "A8:F12");
await render("legenda_depois", "LEGENDA AUDITORIA", "A1:C9");
await render("correcoes_depois", "CORREÇÕES AUDITADAS", "A1:F7");
await (await SpreadsheetFile.exportXlsx(wb)).save(output);
console.log(`Arquivo auditado: ${output}`);
console.log(`Células marcadas nas abas de origem: ${marked.length}`);
