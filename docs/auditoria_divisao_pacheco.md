# Auditoria dos quatro arquivos de `data/processed/divisao/`

**Data:** 2026-09-29
**Responsável pela etapa:** Pacheco
**Estado:** `UNDER_REVIEW`. Esta auditoria não aprova a base canônica nem libera o handoff para Benjamin.

**Histórico:** os números de colunas e endereços neste relatório registram o estado **anterior** à deduplicação conservadora feita depois. Para a estrutura atual dos XLSX, consultar `docs/deduplicacao_divisao_pacheco.md` e a aba `Leia-me` de cada planilha.

## Escopo e método

Foram auditados `desempenho_usinagem_v1.xlsx`, `qualidade_peca_processo_v1.xlsx`, `propriedades_estabilidade_fluido_v1.xlsx` e `economico_v1.xlsx`. A referência foi a planilha imutável `data/raw/ensaio_bancada_alunos (2).xlsx` (SHA-256 `30c5655a777c69db369b4e719b77e38bc47e152b6bd684f7c104d7c10226e4c6`), além da matriz candidata e da aba `Rastreabilidade` de cada arquivo.

Antes de sobrescrever os quatro XLSX, foi criado `data/processed/divisao/backup_pre_auditoria_todos/` com uma cópia de cada um. O backup anterior da auditoria econômica, `backup_pre_auditoria_na/`, também foi preservado. A planilha bruta não foi editada.

O controle cobriu 11 fluidos e 94 campos originais (1.034 células), 1.034 registros de rastreabilidade, as colunas de resumo intencionalmente vazias, os valores de origem, tipos/unidades aparentes, duplicatas entre fontes, somas internas, `NA`, zeros e fórmulas/erros na fonte. Não se aplicou média, mediana, imputação estatística, substituição de `NA` por zero ou decisão multicritério.

| Arquivo | Campos originais | `NA` literal em `Dados` agora | Células laranja nesta auditoria | Resumos vazios | Valores originais alterados agora |
|---|---:|---:|---:|---:|---:|
| Desempenho de usinagem | 17 | 0 | 12 | 22 | 0 |
| Qualidade da peça/processo | 17 | 0 | 0 | 55 | 0 |
| Propriedades/estabilidade do fluido | 34 | 0 | 11 | 363 | 0 |
| Econômico | 26 | 9 | 0 novas | 286 | 0 |

Ao todo, as 726 células de `RESUMO PENDENTE` continuam vazias. As cores já existentes no arquivo econômico permanecem: seis valores reconstruídos em vermelho, nove zeros suspeitos em verde e nove `NA` não resolvidos em rosa. Laranja significa **investigação necessária, sem correção automática**. As cores são acompanhadas de explicações nos `Leia-me` e neste relatório; não devem ser interpretadas como tratamento concluído.

## 1. Desempenho de usinagem

Não há `NA` literal nem zero nos 17 campos originais. Os 44 pares de potência (11 fluidos × quatro condições) em `COMPARATIVO` e `ANÁLISE USINABILIDADE` coincidem numericamente. Por serem potenciais duplicatas, não foram excluídos. Os 11 somatórios de vida da ferramenta em `COMPARATIVO` são iguais à soma das quatro condições dessa própria aba, mas as condições não são sempre iguais às da outra fonte.

| Fluido, condição | `COMPARATIVO` (cm³) | `ANÁLISE USINABILIDADE` (cm³) | Células destacadas em `Dados` |
|---|---:|---:|---|
| B, 3 | 325,5552 | 361,728 | `H3`, `Q3` |
| B, 4 | 325,5552 | 361,728 | `I3`, `R3` |
| C, 3 | 238,74048 | 238,7405 | `H4`, `Q4` |
| C, 4 | 417,79584 | 417,7958 | `I4`, `R4` |
| D, 3 | 325,5552 | 325,555 | `H5`, `Q5` |
| J, 2 | 732,4992 | 732,456 | `G10`, `P10` |

As diferenças de C/D podem refletir arredondamento, mas isso não foi presumido como decisão de reconciliação. As de B e J também requerem conferência da memória experimental. Se uma futura média de vida usar indiscriminadamente as duas fontes, haverá contagem dupla e possível viés; se escolher uma origem sem justificativa, o resultado não será reproduzível. Pacheco deve estabelecer fonte de referência por condição, com evidência e regra de precisão, antes de produzir qualquer resumo.

