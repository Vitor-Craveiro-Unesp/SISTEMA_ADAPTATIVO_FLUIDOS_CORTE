# Template LaTeX do Relatório

## Finalidade

Esta pasta contém a documentação de apoio para a estrutura LaTeX do relatório técnico final do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

O objetivo desta área é registrar as regras de utilização do template e facilitar a manutenção da estrutura do relatório.

Ela não deve funcionar como uma segunda versão independente do relatório final.

O arquivo principal de entrega deverá permanecer em:

```text
report/final/main.tex
```

---

## Template oficial da professora

O relatório final deverá seguir o modelo fornecido pela professora.

As principais exigências confirmadas são:

```text
máximo de 4 páginas
incluindo referências

papel A4

margens de 1,5 cm

fonte principal em 10 pt

espaçamento simples

resumo em português
com até 1200 caracteres com espaço

3 a 5 palavras-chave

texto principal em duas colunas

citações numéricas no texto

referências conforme ABNT
```

Essas regras possuem prioridade sobre modelos genéricos criados anteriormente no projeto.

---

## Estrutura oficial

O relatório deverá seguir as seções definidas pela professora:

```text
Introdução

Material e Método

Resultados e Discussão

Conclusões

Referências
```

Não deverão ser criadas seções adicionais apenas porque existem etapas internas detalhadas no projeto.

---

## Relação com os relatórios internos

O projeto possui relatórios de etapa mais detalhados em:

```text
report/stages/
├── 01_pacheco/
├── 02_benjamin/
├── 03_vitor/
└── 04_marco/
```

Esses documentos servem para:

```text
documentação
auditoria
rastreabilidade
handoff
reprodutibilidade
```

Eles podem conter muito mais informação que o relatório oficial.

A relação esperada é:

```text
relatórios internos
↓
resultados aprovados
↓
integração
↓
seleção do conteúdo essencial
↓
report/final/main.tex
↓
relatório técnico de até 4 páginas
```

---

## Fonte única da verdade

Resultados científicos não deverão ser digitados livremente em diferentes arquivos.

A origem dos resultados deverá ser:

```text
dados
↓
código em R
↓
pipeline
↓
validação
↓
resultado aprovado
↓
relatório
```

O relatório final é um produto de comunicação dos resultados, não a fonte dos cálculos.

---

## Responsabilidade dos integrantes

Nesta fase estamos apenas preparando a base.

Os integrantes serão responsáveis posteriormente por:

```text
implementar o código em R
executar as análises
validar os resultados
gerar tabelas
gerar gráficos
selecionar referências
interpretar os resultados
preencher o relatório
compilar o PDF
```

Nenhum desses resultados deve ser inventado durante a preparação da estrutura.

---

## Contribuição de Pacheco

A etapa de Pacheco deverá fornecer ao relatório final apenas os elementos essenciais de:

```text
origem dos dados
auditoria
reconciliação
base canônica
principais limitações dos dados
```

A documentação completa permanecerá em:

```text
report/stages/01_pacheco/
```

---

## Contribuição de Benjamin

A etapa de Benjamin deverá fornecer os elementos essenciais de:

```text
ADA relevante
redundância
conformidade
critérios
normalização
CRITIC
pesos
```

A documentação completa permanecerá em:

```text
report/stages/02_benjamin/
```

---

## Contribuição de Vitor

A etapa de Vitor deverá fornecer os elementos essenciais de:

```text
TOPSIS
ranking
top 3
cenários
Pareto
sensibilidade
robustez
```

A documentação completa permanecerá em:

```text
report/stages/03_vitor/
```

---

## Contribuição de Marco

Marco será responsável principalmente pela integração e comunicação.

Sua função será:

```text
reunir resultados aprovados
↓
verificar consistência
↓
condensar conteúdo
↓
montar relatório
↓
montar apresentação
```

Marco não deverá recalcular silenciosamente os resultados das etapas anteriores.

A documentação de integração está em:

```text
report/stages/04_marco/
```

---

## Introdução

A introdução final deverá ser curta e objetiva.

Deverá apresentar:

```text
contexto
+
relevância
+
problema
+
objetivo
```

A orientação da professora é utilizar fundamentação breve, com poucas referências relevantes.

---

## Material e Método

A seção deverá permitir compreender e reproduzir a análise.

De forma condensada, deverá explicar:

```text
dados
↓
auditoria
↓
critérios
↓
normalização
↓
CRITIC
↓
TOPSIS
↓
robustez
```

A linguagem computacional principal deverá ser identificada como:

```text
R
```

Outras ferramentas deverão ser mencionadas somente se tiverem sido realmente utilizadas.

---

## Resultados e Discussão

Essa seção deverá combinar:

```text
resultado
+
interpretação
```

e não apenas apresentar gráficos e tabelas.

Os elementos candidatos incluem:

```text
principais achados da auditoria
pesos CRITIC
ranking TOPSIS
top 3
conformidade
Pareto
sensibilidade
robustez
```

O espaço disponível determinará quais elementos serão realmente incluídos.

---

## Conclusões

A conclusão deverá responder diretamente ao objetivo do trabalho.

Ela deverá considerar:

```text
ranking
+
diferença entre alternativas
+
conformidade
+
Pareto
+
sensibilidade
+
robustez
```

Não será obrigatório apresentar um vencedor único caso as análises indiquem instabilidade ou alternativas praticamente equivalentes.

