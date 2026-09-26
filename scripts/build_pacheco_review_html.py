"""Gera um relatório HTML autocontido da etapa Pacheco e da revisão Boss."""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "html" / "relatorio_completo_pacheco_boss_v2.html"


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
    later_numbers = {"impactos": 11, "abertos": 12, "boss": 13, "codigo": 14, "apendices": 15}
    if section_id in later_numbers:
        eyebrow = re.sub(r"^\d+", f"{later_numbers[section_id]:02d}", eyebrow)
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

    # Guia operacional: o parecer define os achados; os campos abaixo explicam
    # como investigá-los sem tomar decisões científicas que pertencem ao grupo.
    problems = [
        {
            "code": "MAJOR-01", "severity": "MAJOR", "title": "Escopo canônico incompleto e sem contrato de exclusão",
            "evidence": "O XLSX tem sete abas, mas source_sheet da base representa quatro. SPEC FLUIDOS contém composição/tipo; EQUA-USN contém parâmetros e memória de cálculo; CAVACOS também não tem decisão formal de escopo. O dicionário não registra descrição, tipo, origem detalhada e transformação completos. A ausência do fluido K em SPEC FLUIDOS deve ser explicada.",
            "risk": "Benjamin pode não receber uma variável potencialmente relevante, misturar especificações técnicas com medições experimentais ou interpretar uma ausência estrutural como dado faltante. Critérios definidos sobre uma cobertura incompleta podem deixar de fora dimensões importantes; a comparação posterior pode ficar enviesada ou impossível de reproduzir.",
            "steps": [
                "Monte uma matriz com uma linha para cada uma das sete abas e, dentro de abas com blocos diferentes, uma linha por bloco: finalidade, campos, unidade, fluido/condição cobertos, tipo de conteúdo (medição, especificação, cálculo auxiliar ou referência), decisão incluir/excluir e justificativa baseada na fonte.",
                "Inspecione SPEC FLUIDOS, EQUA-USN e CAVACOS diretamente na cópia de trabalho. Determine se os campos descrevem as alternativas medidas ou apenas contexto/metadados. Não inclua tudo automaticamente: registre o motivo técnico de cada inclusão ou exclusão e se a informação deve ser entregue como metadado separado.",
                "Investigue na fonte e nos materiais oficiais por que K não aparece em SPEC FLUIDOS. Até obter evidência, registre como lacuna/pendência; não complete por analogia com outros fluidos.",
                "Complete o dicionário: nome estável, descrição operacional, tipo, unidade original e canônica, domínio/valores possíveis, aba/célula ou regra de origem, transformação, significado de NA e restrições conhecidas. Preserve linhagem até a célula fonte.",
                "Atualize o inventário e o handoff com a matriz de cobertura e a decisão pendente ou resolvida. Mudança de escopo exige nova versão dos artefatos derivados."
            ],
            "technique": "Matriz de cobertura fonte→base; análise por blocos; dicionário de dados e linhagem; separação explícita entre variável medida, atributo do fluido e memória de cálculo. Não use o ranking futuro como critério para decidir inclusão.",
            "files": "R/pacheco/inventario.R; R/pacheco/base_canonica.R; results/audit/sheet_inventory_v1.csv; results/audit/variable_inventory_v1.csv; data/processed/dicionario_variaveis_v1.csv; analysis/01–04_PACHECO_*.qmd; handoffs/01_PACHECO_to_BENJAMIN.md",
            "acceptance": "Todas as sete abas e todos os blocos relevantes têm decisão rastreável; nenhuma aba técnica fica silenciosamente fora; a lacuna de K está explicada por fonte ou permanece marcada como pendente; cada coluna canônica tem definição, tipo, unidade, origem e transformação; Boss consegue reconstruir o escopo sem adivinhar.",
            "downstream": "Bloqueia a base canônica e o handoff (etapa 04→Benjamin 06–09). Se o escopo mudar, regenere inventários, base, ADA e handoff; resultados de Benjamin/Vitor já calculados sobre a base antiga devem ser avaliados como SUPERSEDED."
        },
        {
            "code": "MAJOR-02", "severity": "MAJOR", "title": "Valores numéricos também estão classificados como texto",
            "evidence": "A revisão independente encontrou 750 valores conversíveis armazenados ao mesmo tempo em value_numeric e value_text. Isso faz textual_values/missing_summary tratar números válidos como observações textuais e pode mascarar texto operacional como “repetir”.",
            "risk": "Resumos de texto e missing ficam errados; cálculos podem ignorar números ou contar a mesma observação em dois tipos; strings de controle podem escapar da auditoria e chegar como se fossem valores utilizáveis. Isso pode alterar a matriz que Benjamin recebe ou causar falha silenciosa em conversões downstream.",
            "steps": [
                "Preserve value_raw exatamente como lido da célula, sem sobrescrever a evidência original.",
                "Defina uma classificação mutuamente exclusiva para o valor interpretado: ausente; numérico convertido; texto não numérico; ou marcador/erro operacional conhecido. Converta somente quando a cadeia inteira corresponder a um número válido; não aceite conversões parciais que descartem letras/unidades.",
                "Trate separador decimal, espaços, sinal e unidade com regra explícita baseada no padrão da planilha. Não aplique conversão que transforme “repetir”, “-”, ou outro marcador em zero. Mantenha regra e valor bruto rastreáveis.",
                "Regenere value_numeric/value_text e os resumos dependentes. Confirme que a soma das categorias contabiliza cada registro exatamente uma vez e que os marcadores textuais continuam localizáveis."
            ],
            "technique": "Parser estrito com locale definido; classificação por resultado de conversão completo; tabela de decisão para valores ambíguos; testes unitários com número inteiro/decimal, decimal com vírgula, texto operacional, string vazia, NA e zero explícito.",
            "files": "R/pacheco/base_canonica.R; R/pacheco/missing.R; results/audit/missing_summary_v1.csv; results/eda/eda_numeric_summary_v1.csv; tests/testthat/test-pacheco-auditoria.R; handoffs/01_PACHECO_to_BENJAMIN.md",
            "acceptance": "value_numeric e value_text nunca são ambos preenchidos para o mesmo registro, salvo regra de representação claramente justificada; zero continua numérico e distinto de NA; “repetir” continua texto/issue; contagens fecham com 1.034 registros e os resumos não contam números como texto.",
            "downstream": "Bloqueia resumos e base para Benjamin. Se a classificação corrigida mudar valores numéricos, reexecute auditorias, reconciliações, base e ADA; qualquer critério, normalização, peso ou ranking posterior derivado da base antiga precisa ser refeito."
        },
        {
            "code": "MAJOR-03", "severity": "MAJOR", "title": "396 registros sem unidade desapareceram da auditoria de unidades",
            "evidence": "unit_summary_v1.csv contabiliza 638 de 1.034 observações. Em R, aggregate() remove grupos com NA nos campos de agrupamento; portanto, 396 registros com unit=NA não aparecem. Há unidades econômicas embutidas nos rótulos sem estrutura canônica.",
            "risk": "Uma variável pode ser comparada ou combinada com escala/unidade incompatível, gerar conversão incorreta ou aparentar unidade verificada quando parte dos dados foi omitida. Custos e medidas físicas podem contaminar normalização, conformidade, correlação e ranking.",
            "steps": [
                "Faça o inventário de unidades por registro/variável incluindo uma categoria explícita UNKNOWN ou TO_BE_CONFIRMED. Não deixe NA desaparecer no agrupamento; reporte separadamente quantos registros têm unidade confirmada, desconhecida e não aplicável.",
                "Estruture unidade embutida em rótulo econômico somente quando o texto da fonte a declarar inequivocamente. Guarde o rótulo original e a unidade extraída para auditoria.",
                "Separe unit_original de unit_canonical. Normalize símbolos/sinônimos documentados; conversão física só com fator dimensionalmente válido e regra/decisão registrada. Se a unidade não puder ser inferida, não invente.",
                "Reconcilie a cobertura do resumo: a soma de observações por categoria deve dar 1.034, com 638 confirmadas e 396 explicitamente desconhecidas até evidência em contrário. Verifique se os agrupamentos preservam missing e métricas com diferentes unidades."
            ],
            "technique": "Auditoria de cobertura com contagem de NA; chave por domínio+métrica+unidade original/canônica; validação de dimensão física; tabela de mapeamento de unidades e testes de soma de contagens. Não converter unidade apenas para fazer valores parecerem comparáveis.",
            "files": "R/pacheco/unidades.R; R/pacheco/base_canonica.R; results/audit/unit_summary_v1.csv; data/processed/dicionario_variaveis_v1.csv; tests/testthat/test-unidades.R; analysis/02_PACHECO_auditoria.qmd",
            "acceptance": "A auditoria contabiliza todos os 1.034 registros; unidades desconhecidas aparecem explicitamente; campos econômicos têm unidade estruturada apenas com evidência; nenhuma comparação entre unidades incompatíveis é liberada silenciosamente.",
            "downstream": "Bloqueia comparações de critérios/unidades em Benjamin e pode invalidar conformidade e normalização. Mudança de unidade afeta ADA, matriz de decisão, correlações, pesos e ranking: regenere os outputs downstream afetados."
        },
        {
            "code": "MAJOR-04", "severity": "MAJOR", "title": "O CSV perde caracteres Unicode e diverge do RDS",
            "evidence": "A revisão encontrou RDS com UTF-8 correto e CSV com texto corrompido, por exemplo “não” aparecendo como n<U+00E3>o. O problema alcança nomes de métricas, abas e valores textuais.",
            "risk": "Chaves, filtros e junções por fluido/métrica podem falhar por comparação de strings diferentes; relatórios podem exibir texto ilegível; o CSV deixa de ser uma representação intercambiável do RDS e pode produzir resultados diferentes em outra ferramenta/sistema operacional.",
            "steps": [
                "Escolha e documente uma codificação de intercâmbio (UTF-8) para todos os CSVs textuais, não apenas para a base canônica.",
                "Grave explicitamente em UTF-8 com uma rotina compatível com o ambiente R/Windows. Preserve acentos; evite substituir texto por escape literal ou corrigir manualmente o arquivo exportado.",
                "Leia o CSV recém-gerado novamente com codificação declarada e compare com o objeto RDS em colunas-chave, nomes de abas/métricas, unidades, value_raw/value_text e linhagem. Ao ler CSV, declare tipos ou valide-os para não reintroduzir coerção ambígua.",
                "Adicione testes round-trip com exemplos contendo ã, ç, µ, ° e texto operacional. Gere todos os relatórios derivados depois da correção."
            ],
            "technique": "Round-trip de serialização: objeto RDS→CSV UTF-8→leitura tipada→comparação de campos; teste de bytes/encoding para acentos e símbolos de unidade. Verifique saída em uma ferramenta consumidora além do R.",
            "files": "scripts/run_audit.R (exportação da base e artefatos); data/processed/base_canonica_v1.csv; results/audit/*.csv; tests/testthat/test-importacao.R ou teste específico de exportação; handoffs/01_PACHECO_to_BENJAMIN.md",
            "acceptance": "A leitura de volta preserva os campos textuais e identificadores; RDS e CSV representam os mesmos registros/valores; nenhuma sequência mojibake permanece; o teste passa no ambiente Windows utilizado e a codificação é declarada no handoff.",
            "downstream": "Bloqueia o CSV como entrada de Benjamin. Se qualquer agente usou CSV/RDS v1 e strings corrompidas afetaram junções/identificadores, reexecute a partir da importação e avalie todas as etapas dependentes."
        },
        {
            "code": "MAJOR-05", "severity": "MAJOR", "title": "Reconciliação da soma de vida de ferramenta continua sem decisão",
            "evidence": "A soma diverge nos fluidos B (diferença reportada 72,3456), D (-0,0002) e J (-0,0432); os três estão REVIEW_REQUIRED_TOLERANCE_UNDEFINED. A narrativa anterior omitia D. config/tolerancias.yml não autoriza classificar essas diferenças como aceitáveis.",
            "risk": "O valor escolhido pode alterar a medida de desempenho e qualquer análise por fluido. Arredondamento prematuro ou tolerância inventada pode esconder erro de transcrição, unidade, número de repetições ou cálculo; uma decisão inconsistente contamina a matriz de Benjamin e, depois, o ranking e sua robustez.",
            "steps": [
                "Crie uma linha de investigação por B, D e J: abas/células de cada parcela, componentes, fórmula documentada, unidade, precisão exibida, número de medições e valor derivado armazenado.",
                "Recalcule cada soma independentemente dos valores fonte em precisão completa; confira se os componentes estão alinhados à mesma condição e se não há parcela repetida, omitida ou com unidade diferente. Preserve valores originais.",
                "Consulte a regra oficial/material da professora e config/tolerancias.yml. Não transforme a diferença pequena de D/J em aprovação automática e não selecione a fonte que favoreça um fluido.",
                "Registre a decisão e evidência por caso. Se a origem continuar ambígua, use PENDING_EXTERNAL_CONFIRMATION ou REVIEW_REQUIRED e bloqueie somente o campo/fluido afetado, com instrução explícita ao Benjamin. Inclua os três casos em relatório, issue log e handoff."
            ],
            "technique": "Reconciliação parcela a parcela com tabela de auditoria; cálculo independente; diferença absoluta e relativa com denominador/referência declarados; teste de soma com componentes conhecidos. A tolerância só pode vir de regra aprovada, nunca do resultado desejado.",
            "files": "R/pacheco/reconciliacao.R; R/pacheco/formulas.R; config/tolerancias.yml; results/audit/reconciliation_checks_v1.csv; tests/testthat/test-reconciliacao.R; tests/testthat/test-somas.R; analysis/03_PACHECO_reconciliacao.qmd; handoff e relatório Pacheco",
            "acceptance": "B, D e J aparecem em todos os documentos; cada um termina com resultado apoiado por evidência/regra aprovada ou permanece explicitamente bloqueado; nenhum status REVIEW_REQUIRED é apresentado como reconciliado; precision full é mantida até a apresentação.",
            "downstream": "A métrica de vida de ferramenta para os casos em aberto não pode ser tratada como pronta. Se a correção mudar um valor já consumido, reexecute Benjamin e Vitor; marque outputs construídos sobre a base antiga como SUPERSEDED após avaliação do Boss."
        },
        {
            "code": "MAJOR-06", "severity": "MAJOR", "title": "ADA inicial não cobre os diagnósticos exigidos",
            "evidence": "eda_numeric_summary_v1.csv traz n, mínimo, mediana, média e máximo. Faltam desvio-padrão, quartis, amplitude, variáveis constantes/quase constantes, resumo por condição e candidatos a outlier; o artefato de outlier está em NOT_ASSESSED_TOLERANCE_UNDEFINED.",
            "risk": "Dispersão ou assimetria pode ficar oculta; condições experimentais distintas podem ser agregadas indevidamente; variáveis sem variação podem entrar em análises multivariadas; valores extremos podem dominar correlação/normalização. Benjamin teria de inferir ou recalcular diagnósticos que deveriam vir com o handoff.",
            "steps": [
                "Estenda o resumo por domínio+métrica+unidade e, quando aplicável, fluido+condição: n válido, missing, média, mediana, desvio-padrão, Q1, Q3, IQR, mínimo, máximo, amplitude e CV apenas quando a média permitir interpretação. Documente convenção de quartis e comportamento para n pequeno.",
                "Identifique constantes por número de valores únicos e quase constantes por regra quantitativa declarada; não escolha limiar depois de ver qual fluido vence. Entregue a lista ao Benjamin sem excluir variáveis.",
                "Gere dotplots/boxplots ou histogramas apropriados ao n e à escala, com observações individuais quando houver poucos pontos. Um método descritivo como cerca de Tukey (1,5×IQR) pode marcar candidatos, mas não prova erro.",
                "Para cada candidato, confira a célula fonte, unidade, condição e possibilidade de erro. Mantenha valor original; não remova, winsorize ou impute automaticamente. Registre influência potencial e status de investigação.",
                "Mantenha ADA exploratória: não escolha critérios, pesos, exclusões nem vencedor; correlação nesta etapa é exploratória e não substitui a etapa Benjamin."
            ],
            "technique": "Resumo robusto com quantis; análise estratificada por condição; dotplot/boxplot; detecção descritiva de candidatos a outlier e checagem de influência sem exclusão automática; contagem de valores únicos para constantes.",
            "files": "R/pacheco/ada_inicial.R; results/eda/eda_numeric_summary_v1.csv; results/audit/outlier_assessment_v1.csv; tests/testthat/test-medias.R; analysis/05_PACHECO_ada_inicial.qmd; handoff 01",
            "acceptance": "Estatísticas e n/missing são reproduzíveis; estratos/condições não foram colapsados sem justificativa; constantes e quase constantes são listadas; candidatos a outlier têm fonte e status; relatório e handoff interpretam limitações sem afirmar causalidade nem ranking.",
            "downstream": "Benjamin precisa dos diagnósticos antes de avaliar redundância, conformidade e critérios. Mudanças em tipagem, unidade ou reconciliação exigem regenerar a ADA antes de qualquer correlação/matriz de decisão."
        },
        {
            "code": "MAJOR-07", "severity": "MAJOR", "title": "QMDs, STATUS e execução dizem coisas diferentes",
            "evidence": "Os QMDs 01–05 mantêm marcadores de molde como DRAFT, NOT_EXECUTED e TO_BE_FILLED embora existam outputs da execução. STATUS.md marca Pacheco pronto para revisão, mas também descreve inventário/auditoria/ADA como não executados. O handoff não reporta toda a tipagem, Unicode, escopo e caso D.",
            "risk": "Outro integrante não sabe qual arquivo/versão é autoridade, pode consumir um resultado antigo ou presumir que uma análise foi executada quando só há template. Decisões não documentadas reaparecem nas etapas seguintes e a revisão não consegue reproduzir a cadeia de evidências.",
            "steps": [
                "Faça uma tabela de verdade por etapa 01–05: execução real, comando, input/hash, versão de output, validação, limitações, estado Boss. Compare analysis/, report/stages/01_pacheco/, STATUS.md, issue log e handoff.",
                "Para cada QMD, escolha explicitamente: (a) caderno executável que chama o código versionado e renderiza resultados reais; ou (b) relatório que importa os artefatos da versão identificada. Não mantenha texto de template como se fosse resultado.",
                "Remova/substitua DRAFT/NOT_EXECUTED/TO_BE_FILLED somente depois de produzir evidência executada. Não declare APPROVED: o status de aprovação pertence ao Boss após nova revisão.",
                "Atualize handoff com arquivo e hash/versão a consumir, unidades desconhecidas, questões abertas e campos bloqueados, constantes/outliers/condições, falhas de CSV e reconciliações. Declare inelegível para downstream até aprovação.",
                "Renderize os cinco QMDs ou valide que os relatórios apontam para outputs existentes da mesma versão. Use busca automatizada por placeholders e verificação de consistência de status antes do handoff."
            ],
            "technique": "Matriz de rastreabilidade etapa→código→output→relatório→handoff; validação automática de placeholders/status; execução limpa a partir da raiz e render dos QMDs; registro de input/output hashes e versão.",
            "files": "analysis/01–05_PACHECO_*.qmd; report/stages/01_pacheco/; STATUS.md; report/stages/01_pacheco/EXECUCAO_PACHECO_v1.md; handoffs/01_PACHECO_to_BENJAMIN.md; results/audit/",
            "acceptance": "Todos os artefatos contam a mesma história e referem a mesma versão; QMDs executam/renderizam ou declaram claramente que consomem outputs; nenhum placeholder contradiz evidência; handoff segue NOT_RELEASED/READY_FOR_BOSS_REVIEW até decisão de Boss.",
            "downstream": "Sem handoff inequívoco, Benjamin pode usar arquivo errado ou ignorar limitações. Qualquer atualização da base exige novo handoff e avaliação/possível SUPERSEDED dos resultados das etapas 06–12 e de comunicação."
        },
        {
            "code": "MAJOR-08", "severity": "MAJOR", "title": "A suíte Pacheco falha e não protege propriedades científicas",
            "evidence": "test-importacao.R procura data/raw/ensaio_bancada_alunos.xlsx, enquanto o arquivo auditado tem sufixo (2); o teste falha. test-medias.R, test-reconciliacao.R, test-somas.R e test-unidades.R são moldes vazios. O Boss só confirmou três testes de auditoria isoladamente, não a suíte completa.",
            "risk": "Uma mudança pode apagar ausências, converter texto em zero, quebrar chave/linhagem, omitir unidades ou reproduzir uma soma/média errada sem detecção. Um “teste aprovado” parcial pode dar falsa segurança e deixar bug entrar em critérios e ranking.",
            "steps": [
                "Corrija a descoberta do XLSX sem renomear ou editar data/raw. Para teste unitário, use fixture controlada em diretório temporário; para integração, localize o arquivo por extensão/convenção documentada e valide que há exatamente uma fonte esperada.",
                "Implemente testes de leitura/estrutura e hash; chave lógica única e linhagem; classificação mutuamente exclusiva numérico/texto; distinção NA versus zero; cobertura de unidade total; round-trip UTF-8; somas e médias recalculadas; reconciliações que permanecem bloqueadas sem tolerância; determinismo da base.",
                "Inclua testes de borda: input vazio/ausente, duplicata, número com vírgula, marcador “repetir”, unidade desconhecida, grupo com n pequeno, coluna constante e CSV com acentos/símbolos.",
                "Execute o conjunto Pacheco completo no ambiente declarado (não apenas um arquivo de teste), corrija todas as falhas e registre comando, versão R/pacotes e resumo de testes. Não esconda testes com skip ou altere esperado para combinar com resultado sem evidência."
            ],
            "technique": "testthat com fixtures pequenas e determinísticas; testes de propriedades/invariantes; teste de integração contra cópia imutável; comparação round-trip e golden checks apenas quando a fonte/decisão estiver congelada.",
            "files": "tests/testthat/test-importacao.R; test-medias.R; test-reconciliacao.R; test-somas.R; test-unidades.R; test-pacheco-auditoria.R; R/pacheco/; scripts/run_audit.R; renv.lock",
            "acceptance": "Todos os testes relevantes da etapa Pacheco executam no comando documentado e passam; falhas e skips estão justificados; raw permanece intacto; invariantes e casos abertos são testados para falhar de modo explícito, não serem aceitos como válidos.",
            "downstream": "Sem validação automatizada não há base confiável para liberar. Após correção de código, regenere outputs; o Boss revisa novo conjunto; somente então o handoff pode avançar."
        },
        {
            "code": "MINOR-01", "severity": "MINOR", "title": "setwd() cria dependência do diretório global",
            "evidence": "scripts/run_audit.R altera o diretório de trabalho com setwd(project_root), então sucesso depende de estado global e pode interferir em quem chama o script ou em execuções encadeadas.",
            "risk": "Execuções iniciadas de outra pasta, testes, Quarto ou pipeline podem ler/escrever em locais inesperados. Uma execução parcial pode deixar arquivos em diretório incorreto sem erro claro.",
            "steps": [
                "Mantenha project_root explícito e construa caminhos de entrada/saída com file.path(project_root, ...). Faça source() dos scripts usando o caminho absoluto/raiz resolvida, e não assuma que o processo começou na raiz.",
                "Remova setwd() e teste a execução iniciada a partir de uma pasta temporária fora do projeto. Confirme que todos os outputs foram para os caminhos esperados sob a raiz e que o diretório original do processo não mudou."
            ],
            "technique": "Paths ancorados na raiz detectada ou helper padrão do projeto; teste de integração com cwd externo; não introduza dependência nova se a raiz já puder ser encontrada com segurança.",
            "files": "scripts/run_audit.R; R/pacheco/importacao.R; tests/testthat/test-importacao.R",
            "acceptance": "A auditoria roda da raiz e de fora dela sem setwd, resolve inputs relativos ao projeto e escreve somente nos destinos definidos.",
            "downstream": "Não é achado científico, mas pode tornar a reconstrução de qualquer resultado não reprodutível. Afeta regeneração/CI e passa a ser prioritário se execução fora da raiz falhar."
        },
        {
            "code": "MINOR-02", "severity": "MINOR", "title": "A geração da figura está condicionada a uma biblioteca que não usa",
            "evidence": "scripts/run_audit.R verifica requireNamespace('ggplot2'), mas a figura é construída com graphics::barplot; logo a ausência de ggplot2 suprime um PNG que não depende dela.",
            "risk": "A figura de ausência pode sumir em outra instalação apesar de os dados estarem disponíveis, deixando relatório/ADA incompleto e diferenças entre ambientes sem motivo científico.",
            "steps": [
                "Escolha uma implementação: mantenha o gráfico base e remova o if de disponibilidade do ggplot2; ou passe a gerar realmente com ggplot2 e declare a dependência no ambiente.",
                "Garanta fechamento do dispositivo gráfico mesmo se ocorrer erro. Após execução, confirme existência, tamanho não nulo, rótulos e dados representados; teste a rotina sem depender de pacote não usado."
            ],
            "technique": "Geração determinística com graphics base ou dependência explicitamente declarada; teste de artefato (arquivo existe, tamanho > 0) e conferência de taxas/numeradores do gráfico.",
            "files": "scripts/run_audit.R; results/eda/fig_missingness_v1.png; tests/testthat/; renv.lock se ggplot2 permanecer necessário",
            "acceptance": "A mesma figura é produzida consistentemente em ambiente limpo e sua dependência corresponde à implementação utilizada; arquivo é verificável e vinculado à mesma versão dos dados.",
            "downstream": "Pode deixar o relatório e a interpretação de missing sem figura ou variar por ambiente. Não altera números por si só, mas precisa ser corrigido antes da documentação final se a figura for citada."
        },
        {
            "code": "MINOR-03", "severity": "MINOR", "title": "Severidades do issue log não usam o vocabulário do protocolo",
            "evidence": "issue_log_v1.csv usa HIGH, MEDIUM e INFO; AGENTS.md e protocolo Boss usam CRITICAL, MAJOR, MINOR e INFORMATIONAL. O issue log está sendo criado no script da auditoria com níveis misturados.",
            "risk": "Filtros/contagens podem classificar o mesmo risco de formas diferentes, problemas importantes podem ser rebaixados ou omitidos e as equipes podem discordar sobre o que bloqueia handoff.",
            "steps": [
                "Defina a taxonomia oficial e o significado de cada nível a partir do REVIEW_PROTOCOL.md. Revise cada issue individualmente com evidência; não faça substituição em massa automática de HIGH/MEDIUM sem validar a severidade real.",
                "Padronize os valores gerados no issue log, documente o mapeamento histórico e valide por enumeração permitida. Faça relatório/handoff consumirem a mesma taxonomia."
            ],
            "technique": "Enum/validação de domínio para severity; tabela de migração auditável; teste que rejeita nível fora do conjunto permitido; revisão humana de severidade junto ao status/impacto.",
            "files": "scripts/run_audit.R; results/audit/issue_log_v1.csv; agents/REVIEW_PROTOCOL.md; AGENTS.md; reviews/BOSS_REVIEW_PACHECO_v1.md",
            "acceptance": "Issues novas usam apenas níveis do protocolo; cada issue anterior tem classificação revisada e rastreável; contagem e bloqueio no relatório batem com o issue log e o parecer.",
            "downstream": "Pode fazer um bloqueio passar despercebido ou a equipe priorizar incorretamente. Não muda por si só valores numéricos, mas afeta triagem e a decisão formal de liberação para Benjamin."
        },
    ]

    def problem_card(number: int, problem: dict[str, object]) -> str:
        steps_html = "".join(f"<li>{esc(step)}</li>" for step in problem["steps"])
        return f'''<article id="problema-{number:02d}" class="plan-card detailed-plan"><div class="problem-number">{number:02d}</div><div class="plan-body">
          <div class="plan-title"><span>{esc(problem['code'])} · {esc(problem['severity'])}</span><h3>{esc(problem['title'])}</h3></div>
          <div class="plan-field evidence"><h4>O problema e a evidência</h4><p>{esc(problem['evidence'])}</p></div>
          <div class="plan-field risk"><h4>O que pode acontecer se não resolver</h4><p>{esc(problem['risk'])}</p></div>
          <div class="plan-field steps"><h4>O que Pacheco pode fazer, passo a passo</h4><ol>{steps_html}</ol></div>
          <div class="plan-field"><h4>Técnicas úteis</h4><p>{esc(problem['technique'])}</p></div>
          <div class="plan-field"><h4>Arquivos a conferir/atualizar</h4><p><code>{esc(problem['files'])}</code></p></div>
          <div class="plan-field acceptance"><h4>Como saber que ficou resolvido</h4><p>{esc(problem['acceptance'])}</p></div>
          <div class="plan-field downstream"><h4>Impacto e reprocessamento das próximas etapas</h4><p>{esc(problem['downstream'])}</p></div>
        </div></article>'''

    by_code = {problem["code"]: problem for problem in problems}
    group_specs = [
        ("base", "Problemas com a base e com os dados", "MAJOR-01 MAJOR-02 MAJOR-03 MAJOR-05 MAJOR-06".split(),
         "Escopo, representação de valores, unidades, reconciliação e diagnóstico inicial. Primeiro confirme a fonte; depois corrija regras e regenere os dados derivados."),
        ("codigo", "Problemas com o código e a execução", "MAJOR-04 MAJOR-08 MINOR-01 MINOR-02".split(),
         "Exportação, testes e execução reproduzível. Essas falhas podem produzir arquivos divergentes ou impedir que outra pessoa repita a análise."),
        ("arquitetura", "Problemas de arquitetura, documentação e governança", "MAJOR-07 MINOR-03".split(),
         "Estados contraditórios, handoff e vocabulário de severidade. Corrija a comunicação da versão e o controle de aprovação antes de liberar qualquer consumidor."),
    ]
    group_html: dict[str, str] = {}
    problem_number = 0
    for group_id, title, codes, intro in group_specs:
        cards = []
        for code in codes:
            problem_number += 1
            cards.append(problem_card(problem_number, by_code[code]))
        group_html[group_id] = f'''<p class="lead">{esc(intro)}</p><div class="group-count">{len(codes)} achados do parecer do Boss</div><div class="plan-list">{''.join(cards)}</div>'''
    if problem_number != len(problems) or set(by_code) != {code for _, _, codes, _ in group_specs for code in codes}:
        raise ValueError("A classificação deve cobrir cada achado exatamente uma vez.")

    css = r'''
    :root{--navy:#17365d;--blue:#1677b8;--cyan:#42b7c6;--ink:#1e293b;--muted:#64748b;--paper:#fff;--bg:#eef3f7;--line:#d8e1e8;--danger:#b42318;--warn:#b54708;--ok:#027a48;--shadow:0 18px 50px rgba(23,54,93,.12)}
    *{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,"Segoe UI",Arial,sans-serif;line-height:1.62}
    a{color:var(--blue)}code{font-family:"Cascadia Code",Consolas,monospace;background:#edf2f7;border-radius:4px;padding:.08rem .28rem;font-size:.9em}
    .layout{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1600px;margin:auto}.sidebar{height:100vh;position:sticky;top:0;background:var(--navy);color:#fff;padding:28px 22px;overflow:auto}.brand{font-weight:800;font-size:1.05rem;line-height:1.25;margin-bottom:8px}.brand-sub{font-size:.78rem;color:#b9d4e7;margin-bottom:28px}.sidebar nav{display:grid;gap:3px}.sidebar a{color:#d8e8f3;text-decoration:none;padding:9px 12px;border-radius:8px;font-size:.84rem}.sidebar a:hover,.sidebar a.active{background:rgba(255,255,255,.12);color:#fff}.sidebar .pdf-link{margin-top:22px;border:1px solid rgba(255,255,255,.3);display:block;text-align:center}.content{min-width:0;padding:34px 46px 80px}.hero{background:linear-gradient(135deg,#17365d 0%,#1a5d86 62%,#168b9c 100%);color:#fff;border-radius:22px;padding:56px;box-shadow:var(--shadow);position:relative;overflow:hidden}.hero:after{content:"";position:absolute;width:320px;height:320px;border:55px solid rgba(255,255,255,.08);border-radius:50%;right:-100px;top:-130px}.kicker{text-transform:uppercase;letter-spacing:.13em;color:#aee9f0;font-weight:700;font-size:.78rem}.hero h1{font-size:clamp(2rem,4vw,3.65rem);line-height:1.05;max-width:900px;margin:12px 0 20px}.hero p{max-width:820px;color:#e2f1f6;font-size:1.08rem}.status-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.status-pill{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.25);padding:9px 14px;border-radius:999px;font-size:.82rem;font-weight:700}.status-pill.alert{background:#fff1e7;color:#8f3f00;border-color:#ffd2ae}
    .metric-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:24px 0}.metric{background:#fff;border-radius:15px;padding:22px;border:1px solid var(--line);box-shadow:0 8px 24px rgba(23,54,93,.06)}.metric strong{display:block;font-size:2rem;color:var(--navy);line-height:1}.metric span{display:block;color:var(--muted);font-size:.82rem;margin-top:8px}.report-section{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:32px;margin-top:24px;box-shadow:0 10px 30px rgba(23,54,93,.055);scroll-margin-top:20px}.section-heading span{font-size:.75rem;text-transform:uppercase;letter-spacing:.12em;color:var(--blue);font-weight:800}.section-heading h2{font-size:1.8rem;color:var(--navy);margin:4px 0 18px;line-height:1.2}.report-section h3{color:var(--navy);margin:1.5rem 0 .55rem}.report-section h4{color:#244f72}.lead{font-size:1.08rem;color:#334155}.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.why-card{border-left:4px solid var(--cyan);background:#f5fafc;padding:18px;border-radius:10px}.why-card strong{display:block;color:var(--navy);margin-bottom:5px}.timeline{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:24px 0}.step{background:#eef7fa;border-radius:12px;padding:16px 12px;text-align:center;font-size:.8rem}.step b{display:block;color:var(--blue);font-size:1.1rem;margin-bottom:5px}.callout{border-left:5px solid var(--blue);background:#edf7fb;padding:18px 20px;border-radius:8px;margin:20px 0}.callout.alert{border-color:var(--warn);background:#fff7ed}.table-scroll{overflow:auto;border:1px solid var(--line);border-radius:10px;margin:10px 0 22px}.table-tools{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:20px;color:var(--muted);font-size:.78rem}.table-tools input{border:1px solid var(--line);border-radius:8px;padding:8px 10px;width:min(300px,55vw)}table{width:100%;border-collapse:collapse;font-size:.76rem}th{background:var(--navy);color:#fff;text-align:left;position:sticky;top:0}th,td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}tbody tr:nth-child(even){background:#f7f9fb}tbody tr:hover{background:#eaf5fa}.chart-card{background:#fff;border:1px solid var(--line);border-radius:13px;padding:16px}.chart-card svg{width:100%;height:auto}.gridline{stroke:#dde5ea;stroke-width:1}.bar{fill:#3384b9;stroke:#17365d;stroke-width:1}.axis-label{font:12px "Segoe UI",Arial;fill:#475569}.bar-value{font:700 12px "Segoe UI",Arial;fill:#17365d}.issues{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}.issue-card{border:1px solid var(--line);border-top:5px solid var(--blue);border-radius:12px;padding:18px;background:#fff}.issue-card.high{border-top-color:var(--danger)}.issue-card.medium{border-top-color:var(--warn)}.issue-card.info{border-top-color:var(--blue)}.issue-card header{display:flex;justify-content:space-between;align-items:center}.issue-id{font-family:monospace;font-weight:700}.badge{font-size:.69rem;padding:4px 8px;border-radius:999px;font-weight:800}.badge.high{background:#fee4e2;color:#b42318}.badge.medium{background:#fef0c7;color:#93370d}.badge.info{background:#dbeafe;color:#1e40af}.issue-card h3{font-size:1rem}.issue-card dl{margin:0}.issue-card dl div{margin-top:9px}.issue-card dt{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);font-weight:700}.issue-card dd{margin:2px 0;font-size:.86rem}.review-banner{display:grid;grid-template-columns:auto 1fr;gap:18px;background:#fff7ed;border:1px solid #fed7aa;border-radius:13px;padding:20px;margin-bottom:20px}.review-banner strong{font-size:1.35rem;color:#9a3412}.review-content h2,.review-content h3,.review-content h4{scroll-margin-top:20px}.review-content pre,.code-file pre{background:#0f2034;color:#e5edf4;padding:18px;border-radius:10px;overflow:auto;font-size:.76rem;line-height:1.5}.review-content blockquote{border-left:4px solid var(--blue);margin:16px 0;padding:8px 18px;background:#f0f8fb}.code-file{border:1px solid var(--line);border-radius:12px;margin:10px 0;overflow:hidden}.code-file summary{cursor:pointer;display:flex;justify-content:space-between;padding:14px 16px;background:#f3f7fa;color:var(--navy);font-weight:800}.code-file summary small{color:var(--muted);font-weight:500}.code-file pre{margin:0;border-radius:0;max-height:650px}.empty{color:var(--muted);font-style:italic}.footer{color:var(--muted);text-align:center;padding:35px 10px;font-size:.78rem}
    .plan-list{display:grid;gap:18px}.plan-card{display:grid;grid-template-columns:72px 1fr;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;scroll-margin-top:20px}.problem-number{background:linear-gradient(160deg,var(--navy),#236e98);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.45rem}.plan-body{padding:20px}.plan-title{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}.plan-title span{font-size:.7rem;background:#fff0e2;color:#9a3412;padding:4px 8px;border-radius:999px;font-weight:800}.plan-title h3{margin:0}.plan-body p{margin:.45rem 0}.plan-field{padding:13px 16px;margin:10px 0;border-radius:9px;background:#f5f8fa}.plan-field h4{margin:0 0 4px;color:var(--navy);font-size:.9rem}.plan-field p,.plan-field li{font-size:.9rem}.plan-field ol{margin:.4rem 0;padding-left:1.5rem}.plan-field li{padding:3px 0}.plan-field.evidence{border-left:4px solid var(--blue)}.plan-field.risk{border-left:4px solid var(--danger);background:#fff5f4}.plan-field.steps{border-left:4px solid var(--cyan);background:#f1fbfc}.plan-field.acceptance{border-left:4px solid var(--ok);background:#f0faf5}.plan-field.downstream{border-left:4px solid var(--warn);background:#fff8ed}.category-index{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:20px 0}.category-index a{border:1px solid var(--line);background:#f5f9fc;padding:18px;border-radius:12px;text-decoration:none;color:var(--navy);font-weight:800}.category-index a:hover{background:#e9f4f9}.category-index small{display:block;color:var(--muted);font-weight:500;margin-top:5px}.group-count{display:inline-block;font-size:.8rem;color:#475569;background:#eaf2f7;border-radius:999px;padding:5px 12px;margin:4px 0 18px}.pipeline{display:grid;grid-template-columns:repeat(5,minmax(150px,1fr));gap:28px;align-items:stretch;margin:22px 0;overflow-x:auto;padding:5px 2px 12px}.pipeline-node{position:relative;background:#f1f7fa;border:1px solid var(--line);border-radius:12px;padding:16px;min-width:145px}.pipeline-node:not(:last-child):after{content:'➜';position:absolute;right:-24px;top:40%;font-size:1.25rem;color:var(--blue);font-weight:800}.pipeline-node b{display:block;color:var(--navy);font-size:.95rem}.pipeline-node small{display:block;color:var(--muted);margin-top:5px}.pipeline-node.gate{border:2px solid var(--warn);background:#fff8ed}.guardrails{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.guardrail{padding:14px;border-radius:10px;background:#f4f8fb;border:1px solid var(--line)}.guardrail b{display:block;color:var(--navy)}.minor-plan .problem-number{background:linear-gradient(160deg,#596b7d,#8094a5)}
    @media(max-width:1050px){.layout{grid-template-columns:1fr}.sidebar{height:auto;position:relative}.sidebar nav{grid-template-columns:repeat(3,1fr)}.content{padding:24px}.metric-grid{grid-template-columns:repeat(2,1fr)}.timeline{grid-template-columns:repeat(2,1fr)}.why-grid{grid-template-columns:repeat(2,1fr)}}
    @media(max-width:650px){.sidebar nav{grid-template-columns:1fr 1fr}.content{padding:12px}.hero{padding:32px 24px;border-radius:14px}.report-section{padding:22px 16px}.metric-grid,.why-grid,.issues,.guardrails,.category-index{grid-template-columns:1fr}.timeline{grid-template-columns:1fr}.table-tools{align-items:flex-start;flex-direction:column}.plan-card{grid-template-columns:1fr}.problem-number{padding:8px;place-items:start}.pipeline{grid-template-columns:repeat(5,minmax(145px,1fr))}}
    @media print{body{background:#fff}.layout{display:block}.sidebar{display:none}.content{padding:0}.hero,.report-section{box-shadow:none}.report-section{border:none;border-radius:0}.plan-title,.plan-field,.issue-card{break-inside:avoid}.code-file pre{max-height:none}.table-tools{display:none}}
    '''

    js = r'''
    function filterTable(id, query){const q=query.toLowerCase();document.querySelectorAll(`#${id} tbody tr`).forEach(row=>{row.hidden=!row.innerText.toLowerCase().includes(q)});}
    const links=[...document.querySelectorAll('.sidebar nav a')];const sections=links.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){links.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+entry.target.id));}})},{rootMargin:'-20% 0px -70% 0px'});sections.forEach(s=>observer.observe(s));
    document.querySelectorAll('.code-file').forEach((d,i)=>{if(i===0)d.open=true});
    '''

    document = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Relatório Pacheco + Revisão Boss · Guia v2</title><meta name="description" content="Guia técnico da etapa Pacheco: problemas da base, do código e da arquitetura, plano de correção, efeitos downstream e revisão do AGENTE_BOSS."><style>{css}</style></head>
    <body><div class="layout"><aside class="sidebar"><div class="brand">Fluidos de Corte</div><div class="brand-sub">Etapa Pacheco + revisão metodológica</div><nav>
      <a href="#visao">Visão geral</a><a href="#importancia">Por que importa</a><a href="#metodo">Método</a><a href="#auditoria">Auditoria</a><a href="#resultados">Resultados</a><a href="#issues">Pendências</a><a href="#plano">Roteiro de correção</a><a href="#problemas-base">Problemas da base</a><a href="#problemas-codigo">Problemas do código</a><a href="#problemas-arquitetura">Arquitetura e outros</a><a href="#impactos">Efeitos downstream</a><a href="#abertos">Riscos adicionais</a><a href="#boss">Parecer Boss</a><a href="#codigo">Código</a><a href="#apendices">Apêndices</a>
    </nav><a class="pdf-link" href="relatorio_completo_pacheco_boss_v2.pdf">Abrir esta versão em PDF</a></aside><main class="content">
    <header class="hero" id="top"><div class="kicker">Guia técnico v2 · dados Pacheco v1 sob revisão</div><h1>Do arquivo bruto à base auditável</h1><p>O que foi realizado pelo AGENTE_PACHECO, por que a etapa é essencial para o ranking multicritério, quais códigos tornam o trabalho reproduzível e o que o AGENTE_BOSS determinou antes do avanço para Benjamin. Os achados estão separados em base/dados, código e arquitetura.</p><div class="status-row"><span class="status-pill">Branch agente_pacheco</span><span class="status-pill">1.034 registros canônicos</span><span class="status-pill">11 fluidos</span><span class="status-pill alert">Boss: CHANGES_REQUESTED</span></div></header>
    <div class="metric-grid"><div class="metric"><strong>7</strong><span>abas inventariadas</span></div><div class="metric"><strong>1.034</strong><span>registros canônicos</span></div><div class="metric"><strong>15</strong><span>ausências preservadas</span></div><div class="metric"><strong>0</strong><span>duplicatas de origem</span></div></div>
    {section('visao','01 · Visão geral','O que foi feito',f'''<p class="lead">A etapa Pacheco transformou uma planilha com blocos heterogêneos em um conjunto auditável de evidências. O arquivo bruto permaneceu imutável e cada observação da base canônica pode ser rastreada até a aba e célula de origem.</p><div class="timeline"><div class="step"><b>01</b>Inventário</div><div class="step"><b>02</b>Auditoria</div><div class="step"><b>03</b>Reconciliação</div><div class="step"><b>04</b>Base canônica</div><div class="step"><b>05</b>ADA inicial</div></div><div class="callout alert"><strong>Estado atual:</strong> o AGENTE_BOSS solicitou mudanças. A base e o handoff não estão liberados para Benjamin até correção e nova revisão.</div>''')}
    {section('importancia','02 · Fundamento','Por que esta etapa é importante','''<div class="why-grid"><div class="why-card"><strong>Evita ranking sobre dados errados</strong>Erros upstream contaminariam critérios, pesos CRITIC, TOPSIS e análises de robustez.</div><div class="why-card"><strong>Preserva evidência</strong>Cada número mantém arquivo, aba, célula, unidade e contexto de origem.</div><div class="why-card"><strong>Separa ausência de zero</strong>Impedir que dados faltantes sejam convertidos em desempenho real evita conclusões falsas.</div><div class="why-card"><strong>Expõe divergências</strong>Somatórios e custos foram confrontados entre abas em vez de aceitos automaticamente.</div><div class="why-card"><strong>Torna a análise reproduzível</strong>O código R reconstrói a cópia, a base e os diagnósticos sem edição manual.</div><div class="why-card"><strong>Respeita responsabilidades</strong>Pacheco prepara e audita; Benjamin define critérios; Vitor ranqueia; Boss revisa.</div></div>''')}
    {section('metodo','03 · Método','Fonte, cópia e estrutura',f'''<h3>Arquivos de entrada</h3>{table_html(raw_inventory,table_id='raw-table')}<h3>Integridade da cópia</h3>{table_html(copy_check,table_id='copy-table')}<h3>Abas do XLSX</h3>{table_html(sheets,['sheet_index','sheet_name','rows_read','columns_read','non_blank_cells','provisional_header_row'],'sheet-table')}<div class="callout"><strong>Estratégia:</strong> como a planilha não é uma tabela retangular única, cada bloco foi extraído para formato longo, com representação original, numérica/textual e linhagem por célula.</div>''')}
    {section('auditoria','04 · Qualidade','Como os dados foram auditados',f'''<p>Foram verificados arquivos, abas, tipos aparentes, ausências, zeros explícitos, unidades, fórmulas OOXML, duplicidade de origem e consistência entre valores armazenados em abas diferentes.</p><h3>Ausências e zeros</h3>{table_html(missing,table_id='missing-table')}<h3>Unidades identificadas</h3>{table_html(units,table_id='unit-table')}''')}
    {section('resultados','05 · Resultados','O que a execução encontrou',f'''<div class="chart-card">{missingness_svg(missing)}</div><h3>Reconciliação entre abas</h3><p>O status distingue igualdade exata, equivalência de precisão de máquina, ausência de insumo e diferença que exige revisão porque a tolerância metodológica ainda não foi definida.</p>{table_html(reconciliation,table_id='reconciliation-table')}<h3>Estatísticas descritivas iniciais</h3>{table_html(numeric,table_id='numeric-table')}''')}
    {section('issues','06 · Pendências','Problemas preservados e ações requeridas',f'''<p>Nenhum destes itens foi corrigido silenciosamente. Eles permanecem visíveis até que a evidência seja obtida e a decisão seja documentada.</p><div class="issues">{''.join(issue_cards)}</div>''')}
    {section('plano','07 · Roteiro','Onde começar a correção',f'''<p class="lead">Os 11 achados oficiais do Boss foram agrupados pelo tipo principal de trabalho. A numeração deste guia segue a ordem dos grupos; o código MAJOR/MINOR continua sendo a referência oficial do parecer. Cada item explica evidência, consequência, passos para Pacheco, técnicas, arquivos, critério de aceite e reprocessamento.</p><div class="category-index"><a href="#problemas-base">Base e dados <small>5 achados · fonte, tipos, unidades, reconciliação e ADA</small></a><a href="#problemas-codigo">Código e execução <small>4 achados · Unicode, testes, caminhos e gráficos</small></a><a href="#problemas-arquitetura">Arquitetura e documentação <small>2 achados · estados, handoff e severidades</small></a></div><div class="callout alert"><b>Sequência de trabalho:</b> confirmar evidência na fonte → corrigir na etapa proprietária → gerar nova versão → reexecutar auditorias/ADA e testes → atualizar STATUS e handoff → pedir nova revisão ao Boss. Não libere a base ao Benjamin enquanto o veredito for CHANGES_REQUESTED.</div>''')}
    {section('problemas-base','08 · Base e dados','Problemas com a base e como resolver',group_html['base'])}
    {section('problemas-codigo','09 · Código','Problemas com o código e como resolver',group_html['codigo'])}
    {section('problemas-arquitetura','10 · Governança','Problemas de arquitetura e outros',group_html['arquitetura'])}
    {section('impactos','08 · Dependências','O que fica bloqueado e o que precisa ser refeito',f'''<p class="lead">A etapa Pacheco é upstream. Um problema de escopo, tipo, unidade, reconciliação ou codificação pode mudar os valores ou as chaves que as próximas etapas usam. O Boss ainda não liberou o handoff.</p><div class="pipeline" role="img" aria-label="Fluxo de dependências: fonte original, Pacheco etapas 01 a 05, revisão obrigatória do Boss, Benjamin etapas 06 a 09, Vitor etapas 10 a 12 e integração Marco"><div class="pipeline-node"><b>Fonte original</b><small>XLSX bruto imutável, inventário e hash</small></div><div class="pipeline-node"><b>Pacheco · 01–05</b><small>Auditoria, reconciliação, base e ADA</small></div><div class="pipeline-node gate"><b>Gate Boss</b><small>CHANGES_REQUESTED · handoff não liberado</small></div><div class="pipeline-node"><b>Benjamin · 06–09</b><small>ADA avançada, conformidade e critérios</small></div><div class="pipeline-node"><b>Vitor → Marco</b><small>TOPSIS/robustez → relatório/apresentação</small></div></div><div class="callout alert"><b>Se a base mudar:</b> crie nova versão, regenere os outputs de Pacheco, atualize o handoff e peça nova revisão do Boss. Se Benjamin ou Vitor já tiverem calculado resultados, o Boss deve avaliar quais ficaram SUPERSEDED e quais precisam ser reexecutados. Não corrija a divergência apenas no relatório final.</div><div class="guardrails"><div class="guardrail"><b>Raw é imutável</b>Não corrigir nem sobrescrever data/raw. Faça correções via código/regra rastreável e preserve a célula original.</div><div class="guardrail"><b>NA não é zero</b>Não imputar ausência como zero. Classifique significado somente com evidência.</div><div class="guardrail"><b>Tolerância precisa de autoridade</b>Não inventar limite nem aprovar diferença porque parece pequena; use regra oficial documentada.</div><div class="guardrail"><b>Outlier é candidato, não erro</b>Não excluir, winsorizar ou substituir automaticamente valores extremos.</div><div class="guardrail"><b>Não antecipar a etapa Benjamin/Vitor</b>Pacheco não seleciona critério, peso, normalização ou vencedor para resolver problema de dado.</div><div class="guardrail"><b>Precisão completa</b>Manter precisão de cálculo; arredondar apenas para apresentação.</div><div class="guardrail"><b>Decisão rastreável</b>Valor reconciliado deve apontar para regra, issue, evidência e origem; dúvidas externas ficam PENDING_EXTERNAL_CONFIRMATION.</div><div class="guardrail"><b>Handoff não é aprovação</b>Arquivo existente ou base reproduzível não equivale a APPROVED; somente Boss libera após nova revisão.</div></div>''')}
    {section('abertos','09 · Além dos 11 achados','Riscos técnicos e limitações que também precisam aparecer',f'''<p class="lead">Esta seção preserva observações do parecer e issues de origem que não são contadas entre os 8 MAJOR e 3 MINOR. Assim, a severidade oficial não muda, mas nenhum ponto de rastreabilidade ou limitação fica escondido.</p><article class="issue-card medium"><header><span class="issue-id">RASTREABILIDADE DO BRUTO · PARTIAL</span><span class="badge medium">RISCO DE CONTROLE</span></header><h3>Integridade atual foi confirmada; histórico desde o recebimento não foi comprovado</h3><p>O hash SHA-256 da cópia coincide hoje com o bruto, mas o XLSX bruto não está rastreado pelo Git e o Boss não encontrou hash independente de recebimento anterior. Isso não prova alteração; significa que a cadeia histórica completa não pode ser verificada apenas com o repositório.</p><p><b>O que fazer:</b> mantenha o bruto em local protegido e somente leitura; arquive um manifesto de recebimento com nome original, data/fonte, tamanho e SHA-256 em checkpoint confiável; registre quem recebeu e qualquer substituição como nova versão. Não coloque dados potencialmente sensíveis em Git sem decisão explícita de governança.</p><p><b>Se não resolver:</b> no futuro pode não ser possível provar qual arquivo originou a base ou distinguir uma atualização legítima de substituição acidental.</p></article><div class="issues" style="margin-top:16px"><article class="issue-card high"><header><span class="issue-id">PCH-004 · ACIDEZ</span><span class="badge high">OPEN</span></header><h3>O texto “repetir” ocupa o lugar de uma medida</h3><p><b>Faça:</b> preservar o marcador e célula; verificar caderno/registro de laboratório; pedir repetição/valor oficial se necessário; atualizar somente em nova versão com fonte. Até resolver, sinalize a medida como indisponível para cálculos numéricos daquela variável.</p><p><b>Se não resolver:</b> converter para zero ou ignorar como missing sem rastro cria desempenho falso ou comparação com n diferente. Benjamin deve receber a restrição por métrica/fluido.</p></article><article class="issue-card high"><header><span class="issue-id">PCH-005 · ECONÔMICO</span><span class="badge high">OPEN</span></header><h3>Há células econômicas ausentes na fonte</h3><p><b>Faça:</b> quantificar por fluido/variável; identificar se é não aplicável, não medido ou desconhecido apenas com evidência; buscar confirmação na fonte autorizada; manter NA caso permaneça sem informação.</p><p><b>Se não resolver:</b> comparações de custo podem usar amostras desiguais ou produzir ranking econômico incompleto. A etapa seguinte precisa bloquear/limitar os campos afetados explicitamente.</p></article><article class="issue-card medium"><header><span class="issue-id">PCH-002 · MEMÓRIA DE CÁLCULO</span><span class="badge medium">OPEN</span></header><h3>O XLSX não contém fórmulas OOXML, embora haja valores calculados</h3><p><b>Faça:</b> registrar que os valores estão armazenados como valores; recuperar fórmula/memória de cálculo de fonte oficial, caderno ou documentação quando existir; reproduzir independentemente o cálculo a partir das parcelas disponíveis e mostrar a comparação.</p><p><b>Se não resolver:</b> a reprodução do valor pode não ser demonstrável, mesmo que ele pareça plausível. Marque origem/método como incompletos e não o trate como plenamente validado.</p></article><article class="issue-card medium"><header><span class="issue-id">PCH-003 · CAVACOS</span><span class="badge medium">CONFIRMAR</span></header><h3>A aba CAVACOS contém uma identificação de produto, sem dados experimentais observados</h3><p><b>Faça:</b> confirme com a fonte se é apenas referência, se faltam dados da aba ou se o material não faz parte do escopo. Registre decisão de inclusão/exclusão na matriz de cobertura do problema 1.</p><p><b>Se não resolver:</b> uma aba potencialmente relevante pode ser descartada sem justificativa ou pode ser confundida com medição que não existe.</p></article></div><div class="callout"><b>Sobre as fórmulas:</b> o Boss confirmou zero fórmulas OOXML detectadas. Isso é um achado informativo, não uma prova de que todos os valores armazenados estejam corretos. Valide valores derivados com memória de cálculo ou recálculo independente quando aplicável.</div><div class="callout"><b>Controle de versão:</b> a correção deve gerar artefatos coerentes com a nova versão. A base v1 pode permanecer como evidência histórica; não sobrescreva silenciosamente a trilha aprovada/em revisão.</div>''')}
    {section('boss','10 · Revisão independente','Parecer do AGENTE_BOSS',f'''<div class="review-banner"><strong>CHANGES_REQUESTED</strong><div><b>0 críticos · 8 maiores · 3 menores · 4 informativos</b><br>A base canônica e o handoff não estão liberados para Benjamin. Pacheco deve corrigir os achados na origem e submeter uma nova versão.</div></div><div class="review-content">{markdown_to_html(review)}</div>''')}
    {section('codigo','11 · Reprodutibilidade','Código utilizado',f'''<p>Os arquivos abaixo implementam leitura, inventário, classificação de ausências, normalização de unidades, reconciliação, construção canônica, ADA inicial, orquestração e testes. Clique em cada arquivo para expandir.</p>{''.join(code_details(path) for path in code_files)}''')}
    {section('apendices','12 · Evidências','Dicionário, variáveis e handoff',f'''<details open><summary><b>Dicionário canônico</b></summary>{table_html(dictionary,table_id='dictionary-table')}</details><details><summary><b>Inventário completo de variáveis</b></summary>{table_html(variables,table_id='variables-table')}</details><details><summary><b>Handoff Pacheco → Benjamin</b></summary><div class="review-content">{markdown_to_html(handoff)}</div></details>''')}
    <footer class="footer">Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte · Relatório Pacheco v1 · Parecer Boss: CHANGES_REQUESTED</footer>
    </main></div><script>{js}</script></body></html>'''

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = "\n".join(line.rstrip() for line in document.splitlines()) + "\n"
    OUTPUT.write_text(document, encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    build_html()
