# Apresentação em LaTeX

## Finalidade

Esta pasta é destinada à construção da apresentação final do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

A apresentação deverá ser desenvolvida em:

```text
LaTeX
+
Beamer
```

e utilizar apenas resultados científicos já executados, validados e aprovados.

---

# Estado atual

```text
PRESENTATION_STATUS = BASE_PREPARED

SCIENTIFIC_RESULTS = NOT_GENERATED

FINAL_SLIDES = NOT_CREATED
```

Nesta fase, esta pasta funciona apenas como base estrutural.

---

# Relação com os resultados

A apresentação deverá ser construída a partir de resultados oficiais provenientes de:

```text
results/
report/stages/
report/final/
handoffs/
```

Não inserir resultados preliminares ou valores ainda não validados.

---

# Regra principal

A apresentação deve seguir:

```text
dados validados
↓
análises aprovadas
↓
resultados finais
↓
síntese científica
↓
slides
```

e nunca:

```text
slide
↓
valor digitado manualmente
↓
resultado sem rastreabilidade
```

---

# Figuras

As figuras utilizadas na apresentação deverão ser armazenadas em:

```text
presentation/figures/
```

quando forem produzidas.

Atualmente essa pasta pode permanecer vazia, contendo apenas:

```text
.gitkeep
```

---

# Figuras científicas

Figuras que representem resultados deverão ser:

```text
geradas por código
validadas
rastreáveis
coerentes com o relatório
```

Não alterar manualmente valores científicos em figuras.

---

# Material externo

Logos, imagens institucionais ou outros materiais fornecidos pela professora deverão ser preservados conforme sua origem e função.

Não apresentar material externo como se fosse resultado produzido pelo grupo.

---

# Resultados que poderão aparecer futuramente

Dependendo dos resultados reais, a apresentação poderá incluir:

```text
estrutura dos dados
auditoria
ADA
critérios
conformidade
pesos CRITIC
ranking TOPSIS
cenários
Pareto
sensibilidade
robustez
conclusões
```

A seleção final dependerá do que for realmente executado e aprovado.

---

# Organização narrativa

A apresentação deverá seguir uma sequência coerente.

Estrutura conceitual:

```text
problema
↓
dados
↓
auditoria
↓
metodologia
↓
resultados
↓
robustez
↓
conclusões
```

---

# Não sobrecarregar os slides

Evitar:

```text
parágrafos longos
tabelas muito grandes
fórmulas desnecessárias
excesso de números
```

Priorizar:

```text
mensagem principal
figuras
tabelas resumidas
interpretação
```

---

# Fórmulas

Somente fórmulas essenciais deverão aparecer.

Exemplos possíveis:

```text
CRITIC
TOPSIS
```

quando forem necessárias para explicar a metodologia.

---

# CRITIC

Caso apresentado, deixar claro que:

```text
peso CRITIC
=
peso informacional
```

e não:

```text
importância técnica absoluta
```

---

# TOPSIS

Caso apresentado, explicar que o ranking depende de:

```text
critérios
normalização
pesos
alternativas
```

e deverá ser acompanhado pela análise de robustez.

---

# Conformidade

Conformidade técnica deverá permanecer separada de desempenho multicritério.

A apresentação poderá mostrar, por exemplo:

```text
ranking
+
TOPSIS
+
conformidade
+
robustez
```

sem misturar os conceitos.

---

# Robustez

O ranking final deverá ser apresentado junto das evidências de robustez quando essas análises estiverem concluídas.

Possíveis elementos:

```text
cenários
LOCO
LOAO
normalização alternativa
rank reversal
sensibilidade dos pesos
Pareto
```

---

# Consistência com o relatório

A apresentação deverá ser consistente com:

```text
report/final/main.tex
```

Não poderá existir:

```text
valor diferente
ranking diferente
peso diferente
conclusão diferente
```

entre relatório e apresentação sem justificativa formal.

---

# Responsabilidade

A integração final da apresentação é responsabilidade principal de:

```text
Marco
```

com revisão de:

```text
Pacheco
Benjamin
Vitor
Marco
```

---

# Revisão

Antes da apresentação final:

```text
[ ] resultados conferidos
[ ] ranking conferido
[ ] pesos conferidos
[ ] conformidade conferida
[ ] robustez conferida
[ ] figuras legíveis
[ ] tabelas legíveis
[ ] texto revisado
[ ] relatório e slides consistentes
[ ] apresentação ensaiada
```

---

# Fonte dos números

Todo número científico apresentado deverá ser rastreável até um resultado validado do projeto.

Evitar digitação manual sempre que possível.

---

# Arquivos futuros

Quando a apresentação for implementada, esta pasta poderá conter arquivos como:

```text
main.tex
preamble.tex
theme.tex
sections/
```

somente se essa estrutura fizer parte da implementação realmente adotada.

Não é necessário criar novos arquivos apenas por causa deste README.

---

# Status

```text
PRESENTATION_LATEX_STATUS = BASE_PREPARED

CONTENT_STATUS = NOT_WRITTEN

RESULTS_STATUS = NOT_GENERATED

COMPILATION_STATUS = NOT_EXECUTED
```

---

# Princípio final

> A apresentação deve ser uma síntese fiel do trabalho executado. Ela não deve criar resultados, reinterpretar silenciosamente a metodologia ou apresentar como definitiva uma conclusão que ainda não tenha sido validada.