## 2. Qualidade da peça/processo

Não há `NA` literal nem zero nos 17 campos originais. Os valores de `Dados` foram mantidos. `Presença de rebarba` é categórica (`sim`/`não`). As quatro colunas de `Forma do cavaco` contêm `ruptura` nas 44 observações: é uma categoria constante nesta amostra, não uma medida numérica. Não foi calculada média nem codificação. `Circularidade`, `concentricidade` e rugosidade permanecem separados por condição; agregação depende de definição posterior e de conferência das unidades/protocolo.

Risco: forçar uma média numérica de campos categóricos ou tratar uma variável constante como fonte de discriminação cria resultados artificiais. Pacheco deve manter tipo categórico e documentar o significado de cada condição antes do handoff. Os cinco campos de resumo permanecem vazios para cada fluido.

## 3. Propriedades/estabilidade do fluido

Não há `NA` literal, mas quatro células da acidez contêm o texto `repetir`: `Dados!O5`, `O6`, `O7`, `O9` (D, E, F, H). São medições numéricas ainda não disponíveis. Ficaram como texto, em laranja; não foram imputadas. É necessário obter o novo ensaio ou registrar uma ausência irresolúvel com sua origem.

`Dados!L3` (B, sólidos suspensos) contém `1 kg`, enquanto os demais valores da coluna são numéricos e o cabeçalho não explicita unidade. A conversão para 1000 não foi feita, porque não está demonstrado que os demais números estejam em gramas ou representem a mesma grandeza. Pacheco deve verificar o protocolo e a unidade antes da padronização.

As duas origens de concentração coincidem para nove fluidos, mas divergem para J e K:

| Fluido | `COMPARATIVO` | `ANÁLISE EMULSÕES` | Células laranja |
|---|---:|---:|---|
| J | 9,0% | 8,5% | `Dados!C10`, `S10` |
| K | 9,5% | 9,0% | `Dados!C11`, `S11` |

Não se escolheu uma origem nem se preencheu a concentração econômica de J/K. As células `Dados!V4` e `V6` (C e E) contêm `*fungos`, em vez de `fungos`/`isento`; o significado do asterisco precisa ser recuperado da fonte. Variações de maiúsculas/minúsculas em categorias como `sim`/`SIM` também exigem um dicionário antes de qualquer codificação, sem mudança dos textos brutos aqui.

`CORROSÃO NO FOFO` apresenta zero nos 11 fluidos (`Dados!X2:X12`). Esses zeros constam da origem e não há evidência de dependência ausente; não foram marcados como `NA` escondido. A variável é constante nesta amostra. Usá-la sem considerar a ausência de variação pode afetar análises estatísticas posteriores. Os 33 resumos por fluido permanecem vazios.

## 4. Econômico

A auditoria econômica anterior foi preservada integralmente. Em `Dados`, os seis números reconstruídos continuam em vermelho, os nove zeros suspeitos de J/K continuam verdes sem mudança de valor, e os nove `NA` não resolvidos continuam rosas. Não foram preenchidos `CUSTO TOTAL ANUAL`, concentração ou fator de correção de J/K. Outros 17 zeros foram mantidos como registrados; esta checagem não comprova que todos sejam zeros reais, apenas não encontrou a mesma evidência de dependência ausente usada para os nove marcados.

Uma conferência da planilha bruta com fórmulas habilitadas corrigiu uma interpretação anterior: a aba `AVALIAÇÃO ECONÔMICA` **contém 143 fórmulas OOXML**. Os 15 `NA` mapeados originalmente na matriz candidata não são 15 células brutas vazias: **nove** são células vazias, e **seis** são resultados em cache `#DIV/0!` de fórmulas de J/K (`AF40`, `AF41`, `AF43`, `AI40`, `AI41`, `AI43`). `Rastreabilidade` registra `NA` para esses seis erros, não o valor literal bruto. Os campos `AF40`/`AI40` (custo da ferramenta/lote) e `AF41`/`AI41` (subtotal operação/ferramenta) foram reconstruídos na auditoria anterior com a vida de ferramenta externa; `AF43`/`AI43` (custo total anual) permanecem `NA` por insumos faltantes. Os endereços da aba econômica conferem com a planilha bruta.

