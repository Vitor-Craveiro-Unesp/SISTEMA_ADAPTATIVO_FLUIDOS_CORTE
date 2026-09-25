# REVIEW PROTOCOL

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Este documento define o protocolo formal de revisão utilizado pelo:

```text
AGENTE_BOSS
```

sobre o trabalho produzido por:

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
```

---

# 1. Objetivo

O objetivo do protocolo é garantir que nenhuma etapa seja considerada concluída apenas porque:

```text
o código executou
o arquivo existe
o gráfico foi gerado
o resultado parece plausível
```

A aprovação exige evidência de que a etapa é:

```text
coerente
rastreável
reproduzível
validada
compatível com suas entradas
compatível com as etapas seguintes
```

---

# 2. Princípio fundamental

```text
AGENTE RESPONSÁVEL
↓
IMPLEMENTA
↓
EXECUTA
↓
VALIDA
↓
DOCUMENTA
↓
SOLICITA REVISÃO
↓
AGENTE_BOSS
```

O Boss então emite:

```text
APPROVED
```

ou:

```text
CHANGES_REQUESTED
```

ou:

```text
BLOCKED
```

---

# 3. Revisão não substitui autoria

O `AGENTE_BOSS` revisa.

O agente responsável corrige.

Regra:

```text
ERRO DE DADOS
→ Pacheco

ERRO DE CRITÉRIO / CRITIC
→ Benjamin

ERRO DE TOPSIS / ROBUSTEZ
→ Vitor

ERRO DE RELATÓRIO / APRESENTAÇÃO
→ Marco
```

---

# 4. Estados formais

## `APPROVED`

A etapa está suficientemente validada para alimentar a próxima etapa.

---

## `CHANGES_REQUESTED`

Há um ou mais problemas corrigíveis antes da aprovação.

---

## `BLOCKED`

Existe problema que impede avanço confiável.

---

## `UNDER_REVIEW`

A revisão ainda não foi concluída.

---

## `SUPERSEDED`

A etapa já foi aprovada anteriormente, mas uma mudança upstream tornou aquela versão obsoleta.

---

# 5. Severidade dos problemas

Toda questão encontrada deverá ser classificada como:

```text
CRITICAL
MAJOR
MINOR
INFORMATIONAL
```

---

# 6. CRITICAL

Problema capaz de invalidar diretamente os resultados científicos.

Exemplos:

```text
dados errados
raw alterado
base incorreta
critério invertido
TARGET inventado
peso CRITIC incorreto
TOPSIS implementado incorretamente
resultado fabricado
uso de versão superseded
```

Regra geral:

```text
CRITICAL
→ BLOCKED
```

---

# 7. MAJOR

Problema relevante que precisa ser corrigido antes da aprovação.

Exemplos:

```text
documentação insuficiente para reproduzir
critério sem justificativa
regra de normalização ambígua
handoff incompleto
limitação importante omitida
```

Regra geral:

```text
MAJOR
→ CHANGES_REQUESTED
```

---

# 8. MINOR

Problema de baixa influência científica.

Exemplos:

```text
legenda incompleta
nome inconsistente
casas decimais inconsistentes
pequena falha documental
```

Pode exigir correção, mas não necessariamente bloqueia toda a etapa.

---

# 9. INFORMATIONAL

Observação ou sugestão sem impacto obrigatório na aprovação.

Exemplo:

```text
sugestão de gráfico adicional
melhoria opcional de texto
melhoria futura de automação
```

---

# 10. Estrutura mínima de uma issue

Toda issue de revisão deve registrar:

```text
REVIEW_ID = TO_BE_FILLED

SEVERITY = TO_BE_FILLED

STATUS = OPEN

RESPONSIBLE_AGENT = TO_BE_FILLED

FILE = TO_BE_FILLED

LOCATION = TO_BE_FILLED

ISSUE = TO_BE_FILLED

