# Auditoria pontual de NA — planilhas da divisão Pacheco

**Data:** 2026-09-29
**Estado:** `UNDER_REVIEW` — esta auditoria não aprova a base canônica nem libera o handoff para Benjamin.

## Escopo e preservação

Foram conferidos os quatro arquivos de `data/processed/divisao/` contra `data/processed/matriz_candidata_completa_v1.xlsx` e, nos pontos indicados, contra `data/raw/ensaio_bancada_alunos (2).xlsx`. Antes da edição, cópias dos quatro XLSX foram guardadas em `data/processed/divisao/backup_pre_auditoria_na/`. O arquivo em `data/raw/` não foi modificado.

| Arquivo | Resultado |
|---|---|
| `economico_v1.xlsx` | Seis `NA` reconstruídos em `Dados`; nove zeros marcados; nove `NA` remanescentes marcados; legenda e contagens adicionadas em `Leia-me`. |
| `desempenho_usinagem_v1.xlsx` | Sem alteração; backup idêntico, inclusive binariamente. |
| `qualidade_peca_processo_v1.xlsx` | Sem alteração; backup idêntico, inclusive binariamente. |
| `propriedades_estabilidade_fluido_v1.xlsx` | Sem alteração; backup idêntico, inclusive binariamente. |

`Dicionário` e `Rastreabilidade` no arquivo econômico continuam registrando a **extração da fonte**, inclusive 15 registros mapeados para `NA`. Auditoria posterior mostrou que nove correspondem a células brutas vazias e seis a caches de fórmula `#DIV/0!`; portanto, `Valor bruto = NA` não reproduz literalmente esses seis erros da fonte. Os seis valores reconstruídos aparecem em `Dados`, sem substituir silenciosamente o histórico da extração. As colunas `RESUMO PENDENTE` continuam vazias. Ver `docs/auditoria_divisao_pacheco.md`.

## Seis valores reconstruídos — fundo vermelho

| Fluido | Célula em `economico_v1.xlsx` | Campo | Valor inserido | Base do cálculo |
|---|---|---|---:|---|
| J | `Dados!AA10` | Vida da ferramenta | 2242,7 | `COMPARATIVO!F17`: somatório original 2242,7136 cm³, exibido aqui com uma casa decimal conforme a instrução. |
| K | `Dados!AA11` | Vida da ferramenta | 2450,7 | `COMPARATIVO!F18`: somatório original 2450,7072 cm³, exibido aqui com uma casa decimal. |
| J | `Dados!I10` | Custo da ferramenta para o lote | 0,8918 | `100 × 20 ÷ 2242,7 = 0,8917822268…`, arredondado a quatro casas. |
| K | `Dados!I11` | Custo da ferramenta para o lote | 0,8161 | `100 × 20 ÷ 2450,7 = 0,8160933611…`, arredondado a quatro casas. |
| J | `Dados!N10` | Custo total anual operação/ferramenta | 117,5584 | `116,6666667 + 100 × 20 ÷ 2242,7 = 117,5584489…`, arredondado a quatro casas. |
| K | `Dados!N11` | Custo total anual operação/ferramenta | 117,4828 | `116,6666667 + 100 × 20 ÷ 2450,7 = 117,4827600…`, arredondado a quatro casas. |

Para o último cálculo, usou-se o custo da ferramenta/lote **antes de arredondá-lo**. Em J, somar os números já exibidos (`116,6666667 + 0,8918`) produziria `117,5585` em quatro casas; essa diferença de 0,0001 é apenas efeito de arredondamento intermediário, não um novo dado. Os valores foram gravados como números, sem inserir fórmulas no XLSX derivado. **Correção posterior:** a planilha bruta tem fórmulas OOXML nesses campos (`AF40`/`AF41` e `AI40`/`AI41`), mas seu cache contém `#DIV/0!` por falta da vida da ferramenta em `AF38`/`AI38`. A sequência local é reproduzível pelo script `scripts/auditar_na_divisao_pacheco.mjs`.

O campo `Custo total anual operação/ferramenta` **não** substitui `CUSTO TOTAL ANUAL`: são colunas distintas, e a segunda permanece ausente em J e K.

## Nove zeros suspeitos — fundo verde, valor preservado

Esses zeros podem esconder ausência de insumos; **não foram transformados em `NA` nem usados para completar outros valores**.

| Fluido | Células | Campos |
|---|---|---|
| J | `Dados!E10`, `F10`, `G10`, `K10`, `L10`, `M10` | Consumo anual pela troca; custo anual da troca; custo anual do fluido; custo da reposição anual; custo da reposição mensal; custo do enchimento. |
| K | `Dados!E11`, `F11`, `M11` | Consumo anual pela troca; custo anual da troca; custo do enchimento. |

