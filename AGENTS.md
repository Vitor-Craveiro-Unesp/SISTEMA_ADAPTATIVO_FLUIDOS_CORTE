# AGENTS

## Finalidade

Este arquivo é o ponto de entrada para o sistema multiagente do projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

O projeto utiliza cinco agentes especializados:

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

Cada agente possui responsabilidade própria.

O `AGENTE_BOSS` atua como supervisor metodológico e integrador dos demais agentes.

---

# 1. Arquitetura multiagente

```text
                    AGENTE_BOSS
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ↓              ↓              ↓
 AGENTE_PACHECO   AGENTE_BENJAMIN   AGENTE_VITOR
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                   AGENTE_MARCO
                         │
                         ↓
                  integração final
                         │
                         ↓
                    AGENTE_BOSS
```

O fluxo científico permanece:

```text
Pacheco
↓
Benjamin
↓
Vitor
↓
Marco
```

O `AGENTE_BOSS` supervisiona o fluxo sem substituir silenciosamente o responsável de cada etapa.

---

# 2. Arquivos dos agentes

Os agentes estão documentados em:

```text
agents/
├── README.md
├── AGENTE_PACHECO.md
├── AGENTE_BENJAMIN.md
├── AGENTE_VITOR.md
├── AGENTE_MARCO.md
├── AGENTE_BOSS.md
└── REVIEW_PROTOCOL.md
```

---

# 3. Regra de roteamento

Antes de executar qualquer tarefa, identificar:

```text
qual etapa?
↓
qual responsável?
↓
qual agente?
↓
quais entradas devem ser lidas?
↓
há necessidade de revisão do AGENTE_BOSS?
```

---

# 4. Roteamento principal

## Dados, auditoria e preparação

Enviar para:

```text
AGENTE_PACHECO
```

Quando a tarefa envolver:

```text
dados brutos
inventário
leitura da planilha
auditoria
missing
duplicatas
tipos
unidades
fórmulas
reconciliação
base canônica
ADA inicial
```

---

## Critérios e ponderação

Enviar para:

```text
AGENTE_BENJAMIN
```

Quando a tarefa envolver:

```text
ADA bivariada
ADA multivariada
correlação
redundância
PCA
conformidade
critérios
TARGET
matriz de decisão
normalização
CRITIC
pesos informacionais
```

---

## Ranking e robustez

Enviar para:

```text
AGENTE_VITOR
```

Quando a tarefa envolver:

```text
TOPSIS
ranking
gaps
cenários
Pareto
sensibilidade
LOCO
LOAO
rank reversal
robustez
estabilidade do ranking
```

---

## Integração e comunicação

Enviar para:

```text
AGENTE_MARCO
```

Quando a tarefa envolver:

```text
integração de resultados
relatório
tabelas finais
figuras finais
apresentação
conclusões
limitações
consistência entre relatório e slides
```

---

## Revisão, auditoria e integração global

Enviar para:

```text
AGENTE_BOSS
```

Quando a tarefa envolver:

```text
revisão de trabalho dos outros agentes
aprovação de etapa
checagem de handoff
consistência metodológica
conflito entre resultados
problema entre etapas
controle de versão científica
rastreabilidade
checagem de resultados obsoletos
revisão final
```

---

# 5. Regra de propriedade da etapa

Cada etapa possui um agente proprietário.

```text
Pacheco
→ etapas 01 a 05

Benjamin
→ etapas 06 a 09

Vitor
→ etapas 10 a 12

Marco
→ integração, relatório e apresentação
```

O agente proprietário é responsável por:

```text
implementar
executar
validar
interpretar
documentar
```

sua etapa.

O `AGENTE_BOSS` revisa, mas não assume automaticamente a autoria da etapa.

---

# 6. AGENTE_PACHECO

Arquivo:

```text
agents/AGENTE_PACHECO.md
```

Área principal:

```text
dados
```

Arquivos prioritários:

```text
data/raw/
data/interim/
data/processed/

analysis/01_PACHECO_inventario.qmd
analysis/02_PACHECO_auditoria.qmd
analysis/03_PACHECO_reconciliacao.qmd
analysis/04_PACHECO_base_canonica.qmd
analysis/05_PACHECO_ada_inicial.qmd

R/pacheco/

report/stages/01_pacheco/

handoffs/01_PACHECO_to_BENJAMIN.md
```

---

# 7. AGENTE_BENJAMIN

Arquivo:

```text
agents/AGENTE_BENJAMIN.md
```

Área principal:

```text
estrutura estatística e multicritério
```

Arquivos prioritários:

