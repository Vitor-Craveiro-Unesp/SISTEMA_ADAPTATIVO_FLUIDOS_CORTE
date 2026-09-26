"""Gera o relatório técnico completo da etapa Pacheco e da revisão Boss."""

from __future__ import annotations

import csv
import re
import textwrap
from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    LongTable,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing, String
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "relatorio_completo_pacheco_boss_v1.pdf"
REVIEW = ROOT / "reviews" / "BOSS_REVIEW_PACHECO_v1.md"


def register_fonts() -> tuple[str, str, str]:
    regular = Path("C:/Windows/Fonts/arial.ttf")
    bold = Path("C:/Windows/Fonts/arialbd.ttf")
    mono = Path("C:/Windows/Fonts/consola.ttf")
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("ReportSans", str(regular)))
        pdfmetrics.registerFont(TTFont("ReportSansBold", str(bold)))
        if mono.exists():
            pdfmetrics.registerFont(TTFont("ReportMono", str(mono)))
        return "ReportSans", "ReportSansBold", "ReportMono" if mono.exists() else "Courier"
    return "Helvetica", "Helvetica-Bold", "Courier"


FONT, FONT_BOLD, FONT_MONO = register_fonts()
NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2C7FB8")
LIGHT_BLUE = colors.HexColor("#EAF3F8")
LIGHT_GREY = colors.HexColor("#F2F4F5")
RED = colors.HexColor("#A61B1B")
AMBER = colors.HexColor("#B36B00")
GREEN = colors.HexColor("#26734D")


class ReviewDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=self.draw_header_footer))
        self._bookmark_id = 0

    def beforeDocument(self):
        # multiBuild executa várias passagens para estabilizar o sumário.
        # Reiniciar o contador mantém as chaves de bookmark determinísticas.
        self._bookmark_id = 0
        super().beforeDocument()

    def draw_header_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D3DCE3"))
        canvas.line(self.leftMargin, A4[1] - 1.35 * cm, A4[0] - self.rightMargin, A4[1] - 1.35 * cm)
        canvas.setFont(FONT, 7.5)
        canvas.setFillColor(colors.HexColor("#5D6D7E"))
        canvas.drawString(self.leftMargin, A4[1] - 1.05 * cm, "Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte")
        canvas.drawRightString(A4[0] - self.rightMargin, 0.8 * cm, f"Página {doc.page}")
        canvas.drawString(self.leftMargin, 0.8 * cm, "Pacheco v1 | Revisão AGENTE_BOSS")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in {"ReportHeading1", "ReportHeading2"}:
            level = 0 if flowable.style.name == "ReportHeading1" else 1
            text = flowable.getPlainText()
            key = f"bookmark-{self._bookmark_id}"
            self._bookmark_id += 1
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=False)
            self.notify("TOCEntry", (level, text, self.page, key))


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontName=FONT_BOLD, fontSize=24, leading=29, textColor=NAVY, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="CoverSub", fontName=FONT, fontSize=12, leading=17, textColor=colors.HexColor("#455A64"), alignment=TA_CENTER))
styles.add(ParagraphStyle(name="ReportHeading1", parent=styles["Heading1"], fontName=FONT_BOLD, fontSize=16, leading=20, textColor=NAVY, spaceBefore=10, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle(name="ReportHeading2", parent=styles["Heading2"], fontName=FONT_BOLD, fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name="FindingHeading", parent=styles["Heading3"], fontName=FONT_BOLD, fontSize=10.5, leading=14, textColor=NAVY, spaceBefore=7, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="BodyTextCustom", fontName=FONT, fontSize=9.2, leading=13.2, alignment=TA_JUSTIFY, textColor=colors.HexColor("#263238"), spaceAfter=6))
styles.add(ParagraphStyle(name="Small", fontName=FONT, fontSize=7.5, leading=10, textColor=colors.HexColor("#37474F")))
styles.add(ParagraphStyle(name="TableCell", fontName=FONT, fontSize=6.2, leading=7.7, wordWrap="CJK"))
styles.add(ParagraphStyle(name="TableHead", fontName=FONT_BOLD, fontSize=6.3, leading=7.8, textColor=colors.white, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="CodeCustom", fontName=FONT_MONO, fontSize=6.5, leading=8.2, leftIndent=5, rightIndent=5, borderColor=colors.HexColor("#D5DBDB"), borderWidth=0.5, borderPadding=6, backColor=colors.HexColor("#F8F9F9"), spaceAfter=6))
styles.add(ParagraphStyle(name="Callout", fontName=FONT, fontSize=9, leading=13, leftIndent=8, rightIndent=8, borderColor=BLUE, borderWidth=0.8, borderPadding=8, backColor=LIGHT_BLUE, spaceAfter=8))


def p(text: str, style: str = "BodyTextCustom") -> Paragraph:
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), styles[style])


