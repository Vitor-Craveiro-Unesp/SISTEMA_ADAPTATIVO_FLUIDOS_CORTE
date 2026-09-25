# Exemplo Base de Tabelas

## Finalidade

Esta pasta funciona como referência para a criação das tabelas utilizadas no projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Ela contém apenas a estrutura conceitual e as regras de qualidade que deverão ser seguidas pelos integrantes durante a execução.

Nesta fase:

```text
TABLES_STATUS = NOT_GENERATED
```

Nenhuma tabela científica precisa ser criada agora.

---

## Princípio principal

As tabelas científicas devem representar resultados efetivamente produzidos pelas análises.

A cadeia esperada é:

```text
dados
↓
código em R
↓
resultado validado
↓
tabela
↓
relatório / apresentação
```

Evitar:

```text
resultado
↓
copiar manualmente
↓
digitar novamente na tabela
```

sempre que for possível automatizar o processo.

---

# Tipos de tabelas esperados

Dependendo dos resultados obtidos, o projeto poderá gerar tabelas relacionadas a:

```text
auditoria
ADA
conformidade
critérios
matriz de decisão
normalização
CRITIC
TOPSIS
ranking
cenários
Pareto
sensibilidade
robustez
```

Nem todas precisam aparecer no relatório ou na apresentação final.

---

# Tabelas de auditoria

Pacheco poderá produzir tabelas contendo, por exemplo:

```text
aba
variável
fluido
valor original
valor recalculado
diferença
status
decisão
```

Essas tabelas deverão permitir rastrear inconsistências encontradas na fonte original.

---

# Tabela de inventário

Uma tabela de inventário poderá conter:

| Campo | Descrição |
|---|---|
| Aba | nome da aba |
| Linhas | quantidade observada |
| Colunas | quantidade observada |
| Fórmulas | presença ou quantidade |
| Erros | problemas identificados |
| Status | situação da aba |

Os valores reais deverão ser gerados durante a auditoria.

---

# Tabela de problemas

Quando apropriado, a estrutura poderá incluir:

| Issue ID | Local | Variável | Descrição | Severidade | Status |
|---|---|---|---|---|---|
| `TO_BE_FILLED` |  |  |  |  |  |

Nenhum problema deve ser inventado para preencher o modelo.

---

# Tabela de reconciliação

Poderá ser utilizada para documentar divergências entre fontes:

| Issue ID | Fonte A | Fonte B | Decisão | Justificativa |
|---|---|---|---|---|
| `TO_BE_FILLED` |  |  |  |  |

---

# Tabelas de ADA

As tabelas exploratórias poderão conter:

```text
n
média
mediana
desvio-padrão
mínimo
máximo
quartis
missing
```

quando essas medidas forem adequadas às variáveis analisadas.

Exemplo estrutural:

| Variável | n | Média | Mediana | DP | Mín. | Máx. |
|---|---:|---:|---:|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |  |  |  |

---

# Tabela de correlação

Caso uma matriz de correlação seja apresentada, deverá ser identificado:

```text
método utilizado
tratamento de missing
variáveis incluídas
```

Exemplo:

```text
CORRELATION_METHOD = TO_BE_FILLED
```

Não apresentar apenas números sem contextualizar o método.

---

# Tabela de critérios

Benjamin poderá produzir uma tabela contendo:

| Critério | Descrição | Unidade | Direção | Status |
|---|---|---|---|---|
| `TO_BE_FILLED` |  |  |  |  |

Direções possíveis:

```text
BENEFIT
COST
TARGET
RESTRICTION
DIAGNOSTIC
```

---

# Critérios excluídos

Critérios removidos da análise devem permanecer documentados.

Exemplo:

| Variável | Status | Motivo |
|---|---|---|
| `TO_BE_FILLED` | `REJECTED` | `TO_BE_FILLED` |

A exclusão deve possuir justificativa estatística, técnica ou de qualidade dos dados.

