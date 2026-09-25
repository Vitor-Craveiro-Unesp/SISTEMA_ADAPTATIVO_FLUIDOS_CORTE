# Guia de Estudos

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Esta pasta reúne materiais de estudo necessários para compreender, implementar, revisar e apresentar o projeto.

O objetivo não é apenas reunir links.

A estrutura deve permitir que os integrantes entendam:

```text
o problema técnico
↓
os dados
↓
a estatística
↓
a decisão multicritério
↓
a implementação
↓
a robustez
↓
a comunicação científica
```

---

# 1. Estrutura

```text
estudo/
│
├── README.md
│
├── link_video/
│   └── arquivos .txt com vídeos
│
└── link_material_estudo/
    └── arquivos .txt com materiais escritos
```

---

# 2. Idiomas

Os materiais são separados em:

```text
PT
→ português

EN
→ inglês
```

Sempre que possível, cada assunto deverá possuir:

```text
material em português
+
material em inglês
```

O material em inglês não é apenas complementar.

Em alguns temas técnicos, especialmente:

```text
CRITIC
TOPSIS
MCDM
rank reversal
sensitivity analysis
robustness analysis
```

a literatura mais completa pode estar em inglês.

---

# 3. Tipos de material

## `link_video/`

Contém links para:

```text
aulas
cursos
seminários
demonstrações
explicações conceituais
implementações comentadas
```

---

## `link_material_estudo/`

Contém links para:

```text
artigos
livros
capítulos
apostilas
documentação oficial
manuais
papers metodológicos
tutoriais técnicos
```

---

# 4. Regra de qualidade

Não adicionar qualquer resultado encontrado na internet.

Preferir:

```text
universidades
documentação oficial
artigos científicos
livros
editoras acadêmicas
autores reconhecidos
instituições técnicas
canais educacionais confiáveis
```

---

# 5. Evitar como fonte principal

Evitar depender exclusivamente de:

```text
blogs sem referência
sites de conteúdo automático
resumos gerados por IA
vídeos sem fonte
posts de redes sociais
código sem explicação
```

Esses materiais podem eventualmente ajudar na intuição, mas não devem substituir fontes técnicas.

---

# 6. Material original versus material de estudo

A pasta:

```text
estudo/
```

contém referências educacionais.

Ela não substitui:

```text
data/raw/
```

nem:

```text
material oficial fornecido pela professora
```

---

# 7. Prioridade de fontes

Quando houver conflito:

```text
material oficial da disciplina/professora
↓
fonte técnica ou científica primária
↓
documentação oficial
↓
material didático confiável
↓
conteúdo complementar
```

---

# 8. Ordem geral de estudo

A sequência recomendada é:

```text
01 — Fluidos de corte
↓
02 — Auditoria e qualidade de dados
↓
03 — ADA / EDA
↓
04 — Correlação, redundância e PCA
↓
05 — Conformidade e construção de critérios
↓
06 — MCDM / MCDA
↓
07 — CRITIC
↓
08 — TOPSIS
↓
09 — Pareto
↓
10 — Sensibilidade e robustez
↓
11 — R e reprodutibilidade
↓
12 — Git, Docker e pipeline
↓
13 — Quarto e LaTeX
↓
14 — Comunicação científica
```

---

# 9. Nível 01 — Fluidos de corte

Arquivos:

```text
01_FLUIDOS_CORTE_PT.txt
01_CUTTING_FLUIDS_EN.txt
```

Objetivo:

```text
entender o domínio do problema
```

Estudar:

```text
usinagem
função do fluido de corte
lubrificação
refrigeração
desgaste de ferramenta
vida de ferramenta
acabamento superficial
cavaco
emulsões
concentração
propriedades físico-químicas
aspectos econômicos
```

---

# 10. Nível 02 — Auditoria de dados

Arquivos:

```text
02_AUDITORIA_DADOS_PT.txt
02_DATA_AUDITING_EN.txt
```

Estudar:

```text
data quality
missing
duplicatas
tipos
unidades
consistência
validação
reconciliação
proveniência
data lineage
dados derivados
auditoria de fórmulas
```

Regra importante:

```text
detectar
≠
corrigir
```

---

# 11. Nível 03 — ADA / EDA

Arquivos:

```text
03_ADA_PT.txt
03_EDA_EN.txt
```

Estudar:

```text
estatística descritiva
distribuições
média
mediana
variância
desvio-padrão
quartis
outliers
visualização
comparação entre grupos
exploração de padrões
```

---