As fórmulas brutas de J são `AF40=(AF33/AF38)*AF39`, `AF41=AF36+AF40` e `AF43=AF29+AF41`; K usa a mesma estrutura nas células `AI`. A vida da ferramenta em `AF38`/`AI38` está vazia na fonte. A reconstrução local em `Dados` é um valor estático auditado, não recálculo da planilha bruta. Para sanar definitivamente a origem, Pacheco deve investigar entradas faltantes, verificar a memória de cálculo e reexecutar o pipeline sem sobrescrever `data/raw/`.

## Problema transversal: endereços `COMPARATIVO` deslocados

Nas abas `Rastreabilidade` de desempenho, qualidade e propriedades, **todos os 341 registros com origem `COMPARATIVO` apontam seis linhas acima da célula física do XLSX bruto**. Exemplo: o fluido A, potência condição 1, informa `COMPARATIVO!V3`, mas o valor 2,5 está em `COMPARATIVO!V9`; `V3` está vazio. A célula indicada + 6 linhas reproduz o valor registrado em todos os 341 casos verificados (99 + 99 + 143). Algumas coincidências de valor em endereço errado não tornam a referência correta.

Não corrigi esses endereços apenas nos quatro XLSX: a mesma linhagem é derivada da base/código upstream, e um remendo local criaria duas versões incompatíveis da origem. Os quatro `Leia-me` avisam sobre o problema. Pacheco deve corrigir a regra de numeração de linhas na extração, testar as 341 referências contra o arquivo bruto e **regenerar conjuntamente** base canônica, matriz candidata e quatro divisões; depois o Boss precisa revisar o impacto. Até lá, não se deve usar `source_cell` de `COMPARATIVO` como referência física confiável.

## Correção de registro metodológico anterior

O relatório pontual `docs/auditoria_na_pacheco.md` foi retificado para distinguir a ausência de fórmulas nas **planilhas divididas** da presença de fórmulas na **fonte bruta**. A planilha bruta tem 175 fórmulas OOXML no total: 21 em `EQUA-USN`, 11 em `COMPARATIVO` e 143 em `AVALIAÇÃO ECONÔMICA`. A conclusão anterior de que a planilha bruta não possuía fórmulas não se sustenta. A revisão Boss v1 também contém essa conclusão e precisa de adendo/revisão formal pelo Boss; ela não foi editada silenciosamente nesta etapa.

## Validação e próximos passos da etapa Pacheco

Foi feita comparação célula a célula contra o novo backup. Nesta auditoria, **nenhum valor em `Dados`, `Dicionário` ou `Rastreabilidade` foi alterado**; apenas 12 células de desempenho e 11 de propriedades receberam fundo laranja, e os quatro `Leia-me` ganharam notas de auditoria. As 726 células de resumo seguem vazias. Os XLSX divididos não contêm fórmulas ou células do tipo erro; menções textuais a `#DIV/0!` nas notas são documentação, não falhas do arquivo editado. A validação pode ser repetida com `scripts/validar_auditoria_divisao_pacheco.py`; os diagnósticos de origem com `scripts/inspecionar_divisao_pacheco.py`.

Pendências que pertencem ao Pacheco, antes de qualquer passagem a Benjamin:

1. Corrigir o deslocamento de seis linhas da linhagem `COMPARATIVO` na origem do pipeline e regenerar todos os derivados afetados, preservando as versões anteriores e registrando o impacto.
2. Diferenciar explicitamente célula bruta vazia, erro de fórmula em cache e zero verdadeiro na base canônica e no dicionário.
3. Resolver com evidência as seis diferenças de vida da ferramenta e os conflitos de concentração de J/K, sem escolher a fonte que favoreça qualquer fluido.
4. Conferir as quatro medições `repetir`, a unidade de `1 kg`, a anotação `*fungos` e os nove zeros econômicos suspeitos.
5. Revalidar a matriz candidata e solicitar revisão formal do Boss. Não gerar critérios, pesos, CRITIC, TOPSIS ou ranking enquanto estas pendências estiverem abertas.