---

# Tabela de conformidade

Quando existirem especificações confirmadas:

| Fluido | Variável | Valor observado | Regra | Limite | Status |
|---|---|---:|---|---:|---|
| `TO_BE_FILLED` |  |  |  |  |  |

Possíveis status:

```text
CONFORMING
NON_CONFORMING
PENDING
UNKNOWN
```

A terminologia definitiva deverá ser definida pelos integrantes.

---

# Matriz de decisão

A matriz de decisão terá conceitualmente:

```text
linhas = alternativas
colunas = critérios
```

Representação:

\[
X=[x_{ij}]
\]

Exemplo estrutural:

| Fluido | Critério 1 | Critério 2 | Critério 3 |
|---|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |

Essa tabela deverá ser produzida a partir da base aprovada.

---

# Matriz normalizada

Quando necessário apresentar:

| Fluido | Critério 1 | Critério 2 | Critério 3 |
|---|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |

A tabela deverá indicar qual normalização foi utilizada.

```text
NORMALIZATION_METHOD = TO_BE_FILLED
```

---

# Tabela CRITIC

A saída do CRITIC poderá ser organizada como:

| Critério | DP | Conflito | Informação \(C_j\) | Peso \(w_j\) |
|---|---:|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |  |

Deverá ser validado:

\[
\sum_j w_j \approx 1
\]

---

# Interpretação dos pesos

O título ou nota da tabela deve evitar interpretações incorretas.

Preferir:

```text
Pesos objetivos obtidos pelo método CRITIC
```

Evitar:

```text
Importância técnica dos critérios
```

salvo se houver outra fundamentação independente.

---

# Tabela TOPSIS

Uma tabela principal poderá conter:

| Fluido | \(S_i^+\) | \(S_i^-\) | \(C_i\) | Posição |
|---|---:|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |  |

onde:

\[
C_i=
\frac{S_i^-}
{S_i^+ + S_i^-}
\]

---

# Ranking principal

Uma versão mais compacta poderá conter:

| Posição | Fluido | TOPSIS | Conformidade |
|---:|---|---:|---|
| 1 | `TO_BE_FILLED` |  |  |
| 2 | `TO_BE_FILLED` |  |  |
| 3 | `TO_BE_FILLED` |  |  |

Essa estrutura poderá ser especialmente útil no relatório final.

---

# Precisão do ranking

O ranking deverá ser calculado com os valores completos.

Os valores exibidos poderão ser arredondados.

Portanto:

```text
valor exibido
≠
valor utilizado no cálculo
```

quando houver arredondamento apenas para comunicação.

---

# Empates aparentes

Se dois valores parecerem iguais após arredondamento, a tabela não deverá criar um empate artificial.

A posição oficial deverá utilizar a precisão integral.

---

# Tabela de cenários

Exemplo estrutural:

| Fluido | Cenário base | Cenário 1 | Cenário 2 |
|---|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |

ou:

| Cenário | Fluido | TOPSIS | Posição |
|---|---|---:|---:|
| `TO_BE_FILLED` |  |  |  |

A estrutura definitiva dependerá do número de cenários realmente utilizados.

---

# Tabela de Pareto

Poderá conter:

| Fluido | Fronteira | Dominado | Nº de dominadores |
|---|---:|---|---:|
| `TO_BE_FILLED` |  |  |  |

ou estrutura equivalente.

---

# Tabela de sensibilidade aos pesos

Poderá registrar:

| Perturbação | Critério | 1º lugar | Top 3 | Alteração |
|---|---|---|---|---|
| `TO_BE_FILLED` |  |  |  |  |

A estrutura real deverá refletir a implementação realizada.

---

# Leave-one-criterion-out

Exemplo:

| Critério removido | 1º lugar | Mudança no top 3 | Correlação com ranking-base |
|---|---|---|---:|
| `TO_BE_FILLED` |  |  |  |