def clean_markdown(text: str) -> str:
    return text.replace("**", "").replace("`", "")


def heading(text: str, level: int = 1) -> Paragraph:
    return Paragraph(escape(text), styles["ReportHeading1" if level == 1 else "ReportHeading2"])


def read_csv(relative: str) -> list[dict[str, str]]:
    path = ROOT / relative
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def add_table(story: list, title: str, rows: list[dict[str, str]], columns: list[str] | None = None, max_rows: int | None = None):
    story.append(heading(title, 2))
    if not rows:
        story.append(p("Nenhum registro.", "Small"))
        return
    columns = columns or list(rows[0].keys())
    displayed = rows if max_rows is None else rows[:max_rows]
    data = [[Paragraph(escape(column), styles["TableHead"]) for column in columns]]
    for row in displayed:
        data.append([Paragraph(escape(str(row.get(column, ""))), styles["TableCell"]) for column in columns])
    available = A4[0] - 3.4 * cm
    widths = [available / len(columns)] * len(columns)
    table = LongTable(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B0BEC5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    story.append(table)
    story.append(Spacer(1, 6))
    if max_rows is not None and len(rows) > max_rows:
        story.append(p(f"Tabela abreviada no corpo: {max_rows} de {len(rows)} registros. O CSV integral permanece no projeto.", "Small"))


def add_markdown(story: list, path: Path, title: str):
    story.append(heading(title, 1))
    text = path.read_text(encoding="utf-8")
    in_code = False
    code_lines: list[str] = []
    paragraph: list[str] = []
    table_lines: list[str] = []

    def flush_paragraph():
        if paragraph:
            story.append(p(clean_markdown(" ".join(paragraph))))
            paragraph.clear()

    def flush_code():
        if code_lines:
            wrapped = []
            for line in code_lines:
                wrapped.extend(textwrap.wrap(line, width=105, subsequent_indent="    ", replace_whitespace=False, drop_whitespace=False) or [""])
            story.append(Preformatted("\n".join(wrapped), styles["CodeCustom"]))
            code_lines.clear()

    def flush_table():
        if not table_lines:
            return
        parsed = [[clean_markdown(cell.strip()) for cell in line.strip().strip("|").split("|")] for line in table_lines]
        parsed = [row for row in parsed if not all(re.fullmatch(r":?-{2,}:?", cell or "-") for cell in row)]
        if not parsed:
            table_lines.clear()
            return
        width = A4[0] - 3.4 * cm
        columns = max(len(row) for row in parsed)
        normalized = [row + [""] * (columns - len(row)) for row in parsed]
        cells = []
        for row_index, row in enumerate(normalized):
            cell_style = styles["TableHead"] if row_index == 0 else styles["TableCell"]
            cells.append([Paragraph(escape(cell), cell_style) for cell in row])
        table = LongTable(cells, colWidths=[width / columns] * columns, repeatRows=1)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B0BEC5")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ]))
        story.extend([table, Spacer(1, 5)])
        table_lines.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.startswith("|"):
            flush_table()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_paragraph()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
        elif line.startswith("### "):
            flush_paragraph()
            story.append(Paragraph(escape(clean_markdown(line[4:])), styles["FindingHeading"]))
        elif line.startswith("## "):
            flush_paragraph()
            story.append(heading(line[3:], 2))
        elif line.startswith("# "):
            flush_paragraph()
            story.append(heading(line[2:], 1))
        elif re.match(r"^[-*] ", line):
            flush_paragraph()
            story.append(Paragraph("• " + escape(clean_markdown(line[2:])), styles["BodyTextCustom"]))
        elif re.match(r"^\d+\. ", line):
            flush_paragraph()
            story.append(Paragraph(escape(clean_markdown(line)), styles["BodyTextCustom"]))
        elif line.startswith("|"):
            flush_paragraph()
            table_lines.append(line)
        elif not line.strip() or line.strip() == "---":
            flush_paragraph()
        else:
            paragraph.append(line)
    flush_paragraph()
    flush_code()
    flush_table()


def missingness_chart(rows: list[dict[str, str]]) -> Drawing:
    summary: dict[str, list[tuple[int, int]]] = {}
    for row in rows:
        summary.setdefault(row["data_domain"], []).append((int(row["missing_values"]), int(row["observations"])))
    domains = sorted(summary)
    rates = [sum(m for m, _ in summary[d]) / sum(n for _, n in summary[d]) for d in domains]
    drawing = Drawing(450, 245)
    drawing.add(String(225, 225, "Ausências por domínio da base canônica", textAnchor="middle", fontName=FONT_BOLD, fontSize=12))
    chart = VerticalBarChart()
    chart.x = 55
    chart.y = 45
    chart.height = 155
    chart.width = 360
    chart.data = [rates]
    chart.categoryAxis.categoryNames = domains
    chart.categoryAxis.labels.fontName = FONT
    chart.categoryAxis.labels.fontSize = 7.5
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = max(0.1, min(1.0, max(rates) * 1.25))
    chart.valueAxis.labels.fontName = FONT
    chart.valueAxis.labels.fontSize = 7
    chart.valueAxis.labelTextFormat = lambda value: f"{100 * value:.0f}%"
    chart.bars[0].fillColor = BLUE
    chart.bars[0].strokeColor = NAVY
    drawing.add(chart)
    drawing.add(String(15, 125, "Taxa de ausência", angle=90, textAnchor="middle", fontName=FONT, fontSize=8))
    return drawing


def add_code_file(story: list, relative: str):
    path = ROOT / relative
    story.append(heading(relative, 2))
    lines = path.read_text(encoding="utf-8").splitlines()
    numbered = [f"{index:04d}  {line}" for index, line in enumerate(lines, start=1)]
    wrapped: list[str] = []
    for line in numbered:
        wrapped.extend(textwrap.wrap(line, width=105, subsequent_indent="      ", replace_whitespace=False, drop_whitespace=False) or [""])
    story.append(Preformatted("\n".join(wrapped), styles["CodeCustom"]))


def verdict_from_review(text: str) -> str:
    for verdict in ("BLOCKED", "CHANGES_REQUESTED", "APPROVED"):
        if re.search(rf"\b{verdict}\b", text):
            return verdict
    return "NOT_IDENTIFIED"


def build_pdf():
    if not REVIEW.exists():
        raise FileNotFoundError("A revisão formal do AGENTE_BOSS ainda não foi produzida.")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    review_text = REVIEW.read_text(encoding="utf-8")
    verdict = verdict_from_review(review_text)

    doc = ReviewDocTemplate(
        str(OUTPUT), pagesize=A4,
        leftMargin=1.7 * cm, rightMargin=1.7 * cm,
        topMargin=1.8 * cm, bottomMargin=1.45 * cm,
        title="Relatório completo Pacheco + revisão Boss v1",
        author="Sistema multiagente do projeto",
        subject="Inventário, auditoria, reconciliação, base canônica, ADA inicial e revisão metodológica",
    )
    story: list = []

    story.extend([
        Spacer(1, 2.3 * cm),
        Paragraph("RELATÓRIO TÉCNICO COMPLETO", styles["CoverTitle"]),
        Paragraph("Etapa AGENTE_PACHECO + Revisão formal AGENTE_BOSS", styles["CoverSub"]),
        Spacer(1, 0.8 * cm),
        Table([
            [p("Projeto", "Small"), p("Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte", "Small")],
            [p("Versão", "Small"), p("v1 - 25/09/2026", "Small")],
            [p("Branch", "Small"), p("agente_pacheco", "Small")],
            [p("Status Pacheco", "Small"), p("READY_FOR_BOSS_REVIEW", "Small")],
            [p("Veredito Boss", "Small"), p(verdict, "Small")],
            [p("Fonte", "Small"), p("data/raw/ensaio_bancada_alunos (2).xlsx", "Small")],
        ], colWidths=[4.2 * cm, 11.2 * cm], style=TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), NAVY),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#90A4AE")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ])),
        Spacer(1, 1.2 * cm),
        p("Documento gerado a partir dos artefatos reproduzíveis do projeto. Dados brutos não foram modificados. Ausência não foi convertida em zero, e nenhum valor suspeito foi corrigido silenciosamente.", "Callout"),
        PageBreak(),
        heading("Sumário", 1),
    ])
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOC1", fontName=FONT_BOLD, fontSize=9.5, leading=14, leftIndent=0, firstLineIndent=0, textColor=NAVY),
        ParagraphStyle(name="TOC2", fontName=FONT, fontSize=8.2, leading=11, leftIndent=14, firstLineIndent=0, textColor=colors.HexColor("#455A64")),
    ]
    story.extend([toc, PageBreak()])

    story.append(heading("1. Síntese executiva", 1))
    story.append(p("A etapa Pacheco implementou e executou o inventário do XLSX, a auditoria de estrutura e conteúdo, a reconciliação de valores entre abas, a construção de uma base canônica longa e uma análise descritiva inicial. A etapa não realizou seleção de critérios, conformidade final, CRITIC, TOPSIS, Pareto ou ranking."))
    story.append(p("A base canônica resultante contém 1.034 registros de 11 fluidos (A, B, C, D, E, F, G, H, J, K e M), cada um com rastreabilidade até a aba e célula de origem. Foram preservadas 15 ausências e 36 zeros explícitos. Nenhuma célula de origem foi duplicada no mapeamento canônico."))
    story.append(p(f"O parecer independente do AGENTE_BOSS está reproduzido integralmente neste documento. Veredito identificado: {verdict}.", "Callout"))

    story.append(heading("2. Escopo, governança e limites", 1))
    story.append(p("Pacheco é proprietário das etapas 01 a 05: inventário, auditoria, reconciliação, base canônica e ADA inicial. Benjamin permanece proprietário de critérios, conformidade e CRITIC; Vitor, de ranking e robustez; Marco, de integração e comunicação; Boss, da revisão metodológica."))
    story.append(p("A fonte oficial tem prioridade sobre suposições. data/raw é imutável. Resultados ainda não aprovados não podem alimentar diretamente relatório final, apresentação ou ranking."))

    add_table(story, "2.1 Inventário dos arquivos de entrada", read_csv("results/audit/raw_file_inventory_v1.csv"))
    add_table(story, "2.2 Verificação da cópia de trabalho", read_csv("results/audit/working_copy_verification_v1.csv"))
    add_table(story, "2.3 Inventário das abas", read_csv("results/audit/sheet_inventory_v1.csv"), ["sheet_index", "sheet_name", "rows_read", "columns_read", "non_blank_cells", "provisional_header_row"])

    story.append(heading("3. Método de extração e rastreabilidade", 1))
    story.append(p("A planilha não é uma única tabela retangular. Ela reúne blocos de especificação, resultados de usinabilidade, análise de emulsões, consolidação comparativa e avaliação econômica. Por isso, a base canônica foi organizada em formato longo, preservando os blocos científicos e a célula de origem."))
    story.append(p("Campos canônicos: arquivo, aba, célula, domínio, identificador do fluido, tipo de fluido quando disponível, métrica, condição, unidade, requisito declarado na fonte, valor original, representação numérica, representação textual e indicador de ausência."))
    add_table(story, "3.1 Dicionário canônico", read_csv("data/processed/dicionario_variaveis_v1.csv"), max_rows=None)

    story.append(heading("4. Auditoria de qualidade", 1))
    add_table(story, "4.1 Resumo de ausências", read_csv("results/audit/missing_summary_v1.csv"))
    add_table(story, "4.2 Resumo de unidades", read_csv("results/audit/unit_summary_v1.csv"))
    add_table(story, "4.3 Fórmulas OOXML encontradas", read_csv("results/audit/formula_inventory_v1.csv"))
    add_table(story, "4.4 Avaliação de outliers", read_csv("results/audit/outlier_assessment_v1.csv"))
    story.append(p("A tabela de duplicidade por célula contém 1.034 entradas e nenhuma duplicata. Para evitar dezenas de páginas sem informação adicional, são mostradas amostras; o CSV integral permanece em results/audit/duplicate_source_cell_audit_v1.csv."))
    add_table(story, "4.5 Amostra da auditoria de células de origem", read_csv("results/audit/duplicate_source_cell_audit_v1.csv"), max_rows=35)

    story.append(heading("5. Reconciliação entre abas", 1))
    story.append(p("A vida de ferramenta foi somada nas quatro condições da aba de usinabilidade e comparada ao somatório armazenado em COMPARATIVO. A identidade econômica confrontou custo anual do fluido mais custo anual de operação/ferramenta com o total anual declarado. Sem tolerâncias configuradas, diferenças materiais foram mantidas como pendências."))
    add_table(story, "5.1 Controles de reconciliação", read_csv("results/audit/reconciliation_checks_v1.csv"))

    story.append(heading("6. Registro de problemas", 1))
    add_table(story, "6.1 Issues abertos", read_csv("results/audit/issue_log_v1.csv"), ["issue_id", "severity", "domain", "location", "description", "evidence", "required_action", "status"])

    story.append(heading("7. ADA inicial", 1))
    story.append(p("A análise descritiva inicial resume distribuição numérica e ausências por domínio. Ela é exploratória e não transforma os resultados em decisão multicritério."))
    chart = missingness_chart(read_csv("results/eda/eda_missingness_v1.csv"))
    chart.hAlign = "CENTER"
    story.extend([chart, p("Figura 1 - Taxa de ausência por domínio da base canônica.", "Small")])
    add_table(story, "7.1 Estatísticas numéricas", read_csv("results/eda/eda_numeric_summary_v1.csv"))
    add_table(story, "7.2 Ausências na ADA", read_csv("results/eda/eda_missingness_v1.csv"))

    add_markdown(story, ROOT / "report" / "stages" / "01_pacheco" / "EXECUCAO_PACHECO_v1.md", "8. Relatório Pacheco")
    add_markdown(story, ROOT / "handoffs" / "01_PACHECO_to_BENJAMIN.md", "9. Handoff Pacheco para Benjamin")
    add_markdown(story, REVIEW, "10. Parecer do AGENTE_BOSS")

    story.append(PageBreak())
    story.append(heading("11. Código-fonte reprodutível", 1))
    for relative in [
        "R/pacheco/importacao.R",
        "R/pacheco/inventario.R",
        "R/pacheco/missing.R",
        "R/pacheco/unidades.R",
        "R/pacheco/reconciliacao.R",
        "R/pacheco/base_canonica.R",
        "R/pacheco/ada_inicial.R",
        "scripts/run_audit.R",
        "tests/testthat/test-pacheco-auditoria.R",
    ]:
        add_code_file(story, relative)

    story.append(heading("12. Inventário completo de variáveis da fonte", 1))
    add_table(story, "12.1 Variáveis e exemplos de valores", read_csv("results/audit/variable_inventory_v1.csv"), max_rows=None)

    story.append(heading("13. Reprodutibilidade e validação", 1))
    story.append(p("Comando principal: Rscript scripts/run_audit.R. O script regenera a cópia de trabalho, os hashes, os inventários, a base canônica, o dicionário, os relatórios de qualidade, a reconciliação e a ADA inicial."))
    story.append(p("Os testes verificam: igualdade de hashes entre fonte e cópia, presença da linhagem, unicidade de aba+célula, existência de ausências legítimas, presença de observações textuais e separação entre zero e ausência."))
    story.append(p("Os avisos de localidade emitidos pelo R 4.5.0 referem-se à configuração LC_* do ambiente Windows e não alteraram os artefatos ou o resultado dos testes."))

    story.append(heading("14. Conclusão e condição de avanço", 1))
    story.append(p("A etapa Pacheco produziu os artefatos previstos e preservou a fonte. A passagem para Benjamin depende do veredito formal do Boss e da resolução dos achados classificados no parecer. Até isso ocorrer, nenhum resultado desta etapa deve ser tratado como aprovado para critérios, pesos ou ranking."))
    doc.multiBuild(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