EVIDENCE = TO_BE_FILLED

IMPACT = TO_BE_FILLED

REQUESTED_ACTION = TO_BE_FILLED
```

---

# 11. Não usar comentário vago

Evitar:

```text
“melhorar isso”
“revisar análise”
“acho que está errado”
```

Preferir:

```text
“config/criterios.yml registra a variável como COST,
mas a matriz utilizada pelo TOPSIS foi tratada como BENEFIT.
Verificar orientação e reexecutar a etapa.”
```

---

# 12. Fases de revisão

Toda revisão formal possui cinco fases:

```text
1. PRECHECK
2. INPUT REVIEW
3. METHOD REVIEW
4. OUTPUT REVIEW
5. HANDOFF REVIEW
```

---

# 13. Fase 1 — PRECHECK

Antes de revisar o conteúdo científico, verificar:

```text
responsável correto
arquivo correto
versão correta
status correto
entrada disponível
dependências disponíveis
```

---

# 14. Checklist PRECHECK

```text
[ ] agente responsável identificado

[ ] etapa identificada

[ ] arquivos esperados existem

[ ] versão da entrada conhecida

[ ] status upstream conhecido

[ ] nenhum input crítico está SUPERSEDED

[ ] STATUS.md está coerente

[ ] handoff anterior foi consultado
```

---

# 15. Entrada não aprovada

Se a etapa depender de entrada:

```text
NOT_EXECUTED
UNDER_REVIEW
BLOCKED
SUPERSEDED
```

a revisão pode ser interrompida.

Resultado possível:

```text
BLOCKED
```

---

# 16. Fase 2 — INPUT REVIEW

Objetivo:

```text
garantir que a etapa utilizou a entrada correta
```

Verificar:

```text
arquivo
versão
dimensão
estrutura
configuração
status
```

---

# 17. Regra de versionamento

Não aceitar combinação inconsistente como:

```text
base_canônica_v2
+
CRITIC_v1
+
TOPSIS_v2
```

sem justificativa explícita.

---

# 18. Fase 3 — METHOD REVIEW

Objetivo:

```text
verificar se o método executado corresponde ao método documentado
```

Verificar:

```text
fórmula
transformações
parâmetros
tolerâncias
regras
ordem de operações
casos especiais
```

---

# 19. Parâmetros escondidos

Se um parâmetro científico relevante existir apenas dentro do código:

```text
investigar
```

Pode ser necessário:

```text
documentar
centralizar em config/
registrar decisão
```

---

# 20. Fase 4 — OUTPUT REVIEW

Objetivo:

```text
verificar se as saídas são válidas e interpretadas corretamente
```

Verificar:

```text
dimensões
valores
intervalos possíveis
missing
NaN
Inf
coerência matemática
coerência interpretativa
```

---

# 21. Fase 5 — HANDOFF REVIEW

Antes de liberar para a próxima etapa, verificar se o handoff contém informação suficiente.

O agente downstream não deve precisar adivinhar:

```text
qual arquivo usar
qual versão usar
qual configuração usar
quais limitações existem
```

---

# 22. Revisão de Pacheco

Etapas:

```text
01
02
03
04
05
```

Fluxo:

```text
RAW
↓
INVENTÁRIO
↓
AUDITORIA
↓
RECONCILIAÇÃO
↓
BASE CANÔNICA
↓
ADA INICIAL
```

---

# 23. Checklist Pacheco — dados brutos

```text
[ ] data/raw/ permaneceu imutável

[ ] fonte original identificada

[ ] arquivos utilizados registrados

[ ] nenhuma correção manual foi feita no raw

[ ] caminhos são reproduzíveis
```

---

# 24. Checklist Pacheco — inventário

```text
[ ] abas inventariadas

[ ] dimensões registradas

[ ] cabeçalhos identificados

[ ] variáveis identificadas

[ ] unidades aparentes registradas

[ ] fórmulas relevantes identificadas

