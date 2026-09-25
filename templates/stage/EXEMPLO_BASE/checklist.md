# Checklist de Etapa

## Finalidade

Este arquivo serve como checklist operacional e científico para qualquer etapa do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Ele deve ser utilizado durante todo o ciclo da etapa:

```text
início
↓
execução
↓
validação
↓
documentação
↓
revisão
↓
handoff
```

Este checklist não substitui:

```text
testes automatizados
revisão científica
handoff formal
documentação da etapa
```

Ele funciona como uma camada adicional de controle.

---

# 1. Identificação da etapa

Preencher antes de começar:

```text
STAGE_NAME = TO_BE_FILLED
RESPONSIBLE = TO_BE_FILLED
REVIEWER = TO_BE_FILLED
STATUS = DRAFT
INPUT_VERSION = TO_BE_FILLED
OUTPUT_VERSION = TO_BE_FILLED
```

Checklist:

```text
[ ] nome da etapa definido
[ ] responsável definido
[ ] revisor definido
[ ] objetivo compreendido
[ ] entrada identificada
[ ] saída esperada identificada
```

---

# 2. Leitura das instruções

Antes da implementação:

```text
[ ] README da etapa lido
[ ] arquivo de instrução específico lido
[ ] handoff de entrada lido, quando aplicável
[ ] decisões relacionadas lidas
[ ] limitações herdadas compreendidas
[ ] pendências conhecidas compreendidas
```

---

# 3. Entrada

Confirmar:

```text
[ ] arquivo ou objeto de entrada identificado
[ ] versão conferida
[ ] caminho conferido
[ ] estrutura esperada conferida
[ ] quantidade de linhas conferida, quando aplicável
[ ] quantidade de colunas conferida, quando aplicável
[ ] identificadores conferidos
[ ] unidades conhecidas
[ ] missing conhecidos
```

---

# 4. Origem da entrada

Confirmar:

```text
[ ] origem da entrada conhecida
[ ] etapa responsável pela entrada conhecida
[ ] entrada aprovada, quando necessário
[ ] nenhuma cópia paralela não rastreável sendo utilizada
```

---

# 5. Dados brutos

Se a etapa utilizar dados originais:

```text
[ ] data/raw/ permanece imutável
[ ] nenhuma correção foi feita diretamente no arquivo original
[ ] transformações serão realizadas por código
[ ] origem do arquivo está documentada
```

---

# 6. Ambiente

Antes da execução:

```text
[ ] R disponível
[ ] versão de R conhecida
[ ] dependências instaladas
[ ] renv restaurado, se utilizado
[ ] Docker disponível, se necessário
[ ] diretório de trabalho correto
[ ] caminhos relativos funcionando
```

---

# 7. Git

Antes de alterar o projeto:

```text
[ ] branch correta
[ ] working tree revisada
[ ] nenhuma alteração alheia será sobrescrita
[ ] arquivos temporários não serão versionados
```

---

# 8. Planejamento da análise

Antes de codificar:

```text
[ ] problema da etapa definido
[ ] método definido ou identificado como pendente
[ ] entradas necessárias identificadas
[ ] saídas necessárias identificadas
[ ] validações planejadas
[ ] possíveis casos extremos considerados
```

---

# 9. Implementação

Durante a codificação:

```text
[ ] código organizado
[ ] nomes claros
[ ] funções com responsabilidade definida
[ ] sem caminhos absolutos pessoais
[ ] sem valores mágicos desnecessários
[ ] parâmetros configuráveis separados quando apropriado
[ ] comentários usados apenas onde agregam clareza
```

---

# 10. Reutilização de código

Verificar:

```text
[ ] código compartilhado não foi duplicado desnecessariamente
[ ] funções reutilizáveis foram avaliadas para R/shared/
[ ] etapa não depende de script pessoal fora do repositório
```

---

# 11. Execução

Ao executar:

```text
[ ] código roda sem erro inesperado
[ ] warnings foram revisados
[ ] outputs esperados foram gerados
[ ] nenhum output inesperado foi sobrescrito
[ ] execução é repetível
```

---

# 12. Warnings

Para cada warning:

```text
[ ] foi lido
[ ] impacto científico foi avaliado
[ ] foi resolvido ou documentado
```

Nunca ocultar warnings apenas para "limpar" a execução.

---

# 13. Erros

Se ocorrer erro:

```text
[ ] causa identificada
[ ] correção feita na origem
[ ] não houve ajuste manual apenas para contornar o problema
[ ] etapa foi reexecutada depois da correção
```

Se o erro comprometer a validade:

```text
STATUS = BLOCKED
```

---

# 14. Qualidade dos dados

Quando aplicável:

```text
[ ] tipos verificados
[ ] identificadores verificados
[ ] duplicatas verificadas
[ ] missing verificados
[ ] unidades verificadas
[ ] intervalos verificados
[ ] valores extremos investigados
[ ] variáveis constantes identificadas
[ ] variáveis quase constantes identificadas
```

---

# 15. Transformações

Para cada transformação relevante:

```text
[ ] regra documentada
[ ] justificativa conhecida
[ ] implementação reproduzível
[ ] unidade de entrada conhecida
[ ] unidade de saída conhecida
[ ] impacto downstream avaliado
```

---

# 16. Agregações

Se houver agregação:

```text
[ ] necessidade justificada
[ ] regra explícita
[ ] perda de informação avaliada
[ ] condições experimentais consideradas
[ ] resultado validado
```

---

# 17. Missing

Se houver valores ausentes:

```text
[ ] significado investigado
[ ] não foram convertidos automaticamente para zero
[ ] tratamento documentado
[ ] impacto avaliado
```

---

# 18. Valores extremos

Quando existirem:

```text
[ ] valor confirmado na fonte
[ ] plausibilidade avaliada
[ ] influência analisada
[ ] remoção, se houver, foi justificada
```

---

# 19. Unidades

Confirmar:

```text
[ ] unidades originais conhecidas
[ ] unidades canônicas definidas
[ ] conversões documentadas
[ ] nenhuma mistura de escalas
```

---

# 20. Fórmulas e cálculos

Quando houver cálculos derivados:

```text
[ ] fórmula documentada
[ ] implementação conferida
[ ] denominadores críticos verificados
[ ] divisões por zero tratadas
[ ] NA/NaN/Inf verificados
[ ] arredondamento não afeta o cálculo
```

---

# 21. Cálculo independente

Para resultados críticos:

```text
[ ] segunda verificação realizada, quando aplicável
[ ] caso simples testado
[ ] resultado comparado com expectativa matemática
```

---

# 22. Testes automatizados

Quando aplicável:

```text
[ ] testes criados
[ ] testes executados
[ ] testes passam
[ ] casos extremos cobertos
[ ] erros esperados testados
```

Status:

```text
TEST_STATUS = TO_BE_FILLED
```

---

# 23. Propriedades matemáticas

Quando aplicável:

```text
[ ] soma de pesos verificada
[ ] intervalos esperados verificados
[ ] matriz simétrica verificada
[ ] diagonal verificada
[ ] valores não negativos verificados
[ ] normalização verificada
```

Marcar somente os itens pertinentes à etapa.

---

# 24. Resultados exploratórios

Se houver resultados ainda não aprovados:

```text
[ ] identificados como EXPLORATORY
[ ] não apresentados como oficiais
[ ] limitações registradas
```

---

# 25. Resultados oficiais

Antes de classificar um resultado como oficial:

```text
[ ] entrada aprovada
[ ] método aprovado
[ ] código validado
[ ] testes concluídos
[ ] revisão realizada
```

---

# 26. Tabelas

Para cada tabela relevante:

```text
[ ] gerada a partir dos resultados reais
[ ] título claro
[ ] unidades presentes quando necessárias
[ ] casas decimais adequadas
[ ] missing corretamente representados
[ ] nenhuma digitação manual divergente
```

---

# 27. Figuras

Para cada figura relevante:

```text
[ ] gerada de forma rastreável
[ ] eixos identificados
[ ] unidades identificadas
[ ] legenda adequada
[ ] texto legível
[ ] não depende apenas de cor
[ ] interpretação coerente
```

---

# 28. Interpretação

Para cada resultado importante:

```text
[ ] foi interpretado
[ ] não houve extrapolação
[ ] não houve causalidade indevida
[ ] limitações consideradas
[ ] impacto na próxima etapa explicado
```

---

# 29. Correlação

Se houver correlação:

```text
[ ] método registrado
[ ] tamanho amostral considerado
[ ] missing tratados de forma clara
[ ] correlação não interpretada como causalidade
[ ] sinais positivos e negativos interpretados corretamente
```

---

# 30. Critérios

Se a etapa envolver critérios:

```text
[ ] critérios candidatos identificados
[ ] critérios aprovados documentados
[ ] critérios excluídos documentados
[ ] direções definidas
[ ] TARGET tratados
[ ] restrições separadas de diagnóstico
[ ] redundância avaliada
```

---

# 31. Conformidade

Se aplicável:

```text
[ ] fonte das especificações conhecida
[ ] limites confirmados
[ ] pendências marcadas como pendentes
[ ] hard constraints justificadas
[ ] soft constraints justificadas
[ ] missing não tratados automaticamente como não conformidade
```

---

# 32. Normalização

Se aplicável:

```text
[ ] método definido
[ ] direção dos critérios considerada
[ ] denominador zero tratado
[ ] critérios constantes tratados
[ ] precisão completa mantida
[ ] resultado validado
```

---

# 33. CRITIC

Se aplicável:

```text
[ ] matriz correta utilizada
[ ] correlação definida
[ ] dispersão calculada corretamente
[ ] fórmula implementada corretamente
[ ] soma dos pesos aproximadamente 1
[ ] pesos não negativos
[ ] nenhum NA/NaN/Inf
[ ] associação por nome validada
[ ] critério constante tratado
[ ] caso degenerado tratado
```

---

# 34. TOPSIS

Se aplicável:

```text
[ ] matriz correta utilizada
[ ] pesos corretos utilizados
[ ] orientação confirmada
[ ] ideal positivo correto
[ ] ideal negativo correto
[ ] distâncias corretas
[ ] coeficientes entre 0 e 1
[ ] nenhum NA/NaN/Inf
[ ] ranking ordenado corretamente
[ ] associação por nome validada
```

---

# 35. Ranking

Se aplicável:

```text
[ ] ranking calculado com precisão completa
[ ] arredondamento apenas para apresentação
[ ] gaps avaliados
[ ] empates avaliados
[ ] quase empates avaliados
[ ] top 3 interpretado
[ ] conformidade integrada
```

---

# 36. Cenários

Se aplicável:

```text
[ ] cenários definidos antes da interpretação
[ ] cenários possuem justificativa
[ ] pesos válidos
[ ] comparação com cenário-base realizada
[ ] mudança do vencedor registrada
[ ] estabilidade do top 3 avaliada
```

---

# 37. Pareto

Se aplicável:

```text
[ ] critérios corretamente orientados
[ ] dominância implementada corretamente
[ ] alternativa não domina a si mesma
[ ] alternativas idênticas tratadas corretamente
[ ] fronteira identificada
[ ] relação com TOPSIS interpretada
```

---

# 38. Sensibilidade

Se aplicável:

```text
[ ] perturbações definidas
[ ] pesos renormalizados
[ ] pesos permanecem não negativos
[ ] delta zero reproduz cenário-base
[ ] resultado comparado com ranking-base
```

---

# 39. Leave-one-criterion-out

Se aplicável:

```text
[ ] cada critério removido de forma sistemática
[ ] regra de pesos definida
[ ] CRITIC recalculado quando necessário
[ ] impacto registrado
```

---

# 40. Normalização alternativa

Se aplicável:

```text
[ ] normalização alternativa definida
[ ] CRITIC recalculado
[ ] TOPSIS recalculado
[ ] ranking comparado
```

---

# 41. Leave-one-alternative-out

Se aplicável:

```text
[ ] cada alternativa removida uma vez
[ ] normalização recalculada
[ ] CRITIC recalculado
[ ] TOPSIS recalculado
[ ] alternativa removida não aparece no resultado
[ ] rank reversal avaliado
```

---

# 42. Simulações

Se aplicável:

```text
[ ] seed definida
[ ] número de simulações registrado
[ ] vetores válidos
[ ] configurações inválidas removidas/documentadas
[ ] execução reproduzível
```

---

# 43. Robustez

Se aplicável:

```text
[ ] estabilidade do primeiro lugar avaliada
[ ] estabilidade do top 3 avaliada
[ ] melhor e pior posição avaliadas
[ ] posição média/mediana avaliadas quando úteis
[ ] sensibilidade estrutural considerada
[ ] frequências não interpretadas como probabilidades reais
```

---

# 44. Decisões metodológicas

Confirmar:

```text
[ ] decisões relevantes identificadas
[ ] DEC criada quando necessária
[ ] decisão não foi escolhida pelo resultado desejado
[ ] impacto downstream registrado
```

---

# 45. Limitações

Antes de concluir:

```text
[ ] limitações reais identificadas
[ ] impacto das limitações explicado
[ ] limitações não ocultadas
[ ] nenhuma limitação hipotética apresentada como fato
```

---

# 46. Conclusões

Confirmar:

```text
[ ] conclusão responde ao objetivo da etapa
[ ] conclusão sustentada pelos resultados
[ ] nenhuma conclusão nova apareceu sem suporte
[ ] força da conclusão é proporcional às evidências
```

---

# 47. Reprodutibilidade

Verificar:

```text
[ ] mesma entrada produz mesmo resultado
[ ] caminhos relativos
[ ] dependências conhecidas
[ ] seed definida quando necessário
[ ] nenhuma etapa manual oculta
```

---

# 48. Outputs

Antes do handoff:

```text
[ ] outputs necessários gerados
[ ] nomes claros
[ ] localização correta
[ ] versões identificadas
[ ] arquivos temporários separados
```

---

# 49. Não sobrescrever fonte externa

Confirmar:

```text
[ ] arquivos fornecidos pela professora preservados
[ ] dados brutos preservados
[ ] templates oficiais preservados
[ ] referências externas não modificadas silenciosamente
```

---

# 50. Documentação

Confirmar:

```text
[ ] analysis.qmd atualizado, quando utilizado
[ ] relatório da etapa atualizado
[ ] README atualizado se necessário
[ ] decisões referenciadas
[ ] limitações registradas
[ ] versão registrada
```

---

# 51. Handoff

Antes de entregar à próxima etapa:

```text
[ ] handoff preenchido
[ ] entrada da próxima etapa identificada
[ ] versão informada
[ ] limitações informadas
[ ] problemas pendentes informados
[ ] decisões importantes informadas
[ ] itens congelados informados
```

---

# 52. Problemas bloqueantes

Registrar:

```text
BLOCKING_ISSUES = TO_BE_FILLED
```

Se houver problema bloqueante:

```text
[ ] etapa marcada como BLOCKED
[ ] próxima etapa não iniciou indevidamente
```

---

# 53. Problemas não bloqueantes

Registrar:

```text
NON_BLOCKING_ISSUES = TO_BE_FILLED
```

Confirmar:

```text
[ ] problemas foram comunicados no handoff
```

---

# 54. Revisão cruzada

Antes da aprovação:

```text
[ ] revisor definido
[ ] código revisado
[ ] resultados revisados
[ ] interpretação revisada
[ ] limitações revisadas
[ ] handoff revisado
```

---

# 55. Git antes da integração

Confirmar:

```text
[ ] arquivos corretos versionados
[ ] outputs indevidos não versionados
[ ] commits claros
[ ] branch atualizada
[ ] conflitos resolvidos
[ ] testes executados após resolução de conflitos
```

---

# 56. Aprovação

Preencher:

```text
RESPONSIBLE = TO_BE_FILLED
REVIEWED_BY = TO_BE_FILLED
REVIEW_DATE = TO_BE_FILLED
```

Checklist:

```text
[ ] responsável considera a etapa concluída
[ ] revisor considera a etapa válida
[ ] handoff aprovado
```

---

# 57. Status final

Selecionar:

```text
DRAFT
UNDER_REVIEW
APPROVED
BLOCKED
SUPERSEDED
```

Registrar:

```text
STAGE_STATUS = TO_BE_FILLED
```

---

# 58. Regra de reabertura

Uma etapa aprovada deverá ser reaberta se ocorrer alteração relevante em:

```text
dados de entrada
método
critério
regra
parâmetro
decisão upstream
```

Confirmar:

```text
[ ] impactos downstream identificados
[ ] versões anteriores preservadas
[ ] reexecução realizada quando necessária
```

---

# 59. Checklist mínimo para aprovação

Nenhuma etapa deve ser aprovada sem, no mínimo:

```text
[ ] entrada correta
[ ] código executado
[ ] resultado validado
[ ] limitações registradas
[ ] documentação atualizada
[ ] revisão cruzada
[ ] handoff preparado
```

---

# 60. Estado atual deste template

```text
CHECKLIST_TEMPLATE_STATUS = BASE_PREPARED
```

Os itens acima não estão marcados porque este arquivo é apenas um modelo.

Cada integrante deverá utilizar uma cópia ou adaptação correspondente à sua etapa real.

---

# Princípio final

> Uma etapa só deve avançar quando aquilo que entra, aquilo que é feito e aquilo que sai estiverem claros, validados e rastreáveis.