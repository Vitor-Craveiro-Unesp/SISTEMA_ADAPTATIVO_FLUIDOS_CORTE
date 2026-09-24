# AGENTS.md — Instruções para agentes de IA

## 1. Objetivo do projeto

Este projeto tem como objetivo desenvolver um Sistema Adaptativo de
Classificação Multicritério de Fluidos de Corte.

A análise deve seguir uma sequência estatística rigorosa:

dados brutos
→ auditoria
→ reconciliação
→ base canônica
→ ADA
→ conformidade
→ critérios
→ normalização
→ CRITIC
→ TOPSIS
→ cenários
→ Pareto
→ sensibilidade
→ robustez
→ ranking
→ relatório
→ apresentação.

---

## 2. Linguagem principal

A linguagem principal do projeto é:

R

Não substituir R por Python sem autorização explícita da equipe.

---

## 3. Infraestrutura

O projeto utiliza:

- R
- Docker
- renv
- targets
- testthat
- Quarto
- LaTeX
- Git
- GitHub

---

## 4. Responsáveis

### Pacheco

Responsável por:

- importação dos dados;
- inventário da planilha;
- auditoria estrutural;
- dados faltantes;
- duplicidades;
- unidades;
- erros de soma;
- erros de média;
- validação de fórmulas;
- diferenças numéricas entre abas;
- reconciliação;
- registro de inconsistências;
- construção da base canônica;
- ADA inicial.

---

### Benjamin

Responsável por:

- ADA bivariada;
- ADA multivariada;
- correlação;
- redundância;
- análise de conformidade;
- classificação dos critérios;
- matriz de decisão;
- normalização;
- CRITIC.

---

### Vitor

Responsável por:

- TOPSIS;
- ranking;
- cenários;
- Pareto;
- análise de sensibilidade;
- análise de robustez.

---

### Marco

Responsável por:

- integração dos resultados;
- relatório técnico;
- LaTeX;
- tabelas;
- figuras;
- apresentação;
- conclusão;
- limitações.

---

## 5. Ordem obrigatória do projeto

A ordem das etapas deve ser respeitada.

1. Preparação da infraestrutura
2. Auditoria dos dados
3. Reconciliação entre abas
4. Validação dos cálculos
5. Construção da base canônica
6. ADA univariada
7. ADA bivariada
8. ADA multivariada
9. Análise de conformidade
10. Definição dos critérios
11. Matriz de decisão
12. Normalização
13. CRITIC
14. TOPSIS
15. Cenários
16. Pareto
17. Sensibilidade e robustez
18. Relatório
19. Apresentação
20. Revisão e entrega

Não avançar para uma etapa se o critério de conclusão da etapa anterior
não tiver sido atendido.

---

## 6. Regras obrigatórias

### Dados brutos

A pasta:

data/raw/

é imutável.

Nunca:

- alterar;
- sobrescrever;
- corrigir;
- excluir

arquivos dentro de `data/raw/`.

---

## 7. Correções de dados

Nunca corrigir silenciosamente um valor.

Toda inconsistência deve ser:

1. identificada;
2. registrada;
3. investigada;
4. classificada;
5. documentada;
6. corrigida somente quando houver justificativa.

Decisões importantes devem ser registradas em:

decisions/

---

## 8. Auditoria independente

Não confiar automaticamente em cálculos existentes no Excel.

O R deve recalcular independentemente:

- somas;
- médias;
- totais;
- percentuais;
- custos;
- indicadores;
- demais fórmulas utilizadas na análise.

Sempre comparar:

valor informado
vs.
valor recalculado.

---

## 9. Diferenças entre abas

Quando a mesma variável aparecer em mais de uma aba, comparar os valores.

Registrar:

- fluido;
- variável;
- condição;
- valor na origem A;
- valor na origem B;
- diferença absoluta;
- diferença relativa;
- classificação da divergência.

Classificações possíveis:

- exato;
- arredondamento;
- pequena divergência;
- divergência relevante;
- divergência crítica.

---

## 10. Missing data

Não tratar todos os valores ausentes como equivalentes.

Sempre que possível, distinguir:

- não medido;
- pendente;
- não aplicável;
- erro de fórmula;
- ausente desconhecido.

Não realizar imputação automática sem justificativa.

---

## 11. Outliers

Outlier não significa erro.

Nunca excluir automaticamente uma observação apenas porque ela é extrema.

Outliers devem ser:

- identificados;
- investigados;
- documentados.

---

## 12. Critérios para o ranking

Cada variável candidata ao sistema multicritério deve ser classificada como:

- benefício;
- custo;
- alvo;
- restrição;
- diagnóstico.

Variáveis sem poder discriminante não devem entrar automaticamente no
ranking.

---

## 13. Ranking

O ranking principal será construído utilizando:

CRITIC
+
TOPSIS

O CRITIC será responsável pela determinação dos pesos.

O TOPSIS será responsável pela classificação das alternativas.

Nenhum ranking deve ser produzido antes da aprovação da matriz de decisão.

---

## 14. Análise de robustez

O ranking não deve ser interpretado isoladamente.

Devem ser analisados:

- cenários alternativos;
- alterações de pesos;
- posição média;
- frequência de primeiro lugar;
- frequência no Top 3;
- estabilidade da classificação.

---

## 15. Fonte única dos resultados

Resultados numéricos devem ser produzidos pelo R e armazenados em:

results/

O relatório e a apresentação devem consumir esses resultados.

Evitar digitação manual de números estatísticos.

Fluxo esperado:

R
→ results/
→ relatório
→ apresentação.

---

## 16. Relatórios por etapa

Cada responsável deverá produzir um relatório da sua etapa em:

report/stages/

Estrutura:

- 01_pacheco/
- 02_benjamin/
- 03_vitor/
- 04_marco/

---

## 17. Handoffs

Cada passagem entre responsáveis deve gerar um arquivo em:

handoffs/

Fluxo:

Pacheco → Benjamin

Benjamin → Vitor

Vitor → Marco

Marco → Todos

O handoff deve indicar:

- arquivos oficiais;
- entregáveis;
- decisões tomadas;
- pendências;
- limitações;
- o que não pode ser alterado silenciosamente.

---

## 18. Status do projeto

Antes de iniciar qualquer trabalho, consultar:

STATUS.md

O arquivo deve informar:

- etapa atual;
- responsável;
- situação;
- tarefas concluídas;
- tarefas em andamento;
- pendências;
- próximo handoff.

---

## 19. Mapa do repositório

Antes de procurar arquivos, consultar:

PROJECT_MAP.md

Esse documento informa onde cada componente do projeto está localizado.

---

## 20. Testes

Sempre que possível, utilizar testes automatizados em:

tests/testthat/

Devem existir testes para:

- importação;
- presença dos fluidos;
- somas;
- médias;
- reconciliação entre abas;
- unidades;
- regras de domínio;
- CRITIC;
- TOPSIS.

---

## 21. Git

Não alterar arquivos importantes diretamente sem controle de versão.

Antes de concluir uma etapa:

- salvar alterações;
- executar testes;
- atualizar relatório;
- atualizar STATUS.md;
- gerar handoff;
- realizar commit.

---

## 22. Regra de continuidade

Se uma etapa posterior detectar erro produzido em uma etapa anterior,
não corrigir silenciosamente.

A correção deve retornar à etapa responsável.

Exemplo:

Benjamin encontra erro na base canônica
→ retorna para Pacheco
→ Pacheco corrige
→ registra a decisão
→ gera nova versão
→ Benjamin continua.

---

## 23. Instrução inicial para agentes

Ao entrar no projeto, um agente de IA deve seguir esta ordem:

1. Ler `AGENTS.md`
2. Ler `README.md`
3. Ler `PROJECT_MAP.md`
4. Ler `STATUS.md`
5. Ler as instruções da etapa atual em `instructions/`
6. Ler o handoff anterior, quando existir
7. Ler decisões relevantes em `decisions/`
8. Somente então analisar código, dados e resultados

---

## 24. Princípio fundamental

Primeiro garantir que os dados são confiáveis.

Depois analisar.

Somente depois classificar.