[ ] identificadores investigados
```

---

# 25. Checklist Pacheco — auditoria

```text
[ ] tipos verificados

[ ] missing verificados

[ ] duplicatas verificadas

[ ] unidades verificadas

[ ] fórmulas verificadas

[ ] somas recalculadas quando necessário

[ ] médias recalculadas quando necessário

[ ] inconsistências entre fontes registradas

[ ] issues possuem evidência
```

---

# 26. Checklist Pacheco — reconciliação

```text
[ ] toda correção possui justificativa

[ ] valor original permanece rastreável

[ ] nenhuma decisão foi baseada no ranking futuro

[ ] nenhuma correção foi feita por conveniência

[ ] pendências externas estão explicitadas
```

---

# 27. Checklist Pacheco — base canônica

```text
[ ] base gerada por código

[ ] chaves validadas

[ ] duplicatas avaliadas

[ ] unidades coerentes

[ ] missing conhecidos

[ ] sem Inf inesperado

[ ] sem NaN inesperado

[ ] linhagem documentada

[ ] versão identificada
```

---

# 28. Checklist Pacheco — ADA inicial

```text
[ ] estatísticas descritivas coerentes

[ ] variáveis constantes identificadas

[ ] variáveis quase constantes identificadas

[ ] outliers tratados como diagnóstico

[ ] condições experimentais preservadas quando necessário

[ ] nenhuma conclusão causal indevida
```

---

# 29. Aprovação de Pacheco

Para liberar:

```text
handoffs/01_PACHECO_to_BENJAMIN.md
```

o Boss deve confirmar:

```text
CANONICAL_DATA_STATUS = APPROVED
```

---

# 30. Revisão de Benjamin

Etapas:

```text
06
07
08
09
```

Fluxo:

```text
ADA BIVARIADA
↓
ADA MULTIVARIADA
↓
CONFORMIDADE
↓
CRITÉRIOS
↓
NORMALIZAÇÃO
↓
CRITIC
```

---

# 31. Checklist Benjamin — entrada

```text
[ ] base canônica aprovada

[ ] versão correta utilizada

[ ] nenhuma correção silenciosa de dado

[ ] handoff de Pacheco respeitado
```

---

# 32. Checklist Benjamin — ADA bivariada

```text
[ ] método de correlação documentado

[ ] sinal das correlações interpretado corretamente

[ ] magnitude interpretada com cautela

[ ] correlação não apresentada como causalidade

[ ] redundância não implica exclusão automática
```

---

# 33. Checklist Benjamin — ADA multivariada

```text
[ ] variáveis constantes tratadas

[ ] escalas avaliadas

[ ] PCA, se usada, está identificada como exploratória

[ ] componentes não foram transformados automaticamente em critérios

[ ] interpretação está compatível com os dados
```

---

# 34. Checklist Benjamin — conformidade

```text
[ ] especificações possuem fonte confirmada

[ ] unidades são compatíveis

[ ] limites não foram inventados

[ ] conformidade está separada de desempenho

[ ] regra global de conformidade está documentada
```

---

# 35. Checklist Benjamin — critérios

```text
[ ] critérios candidatos registrados

[ ] critérios incluídos registrados

[ ] critérios excluídos registrados

[ ] exclusões possuem justificativa

[ ] identificadores não entraram como critérios

[ ] critérios não foram selecionados pelo vencedor

[ ] direções foram definidas
```

---

# 36. Checklist Benjamin — TARGET

```text
[ ] todo TARGET possui alvo definido

[ ] alvo possui fonte ou justificativa

[ ] transformação está documentada

[ ] nenhum alvo foi inventado
```

---

# 37. Checklist Benjamin — matriz de decisão

```text
[ ] linhas representam alternativas

[ ] colunas representam critérios aprovados

[ ] unidades são coerentes

[ ] missing foi tratado explicitamente

[ ] agregações foram justificadas