---

## Referências

A professora determinou:

```text
citações numéricas no texto
```

por exemplo:

```text
(1)
(1--3)
```

e referências formatadas conforme:

```text
ABNT
```

A base bibliográfica do projeto está em:

```text
report/final/references.bib
```

Nenhuma referência deverá ser inventada.

---

## Limite de quatro páginas

O limite inclui:

```text
título
autores
afiliação
resumo
palavras-chave
texto
equações
tabelas
figuras
conclusões
referências
```

Portanto, o relatório final deverá priorizar densidade informacional.

---

## Estratégia de síntese

Se o relatório ultrapassar quatro páginas, priorizar a redução nesta ordem:

```text
1. redundâncias textuais
2. detalhes internos da auditoria
3. detalhes auxiliares da ADA
4. tabelas secundárias
5. figuras secundárias
6. explicações metodológicas não essenciais
```

Não alterar silenciosamente:

```text
margens
fonte
tamanho da página
```

apenas para cumprir o limite.

---

## Figuras

As figuras oficiais do relatório deverão ser derivadas dos resultados realmente produzidos.

A origem preferencial será:

```text
R
↓
arquivo de figura
↓
report/final/figures/
↓
main.tex
```

Não corrigir valores científicos manualmente em editores gráficos.

---

## Tabelas

Tabelas científicas deverão ser geradas ou alimentadas a partir dos resultados aprovados.

Pasta prevista:

```text
report/final/tables/
```

Evitar copiar e colar números manualmente quando houver possibilidade de geração reproduzível.

---

## Arquivos de saída

Os PDFs ou demais produtos compilados deverão ser armazenados em:

```text
report/final/output/
```

Essa pasta é destinada a produtos gerados, e não a arquivos-fonte.

---

## `chapters/`

A estrutura atual possui:

```text
report/final/chapters/
```

Como o relatório oficial possui somente quatro páginas, os integrantes deverão decidir durante a implementação se essa pasta será efetivamente necessária.

Não é obrigatório fragmentar o relatório em capítulos.

O arquivo oficial poderá permanecer integralmente em:

```text
report/final/main.tex
```

se isso simplificar a manutenção.

---

## Não duplicar conteúdo

Evitar manter simultaneamente:

```text
main.tex com texto A
```

e:

```text
chapters/*.tex com texto B
```

representando versões diferentes do mesmo relatório.

Deverá existir apenas uma cadeia oficial de compilação.

---

## Material externo

Materiais fornecidos pela professora deverão ser preservados e classificados corretamente.

Exemplos:

```text
template oficial
logos
orientações
normas
referências
documentos técnicos
```

Esses materiais não devem ser confundidos com resultados gerados pelo projeto.

---

## Logos

O template oficial da professora utiliza:

```text
logos/unesp.jpg
logos/estat.png
```

Os arquivos reais deverão ser adicionados somente quando estiverem disponíveis.

Não utilizar substitutos não confirmados.

---

## Informações institucionais

Antes da entrega deverão ser confirmados:

```text
nomes completos dos integrantes
curso
departamento
e-mail
nome da professora
eventuais informações adicionais solicitadas
```

Enquanto isso, utilizar:

```text
TO_BE_FILLED
```

---

## Arredondamento

Os cálculos deverão permanecer em precisão completa.

No relatório, números podem ser arredondados para melhorar a leitura.

Entretanto:

```text
arredondamento de apresentação
≠
arredondamento de cálculo
```

---

## Coerência com a apresentação

Antes da entrega, relatório e apresentação deverão conter:

```text
mesmo ranking
mesmo top 3
mesmos pesos
mesmo Pareto
mesma conclusão de robustez
mesmas limitações
mesma conclusão final
```

---

## Alterações upstream

Se uma alteração ocorrer em uma etapa anterior:

```text
dados
critérios
normalização
pesos
ranking
```

os resultados dependentes deverão ser reexecutados.

O texto final só deverá ser atualizado após a nova versão científica estar aprovada.

---

## Estado atual

Nesta fase:

```text
REPORT_TEMPLATE_STATUS = BASE_PREPARED
FINAL_RESULTS = NOT_EXECUTED
FINAL_TEXT = NOT_WRITTEN
FINAL_PDF = NOT_CREATED
```

Isso é esperado.

A estrutura está sendo preparada antes da execução pelos integrantes.

---

## Checklist futuro

Antes da entrega:

```text
[ ] template oficial preservado
[ ] máximo de 4 páginas
[ ] nomes completos
[ ] afiliação correta
[ ] e-mail correto
[ ] logos oficiais
[ ] resumo <= 1200 caracteres com espaço
[ ] 3 a 5 palavras-chave
[ ] objetivo explícito
[ ] método reproduzível
[ ] R identificado
[ ] resultados oficiais
[ ] figuras atualizadas
[ ] tabelas atualizadas
[ ] discussão interpretativa
[ ] conclusão coerente
[ ] limitações essenciais
[ ] referências reais
[ ] citações numéricas
[ ] ABNT revisada
[ ] PDF conferido
```

---

## Princípio final

> Esta pasta existe para apoiar a construção do relatório, não para antecipar o trabalho científico dos integrantes. O relatório final somente deverá ser preenchido depois que os dados, métodos e resultados correspondentes tiverem sido executados e validados.