Pacheco deve verificar, para cada zero, a presença dos insumos e a memória de cálculo. Só depois decidir, com evidência documentada, se representa zero real ou ausência mascarada. Até lá, qualquer soma econômica dependente desses campos é incerta.

## Nove NA explícitos ainda sem solução — fundo rosa

| Fluido | Células | Campos |
|---|---|---|
| J | `Dados!B10`, `D10`, `P10`, `Q10`, `U10` | CUSTO TOTAL ANUAL; concentração; enchimento do sistema; fator de correção; preço do produto. |
| K | `Dados!B11`, `D11`, `P11`, `Q11` | CUSTO TOTAL ANUAL; concentração; enchimento do sistema; fator de correção. |

Os 15 `NA` explícitos anteriores foram reduzidos a 9 apenas nas células determinadas acima. `CUSTO TOTAL ANUAL` não foi recalculado: ainda faltam dados econômicos essenciais, especialmente preço do produto e enchimento em J, e enchimento em K. Nenhum `NA` virou zero.

### Concentração e fator de correção

Não foi adotada automaticamente a concentração de outra aba. Para J, `COMPARATIVO` registra 9,0% e `ANÁLISE EMULSÕES` 8,5%; para K, 9,5% e 9,0%. A coluna econômica está ausente para ambos. É preciso definir o significado experimental de cada medição e a convenção de unidade antes de qualquer transposição. O fator de correção de J e K continua `NA` porque não foi demonstrada relação determinística segura.

## Outras inconsistências preservadas para revisão

- **Acidez:** em `propriedades_estabilidade_fluido_v1.xlsx`, `Dados!O5`, `O6`, `O7` e `O9` (D, E, F e H) contêm `repetir`. São medições ainda não disponíveis, não números. Permanecem como texto; Pacheco deve buscar a repetição experimental ou registrar ausência irrecuperável.
- **Sólidos suspensos:** `Dados!L3` (B) contém `1 kg`, ao passo que os demais registros da coluna são numéricos. Não foi convertido automaticamente para 1000, pois falta confirmar a unidade-base e a natureza do registro. Pacheco deve conferir caderno/protocolo e padronizar somente com evidência.
- **Potência:** na versão auditada originalmente de `desempenho_usinagem_v1.xlsx`, os 44 pares (11 fluidos × 4 condições) de `COMPARATIVO` e `ANÁLISE USINABILIDADE` coincidiam numericamente. As quatro colunas redundantes do `COMPARATIVO` foram retiradas depois, conforme `docs/deduplicacao_divisao_pacheco.md`.
- **Vida da ferramenta:** as duas fontes não foram reconciliadas. No fluido B, as condições 3 e 4 são 325,5552 no `COMPARATIVO`, mas 361,728 em `ANÁLISE USINABILIDADE`. Há ainda pequenas diferenças em C e D e diferença na condição 2 de J (732,4992 versus 732,456). Os cálculos econômicos de J e K seguiram o somatório do `COMPARATIVO`, como explicitamente solicitado; isso **não** valida a série inteira como canônica. Pacheco deve obter a memória experimental e decidir a origem oficial antes de resumir vida da ferramenta.

## Validação e limites

- Conferência independente após exportação: **6** células vermelhas com números, **9** células verdes ainda iguais a zero e **9** células rosas ainda iguais a `NA`.
- `CUSTO TOTAL ANUAL`, concentração e fator de correção de J/K continuam `NA`.
- Comparação célula a célula com o backup: em `Dados`, somente os seis valores previstos mudaram; as demais alterações de conteúdo foram as 14 células da legenda/contagens em `Leia-me`. Estilos mudaram apenas nas 24 células marcadas e nas 14 células da legenda.
- Nenhuma célula com erro `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` ou `#N/A` foi encontrada **no XLSX derivado** após a edição. A fonte bruta, diferentemente, contém seis caches de fórmula `#DIV/0!` em J/K. Nenhuma outra aba ou resumo foi recalculado.
- A checagem é reproduzível por `scripts/validar_auditoria_na_divisao_pacheco.py`.

Esta é uma correção pontual da **matriz candidata sob revisão**, não uma aprovação metodológica. As pendências da revisão Boss em `reviews/BOSS_REVIEW_PACHECO_v1.md` permanecem abertas; não houve execução de critérios, CRITIC, TOPSIS, pesos, ranking ou robustez, e não houve handoff para Benjamin.