[ ] ordem dos critérios está documentada
```

---

# 38. Checklist Benjamin — normalização

```text
[ ] método principal está documentado

[ ] BENEFIT tratado corretamente

[ ] COST tratado corretamente

[ ] TARGET tratado corretamente

[ ] nenhuma dupla orientação ocorreu

[ ] divisão por zero foi tratada

[ ] nenhuma transformação foi escolhida pelo vencedor
```

---

# 39. Checklist Benjamin — CRITIC

Verificar:

\[
C_j = \sigma_j \sum_k(1-r_{jk})
\]

e:

\[
w_j=\frac{C_j}{\sum_j C_j}
\]

Checklist:

```text
[ ] dispersão calculada conforme documentação

[ ] correlação calculada conforme documentação

[ ] foi utilizado 1-r

[ ] não foi usado 1-|r| silenciosamente

[ ] critérios constantes tratados

[ ] correlação indefinida tratada

[ ] C_j válidos

[ ] pesos finitos

[ ] pesos não negativos

[ ] soma dos pesos ≈ 1

[ ] nenhum fallback silencioso para pesos iguais
```

---

# 40. Checklist Benjamin — interpretação

```text
[ ] pesos chamados de informacionais

[ ] peso alto não foi chamado automaticamente de maior importância técnica

[ ] correlação negativa não foi tratada como erro

[ ] limitações estão registradas
```

---

# 41. Aprovação de Benjamin

Para liberar:

```text
handoffs/02_BENJAMIN_to_VITOR.md
```

confirmar:

```text
CRITERIA_STATUS = APPROVED

NORMALIZATION_STATUS = APPROVED

CRITIC_STATUS = APPROVED
```

---

# 42. Revisão de Vitor

Etapas:

```text
10
11
12
```

Fluxo:

```text
TOPSIS
↓
RANKING PRINCIPAL
↓
CENÁRIOS
↓
PARETO
↓
SENSIBILIDADE
↓
LOCO
↓
NORMALIZAÇÃO ALTERNATIVA
↓
LOAO
↓
RANK REVERSAL
↓
ROBUSTEZ
```

---

# 43. Checklist Vitor — entrada

```text
[ ] critérios aprovados

[ ] normalização aprovada

[ ] pesos CRITIC aprovados

[ ] ordem dos critérios correta

[ ] conformidade recebida

[ ] versão correta dos dados
```

---

# 44. Checklist Vitor — pesos

```text
[ ] número de pesos = número de critérios

[ ] nomes alinhados

[ ] nenhum NA

[ ] nenhum NaN

[ ] nenhum Inf

[ ] nenhum peso negativo

[ ] soma ≈ 1
```

---

# 45. Checklist Vitor — TOPSIS

Verificar:

\[
v_{ij}=w_jr_{ij}
\]

\[
S_i^+
=
\sqrt{
\sum_j(v_{ij}-v_j^+)^2
}
\]

\[
S_i^-
=
\sqrt{
\sum_j(v_{ij}-v_j^-)^2
}
\]

\[
C_i
=
\frac{S_i^-}
{S_i^++S_i^-}
\]

Checklist:

```text
[ ] matriz ponderada correta

[ ] ideal positivo correto

[ ] ideal negativo correto

[ ] distâncias corretas

[ ] coeficiente correto

[ ] C_i entre 0 e 1 quando aplicável

[ ] sem divisão por zero silenciosa

[ ] sem dupla inversão de COST
```

---

# 46. Checklist Vitor — ranking

```text
[ ] ordenação decrescente de C_i

[ ] empates tratados explicitamente

[ ] precisão completa usada no cálculo

[ ] arredondamento apenas na comunicação

[ ] gaps entre posições avaliados

[ ] PRIMARY_RANKING não foi chamado automaticamente de FINAL_RANKING
```

---

# 47. Checklist Vitor — conformidade

```text
[ ] conformidade permanece visível

