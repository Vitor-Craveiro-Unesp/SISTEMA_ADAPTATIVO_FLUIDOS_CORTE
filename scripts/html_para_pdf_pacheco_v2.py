"""Converte o relatório HTML v2 em PDF completo, incluindo conteúdo expansível."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

from lxml import html
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


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "output" / "html" / "relatorio_completo_pacheco_boss_v2.html"
OUTPUT = ROOT / "output" / "html" / "relatorio_completo_pacheco_boss_v2.pdf"
CHART = ROOT / "results" / "eda" / "fig_missingness_v1.png"


def fonts() -> tuple[str, str, str]:
    candidates = (
        ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/consola.ttf"),
        ("C:/Windows/Fonts/DejaVuSans.ttf", "C:/Windows/Fonts/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/DejaVuSansMono.ttf"),
    )
    for regular, bold, mono in candidates:
        if Path(regular).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("PachecoSans", regular))
            pdfmetrics.registerFont(TTFont("PachecoSansBold", bold))
            if Path(mono).exists():
                pdfmetrics.registerFont(TTFont("PachecoMono", mono))
                return "PachecoSans", "PachecoSansBold", "PachecoMono"
            return "PachecoSans", "PachecoSansBold", "Courier"
    return "Helvetica", "Helvetica-Bold", "Courier"


FONT, FONT_BOLD, FONT_MONO = fonts()
NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#1677B8")
PALE = colors.HexColor("#EFF6FA")
GREY = colors.HexColor("#D8E1E8")
RED_PALE = colors.HexColor("#FFF1EF")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitleV2", fontName=FONT_BOLD, fontSize=25, leading=30,
                          alignment=TA_CENTER, textColor=NAVY, spaceAfter=16))
styles.add(ParagraphStyle(name="CoverSubV2", fontName=FONT, fontSize=11, leading=16,
                          alignment=TA_CENTER, textColor=colors.HexColor("#475569"), spaceAfter=10))
styles.add(ParagraphStyle(name="SectionV2", fontName=FONT_BOLD, fontSize=15, leading=19,
                          textColor=NAVY, spaceBefore=18, spaceAfter=10, keepWithNext=True))
styles.add(ParagraphStyle(name="SubsectionV2", fontName=FONT_BOLD, fontSize=11.3, leading=15,
                          textColor=BLUE, spaceBefore=12, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name="MinorHeadingV2", fontName=FONT_BOLD, fontSize=9.4, leading=12.5,
                          textColor=NAVY, spaceBefore=9, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="BodyV2", fontName=FONT, fontSize=8.8, leading=12.7,
                          alignment=TA_JUSTIFY, textColor=colors.HexColor("#243244"), spaceAfter=6))
styles.add(ParagraphStyle(name="ListV2", parent=styles["BodyV2"], leftIndent=16,
                          firstLineIndent=-11, spaceAfter=4))
styles.add(ParagraphStyle(name="CalloutV2", parent=styles["BodyV2"], leftIndent=8,
                          rightIndent=8, borderWidth=0.7, borderColor=BLUE,
                          borderPadding=8, backColor=PALE, spaceAfter=10))
styles.add(ParagraphStyle(name="RiskV2", parent=styles["CalloutV2"],
                          borderColor=colors.HexColor("#B42318"), backColor=RED_PALE))
styles.add(ParagraphStyle(name="TableHeadV2", fontName=FONT_BOLD, fontSize=6, leading=7.5,
                          textColor=colors.white, alignment=TA_LEFT, wordWrap="CJK"))
styles.add(ParagraphStyle(name="TableCellV2", fontName=FONT, fontSize=5.8, leading=7.3,
                          textColor=colors.HexColor("#263238"), wordWrap="CJK"))
styles.add(ParagraphStyle(name="CodeV2", fontName=FONT_MONO, fontSize=6.1, leading=8.1,
                          leftIndent=5, rightIndent=5, borderPadding=5, borderWidth=0.4,
                          borderColor=GREY, backColor=colors.HexColor("#F6F8FA")))


def plain(node) -> str:
    return re.sub(r"\s+", " ", " ".join(node.itertext())).strip()


def para(text: str, style: str = "BodyV2") -> Paragraph:
    return Paragraph(escape(text), styles[style])


class PdfDocument(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(str(filename), pagesize=A4, leftMargin=1.6 * cm,
                         rightMargin=1.6 * cm, topMargin=1.7 * cm,
                         bottomMargin=1.45 * cm,
                         title="Relatório Pacheco + Boss - guia técnico v2",
                         author="Projeto Fluidos de Corte")
        self.addPageTemplates(PageTemplate(id="main", frames=Frame(
            self.leftMargin, self.bottomMargin, self.width, self.height, id="body"),
            onPage=self.decorate))
        self.bookmark_count = 0

    def beforeDocument(self):
        self.bookmark_count = 0
        super().beforeDocument()

    def decorate(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(GREY)
        canvas.line(self.leftMargin, A4[1] - 1.28 * cm,
                    A4[0] - self.rightMargin, A4[1] - 1.28 * cm)
        canvas.setFillColor(colors.HexColor("#64748B"))
        canvas.setFont(FONT, 7.2)
        canvas.drawString(self.leftMargin, A4[1] - 1.02 * cm,
                          "Fluidos de Corte | Pacheco + revisão Boss | Guia v2")
        canvas.drawString(self.leftMargin, 0.78 * cm,
                          "Dados Pacheco v1 sob revisão | CHANGES_REQUESTED")
        canvas.drawRightString(A4[0] - self.rightMargin, 0.78 * cm,
                               f"Página {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in {
            "SectionV2", "SubsectionV2"
        }:
            level = 0 if flowable.style.name == "SectionV2" else 1
            label = flowable.getPlainText()
            key = f"sec-{self.bookmark_count}"
            self.bookmark_count += 1
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(label, key, level=level, closed=False)
            self.notify("TOCEntry", (level, label, self.page, key))


def add_table(story: list, element, doc_width: float):
    rows = []
    for tr in element.xpath(".//tr"):
        cells = tr.xpath("./th|./td")
        if cells:
            rows.append([plain(cell) for cell in cells])
    if not rows:
        return
    columns = max(map(len, rows))
    data = []
    for row_index, row in enumerate(rows):
        style = "TableHeadV2" if row_index == 0 else "TableCellV2"
        normalized = row + [""] * (columns - len(row))
        data.append([para(value, style) for value in normalized])
    table = LongTable(data, colWidths=[doc_width / columns] * columns,
                      repeatRows=1, hAlign="LEFT", splitByRow=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("GRID", (0, 0), (-1, -1), 0.25, GREY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.extend([table, Spacer(1, 8)])


def add_code(story: list, code: str):
    wrapped = []
    for line in code.splitlines():
        wrapped.extend(textwrap.wrap(line.expandtabs(2), width=105,
                                     subsequent_indent="    ",
                                     replace_whitespace=False,
                                     drop_whitespace=False) or [""])
    for offset in range(0, len(wrapped), 35):
        story.append(Preformatted("\n".join(wrapped[offset:offset + 35]),
                                  styles["CodeV2"]))
        story.append(Spacer(1, 4))


def render_node(node, story: list, doc_width: float):
    if not isinstance(node.tag, str):
        return
    tag = node.tag.lower()
    classes = set(node.get("class", "").split())
    if tag in {"script", "style", "input", "footer"}:
        return
    if tag == "svg":
        if CHART.exists():
            chart = Image(str(CHART))
            ratio = chart.imageHeight / chart.imageWidth
            chart.drawWidth = min(doc_width - 0.5 * cm, 15.5 * cm)
            chart.drawHeight = chart.drawWidth * ratio
            story.extend([chart, para("Figura: taxa de ausência por domínio.")])
        return
    if tag == "table":
        add_table(story, node, doc_width)
        return
    if tag == "pre":
        add_code(story, node.text_content())
        return
    if tag in {"h1", "h2", "h3", "h4"}:
        style = {"h1": "SectionV2", "h2": "SectionV2",
                 "h3": "SubsectionV2", "h4": "MinorHeadingV2"}[tag]
        if plain(node):
            story.append(para(plain(node), style))
        return
    if tag == "p":
        if plain(node):
            style = "RiskV2" if "risk" in node.getparent().get("class", "").split() else "BodyV2"
            story.append(para(plain(node), style))
        return
    if tag in {"ul", "ol"}:
        for i, item in enumerate(node.xpath("./li"), start=1):
            prefix = f"{i}. " if tag == "ol" else "• "
            item_text = re.sub(r"^(?:\d+\.\s+|[•-]\s+)", "", plain(item))
            story.append(para(prefix + item_text, "ListV2"))
        return
    if tag == "dl":
        for entry in node.xpath("./div"):
            dt = entry.find("dt")
            dd = entry.find("dd")
            if dt is not None and dd is not None:
                story.append(para(f"{plain(dt)}: {plain(dd)}"))
        return
    if tag == "article" and "detailed-plan" in classes:
        number = node.xpath("./div[contains(@class,'problem-number')]")
        code = node.xpath(".//div[contains(@class,'plan-title')]/span")
        title = node.xpath(".//div[contains(@class,'plan-title')]/h3")
        label = f"Problema {plain(number[0]) if number else '?'} | {plain(code[0]) if code else ''} | {plain(title[0]) if title else ''}"
        story.append(para(label, "SubsectionV2"))
        for field in node.xpath(".//div[contains(@class,'plan-field')]"):
            render_node(field, story, doc_width)
        return
    if tag == "details":
        summary = node.find("summary")
        if summary is not None and plain(summary):
            story.append(para(plain(summary), "SubsectionV2"))
        for child in node:
            if child is not summary:
                render_node(child, story, doc_width)
        return
    if "chart-card" in classes:
        svg = node.find("svg")
        if svg is not None:
            render_node(svg, story, doc_width)
        return
    if "review-banner" in classes or "callout" in classes or "why-card" in classes:
        if plain(node):
            story.append(para(plain(node), "CalloutV2"))
        return
    if "metric-grid" in classes or "timeline" in classes or "pipeline" in classes:
        for child in node:
            if plain(child):
                story.append(para(plain(child)))
        return
    if tag == "header" and "hero" not in classes:
        if plain(node):
            story.append(para(plain(node), "MinorHeadingV2"))
        return
    if tag in {"summary", "span", "strong", "b", "small", "dt", "dd", "li", "th", "td"}:
        return
    for child in node:
        render_node(child, story, doc_width)


def build_pdf():
    if not SOURCE.exists():
        raise FileNotFoundError(f"HTML de origem não encontrado: {SOURCE}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    tree = html.fromstring(SOURCE.read_text(encoding="utf-8"))
    sections = tree.xpath("//main/section")
    if len(sections) != 15:
        raise ValueError(f"Esperadas 15 seções do HTML v2; encontradas {len(sections)}.")
    doc = PdfDocument(str(OUTPUT))
    story: list = [
        Spacer(1, 2.3 * cm),
        para("RELATÓRIO TÉCNICO PACHECO + BOSS", "CoverTitleV2"),
        para("Guia v2 de correção - dados Pacheco v1 sob revisão", "CoverSubV2"),
        Spacer(1, 0.7 * cm),
        para("11 achados oficiais: 5 de base/dados, 4 de código/execução e 2 de arquitetura/documentação.", "CalloutV2"),
        para("Veredito do Boss: CHANGES_REQUESTED. O handoff para Benjamin continua não liberado.", "RiskV2"),
        para(f"Fonte deste PDF: {SOURCE.name}. O documento inclui o conteúdo de todos os blocos expansíveis do HTML."),
        PageBreak(),
        para("Sumário", "SectionV2"),
    ]
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOC1V2", fontName=FONT_BOLD, fontSize=9.3,
                       leading=14, textColor=NAVY),
        ParagraphStyle(name="TOC2V2", fontName=FONT, fontSize=8.1, leading=11,
                       leftIndent=14, textColor=BLUE),
    ]
    story.extend([toc, PageBreak()])
    for section in sections:
        heading = section.xpath("./div[contains(@class,'section-heading')]/h2")
        eyebrow = section.xpath("./div[contains(@class,'section-heading')]/span")
        if heading:
            title = f"{plain(eyebrow[0])} | {plain(heading[0])}" if eyebrow else plain(heading[0])
            story.append(para(title, "SectionV2"))
        for child in section:
            if "section-heading" not in child.get("class", "").split():
                render_node(child, story, doc.width)
    doc.multiBuild(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