---

# Leave-one-alternative-out

Exemplo:

| Alternativa removida | Novo 1º lugar | Rank reversal | Observação |
|---|---|---|---|
| `TO_BE_FILLED` |  |  |  |

---

# Tabela de robustez

Uma tabela sintética poderá conter:

| Fluido | 1º lugar (%) | Top 3 (%) | Posição média | Melhor | Pior |
|---|---:|---:|---:|---:|---:|
| `TO_BE_FILLED` |  |  |  |  |  |

Se forem utilizadas frequências, elas deverão ser descritas como:

```text
frequência nas configurações avaliadas
```

e não como:

```text
probabilidade real de ser o melhor
```

---

# Títulos

Toda tabela apresentada externamente deverá possuir título suficientemente informativo.

Preferir:

```text
Tabela 1. Pesos dos critérios obtidos pelo método CRITIC.
```

em vez de:

```text
Tabela 1. Resultados.
```

---

# Notas

Quando necessário, incluir notas para explicar:

```text
abreviações
unidades
arredondamento
missing
restrições
métodos
símbolos
```

---

# Unidades

Sempre que uma unidade for relevante para interpretação, ela deverá aparecer:

```text
no cabeçalho
```

ou:

```text
em nota
```

de forma inequívoca.

---

# Casas decimais

O número de casas decimais deve ser escolhido de acordo com:

```text
precisão experimental
escala
legibilidade
finalidade da tabela
```

Não utilizar uma quantidade excessiva de casas apenas porque o software as fornece.

---

# Alinhamento

Valores numéricos devem preferencialmente ser alinhados de forma consistente.

Exemplo:

```text
texto → alinhamento à esquerda
números → alinhamento à direita ou decimal
```

---

# Missing

Valores ausentes não devem aparecer como:

```text
0
```

a menos que zero seja realmente o valor observado.

Utilizar representação clara, como:

```text
NA
--
```

ou outra convenção definida pelo grupo.

---

# Valores não aplicáveis

Quando um valor não for aplicável, diferenciá-lo de missing quando necessário.

Exemplo:

```text
NA = ausente
N/A = não aplicável
```

desde que essa convenção seja documentada.

---

# Valores pendentes

Durante a execução interna poderão existir:

```text
TO_BE_FILLED
```

mas esses placeholders não deverão permanecer nas tabelas finais apresentadas à professora.

---

# Destaques visuais

Evitar alterar células manualmente para destacar resultados.

Se houver destaque por:

```text
melhor valor
top 3
não conformidade
```

preferir gerar essa regra de maneira reproduzível ou aplicá-la de forma consistente.

---

# Cores

Tabelas científicas devem permanecer compreensíveis mesmo sem depender exclusivamente de cores.

Se cores forem utilizadas:

```text
cor
+
texto/símbolo
```

deve permitir interpretar o status.

---

# Tabelas no relatório final

O relatório possui limite máximo de:

```text
4 páginas incluindo referências
```

Portanto, poucas tabelas deverão ser selecionadas.

Uma tabela compacta pode substituir vários parágrafos quando bem construída.

---

# Tabelas na apresentação

Evitar tabelas extensas em slides.

Preferir:

```text
top 3
principais pesos
resultados essenciais
```

em vez de exibir toda a matriz quando ela não for necessária para a explicação.

---

# Tabelas internas

Tabelas detalhadas podem permanecer nos relatórios de etapa mesmo quando não forem utilizadas na entrega final.

Exemplos:

```text
lista completa de inconsistências
matriz completa de correlação
todos os cenários
todos os resultados de sensibilidade
```

---

# Local dos resultados

As tabelas científicas geradas pela pipeline deverão ser armazenadas nas áreas apropriadas do projeto.

Exemplos já previstos:

```text
results/tables/
```

e, quando necessárias para os relatórios:

```text
report/stages/.../tables/
report/final/tables/
```

A organização definitiva será realizada pelos integrantes durante a implementação.

---

# Esta pasta não é `results/`

A pasta:

```text
templates/tables/EXEMPLO_BASE/
```

é apenas uma referência estrutural.

Ela não deve receber os resultados oficiais do projeto.

---

# Material externo

Tabelas fornecidas pela professora devem ser classificadas de acordo com sua função.

Se forem:

```text
dados originais
```

devem ser preservadas junto à fonte correspondente.

Se forem:

```text
modelo visual
```

podem ser usadas como referência.

Não apresentar uma tabela externa como resultado do grupo.

---

# Rastreabilidade

Uma tabela científica deve permitir reconstruir conceitualmente:

```text
célula apresentada
↓
resultado calculado
↓
código
↓
base utilizada
```

---

# Reprodutibilidade

Sempre que possível, as tabelas deverão ser geradas diretamente em R.

Pacotes e soluções poderão ser escolhidos pelos integrantes durante a implementação.

Esta base não impõe um pacote específico.

---

# Formato dos arquivos

Dependendo da finalidade, tabelas poderão ser exportadas como:

```text
CSV
TSV
LaTeX
HTML
RDS
```

ou outro formato tecnicamente adequado.

A escolha deverá ser feita durante a implementação.

---

# CSV

Se tabelas forem exportadas em CSV, preservar:

```text
nomes claros
tipos coerentes
decimal consistente
encoding adequado
```

---

# LaTeX

Tabelas destinadas ao relatório poderão futuramente ser geradas em formato compatível com LaTeX.

O objetivo é reduzir a digitação manual de resultados.

---

# Não fixar pacote agora

Nesta fase não será escolhido um pacote obrigatório para tabelas.

Os integrantes poderão utilizar, conforme necessidade real:

```text
knitr
gt
kableExtra
xtable
flextable
```

ou outras soluções adequadas.

A escolha deverá ocorrer durante a implementação.

---

# Versionamento

Quando uma tabela corresponder a resultado oficial, deve ser possível relacioná-la à versão:

```text
dados
método
resultado
```

correspondente.

---

# Atualização

Se um resultado upstream for alterado:

```text
base
critério
normalização
peso
ranking
```

a tabela dependente deverá ser regenerada.

Não atualizar números manualmente apenas para sincronizar a apresentação.

---

# Revisão

Antes de utilizar uma tabela externamente:

```text
[ ] título correto
[ ] fonte correta dos dados
[ ] linhas corretas
[ ] colunas corretas
[ ] unidades corretas
[ ] casas decimais adequadas
[ ] missing identificados
[ ] nenhum valor manual divergente
[ ] interpretação coerente
[ ] versão correta
```

---

# Tabela oficial versus exploratória

É importante distinguir:

```text
EXPLORATORY
```

de:

```text
APPROVED
```

Uma tabela gerada durante testes não deve ser automaticamente utilizada no relatório final.

---

# Responsabilidade dos integrantes

Nesta fase estamos apenas preparando a base.

Os integrantes serão responsáveis por:

```text
definir as tabelas necessárias
implementar sua geração
executar o código
validar os resultados
escolher quais tabelas apresentar
formatar a versão final
```

---

# Estado atual

```text
TABLE_TEMPLATE_STATUS = BASE_PREPARED

SCIENTIFIC_TABLES = NOT_GENERATED

AUDIT_TABLES = NOT_GENERATED

ADA_TABLES = NOT_GENERATED

CRITIC_TABLES = NOT_GENERATED

TOPSIS_TABLES = NOT_GENERATED

ROBUSTNESS_TABLES = NOT_GENERATED
```

---

# Princípio final

> Uma boa tabela deve condensar informação sem esconder sua origem. Os números apresentados devem ser consequência direta da análise reproduzível dos integrantes e não de preenchimento manual da estrutura.