[ ] alternativa não conforme não foi ocultada

[ ] conformidade não foi confundida com ranking
```

---

# 48. Checklist Vitor — cenários

```text
[ ] cenário principal identificado

[ ] cenários alternativos identificados

[ ] pesos normalizados quando necessário

[ ] pesos iguais não usados como fallback silencioso

[ ] perturbações documentadas

[ ] frequências não chamadas de probabilidades
```

---

# 49. Checklist Vitor — Pareto

```text
[ ] critérios orientados adequadamente

[ ] Pareto calculado sem pesos

[ ] dominância implementada corretamente

[ ] TARGET tratado adequadamente

[ ] não dominado não foi chamado automaticamente de vencedor
```

---

# 50. Checklist Vitor — LOCO

```text
[ ] um critério removido por execução

[ ] protocolo de peso documentado

[ ] CRITIC recalculado ou mantido de forma explícita

[ ] rankings comparados corretamente

[ ] influência não confundida com importância técnica
```

---

# 51. Checklist Vitor — normalização alternativa

```text
[ ] método alternativo identificado

[ ] método principal preservado

[ ] comparação documentada

[ ] mudança não foi escolhida para favorecer vencedor
```

---

# 52. Checklist Vitor — LOAO

```text
[ ] uma alternativa removida por execução

[ ] normalização recalculada quando necessário

[ ] CRITIC recalculado ou mantido explicitamente

[ ] alternativa removida não participou da comparação

[ ] ranking dos remanescentes comparado corretamente
```

---

# 53. Checklist Vitor — rank reversal

```text
[ ] mudanças de ordem detectadas

[ ] intensidade avaliada

[ ] fenômeno não ocultado

[ ] interpretação não o classifica automaticamente como erro
```

---

# 54. Checklist Vitor — robustez

```text
[ ] top 1 avaliado

[ ] top 3 avaliado

[ ] conjunto e ordem do top 3 distinguidos

[ ] métricas possuem definição

[ ] nenhuma probabilidade indevida foi inferida

[ ] instabilidade foi comunicada quando presente
```

---

# 55. Aprovação de Vitor

Para liberar:

```text
handoffs/03_VITOR_to_MARCO.md
```

confirmar:

```text
TOPSIS_STATUS = APPROVED

ROBUSTNESS_STATUS = APPROVED
```

quando aplicável.

---

# 56. Revisão de Marco

Fluxo:

```text
RESULTADOS APROVADOS
↓
INTEGRAÇÃO
↓
RELATÓRIO
↓
APRESENTAÇÃO
↓
CONCLUSÕES
↓
ENTREGA
```

---

# 57. Checklist Marco — entrada

```text
[ ] somente resultados APPROVED

[ ] nenhum resultado SUPERSEDED

[ ] versões consistentes

[ ] handoff de Vitor recebido

[ ] resultados anteriores rastreáveis
```

---

# 58. Checklist Marco — números

```text
[ ] ranking consistente

[ ] C_i consistente

[ ] pesos consistentes

[ ] conformidade consistente

[ ] Pareto consistente

[ ] robustez consistente

[ ] unidades consistentes
```

---

# 59. Checklist Marco — relatório formal

```text
[ ] A4

[ ] 10 pt

[ ] margens 1,5 cm

[ ] máximo 4 páginas incluindo referências

[ ] resumo ≤ 1200 caracteres com espaços

[ ] 3 a 5 palavras-chave

[ ] duas colunas

[ ] estrutura oficial preservada
```

---

# 60. Checklist Marco — seções

```text
[ ] Introdução

[ ] Material e Método

[ ] Resultados e Discussão

[ ] Conclusões

[ ] Referências
```

---

# 61. Checklist Marco — conteúdo

```text
[ ] introdução não antecipa resultados indevidamente

[ ] método permite compreender a reprodução

[ ] resultados são interpretados

[ ] conclusões respondem ao objetivo