```text
analysis/06_BENJAMIN_ada_bivariada.qmd
analysis/07_BENJAMIN_ada_multivariada.qmd
analysis/08_BENJAMIN_conformidade.qmd
analysis/09_BENJAMIN_critic.qmd

R/benjamin/

config/criterios.yml

report/stages/02_benjamin/

handoffs/01_PACHECO_to_BENJAMIN.md
handoffs/02_BENJAMIN_to_VITOR.md
```

---

# 8. AGENTE_VITOR

Arquivo:

```text
agents/AGENTE_VITOR.md
```

Área principal:

```text
ranking e robustez
```

Arquivos prioritários:

```text
analysis/10_VITOR_topsis.qmd
analysis/11_VITOR_cenarios_pareto.qmd
analysis/12_VITOR_robustez.qmd

R/vitor/

report/stages/03_vitor/

handoffs/02_BENJAMIN_to_VITOR.md
handoffs/03_VITOR_to_MARCO.md
```

---

# 9. AGENTE_MARCO

Arquivo:

```text
agents/AGENTE_MARCO.md
```

Área principal:

```text
integração e comunicação
```

Arquivos prioritários:

```text
report/stages/04_marco/
report/final/
presentation/
templates/presentation/

R/marco/

handoffs/03_VITOR_to_MARCO.md
handoffs/04_MARCO_to_TODOS.md
```

---

# 10. AGENTE_BOSS

Arquivo:

```text
agents/AGENTE_BOSS.md
```

O `AGENTE_BOSS` deve possuir visão global do projeto.

Arquivos prioritários:

```text
README.md
PROJECT_MAP.md
STATUS.md

config/

decisions/

handoffs/

analysis/

report/

presentation/

agents/REVIEW_PROTOCOL.md
```

O Boss pode consultar qualquer área necessária para revisão.

---

# 11. Ordem de leitura geral

Todo agente deve começar por:

```text
1. README.md
2. AGENTS.md
3. PROJECT_MAP.md
4. STATUS.md
5. config/project.yml
6. seu arquivo específico em agents/
7. instructions/ da sua etapa
8. handoff correspondente
9. analysis/ correspondente
```

---

# 12. Ordem de leitura por agente

## Pacheco

```text
README.md
↓
AGENTS.md
↓
agents/AGENTE_PACHECO.md
↓
STATUS.md
↓
config/
↓
instructions/pacheco/
↓
data/raw/
↓
analysis/01–05
```

---

## Benjamin

```text
README.md
↓
AGENTS.md
↓
agents/AGENTE_BENJAMIN.md
↓
STATUS.md
↓
handoffs/01_PACHECO_to_BENJAMIN.md
↓
config/
↓
instructions/benjamin/
↓
analysis/06–09
```

---

## Vitor

```text
README.md
↓
AGENTS.md
↓
agents/AGENTE_VITOR.md
↓
STATUS.md
↓
handoffs/02_BENJAMIN_to_VITOR.md
↓
config/
↓
instructions/vitor/
↓
analysis/10–12
```

---

## Marco

```text
README.md
↓
AGENTS.md
↓
agents/AGENTE_MARCO.md
↓
STATUS.md
↓
handoffs/03_VITOR_to_MARCO.md
↓
report/
↓
presentation/
```

---

## Boss

```text
README.md
↓
AGENTS.md
↓
agents/AGENTE_BOSS.md
↓
agents/REVIEW_PROTOCOL.md
↓
STATUS.md
↓
PROJECT_MAP.md
↓
config/
↓
handoffs/
↓
artefatos da etapa em revisão
```

---

# 13. Fluxo padrão de uma etapa

```text
AGENTE RESPONSÁVEL
↓
implementa / executa
↓
valida
↓
documenta
↓
prepara handoff
↓
AGENTE_BOSS
↓
revisa
```

O Boss poderá retornar:

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

# 14. APPROVED

Usar quando:

```text
entrada correta
método correto
execução válida
resultados coerentes
validações concluídas
documentação suficiente
handoff completo
```

---

# 15. CHANGES_REQUESTED

Usar quando:

```text
há problema corrigível
```

mas a etapa não precisa ser completamente bloqueada.

Fluxo:

```text
Boss
↓
CHANGES_REQUESTED
↓
agente responsável
↓
corrige
↓
nova versão
↓
Boss revisa novamente
```

---

# 16. BLOCKED

Usar quando existe problema que impede resultado confiável.

Exemplos:

```text
fonte incorreta
base inválida
critério sem definição
peso inválido
normalização indefinida
resultado impossível
handoff incompleto crítico
```

---

# 17. O Boss não deve corrigir silenciosamente

Exemplo incorreto:

```text
AGENTE_BOSS encontra erro no CRITIC
↓
edita peso
↓
continua pipeline
```

Fluxo correto:

```text
AGENTE_BOSS encontra erro
↓
registra problema
↓
devolve para AGENTE_BENJAMIN
↓
Benjamin corrige
↓
nova versão
↓
Boss revisa
```

---

# 18. Exceção para correções triviais

O Boss poderá corrigir diretamente apenas itens claramente não científicos, quando permitido pelo protocolo.

Exemplos:

```text
erro ortográfico
formatação
link interno quebrado
cabeçalho incorreto
```

Correções científicas ou metodológicas devem retornar ao agente responsável.

---

# 19. Responsabilidade sobre dados

Somente o fluxo de Pacheco deve alterar dados derivados relacionados a:

```text
reconciliação
base canônica
```

Se outro agente encontrar erro de dado:

```text
não corrigir localmente
```

Deve reabrir a etapa upstream.

---

# 20. Responsabilidade sobre critérios

Benjamin é responsável por:

```text
definição de critérios
direções
TARGET
normalização principal
CRITIC
```

Vitor não deve redefinir esses itens silenciosamente.

---

# 21. Responsabilidade sobre ranking

Vitor é responsável por:

```text
TOPSIS
cenários
Pareto
robustez
```

Marco não deve recalcular ou alterar esses resultados silenciosamente.

---

# 22. Responsabilidade sobre comunicação

Marco é responsável por:

```text
síntese
relatório
apresentação
```

mas não pode alterar resultados científicos para melhorar narrativa ou layout.

---

# 23. Material da professora

Quando existir material fornecido pela professora:

```text
fonte oficial
```

deve ter prioridade sobre suposições genéricas do agente.

Nenhum agente deve inventar:

```text
limites
especificações
nomes institucionais
regras
valores
```

ausentes da fonte.

---

# 24. Dados brutos

Todos os agentes devem respeitar:

```text
data/raw/ = IMUTÁVEL
```

Nenhum agente deve:

```text
editar
sobrescrever
corrigir diretamente
```

arquivos originais.

---

# 25. Correções

Fluxo obrigatório:

```text
detectar
↓
registrar
↓
investigar
↓
obter evidência
↓
decidir
↓
corrigir por código
```

---

# 26. Critérios

Nenhum agente pode selecionar critérios com base em:

```text
qual fluido vence
```

A escolha deve ser metodologicamente anterior ao ranking.

---

# 27. CRITIC

Regra de referência:

\[
C_j
=
\sigma_j
\sum_k(1-r_{jk})
\]

\[
w_j
=
\frac{C_j}{\sum_jC_j}
\]

Não substituir silenciosamente:

\[
1-r
\]

por:

\[
1-|r|
\]

---

# 28. Interpretação dos pesos

Todos os agentes devem manter:

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

# 29. TOPSIS

Se a matriz já estiver orientada como:

```text
maior = melhor
```

não inverter novamente critérios `COST`.

---

# 30. Conformidade

Todos os agentes devem manter:

```text
conformidade
≠
ranking
```

Uma alternativa poderá ser:

```text
bem classificada
+
não conforme
```

e isso deve ser comunicado.

---

# 31. Pareto

Pareto não utiliza pesos.

```text
PARETO
≠
TOPSIS
```

Alternativa não dominada não significa vencedora automática.

---

# 32. Frequências de robustez

Resultados como:

```text
80% dos cenários em primeiro
```

não devem ser apresentados como:

```text
80% de probabilidade de ser o melhor
```

---

# 33. Resultados preliminares

Resultados preliminares deverão ser identificados como:

```text
EXPLORATORY
```

ou:

```text
UNDER_REVIEW
```

Nunca como resultado final.

---

# 34. Resultados oficiais

Somente resultados:

```text
APPROVED
```

poderão alimentar diretamente:

```text
report/final/
presentation/
```

---

# 35. Handoffs

Os agentes devem utilizar os handoffs como contratos entre etapas.

```text
Pacheco → Benjamin
Benjamin → Vitor
Vitor → Marco
Marco → Todos
```

Nenhum agente deve assumir que uma entrada está pronta apenas porque o arquivo existe.

---

# 36. Mudança upstream

Quando uma etapa anterior mudar:

```text
nova versão
↓
impacto downstream
↓
reexecução necessária
↓
novo handoff
```

Resultados antigos devem ser marcados como:

```text
SUPERSEDED
```

quando aplicável.

---

# 37. STATUS.md

Cada agente deve consultar:

```text
STATUS.md
```

antes de começar.

Ao concluir mudanças relevantes, o status correspondente deverá ser atualizado.

---

# 38. Decisions

Escolhas metodológicas relevantes deverão ser registradas em:

```text
decisions/
```

Não inventar arquivos `DEC-*` sem uma decisão real.

---

# 39. CHANGELOG

Mudanças estruturais relevantes deverão ser registradas em:

```text
CHANGELOG.md
```

Exemplos:

```text
mudança de arquitetura
mudança de pipeline
mudança de metodologia aprovada
mudança na organização dos agentes
```

---

# 40. Escopo dos agentes

Os agentes são auxiliares dos integrantes.

Eles podem:

```text
analisar
propor
implementar
testar
documentar
revisar
```

dentro de seu escopo quando a etapa estiver em execução.

---

# 41. Nesta fase atual

O projeto ainda está na fase:

```text
BASE_PREPARED
```

Portanto, neste momento os agentes não devem fabricar:

```text
resultados
pesos
ranking
critérios finais
robustez
conclusões
```

---

# 42. Arquivos que são apenas moldes

Arquivos de:

```text
templates
instructions
configuração-base
README
checklists
```

podem ser preparados antes da execução.

---

# 43. Arquivos de implementação

Arquivos como:

```text
R/*.R
scripts/*.R
tests/testthat/*.R
_targets.R
```

devem ser implementados durante a execução real pelos responsáveis.

---

# 44. Não inventar API interna antecipadamente

Antes das funções existirem, os agentes não devem assumir:

```text
nomes definitivos de funções
argumentos
classes de retorno
nomes de outputs
```

sem necessidade real.

---

# 45. Protocolo de revisão

O procedimento detalhado do Boss está em:

```text
agents/REVIEW_PROTOCOL.md
```

Ele deve ser seguido para revisões formais.

---

# 46. Regra de roteamento em tarefas ambíguas

Se uma tarefa envolver mais de uma área, identificar:

```text
quem é proprietário da saída principal?
```

Esse agente assume a tarefa.

Exemplo:

```text
interpretar efeito da normalização no ranking
```

Proprietário principal:

```text
AGENTE_VITOR
```

porque a saída principal é a robustez do ranking.

Benjamin poderá ser consultado sobre a normalização.

---

# 47. Tarefa envolvendo erro upstream

Se Vitor detectar possível erro na matriz entregue por Benjamin:

```text
AGENTE_VITOR
→ registra problema

AGENTE_BENJAMIN
→ investiga/corrige

AGENTE_BOSS
→ revisa nova versão
```

---

# 48. Tarefa envolvendo integração

Se Marco encontrar divergência entre relatório e ranking:

```text
AGENTE_MARCO
→ identifica divergência

AGENTE_VITOR
→ valida resultado científico

AGENTE_BOSS
→ verifica consistência final
```

---

# 49. Tarefa envolvendo dados

Se Benjamin identificar valor suspeito:

```text
AGENTE_BENJAMIN
→ não corrige

AGENTE_PACHECO
→ reabre auditoria/reconciliação

AGENTE_BOSS
→ verifica impacto downstream
```

---

# 50. Prioridade de autoridade

Para cada tipo de assunto:

```text
dados
→ Pacheco

critérios / CRITIC
→ Benjamin

ranking / robustez
→ Vitor

relatório / apresentação
→ Marco

aprovação integrada
→ Boss
```

---

# 51. Conflito entre agentes

Se dois agentes discordarem metodologicamente:

```text
registrar argumentos
↓
não alterar resultado silenciosamente
↓
encaminhar ao AGENTE_BOSS
```

O Boss deverá:

```text
consultar fontes
consultar decisões existentes
avaliar impacto
propor resolução
```

Se a decisão for relevante:

```text
criar DEC
```

quando apropriado.

---

# 52. Não inventar consenso

Discordâncias reais devem ser documentadas.

O Boss não deve afirmar consenso quando ele não existe.

---

# 53. Revisão final

Antes da entrega:

```text
AGENTE_PACHECO
→ valida dados

AGENTE_BENJAMIN
→ valida critérios e CRITIC

AGENTE_VITOR
→ valida TOPSIS e robustez

AGENTE_MARCO
→ valida relatório e apresentação

AGENTE_BOSS
→ valida integração total
```

---

# 54. Estado atual dos agentes

```text
MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

AGENTE_PACHECO = NOT_CONFIGURED

AGENTE_BENJAMIN = NOT_CONFIGURED

AGENTE_VITOR = NOT_CONFIGURED

AGENTE_MARCO = NOT_CONFIGURED

AGENTE_BOSS = NOT_CONFIGURED

REVIEW_PROTOCOL = NOT_CONFIGURED
```

Esses status deverão ser atualizados conforme os arquivos em `agents/` forem preenchidos.

---

# 55. Princípio final

> Cada agente deve atuar profundamente em sua área, enquanto o AGENTE_BOSS garante que as partes formem um único projeto coerente. Revisão não significa substituir autoria: problemas científicos devem voltar ao agente responsável, ser corrigidos na origem e passar por nova validação.