# 12. Nível 04 — Correlação, redundância e PCA

Arquivos:

```text
04_CORRELACAO_REDUNDANCIA_PCA_PT.txt
04_CORRELATION_REDUNDANCY_PCA_EN.txt
```

Estudar:

```text
correlação de Pearson
correlação de Spearman
matriz de correlação
redundância
multicolinearidade
PCA
loadings
scores
variância explicada
padronização
```

Regra:

```text
correlação
≠
causalidade
```

---

# 13. Nível 05 — Conformidade e critérios

Arquivos:

```text
05_CONFORMIDADE_CRITERIOS_PT.txt
05_CONFORMITY_CRITERIA_EN.txt
```

Estudar:

```text
requisito técnico
limites
restrições
critério
variável diagnóstica
benefit
cost
target
matriz de decisão
conformidade
```

Regra:

```text
CONFORMIDADE
≠
RANKING
```

---

# 14. Nível 06 — MCDM / MCDA

Arquivos:

```text
06_MCDM_PT.txt
06_MCDM_EN.txt
```

Estudar:

```text
Multiple-Criteria Decision Making
Multiple-Criteria Decision Analysis
alternativas
critérios
pesos
matriz de decisão
normalização
compensação
métodos objetivos
métodos subjetivos
```

Esse nível deve ser compreendido antes de estudar CRITIC e TOPSIS isoladamente.

---

# 15. Nível 07 — CRITIC

Arquivos:

```text
07_CRITIC_PT.txt
07_CRITIC_EN.txt
```

Estudar profundamente:

\[
C_j
=
\sigma_j
\sum_k(1-r_{jk})
\]

e:

\[
w_j
=
\frac{C_j}
{\sum_j C_j}
\]

Compreender:

```text
dispersão
contraste
correlação
conflito
redundância
peso informacional
```

Regra do projeto:

```text
1-r
```

é a formulação principal.

Não substituir silenciosamente por:

```text
1-|r|
```

---

# 16. Interpretação do CRITIC

Compreender que:

```text
peso CRITIC
=
peso informacional
```

e não necessariamente:

```text
importância técnica absoluta
```

---

# 17. Nível 08 — TOPSIS

Arquivos:

```text
08_TOPSIS_PT.txt
08_TOPSIS_EN.txt
```

Estudar profundamente:

```text
matriz normalizada
pesos
matriz ponderada
ideal positivo
ideal negativo
distância Euclidiana
coeficiente de proximidade
ranking
```

Fórmulas principais:

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
{S_i^+ + S_i^-}
\]

---

# 18. Nível 09 — Pareto

Arquivos:

```text
09_PARETO_PT.txt
09_PARETO_EN.txt
```

Estudar:

```text
dominância
não dominância
fronteira de Pareto
trade-off
eficiência de Pareto
```

Regra:

```text
PARETO NÃO UTILIZA PESOS
```

e:

```text
não dominado
≠
vencedor automático
```

---

# 19. Nível 10 — Sensibilidade e robustez

Arquivos:

```text
10_SENSIBILIDADE_ROBUSTEZ_PT.txt
10_SENSITIVITY_ROBUSTNESS_EN.txt
```

Estudar:

```text
sensitivity analysis
robustness analysis
perturbação de pesos
cenários
LOCO
LOAO
rank reversal
estabilidade do ranking
comparação entre rankings
```

---

# 20. LOCO

```text
LOCO
=
Leave-One-Criterion-Out
```

Compreender:

```text
remoção de um critério
↓
novo sistema
↓
novo ranking
↓
comparação
```

---

# 21. LOAO

```text
LOAO
=
Leave-One-Alternative-Out
```

Compreender:

```text
remoção de uma alternativa
↓
recalcular sistema quando necessário
↓
avaliar mudanças entre alternativas restantes
```

---

# 22. Rank reversal

Estudar:

```text
por que o ranking pode mudar
quando alternativas são adicionadas ou removidas
```

Especial atenção ao TOPSIS.

---

# 23. Frequência não é probabilidade

Regra:

```text
frequência em cenários
≠
probabilidade real
```

---

# 24. Nível 11 — R e reprodutibilidade

Arquivos:

```text
11_R_REPRODUTIBILIDADE_PT.txt
11_R_REPRODUCIBILITY_EN.txt
```

Estudar:

```text
R
RStudio
projetos .Rproj
funções
data frames
tidyverse
importação
visualização
programação funcional
tratamento de erros
testes
reprodutibilidade
```

---

# 25. R — tópicos importantes

Todos devem conhecer pelo menos:

```text
objetos
vetores
listas
data.frame
tibble
funções
if
for
apply/map
pipes
NA
is.na
group_by
summarise
mutate
pivot
joins
read/write
```

---

# 26. Nível 12 — Git, Docker e pipeline

Arquivos:

```text
12_GIT_DOCKER_PIPELINE_PT.txt
12_GIT_DOCKER_PIPELINE_EN.txt
```

Estudar:

```text
Git
commit
branch
merge
pull request
.gitignore
Docker
Dockerfile
Docker Compose
renv
targets
testthat
CI
```

---

# 27. Git

Todos os integrantes devem compreender pelo menos:

```text
git status
git add
git commit
git pull
git push
git branch
git switch
merge
conflitos
```

---

# 28. Docker

Compreender:

```text
imagem
container
Dockerfile
volume
build
compose
```

---

# 29. renv

Compreender:

```text
dependências
snapshot
restore
renv.lock
```

---

# 30. targets

Compreender:

```text
pipeline
dependência
target
invalidade
reexecução
cache
```

---

# 31. testthat

Compreender:

```text
teste unitário
expect_equal
expect_true
expect_error
casos conhecidos
regressão
```

---

# 32. Nível 13 — Quarto e LaTeX

Arquivos:

```text
13_QUARTO_LATEX_PT.txt
13_QUARTO_LATEX_EN.txt
```

Estudar:

```text
Quarto
QMD
Markdown
chunks R
renderização
LaTeX
tabelas
figuras
equações
referências
Beamer
```

---

# 33. Nível 14 — Comunicação científica

Arquivos:

```text
14_COMUNICACAO_CIENTIFICA_PT.txt
14_SCIENTIFIC_COMMUNICATION_EN.txt
```

Estudar:

```text
escrita científica
interpretação
resultados
discussão
conclusão
limitações
visualização
apresentação oral
storytelling científico
```

---

# 34. Ordem de estudo de Pacheco

Prioridade alta:

```text
01 — Fluidos de corte
02 — Auditoria de dados
03 — ADA
11 — R e reprodutibilidade
12 — Git, Docker e pipeline
```

Depois:

```text
04 — Correlação / PCA
05 — Conformidade / critérios
06 — MCDM
```

Pacheco também deve conhecer conceitualmente:

```text
CRITIC
TOPSIS
robustez
```

para entender como sua base será utilizada downstream.

---

# 35. Ordem de estudo de Benjamin

Prioridade alta:

```text
03 — ADA
04 — Correlação / PCA
05 — Conformidade / critérios
06 — MCDM
07 — CRITIC
11 — R e reprodutibilidade
```

Depois:

```text
08 — TOPSIS
09 — Pareto
10 — Robustez
```

---

# 36. Ordem de estudo de Vitor

Prioridade alta:

```text
05 — Critérios
06 — MCDM
07 — CRITIC
08 — TOPSIS
09 — Pareto
10 — Sensibilidade e robustez
11 — R e reprodutibilidade
```

Vitor deve compreender bem o CRITIC mesmo que Benjamin seja responsável por implementá-lo, pois os pesos são entrada do TOPSIS.

---

# 37. Ordem de estudo de Marco

Prioridade alta:

```text
01 — Fluidos de corte
06 — MCDM
07 — CRITIC
08 — TOPSIS
09 — Pareto
10 — Robustez
13 — Quarto / LaTeX
14 — Comunicação científica
```

Marco precisa compreender os métodos o suficiente para explicá-los corretamente.

---

# 38. Conhecimento comum obrigatório

Todos os quatro devem compreender pelo menos conceitualmente:

```text
problema de fluidos de corte
qualidade dos dados
ADA
critérios
normalização
CRITIC
TOPSIS
Pareto
robustez
reprodutibilidade
```

Especialização não significa isolamento.

---

# 39. Conhecimento do AGENTE_BOSS

O `AGENTE_BOSS` deve possuir documentação suficiente para revisar todos os tópicos:

```text
01 a 14
```

com atenção especial a:

```text
auditoria
reconciliação
critérios
normalização
CRITIC
TOPSIS
robustez
comunicação científica
```

---

# 40. Níveis de prioridade

Os materiais podem futuramente ser marcados como:

```text
[OBRIGATÓRIO]

[RECOMENDADO]

[COMPLEMENTAR]

[AVANÇADO]
```

---

# 41. Formato dos arquivos `.txt`

Cada arquivo deverá seguir preferencialmente:

```text
TEMA:
...

IDIOMA:
PT / EN

TIPO:
VÍDEO / MATERIAL

NÍVEL:
OBRIGATÓRIO / RECOMENDADO / COMPLEMENTAR / AVANÇADO

TÍTULO:
...

FONTE:
...

LINK:
...

MOTIVO:
...

PARA QUEM:
PACHECO / BENJAMIN / VITOR / MARCO / TODOS

TÓPICOS COBERTOS:
...

OBSERVAÇÕES:
...
```

---

# 42. Exemplo

```text
TEMA:
TOPSIS

IDIOMA:
EN

TIPO:
MATERIAL

NÍVEL:
OBRIGATÓRIO

TÍTULO:
TO_BE_FILLED

FONTE:
TO_BE_FILLED

LINK:
TO_BE_FILLED

MOTIVO:
Explicar a formulação e o procedimento completo do TOPSIS.

PARA QUEM:
VITOR / BENJAMIN / MARCO

TÓPICOS COBERTOS:
normalização
matriz ponderada
ideal positivo
ideal negativo
distâncias
coeficiente de proximidade

OBSERVAÇÕES:
TO_BE_FILLED
```

---

# 43. Não duplicar links sem necessidade

Se o mesmo material for útil para vários integrantes:

```text
um único registro
```

pode indicar:

```text
PARA QUEM:
TODOS
```

---

# 44. Links quebrados

Quando um link deixar de funcionar:

```text
não apagar imediatamente
```

Registrar:

```text
STATUS = BROKEN
```

e buscar substituição.

---

# 45. Data de verificação

Quando os links forem preenchidos, poderá ser utilizado:

```text
VERIFICADO_EM:
AAAA-MM-DD
```

para facilitar manutenção.

---

# 46. Fonte primária dos métodos

Sempre que possível, incluir:

```text
paper original do CRITIC
paper original ou referência clássica do TOPSIS
literatura de MCDA/MCDM
fontes acadêmicas sobre Pareto
literatura de análise de sensibilidade
```

Além de materiais didáticos.

---

# 47. Vídeo não substitui paper

Para métodos centrais:

```text
CRITIC
TOPSIS
robustez
```

é recomendável possuir:

```text
vídeo explicativo
+
material escrito
+
fonte acadêmica
```

---

# 48. Implementação não substitui teoria

Um tutorial com código R não é suficiente se o integrante não compreender:

```text
o que a fórmula faz
por que ela é usada
quais hipóteses existem
quais limitações existem
```

---

# 49. Teoria não substitui implementação

Da mesma forma, compreender a fórmula não basta.

O integrante responsável deverá conseguir:

```text
implementar
testar
validar
interpretar
```

---

# 50. Relação com os agentes

Os arquivos em:

```text
agents/
```

podem indicar quais materiais desta pasta devem ser consultados durante uma etapa.

---

# 51. Relação com instructions

```text
estudo/
→ aprender

instructions/
→ executar a etapa

agents/
→ orientar o agente

analysis/
→ registrar a execução
```

---

# 52. Relação com o relatório

Os materiais de estudo não devem ser automaticamente citados no relatório.

Uma fonte somente deve entrar em:

```text
report/final/references.bib
```

se for efetivamente utilizada como referência científica no trabalho.

---

# 53. Status atual

```text
STUDY_STRUCTURE_STATUS = BASE_PREPARED

VIDEO_LINKS_STATUS = NOT_FILLED

WRITTEN_MATERIAL_LINKS_STATUS = NOT_FILLED

PT_MATERIAL_STATUS = NOT_FILLED

EN_MATERIAL_STATUS = NOT_FILLED
```

---

# 54. Próxima etapa da pasta `estudo/`

A próxima etapa é preencher:

```text
estudo/link_video/
```

e:

```text
estudo/link_material_estudo/
```

com fontes reais e verificadas.

---

# 55. Critério de sucesso

A pasta estará completa quando o grupo possuir material suficiente para estudar:

```text
domínio técnico
+
qualidade de dados
+
estatística exploratória
+
multivariada
+
MCDA/MCDM
+
CRITIC
+
TOPSIS
+
Pareto
+
robustez
+
R
+
reprodutibilidade
+
infraestrutura
+
comunicação científica
```

em:

```text
português
+
inglês
```

---

# 56. Princípio final

> A pasta `estudo/` existe para que nenhum integrante precise aplicar um método como uma caixa-preta. Antes de implementar, é necessário compreender; antes de interpretar, é necessário compreender o método; e antes de defender o resultado, é necessário conhecer suas limitações.