[ ] nenhuma conclusão nova foi inventada

[ ] limitações relevantes aparecem
```

---

# 62. Checklist Marco — terminologia

```text
[ ] CRITIC = peso informacional

[ ] Pareto não tratado como ranking

[ ] conformidade separada de desempenho

[ ] frequência de cenários não tratada como probabilidade

[ ] instabilidade não escondida
```

---

# 63. Checklist Marco — tabelas

```text
[ ] valores vêm de resultados aprovados

[ ] números não foram digitados manualmente sem necessidade

[ ] arredondamento consistente

[ ] unidades presentes

[ ] títulos claros
```

---

# 64. Checklist Marco — figuras

```text
[ ] figuras respondem a uma pergunta

[ ] fonte científica atual

[ ] nenhum output superseded

[ ] eixos e legendas corretos

[ ] unidades corretas
```

---

# 65. Checklist Marco — apresentação

```text
[ ] mesmos resultados do relatório

[ ] mesmo ranking

[ ] mesma conformidade

[ ] mesma interpretação

[ ] nenhuma alteração científica para melhorar visual
```

---

# 66. Checklist Marco — referências

```text
[ ] somente referências utilizadas

[ ] nenhuma referência inventada

[ ] citações correspondem às referências

[ ] formato solicitado respeitado
```

---

# 67. Aprovação de Marco

Antes de liberar:

```text
handoffs/04_MARCO_to_TODOS.md
```

o Boss deve confirmar que relatório e apresentação estão cientificamente consistentes.

---

# 68. Revisão transversal

Depois das revisões individuais, o Boss deverá realizar uma revisão integrada.

---

# 69. Cadeia end-to-end

Deve ser possível seguir:

```text
RAW
↓
AUDITORIA
↓
RECONCILIAÇÃO
↓
BASE CANÔNICA
↓
CRITÉRIOS
↓
NORMALIZAÇÃO
↓
CRITIC
↓
TOPSIS
↓
ROBUSTEZ
↓
RELATÓRIO
↓
APRESENTAÇÃO
```

---

# 70. Checklist de rastreabilidade

```text
[ ] conclusão aponta para resultado

[ ] resultado aponta para método

[ ] método aponta para configuração

[ ] configuração aponta para dados

