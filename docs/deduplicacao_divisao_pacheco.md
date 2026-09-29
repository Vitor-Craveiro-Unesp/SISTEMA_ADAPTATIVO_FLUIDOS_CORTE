# Deduplicação conservadora das quatro planilhas divididas

**Data:** 2026-09-29
**Responsável:** Pacheco
**Estado:** `UNDER_REVIEW` — a base canônica e o handoff para Benjamin não foram aprovados.

## Regra aplicada

Uma coluna só foi retirada desta **projeção** quando representava a mesma medida, na mesma condição, com os 11 valores exatamente iguais aos de outra coluna do mesmo XLSX. A cópia retida veio da aba experimental mais direta, `ANÁLISE USINABILIDADE` ou `ANÁLISE EMULSÕES`. Igualdade casual de vetores de variáveis com significados ou condições diferentes não foi tratada como duplicação científica. Não houve média, imputação, substituição de valor ou edição de `data/raw/` e da base canônica.

| Arquivo | Campos originais antes → depois | Cópias exatas retiradas | Campos que requerem investigação |
|---|---:|---|---|
| `desempenho_usinagem_v1.xlsx` | 17 → 12 | Quatro colunas de potência (condições 1–4) e vida da ferramenta na condição 1, todas do `COMPARATIVO` | Pares de vida nas condições 2–4 entre as duas origens; seis pares de células divergem. O somatório não é cópia de uma condição. |
| `qualidade_peca_processo_v1.xlsx` | 17 → 17 | Nenhuma | As quatro condições de forma do cavaco são observações distintas, embora todas as respostas sejam `ruptura`. |
| `propriedades_estabilidade_fluido_v1.xlsx` | 34 → 33 | `comparativo | nevoa`, idêntica a `emulsao | NÉVOA` nos 11 fluidos | Concentração média entre abas diverge para J e K. |
| `economico_v1.xlsx` | 26 → 26 | Nenhuma | Dados ausentes, fórmulas com erro e zeros suspeitos continuam como na auditoria anterior. |

Os 66 campos `RESUMO PENDENTE` continuam intactos e vazios (726 células). Os 11 fluidos foram mantidos, na mesma ordem. O total das quatro projeções passou de 94 para **88 colunas originais**, e de 1.034 para **968 registros ativos de rastreabilidade**, mantendo todos os valores das colunas retidas. Os registros das seis colunas retiradas continuam disponíveis no backup e nas fontes upstream.

## O que continua marcado como possível duplicata

- Em desempenho, somente vida da ferramenta nas condições 2, 3 e 4 das duas origens. Há seis divergências de célula: B nas condições 3/4, C nas condições 3/4, D na condição 3 e J na condição 2. Nem as coincidências parciais nem pequenos desvios de arredondamento justificam escolher uma origem sem evidência.
- Em propriedades, `concentracao_media` do `COMPARATIVO` e `CONCENTRAÇÃO MÉDIA` de `ANÁLISE EMULSÕES`, porque J/K diferem. Essas colunas continuam destacadas como possíveis duplicatas a reconciliar.
- O somatório de vida da ferramenta foi mantido como **agregado original**, sem a etiqueta de duplicata. Ele não deve ser usado simultaneamente com suas condições como critério independente sem decisão de Benjamin e revisão de Pacheco/Boss.

Igualdade de valores não é suficiente para excluir `bacterias` e `ESPUMA`, `CONTAGEM ANTES MISTURA` e `CONTAGEM INÍCIO ENSAIO`, ou quatro condições de `forma_cavaco`: são variáveis/tempos/condições distintos. Elas podem ser constantes nesta amostra, mas essa é outra questão estatística.

## Rastreabilidade, segurança e validação

Antes da alteração, os quatro XLSX e a legenda foram copiados para `data/processed/divisao/backup_pre_deduplicacao/`. O código de transformação é `scripts/deduplicar_divisao_pacheco.mjs`; a verificação independente é `scripts/validar_deduplicacao_divisao_pacheco.py`. O validador compara célula a célula os dados retidos, as marcações de auditoria, o dicionário, a rastreabilidade, os resumos vazios e as duas planilhas que não foram alteradas. A visualização de `Dados` e `Leia-me` também foi conferida.

**Pendência upstream:** os endereços físicos dos registros restantes do `COMPARATIVO` continuam deslocados em seis linhas. Após a retirada, são 44 em desempenho, 99 em qualidade e 132 em propriedades (275 no total). Esta deduplicação não corrige esse erro, que deve ser tratado na origem e revalidado pelo Boss. Também não resolve divergências experimentais, medições `repetir`, unidades ou ausências econômicas.

Esta é uma limpeza local das projeções, **não** uma nova base canônica aprovada. Quando Pacheco corrigir e regenerar a base upstream, deve reaplicar a regra de deduplicação e revalidar qualquer resultado downstream; cópias antigas não devem ser misturadas com os arquivos atuais.
