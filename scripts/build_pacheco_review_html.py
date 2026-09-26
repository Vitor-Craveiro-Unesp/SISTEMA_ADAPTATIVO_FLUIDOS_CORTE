"""Gera um relatório HTML autocontido da etapa Pacheco e da revisão Boss."""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "html" / "relatorio_completo_pacheco_boss_v1.html"


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value))


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def slug(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text or "secao"


def inline_markdown(text: str) -> str:
    text = esc(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    code: list[str] = []
    in_code = False
    table: list[list[str]] = []

    def flush_paragraph():
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list():
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    def flush_code():
        if code:
            output.append(f"<pre><code>{esc(chr(10).join(code))}</code></pre>")
            code.clear()

    def flush_table():
        if not table:
            return
        rows = [row for row in table if not all(re.fullmatch(r":?-{2,}:?", cell or "-") for cell in row)]
        if rows:
            columns = max(map(len, rows))
            rows = [row + [""] * (columns - len(row)) for row in rows]
            output.append('<div class="table-scroll"><table>')
            output.append("<thead><tr>" + "".join(f"<th>{inline_markdown(cell)}</th>" for cell in rows[0]) + "</tr></thead><tbody>")
            for row in rows[1:]:
                output.append("<tr>" + "".join(f"<td>{inline_markdown(cell)}</td>" for cell in row) + "</tr>")
            output.append("</tbody></table></div>")
        table.clear()

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph(); flush_list(); flush_table()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue
        if not line.startswith("|"):
            flush_table()
        heading_match = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading_match:
            flush_paragraph(); flush_list()
            level = min(4, len(heading_match.group(1)) + 1)
            title = heading_match.group(2)
            output.append(f'<h{level} id="{slug(title)}">{inline_markdown(title)}</h{level}>')
        elif line.startswith("|"):
            flush_paragraph(); flush_list()
            table.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif re.match(r"^[-*]\s+", line):
            flush_paragraph()
            if list_type != "ul":
                flush_list(); output.append("<ul>"); list_type = "ul"
            output.append(f"<li>{inline_markdown(re.sub(r'^[-*]\\s+', '', line))}</li>")
        elif re.match(r"^\d+\.\s+", line):
            flush_paragraph()
            if list_type != "ol":
                flush_list(); output.append("<ol>"); list_type = "ol"
            output.append(f"<li>{inline_markdown(re.sub(r'^\\d+\\.\\s+', '', line))}</li>")
        elif line.startswith(">"):
            flush_paragraph(); flush_list()
            output.append(f"<blockquote>{inline_markdown(line.lstrip('> '))}</blockquote>")
        elif not line.strip() or line.strip() == "---":
            flush_paragraph(); flush_list()
        else:
            paragraph.append(line)
    flush_paragraph(); flush_list(); flush_code(); flush_table()
    return "\n".join(output)


def table_html(rows: list[dict[str, str]], columns: list[str] | None = None, table_id: str | None = None) -> str:
    if not rows:
        return '<p class="empty">Nenhum registro.</p>'
    columns = columns or list(rows[0])
    table_id = table_id or "table-" + slug("-".join(columns))
    head = "".join(f"<th>{esc(column)}</th>" for column in columns)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{esc(row.get(column, ''))}</td>" for column in columns) + "</tr>")
    return f'''<div class="table-tools"><label>Filtrar tabela <input type="search" placeholder="Digite para filtrar…" oninput="filterTable('{table_id}', this.value)"></label><span>{len(rows)} registros</span></div>
    <div class="table-scroll"><table id="{table_id}"><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>'''


def section(section_id: str, eyebrow: str, title: str, content: str) -> str:
    return f'''<section id="{section_id}" class="report-section">
      <div class="section-heading"><span>{esc(eyebrow)}</span><h2>{esc(title)}</h2></div>
      {content}
    </section>'''


def missingness_svg(rows: list[dict[str, str]]) -> str:
    totals: dict[str, list[int]] = {}
    for row in rows:
        domain = row["data_domain"]
        totals.setdefault(domain, [0, 0])
        totals[domain][0] += int(row["missing_values"])
        totals[domain][1] += int(row["observations"])
    domains = sorted(totals)
    rates = [totals[d][0] / totals[d][1] if totals[d][1] else 0 for d in domains]
    max_rate = max(max(rates) * 1.25, 0.1)
    width, height = 760, 330
    left, top, bottom = 65, 35, 65
    plot_h = height - top - bottom
    plot_w = width - left - 30
    bar_space = plot_w / max(1, len(domains))
    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-labelledby="chart-title chart-desc">',
             '<title id="chart-title">Taxa de ausência por domínio</title>',
             '<desc id="chart-desc">Gráfico de barras mostrando a proporção de valores ausentes em cada domínio da base canônica.</desc>']
    for tick in range(6):
        rate = max_rate * tick / 5
        y = top + plot_h - (rate / max_rate) * plot_h
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" class="gridline"/>')
        parts.append(f'<text x="{left-10}" y="{y+4:.1f}" text-anchor="end" class="axis-label">{rate*100:.0f}%</text>')
    for index, (domain, rate) in enumerate(zip(domains, rates)):
        bar_w = bar_space * 0.52
        x = left + index * bar_space + (bar_space - bar_w) / 2
        bar_h = (rate / max_rate) * plot_h
        y = top + plot_h - bar_h
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="5" class="bar"><title>{esc(domain)}: {rate*100:.2f}%</title></rect>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{top+plot_h+25}" text-anchor="middle" class="axis-label">{esc(domain)}</text>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{max(y-8, 18):.1f}" text-anchor="middle" class="bar-value">{rate*100:.2f}%</text>')
    parts.append("</svg>")
    return "".join(parts)


def code_details(relative: str) -> str:
    code = (ROOT / relative).read_text(encoding="utf-8")
    return f'''<details class="code-file"><summary><span>{esc(relative)}</span><small>{len(code.splitlines())} linhas</small></summary><pre><code>{esc(code)}</code></pre></details>'''


def build_html():
    raw_inventory = read_csv("results/audit/raw_file_inventory_v1.csv")
    copy_check = read_csv("results/audit/working_copy_verification_v1.csv")
    sheets = read_csv("results/audit/sheet_inventory_v1.csv")
    missing = read_csv("results/audit/missing_summary_v1.csv")
    units = read_csv("results/audit/unit_summary_v1.csv")
    reconciliation = read_csv("results/audit/reconciliation_checks_v1.csv")
    issues = read_csv("results/audit/issue_log_v1.csv")
    numeric = read_csv("results/eda/eda_numeric_summary_v1.csv")
    dictionary = read_csv("data/processed/dicionario_variaveis_v1.csv")
    variables = read_csv("results/audit/variable_inventory_v1.csv")
    review_path = ROOT / "reviews" / "BOSS_REVIEW_PACHECO_v1.md"
    review = review_path.read_text(encoding="utf-8")
    handoff = (ROOT / "handoffs" / "01_PACHECO_to_BENJAMIN.md").read_text(encoding="utf-8")

    issue_cards = []
    for issue in issues:
        severity = issue["severity"].lower()
        issue_cards.append(f'''<article class="issue-card {severity}">
          <header><span class="issue-id">{esc(issue['issue_id'])}</span><span class="badge {severity}">{esc(issue['severity'])}</span></header>
          <h3>{esc(issue['description'])}</h3>
          <dl><div><dt>Local</dt><dd>{esc(issue['location'])}</dd></div><div><dt>Evidência</dt><dd>{esc(issue['evidence'])}</dd></div><div><dt>Ação requerida</dt><dd>{esc(issue['required_action'])}</dd></div></dl>
        </article>''')

    code_files = [
        "R/pacheco/importacao.R", "R/pacheco/inventario.R", "R/pacheco/missing.R",
        "R/pacheco/unidades.R", "R/pacheco/reconciliacao.R", "R/pacheco/base_canonica.R",
        "R/pacheco/ada_inicial.R", "scripts/run_audit.R", "tests/testthat/test-pacheco-auditoria.R",
    ]

    problems = [
        ("MAJOR-01", "Escopo canônico incompleto", "A base utiliza quatro das sete abas sem contrato formal de inclusão ou exclusão.", "Criar um mapa de cobertura de todas as abas; incorporar SPEC FLUIDOS e EQUA-USN quando pertinentes ou justificar formalmente sua exclusão; documentar a ausência de K em SPEC FLUIDOS; completar o dicionário com descrição, tipo, origem e transformação."),
        ("MAJOR-02", "Separação numérico/textual incorreta", "750 observações aparecem ao mesmo tempo em value_numeric e value_text.", "Preencher value_numeric quando a conversão for válida; preencher value_text somente para conteúdo não convertível; preservar value_raw; regenerar os resumos e criar testes para números, textos, zeros e ausências."),
        ("MAJOR-03", "Auditoria de unidades incompleta", "396 registros sem unidade foram omitidos e unidades econômicas presentes nos rótulos não foram estruturadas.", "Manter UNKNOWN/TO_BE_CONFIRMED no resumo, extrair apenas unidades explicitamente declaradas nos rótulos e testar se toda observação aparece no inventário de unidades."),
        ("MAJOR-04", "CSV perde Unicode", "O RDS preserva acentos, mas o CSV contém sequências como n<U+00E3>o.", "Normalizar strings e gravar o CSV explicitamente em UTF-8; reler o arquivo e executar teste de round-trip comparando chaves, métricas, abas e valores textuais com o RDS."),
        ("MAJOR-05", "Reconciliação ainda aberta", "B, D e J possuem diferenças na soma de vida de ferramenta, mas a narrativa anterior não citava D.", "Rastrear cada parcela às células de origem, verificar transcrição ou arredondamento, manter precisão completa e documentar a fonte prevalente; se não houver evidência, bloquear a métrica para os casos afetados."),
        ("MAJOR-06", "ADA inicial insuficiente", "Faltam dispersão, quartis, amplitude, variáveis constantes, resumo por condição e candidatos a outlier.", "Adicionar DP, Q1, Q3, IQR, amplitude e CV quando aplicável; analisar por fluido e condição; identificar constantes e quase constantes; sinalizar outliers sem removê-los automaticamente."),
        ("MAJOR-07", "Cadernos e STATUS contraditórios", "Os QMDs ainda contêm DRAFT, NOT_EXECUTED e TO_BE_FILLED incompatíveis com a execução registrada.", "Transformar 01-05 em cadernos executáveis ou relatórios que consumam artefatos reais; remover estados obsoletos; alinhar STATUS, handoff e relatório e testar a inexistência de placeholders."),
        ("MAJOR-08", "Suíte de testes incompleta", "O teste de importação procura um arquivo inexistente e quatro arquivos de teste são apenas moldes.", "Corrigir a descoberta do XLSX sem renomear o bruto; implementar testes de soma, reconciliação, unidades, chaves, tipos, Unicode e estatísticas; executar e registrar a suíte Pacheco completa."),
        ("MINOR-01", "Uso de setwd()", "O script altera o diretório global e cria estado oculto.", "Manter project_root explícito, construir caminhos com file.path(project_root, ...) e testar a execução iniciada fora da raiz."),
        ("MINOR-02", "Dependência desnecessária de ggplot2", "O código testa ggplot2, mas a figura é produzida por gráficos base.", "Remover a checagem de ggplot2 ou gerar realmente com essa biblioteca; adicionar teste que confirme a criação do PNG."),
        ("MINOR-03", "Severidades não padronizadas", "O issue log usa HIGH/MEDIUM/INFO e o protocolo usa CRITICAL/MAJOR/MINOR/INFORMATIONAL.", "Adotar o vocabulário do protocolo, mapear registros antigos e validar automaticamente os níveis permitidos."),
    ]
    plan_html = "".join(
        f'''<article class="plan-card"><div class="problem-number">{number:02d}</div><div class="plan-body"><div class="plan-title"><span>{esc(code)}</span><h3>{esc(title)}</h3></div><p><b>Problema:</b> {esc(problem)}</p><p><b>Sugestão de solução:</b> {esc(solution)}</p></div></article>'''
        for number, (code, title, problem, solution) in enumerate(problems, start=1)
    )

    css = r'''
    :root{--navy:#17365d;--blue:#1677b8;--cyan:#42b7c6;--ink:#1e293b;--muted:#64748b;--paper:#fff;--bg:#eef3f7;--line:#d8e1e8;--danger:#b42318;--warn:#b54708;--ok:#027a48;--shadow:0 18px 50px rgba(23,54,93,.12)}
    *{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,"Segoe UI",Arial,sans-serif;line-height:1.62}
    a{color:var(--blue)}code{font-family:"Cascadia Code",Consolas,monospace;background:#edf2f7;border-radius:4px;padding:.08rem .28rem;font-size:.9em}
    .layout{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1600px;margin:auto}.sidebar{height:100vh;position:sticky;top:0;background:var(--navy);color:#fff;padding:28px 22px;overflow:auto}.brand{font-weight:800;font-size:1.05rem;line-height:1.25;margin-bottom:8px}.brand-sub{font-size:.78rem;color:#b9d4e7;margin-bottom:28px}.sidebar nav{display:grid;gap:3px}.sidebar a{color:#d8e8f3;text-decoration:none;padding:9px 12px;border-radius:8px;font-size:.84rem}.sidebar a:hover,.sidebar a.active{background:rgba(255,255,255,.12);color:#fff}.sidebar .pdf-link{margin-top:22px;border:1px solid rgba(255,255,255,.3);display:block;text-align:center}.content{min-width:0;padding:34px 46px 80px}.hero{background:linear-gradient(135deg,#17365d 0%,#1a5d86 62%,#168b9c 100%);color:#fff;border-radius:22px;padding:56px;box-shadow:var(--shadow);position:relative;overflow:hidden}.hero:after{content:"";position:absolute;width:320px;height:320px;border:55px solid rgba(255,255,255,.08);border-radius:50%;right:-100px;top:-130px}.kicker{text-transform:uppercase;letter-spacing:.13em;color:#aee9f0;font-weight:700;font-size:.78rem}.hero h1{font-size:clamp(2rem,4vw,3.65rem);line-height:1.05;max-width:900px;margin:12px 0 20px}.hero p{max-width:820px;color:#e2f1f6;font-size:1.08rem}.status-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.status-pill{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.25);padding:9px 14px;border-radius:999px;font-size:.82rem;font-weight:700}.status-pill.alert{background:#fff1e7;color:#8f3f00;border-color:#ffd2ae}
    .metric-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:24px 0}.metric{background:#fff;border-radius:15px;padding:22px;border:1px solid var(--line);box-shadow:0 8px 24px rgba(23,54,93,.06)}.metric strong{display:block;font-size:2rem;color:var(--navy);line-height:1}.metric span{display:block;color:var(--muted);font-size:.82rem;margin-top:8px}.report-section{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:32px;margin-top:24px;box-shadow:0 10px 30px rgba(23,54,93,.055);scroll-margin-top:20px}.section-heading span{font-size:.75rem;text-transform:uppercase;letter-spacing:.12em;color:var(--blue);font-weight:800}.section-heading h2{font-size:1.8rem;color:var(--navy);margin:4px 0 18px;line-height:1.2}.report-section h3{color:var(--navy);margin:1.5rem 0 .55rem}.report-section h4{color:#244f72}.lead{font-size:1.08rem;color:#334155}.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.why-card{border-left:4px solid var(--cyan);background:#f5fafc;padding:18px;border-radius:10px}.why-card strong{display:block;color:var(--navy);margin-bottom:5px}.timeline{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:24px 0}.step{background:#eef7fa;border-radius:12px;padding:16px 12px;text-align:center;font-size:.8rem}.step b{display:block;color:var(--blue);font-size:1.1rem;margin-bottom:5px}.callout{border-left:5px solid var(--blue);background:#edf7fb;padding:18px 20px;border-radius:8px;margin:20px 0}.callout.alert{border-color:var(--warn);background:#fff7ed}.table-scroll{overflow:auto;border:1px solid var(--line);border-radius:10px;margin:10px 0 22px}.table-tools{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:20px;color:var(--muted);font-size:.78rem}.table-tools input{border:1px solid var(--line);border-radius:8px;padding:8px 10px;width:min(300px,55vw)}table{width:100%;border-collapse:collapse;font-size:.76rem}th{background:var(--navy);color:#fff;text-align:left;position:sticky;top:0}th,td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}tbody tr:nth-child(even){background:#f7f9fb}tbody tr:hover{background:#eaf5fa}.chart-card{background:#fff;border:1px solid var(--line);border-radius:13px;padding:16px}.chart-card svg{width:100%;height:auto}.gridline{stroke:#dde5ea;stroke-width:1}.bar{fill:#3384b9;stroke:#17365d;stroke-width:1}.axis-label{font:12px "Segoe UI",Arial;fill:#475569}.bar-value{font:700 12px "Segoe UI",Arial;fill:#17365d}.issues{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}.issue-card{border:1px solid var(--line);border-top:5px solid var(--blue);border-radius:12px;padding:18px;background:#fff}.issue-card.high{border-top-color:var(--danger)}.issue-card.medium{border-top-color:var(--warn)}.issue-card.info{border-top-color:var(--blue)}.issue-card header{display:flex;justify-content:space-between;align-items:center}.issue-id{font-family:monospace;font-weight:700}.badge{font-size:.69rem;padding:4px 8px;border-radius:999px;font-weight:800}.badge.high{background:#fee4e2;color:#b42318}.badge.medium{background:#fef0c7;color:#93370d}.badge.info{background:#dbeafe;color:#1e40af}.issue-card h3{font-size:1rem}.issue-card dl{margin:0}.issue-card dl div{margin-top:9px}.issue-card dt{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);font-weight:700}.issue-card dd{margin:2px 0;font-size:.86rem}.review-banner{display:grid;grid-template-columns:auto 1fr;gap:18px;background:#fff7ed;border:1px solid #fed7aa;border-radius:13px;padding:20px;margin-bottom:20px}.review-banner strong{font-size:1.35rem;color:#9a3412}.review-content h2,.review-content h3,.review-content h4{scroll-margin-top:20px}.review-content pre,.code-file pre{background:#0f2034;color:#e5edf4;padding:18px;border-radius:10px;overflow:auto;font-size:.76rem;line-height:1.5}.review-content blockquote{border-left:4px solid var(--blue);margin:16px 0;padding:8px 18px;background:#f0f8fb}.code-file{border:1px solid var(--line);border-radius:12px;margin:10px 0;overflow:hidden}.code-file summary{cursor:pointer;display:flex;justify-content:space-between;padding:14px 16px;background:#f3f7fa;color:var(--navy);font-weight:800}.code-file summary small{color:var(--muted);font-weight:500}.code-file pre{margin:0;border-radius:0;max-height:650px}.empty{color:var(--muted);font-style:italic}.footer{color:var(--muted);text-align:center;padding:35px 10px;font-size:.78rem}
    .plan-list{display:grid;gap:18px}.plan-card{display:grid;grid-template-columns:72px 1fr;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff}.problem-number{background:linear-gradient(160deg,var(--navy),#236e98);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.45rem}.plan-body{padding:20px}.plan-title{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.plan-title span{font-size:.7rem;background:#fff0e2;color:#9a3412;padding:4px 8px;border-radius:999px;font-weight:800}.plan-title h3{margin:0}.plan-body p{margin:.65rem 0}
    @media(max-width:1050px){.layout{grid-template-columns:1fr}.sidebar{height:auto;position:relative}.sidebar nav{grid-template-columns:repeat(3,1fr)}.content{padding:24px}.metric-grid{grid-template-columns:repeat(2,1fr)}.timeline{grid-template-columns:repeat(2,1fr)}.why-grid{grid-template-columns:repeat(2,1fr)}}
    @media(max-width:650px){.sidebar nav{grid-template-columns:1fr 1fr}.content{padding:12px}.hero{padding:32px 24px;border-radius:14px}.report-section{padding:22px 16px}.metric-grid,.why-grid,.issues{grid-template-columns:1fr}.timeline{grid-template-columns:1fr}.table-tools{align-items:flex-start;flex-direction:column}.plan-card{grid-template-columns:1fr}.problem-number{padding:8px;place-items:start}}
    @media print{body{background:#fff}.layout{display:block}.sidebar{display:none}.content{padding:0}.hero,.report-section{box-shadow:none;break-inside:avoid}.report-section{border:none;border-radius:0}.code-file pre{max-height:none}.table-tools{display:none}}
    '''

    js = r'''
    function filterTable(id, query){const q=query.toLowerCase();document.querySelectorAll(`#${id} tbody tr`).forEach(row=>{row.hidden=!row.innerText.toLowerCase().includes(q)});}
    const links=[...document.querySelectorAll('.sidebar nav a')];const sections=links.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){links.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+entry.target.id));}})},{rootMargin:'-20% 0px -70% 0px'});sections.forEach(s=>observer.observe(s));
    document.querySelectorAll('.code-file').forEach((d,i)=>{if(i===0)d.open=true});
    '''

    document = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Relatório Pacheco + Revisão Boss</title><meta name="description" content="Relatório completo da etapa Pacheco: inventário, auditoria, reconciliação, base canônica, ADA inicial, código e revisão do AGENTE_BOSS."><style>{css}</style></head>
    <body><div class="layout"><aside class="sidebar"><div class="brand">Fluidos de Corte</div><div class="brand-sub">Etapa Pacheco + revisão metodológica</div><nav>
      <a href="#visao">Visão geral</a><a href="#importancia">Por que importa</a><a href="#metodo">Método</a><a href="#auditoria">Auditoria</a><a href="#resultados">Resultados</a><a href="#issues">Pendências</a><a href="#plano">Como resolver</a><a href="#boss">Parecer Boss</a><a href="#codigo">Código</a><a href="#apendices">Apêndices</a>
    </nav><a class="pdf-link" href="../pdf/relatorio_completo_pacheco_boss_v1.pdf">Abrir versão em PDF</a></aside><main class="content">
    <header class="hero" id="top"><div class="kicker">Relatório técnico completo · v1</div><h1>Do arquivo bruto à base auditável</h1><p>O que foi realizado pelo AGENTE_PACHECO, por que a etapa é essencial para o ranking multicritério, quais códigos tornam o trabalho reproduzível e o que o AGENTE_BOSS determinou antes do avanço para Benjamin.</p><div class="status-row"><span class="status-pill">Branch agente_pacheco</span><span class="status-pill">1.034 registros canônicos</span><span class="status-pill">11 fluidos</span><span class="status-pill alert">Boss: CHANGES_REQUESTED</span></div></header>
    <div class="metric-grid"><div class="metric"><strong>7</strong><span>abas inventariadas</span></div><div class="metric"><strong>1.034</strong><span>registros canônicos</span></div><div class="metric"><strong>15</strong><span>ausências preservadas</span></div><div class="metric"><strong>0</strong><span>duplicatas de origem</span></div></div>
    {section('visao','01 · Visão geral','O que foi feito',f'''<p class="lead">A etapa Pacheco transformou uma planilha com blocos heterogêneos em um conjunto auditável de evidências. O arquivo bruto permaneceu imutável e cada observação da base canônica pode ser rastreada até a aba e célula de origem.</p><div class="timeline"><div class="step"><b>01</b>Inventário</div><div class="step"><b>02</b>Auditoria</div><div class="step"><b>03</b>Reconciliação</div><div class="step"><b>04</b>Base canônica</div><div class="step"><b>05</b>ADA inicial</div></div><div class="callout alert"><strong>Estado atual:</strong> o AGENTE_BOSS solicitou mudanças. A base e o handoff não estão liberados para Benjamin até correção e nova revisão.</div>''')}
    {section('importancia','02 · Fundamento','Por que esta etapa é importante','''<div class="why-grid"><div class="why-card"><strong>Evita ranking sobre dados errados</strong>Erros upstream contaminariam critérios, pesos CRITIC, TOPSIS e análises de robustez.</div><div class="why-card"><strong>Preserva evidência</strong>Cada número mantém arquivo, aba, célula, unidade e contexto de origem.</div><div class="why-card"><strong>Separa ausência de zero</strong>Impedir que dados faltantes sejam convertidos em desempenho real evita conclusões falsas.</div><div class="why-card"><strong>Expõe divergências</strong>Somatórios e custos foram confrontados entre abas em vez de aceitos automaticamente.</div><div class="why-card"><strong>Torna a análise reproduzível</strong>O código R reconstrói a cópia, a base e os diagnósticos sem edição manual.</div><div class="why-card"><strong>Respeita responsabilidades</strong>Pacheco prepara e audita; Benjamin define critérios; Vitor ranqueia; Boss revisa.</div></div>''')}
    {section('metodo','03 · Método','Fonte, cópia e estrutura',f'''<h3>Arquivos de entrada</h3>{table_html(raw_inventory,table_id='raw-table')}<h3>Integridade da cópia</h3>{table_html(copy_check,table_id='copy-table')}<h3>Abas do XLSX</h3>{table_html(sheets,['sheet_index','sheet_name','rows_read','columns_read','non_blank_cells','provisional_header_row'],'sheet-table')}<div class="callout"><strong>Estratégia:</strong> como a planilha não é uma tabela retangular única, cada bloco foi extraído para formato longo, com representação original, numérica/textual e linhagem por célula.</div>''')}
    {section('auditoria','04 · Qualidade','Como os dados foram auditados',f'''<p>Foram verificados arquivos, abas, tipos aparentes, ausências, zeros explícitos, unidades, fórmulas OOXML, duplicidade de origem e consistência entre valores armazenados em abas diferentes.</p><h3>Ausências e zeros</h3>{table_html(missing,table_id='missing-table')}<h3>Unidades identificadas</h3>{table_html(units,table_id='unit-table')}''')}
    {section('resultados','05 · Resultados','O que a execução encontrou',f'''<div class="chart-card">{missingness_svg(missing)}</div><h3>Reconciliação entre abas</h3><p>O status distingue igualdade exata, equivalência de precisão de máquina, ausência de insumo e diferença que exige revisão porque a tolerância metodológica ainda não foi definida.</p>{table_html(reconciliation,table_id='reconciliation-table')}<h3>Estatísticas descritivas iniciais</h3>{table_html(numeric,table_id='numeric-table')}''')}
    {section('issues','06 · Pendências','Problemas preservados e ações requeridas',f'''<p>Nenhum destes itens foi corrigido silenciosamente. Eles permanecem visíveis até que a evidência seja obtida e a decisão seja documentada.</p><div class="issues">{''.join(issue_cards)}</div>''')}
    {section('plano','07 · Plano de correção','Como resolver cada problema',f'''<p class="lead">Os 11 itens abaixo transformam o parecer do Boss em uma sequência prática de trabalho, numerada para facilitar distribuição, acompanhamento e nova revisão.</p><div class="plan-list">{plan_html}</div>''')}
    {section('boss','08 · Revisão independente','Parecer do AGENTE_BOSS',f'''<div class="review-banner"><strong>CHANGES_REQUESTED</strong><div><b>0 críticos · 8 maiores · 3 menores · 4 informativos</b><br>A base canônica e o handoff não estão liberados para Benjamin. Pacheco deve corrigir os achados na origem e submeter uma nova versão.</div></div><div class="review-content">{markdown_to_html(review)}</div>''')}
    {section('codigo','09 · Reprodutibilidade','Código utilizado',f'''<p>Os arquivos abaixo implementam leitura, inventário, classificação de ausências, normalização de unidades, reconciliação, construção canônica, ADA inicial, orquestração e testes. Clique em cada arquivo para expandir.</p>{''.join(code_details(path) for path in code_files)}''')}
    {section('apendices','10 · Evidências','Dicionário, variáveis e handoff',f'''<details open><summary><b>Dicionário canônico</b></summary>{table_html(dictionary,table_id='dictionary-table')}</details><details><summary><b>Inventário completo de variáveis</b></summary>{table_html(variables,table_id='variables-table')}</details><details><summary><b>Handoff Pacheco → Benjamin</b></summary><div class="review-content">{markdown_to_html(handoff)}</div></details>''')}
    <footer class="footer">Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte · Relatório Pacheco v1 · Parecer Boss: CHANGES_REQUESTED</footer>
    </main></div><script>{js}</script></body></html>'''

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(document, encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    build_html()