[ ] dados processados apontam para raw
```

---

# 71. Revisão de versões

Verificar que todos os artefatos finais pertencem à mesma cadeia de versões.

---

# 72. Mudança upstream

Quando uma etapa aprovada mudar:

```text
identificar mudança
↓
identificar dependências
↓
marcar outputs antigos
↓
reexecutar downstream
↓
revisar novamente
```

---

# 73. Regra de invalidação

Exemplo:

```text
BASE CANÔNICA ALTERADA
↓
ADA pode precisar mudar
↓
CRITIC pode precisar mudar
↓
TOPSIS pode precisar mudar
↓
ROBUSTEZ pode precisar mudar
↓
RELATÓRIO pode precisar mudar
```

---

# 74. SUPERSEDED

Resultados antigos afetados devem ser marcados:

```text
SUPERSEDED
```

e não continuar como outputs oficiais.

---

# 75. Não corrigir somente no relatório

Regra proibida:

```text
erro no dado
↓
corrigir número no LaTeX
```

Fluxo correto:

```text
erro no dado
↓
Pacheco
↓
base nova
↓
reexecução
↓
novo resultado
↓
relatório atualizado
```

---

# 76. Revisão de código

Quando o código real existir, o Boss deverá verificar:

```text
clareza
caminhos relativos
ausência de estado oculto
ausência de valores científicos hard-coded
tratamento de erros
reprodutibilidade
```

---

# 77. Valores hard-coded

Nem todo valor hard-coded é incorreto.

Mas parâmetros científicos relevantes devem ter:

```text
origem
justificativa
documentação
```

---

# 78. Caminhos absolutos

Evitar:

```text
C:/Users/...
/home/nome/...
```

na implementação oficial.

Preferir caminhos relativos ao projeto.

---

# 79. Workspace

Não depender de:

```text
.RData
objetos antigos
sessão manual prévia
```

---

# 80. Testes

Quando implementados:

```text
testthat
```

deve verificar propriedades críticas.

Mas:

```text
TESTS_PASSING
≠
SCIENTIFIC_APPROVAL
```

---

# 81. CI

Quando implementada plenamente:

```text
CI_GREEN
```

também não substitui revisão científica.

---

# 82. targets

Quando a pipeline existir, o Boss deverá verificar:

```text
dependências corretas
reexecução automática quando input muda
outputs coerentes
```

---

# 83. renv

Quando configurado, verificar que:

```text
renv.lock
```

representa o ambiente real usado.

---

# 84. Docker

Quando implementado, verificar se:

```text
ambiente containerizado
```

consegue reproduzir a execução relevante.

---

# 85. Revisão independente

O Boss deve verificar a lógica sem assumir que o agente responsável está correto.

---

# 86. Revisão proporcional ao risco

A profundidade da revisão deve ser maior em:

```text
reconciliação
base canônica
critérios
normalização
CRITIC
TOPSIS
robustez
conclusão
```

---

# 87. Não duplicar todo o projeto

O Boss não precisa reexecutar manualmente cada linha de análise.

Deve buscar evidência suficiente para confiar na etapa.

---

# 88. Verificação independente

Quando necessário, o Boss pode realizar:

```text
checagem pontual
recálculo independente
teste com exemplo simples
validação de fórmula
```

sem assumir autoria da etapa.

---

# 89. Exemplo de recálculo independente

Para TOPSIS, o Boss pode selecionar uma alternativa e confirmar manualmente:

```text
produto peso × normalização
distância
C_i
```

como teste de coerência.

---

# 90. Exemplo para CRITIC

O Boss pode confirmar para um critério:

```text
σ_j
correlações
soma de conflitos
C_j
peso
```

---

# 91. Evidência de revisão

A revisão deve deixar um registro suficiente para responder:

```text
quem revisou?
o que revisou?
o que encontrou?
qual foi o status?
```

---

# 92. Template de revisão

Quando apropriado, utilizar:

```text
REVIEW_ID = TO_BE_FILLED

DATE = TO_BE_FILLED

REVIEWER = AGENTE_BOSS

TARGET_AGENT = TO_BE_FILLED

STAGE = TO_BE_FILLED

INPUT_VERSION = TO_BE_FILLED

OUTPUT_VERSION = TO_BE_FILLED

RESULT = UNDER_REVIEW
```

---

# 93. Issues da revisão

```text
CRITICAL = 0

MAJOR = 0

MINOR = 0

