# 02_auditoria_dados.md — Auditoria de Qualidade e Consistência dos Dados

## 1. Responsável

**Pacheco**

---

## 2. Objetivo

Realizar uma auditoria sistemática da qualidade dos dados presentes no arquivo
XLSX original e nos objetos intermediários gerados durante a importação.

Esta subetapa deve identificar:

- dados faltantes;
- registros incompletos;
- valores pendentes;
- erros de fórmula;
- duplicidades;
- tipos incompatíveis;
- unidades inconsistentes;
- mistura de texto e número;
- erros de soma;
- erros de média;
- totais incorretos;
- cálculos derivados incorretos;
- valores impossíveis;
- valores suspeitos;
- variáveis constantes;
- variáveis quase constantes;
- problemas que possam afetar etapas posteriores.

Nenhuma correção deverá ser aplicada sem registro.

---

# 3. Entradas

Utilizar:

```text
data/raw/ensaio_bancada_alunos.xlsx