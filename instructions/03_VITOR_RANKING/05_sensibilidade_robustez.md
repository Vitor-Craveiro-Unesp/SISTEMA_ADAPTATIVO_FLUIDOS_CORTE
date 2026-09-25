# 05_sensibilidade_robustez.md — Análise de Sensibilidade e Robustez do Ranking Multicritério

## 1. Responsável

**Vitor**

---

## 2. Objetivo

Avaliar sistematicamente quanto o ranking dos fluidos depende das escolhas
metodológicas utilizadas no modelo multicritério.

A análise de sensibilidade deve investigar principalmente o efeito de mudanças
plausíveis em:

- pesos dos critérios;
- presença ou ausência de critérios;
- método de normalização;
- conjunto de alternativas;
- regras de conformidade, quando aplicável.

A pergunta central desta etapa é:

> Pequenas alterações razoáveis na metodologia produzem pequenas alterações
> no ranking ou modificam completamente a decisão?

Além da sensibilidade, esta etapa deverá integrar os resultados obtidos no
ranking principal, nos cenários e na análise de Pareto para avaliar a robustez
das conclusões.

---

# PARTE I — ANÁLISE DE SENSIBILIDADE

## 3. Princípio fundamental

A análise de sensibilidade não deve procurar um ranking diferente.

Ela deve testar a estabilidade do ranking principal.

O cenário principal permanece:

```text
matriz aprovada
+
normalização principal
+
pesos CRITIC
+
TOPSIS