INFORMATIONAL = 0
```

Valores reais serão preenchidos durante a revisão.

---

# 94. Resultado final da revisão

Usar apenas um:

```text
RESULT = APPROVED
```

ou:

```text
RESULT = CHANGES_REQUESTED
```

ou:

```text
RESULT = BLOCKED
```

---

# 95. Condição mínima para APPROVED

Não deve existir:

```text
CRITICAL aberto
```

nem:

```text
MAJOR aberto
```

que possa comprometer a etapa.

---

# 96. MINOR aberto

Um problema `MINOR` poderá permanecer apenas se:

```text
não alterar resultado
estiver documentado
for conscientemente aceito
```

---

# 97. INFORMATIONAL aberto

Não bloqueia aprovação.

---

# 98. Re-revisão

Após `CHANGES_REQUESTED`:

```text
agente corrige
↓
nova versão
↓
Boss revisa apenas alterações
+
efeitos colaterais relevantes
```

---

# 99. Correção que altera resultado

Se a correção modificar resultados científicos:

```text
revisão downstream pode ser necessária
```

---

# 100. Correção puramente editorial

Se alterar apenas:

```text
ortografia
formatação
```

não exige reexecução científica.

---

# 101. Conflito entre agentes

Quando houver divergência:

```text
identificar ponto de conflito
↓
reunir evidências
↓
consultar fontes
↓
consultar decisões
↓
avaliar impacto
↓
resolver
```

---

# 102. Não decidir por autoridade informal

Não usar:

```text
“acho melhor”
```

como único fundamento metodológico.

---

# 103. Decisões importantes

Se a resolução modificar metodologia ou regra importante:

```text
decisions/
```

deve ser considerada.

---

# 104. Material oficial

Documentação fornecida pela professora possui prioridade sobre templates genéricos.

---

# 105. Lacuna na fonte

Se a documentação oficial não responder a uma questão:

```text
não inventar
```

Registrar:

```text
TO_BE_CONFIRMED
```

ou tomar decisão metodológica documentada quando apropriado.

---

# 106. Integridade científica

Durante toda revisão, buscar:

```text
seleção de método pelo resultado
alteração manual de números
remoção seletiva de casos
omissão de limitações
interpretação exagerada
```

---

# 107. Resultado inconveniente

Resultado desfavorável à hipótese ou preferência da equipe continua sendo resultado válido.

---

# 108. Instabilidade

Se a análise mostrar instabilidade:

```text
documentar
```

e não modificar método para escondê-la.

---

# 109. Missing

Verificar sempre:

```text
NA != 0
```

---

# 110. Outlier

Verificar que:

```text
outlier
≠
erro automático
```

---

# 111. Correlação

Verificar que:

```text
correlação
≠
causalidade
```

---

# 112. CRITIC

Verificar que:

```text
peso informacional
≠
importância técnica absoluta
```

---

# 113. Pareto

Verificar que:

```text
não dominado
≠
primeiro colocado
```

---

# 114. Robustez

Verificar que:

```text
frequência de cenários
≠
probabilidade real
```

---

# 115. Estado atual

Nesta fase:

```text
REVIEW_PROTOCOL_STATUS = BASE_PREPARED

SCIENTIFIC_REVIEWS = NOT_STARTED

GLOBAL_REVIEW_STATUS = NOT_STARTED

FINAL_REVIEW_STATUS = NOT_READY
```

---

# 116. Uso durante a fase BASE_PREPARED

Enquanto não houver execução científica, o Boss deve revisar apenas:

```text
estrutura
documentação
configuração-base
templates
responsabilidades
dependências
```

Não exigir resultados ainda inexistentes.

---

# 117. Não preencher checklists antecipadamente

Os itens deste arquivo são regras de revisão.

Eles não devem ser marcados como concluídos antes da execução real.

---

# 118. Critério de encerramento de uma revisão

Uma revisão pode ser encerrada quando:

```text
escopo foi verificado
issues foram registradas
severidades foram atribuídas
responsáveis foram definidos
status final foi emitido
```

---

# 119. Critério de encerramento do projeto

Antes da entrega final, o Boss deverá verificar:

```text
Pacheco = APPROVED
Benjamin = APPROVED
Vitor = APPROVED
Marco = APPROVED
```

e depois executar:

```text
GLOBAL_FINAL_REVIEW
```

---

# 120. Revisão final global

A revisão final deverá confirmar:

```text
dados corretos
↓
métodos corretos
↓
resultados corretos
↓
interpretação correta
↓
relatório correto
↓
apresentação correta
```

---

# 121. Saída final do Boss

Somente após essa revisão:

```text
FINAL_REVIEW_STATUS = APPROVED
```

poderá ser utilizado.

---

# 122. Princípio final

> A revisão não deve perguntar apenas “o resultado parece correto?”. Deve perguntar “consigo reconstruir de onde esse resultado veio, verificar como foi calculado, identificar quais decisões o produziram e confirmar que a interpretação respeita as evidências?”.