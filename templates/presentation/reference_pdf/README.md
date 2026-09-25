# Reference PDF

## Finalidade

Esta pasta é destinada a armazenar arquivos PDF utilizados como **referência de layout, estrutura visual ou orientação de apresentação**.

Ela não deve ser utilizada para armazenar resultados científicos gerados pelo projeto.

Exemplos de materiais adequados para esta pasta:

```text
modelo de apresentação fornecido pela professora
PDF de referência visual
apresentação-modelo
guia institucional
material com identidade visual
exemplo de organização de slides
```

---

## Papel no projeto

A função desta pasta é permitir que os integrantes consultem uma referência externa ao montar a apresentação final.

Fluxo conceitual:

```text
PDF de referência
↓
análise visual e estrutural
↓
adaptação no template LaTeX
↓
apresentação do projeto
```

O PDF de referência não deve ser modificado para produzir resultados científicos.

---

## Prioridade do material fornecido pela professora

Quando a professora fornecer um modelo oficial de apresentação, esse material deverá ser considerado a principal referência visual.

A prioridade será:

```text
material oficial da professora
>
modelo genérico criado pelo grupo
```

Portanto, elementos como:

```text
cores
fontes
logos
cabeçalhos
rodapés
disposição dos elementos
proporções
estilo dos títulos
```

deverão ser adaptados conforme o material oficial, quando aplicável.

---

## Preservação do arquivo original

Arquivos de referência fornecidos externamente devem ser preservados em sua forma original.

Evitar:

```text
sobrescrever
editar diretamente
converter e substituir
alterar conteúdo
```

O objetivo é manter uma cópia rastreável da fonte utilizada como referência.

---

## Material externo

Podem ser armazenados aqui arquivos fornecidos por:

```text
professora
disciplina
departamento
instituição
```

quando sua função principal for servir como referência para a apresentação.

---

## O que NÃO deve ser colocado aqui

Não utilizar esta pasta para:

```text
dados brutos
bases tratadas
tabelas de resultados
gráficos científicos
ranking
pesos CRITIC
resultados TOPSIS
resultados de sensibilidade
PDF final da apresentação
PDF final do relatório
```

Esses artefatos pertencem às áreas correspondentes do projeto.

---

## Diferença entre `reference_pdf/` e `assets/`

### `reference_pdf/`

Armazena documentos completos utilizados como referência.

Exemplo conceitual:

```text
modelo_apresentacao_professora.pdf
```

### `latex/assets/`

Armazena elementos visuais individuais utilizados diretamente na apresentação.

Exemplos:

```text
logo oficial
imagem institucional
elemento gráfico fornecido pela professora
```

Assim:

```text
PDF completo de referência
→ reference_pdf/

logo extraída ou fornecida separadamente
→ latex/assets/
```

---

## Diferença entre `reference_pdf/` e `figures/`

A pasta:

```text
templates/presentation/latex/figures/
```

será utilizada para figuras efetivamente inseridas na apresentação.

Quando forem figuras científicas, elas deverão preferencialmente ser produzidas de forma reproduzível a partir das análises do projeto.

Já:

```text
templates/presentation/reference_pdf/
```

serve apenas como fonte de referência.

---

## Uso pela equipe

Durante a montagem da apresentação, os integrantes poderão consultar os PDFs desta pasta para reproduzir ou adaptar características como:

```text
hierarquia visual
organização dos slides
espaçamentos
posicionamento de logos
tipografia
uso de títulos
proporção entre texto e figuras
```

A adaptação deverá ser feita nos arquivos:

```text
templates/presentation/latex/
```

especialmente:

```text
theme.tex
preamble.tex
commands.tex
sections/
```

---

## Uso pelo Marco

Como responsável principal pela integração e comunicação, Marco poderá utilizar esta pasta para comparar:

```text
referência visual
×
apresentação produzida
```

sem alterar resultados científicos produzidos pelos demais integrantes.

---

## Uso de conteúdo científico presente em um PDF de referência

O fato de um PDF estar nesta pasta não significa automaticamente que seu conteúdo científico possa ser utilizado como evidência no projeto.

Se o documento também contiver:

```text
referências
normas
dados
especificações
orientações metodológicas
```

essas informações deverão ser avaliadas separadamente antes de serem utilizadas.

---

## Referência visual não é resultado

Nunca apresentar como resultado do projeto um número, gráfico ou conclusão apenas porque aparece em um PDF utilizado como modelo visual.

A origem dos resultados científicos deve permanecer:

```text
dados do projeto
↓
análise em R
↓
validação
↓
resultado oficial
```

---

## Arquivos futuros

Nesta fase de preparação da base:

```text
REFERENCE_PDF_STATUS = AWAITING_EXTERNAL_MATERIAL
```

Não é necessário adicionar um PDF apenas para preencher a pasta.

Quando houver material real fornecido pela professora ou outra referência aprovada, ele poderá ser colocado aqui.

---

## Nomenclatura

Quando possível, utilizar nomes claros.

Exemplos apenas de padrão:

```text
modelo_apresentacao_professora.pdf
referencia_visual_disciplina.pdf
modelo_institucional.pdf
```

Os nomes reais deverão corresponder aos arquivos efetivamente recebidos.

---

## Controle de origem

Para cada material importante, deve ser possível saber:

```text
quem forneceu
↓
qual é sua finalidade
↓
como foi utilizado
```

Se necessário, registrar essa informação neste README ou na documentação apropriada do projeto.

---

## Regra para logos e imagens

Caso um PDF contenha logos ou elementos visuais que precisem ser utilizados diretamente na apresentação, os integrantes deverão preferir os arquivos originais desses elementos quando disponíveis.

Não extrair imagens de baixa qualidade de um PDF se a professora ou instituição fornecer o arquivo oficial separadamente.

---

## Princípio final

> Esta pasta preserva as referências utilizadas para orientar a apresentação; ela não substitui os dados, a análise estatística nem os resultados produzidos pelos integrantes.

---

## Estado atual

```text
REFERENCE_PDF_README_STATUS = BASE_PREPARED
REFERENCE_PDF_STATUS = AWAITING_EXTERNAL_MATERIAL
OFFICIAL_PRESENTATION_REFERENCE = TO_BE_FILLED
```