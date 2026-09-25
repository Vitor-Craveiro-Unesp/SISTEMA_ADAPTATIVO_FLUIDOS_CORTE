# Arquitetura Multiagente

## Projeto

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Esta pasta contém a definição dos cinco agentes especializados utilizados para auxiliar os integrantes do projeto.

Os agentes são:

```text
AGENTE_PACHECO
AGENTE_BENJAMIN
AGENTE_VITOR
AGENTE_MARCO
AGENTE_BOSS
```

Cada agente possui:

```text
responsabilidade
escopo
arquivos prioritários
limites
entradas
saídas
regras de revisão
```

O objetivo da arquitetura é permitir que cada integrante possua um agente especializado em sua parte do projeto, mantendo ao mesmo tempo uma supervisão global por meio do `AGENTE_BOSS`.

---

# 1. Estrutura

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

# 2. Papel do `AGENTS.md`

O arquivo:

```text
AGENTS.md
```

localizado na raiz do projeto funciona como:

```text
ROTEADOR CENTRAL
```

Ele identifica:

```text
qual tarefa foi solicitada
↓
qual etapa é afetada
↓
qual agente é responsável
↓
quais arquivos devem ser consultados
↓
se é necessária revisão do AGENTE_BOSS
```

---

# 3. Papel desta pasta

A pasta:

```text
agents/
```

define o comportamento individual dos agentes.

Enquanto:

```text
AGENTS.md
→ decide QUEM deve atuar
```

os arquivos desta pasta definem:

```text
COMO cada agente deve atuar
```

---

# 4. Arquitetura geral

```text
                         AGENTE_BOSS
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ↓                ↓                ↓
      AGENTE_PACHECO   AGENTE_BENJAMIN   AGENTE_VITOR
             │                │                │
             └────────────────┼────────────────┘
                              ↓
                        AGENTE_MARCO
                              │
                              ↓
                       integração final
                              │
                              ↓
                         AGENTE_BOSS
```

O fluxo científico do trabalho permanece:

```text
Pacheco
↓
Benjamin
↓
Vitor
↓
Marco
```

O `AGENTE_BOSS` supervisiona o fluxo.

---

# 5. Princípio de propriedade

Cada parte do projeto possui um responsável principal.

```text
dados
→ Pacheco

critérios e CRITIC
→ Benjamin

ranking e robustez
→ Vitor

relatório e apresentação
→ Marco

revisão integrada
→ Boss
```

O agente responsável pela etapa é chamado de:

```text
AGENTE PROPRIETÁRIO
```

---

# 6. AGENTE_PACHECO

Arquivo:

```text
agents/AGENTE_PACHECO.md
```

Especialidade:

```text
dados
auditoria
reconciliação
base canônica
ADA inicial
```

Responsável por apoiar Pacheco nas etapas:

```text
01
02
03
04
05
```

---

# 7. AGENTE_BENJAMIN

Arquivo:

```text
agents/AGENTE_BENJAMIN.md
```

Especialidade:

```text
ADA bivariada
ADA multivariada
correlação
redundância
conformidade
critérios
normalização
CRITIC
```

Responsável por apoiar Benjamin nas etapas:

```text
06
07
08
09
```

---

# 8. AGENTE_VITOR

Arquivo:

```text
agents/AGENTE_VITOR.md
```

Especialidade:

```text
TOPSIS
ranking
cenários
Pareto
sensibilidade
LOCO
LOAO
rank reversal
robustez
```

Responsável por apoiar Vitor nas etapas:

```text
10
11
12
```

---

# 9. AGENTE_MARCO

Arquivo:

```text
agents/AGENTE_MARCO.md
```

Especialidade:

```text
integração
relatório
tabelas finais
figuras finais
apresentação
conclusões
limitações
```

Marco trabalha principalmente com resultados já validados.

---

# 10. AGENTE_BOSS

Arquivo:

```text
agents/AGENTE_BOSS.md
```

Especialidade:

```text
revisão global
auditoria metodológica
consistência entre etapas
handoffs
controle de versões científicas
integração final
```

O Boss possui acesso conceitual ao projeto inteiro.

---

# 11. O Boss não substitui os outros agentes

O Boss deve:

```text
revisar
identificar erros
avaliar consistência
solicitar correções
aprovar
bloquear quando necessário
```

O Boss não deve:

```text
corrigir silenciosamente resultado científico
reescrever metodologia do responsável sem registro
alterar pesos
trocar critérios
corrigir dados diretamente
mudar ranking
```

---

# 12. Fluxo de uma etapa

Fluxo padrão:

```text
AGENTE RESPONSÁVEL
↓
entende entrada
↓
implementa
↓
executa
↓
valida
↓
interpreta
↓
documenta
↓
prepara handoff
↓
AGENTE_BOSS
↓
revisa
```

---

# 13. Resultado da revisão

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

Significa que a etapa está apta a alimentar a próxima etapa.

Requer, quando aplicável:

```text
entrada correta
método documentado
código executável
resultado validado
limitações registradas
handoff completo
```

---

# 15. CHANGES_REQUESTED

Significa que a etapa possui problema corrigível.

Fluxo:

```text
Boss identifica problema
↓
registra comentário
↓
devolve ao agente responsável
↓
agente corrige
↓
nova versão
↓
nova revisão
```

---

# 16. BLOCKED

Utilizado quando existe problema que impede avanço confiável.

Exemplos:

```text
entrada inválida
dados inconsistentes
falta de especificação essencial
matriz inválida
peso inválido
resultado não reproduzível
```

---

# 17. Protocolo de revisão

As regras formais de revisão estão em:

```text
agents/REVIEW_PROTOCOL.md
```

Esse arquivo deve ser utilizado pelo `AGENTE_BOSS` em checkpoints.

---

# 18. Independência dos agentes

Cada agente deve permanecer dentro de seu escopo.

Exemplo:

```text
AGENTE_VITOR encontra problema nos dados
```

ele não deve corrigir a base.

Fluxo correto:

```text
AGENTE_VITOR
↓
registra problema
↓
AGENTE_PACHECO
↓
investiga e corrige upstream
↓
nova versão
↓
reexecução downstream
```

---

# 19. Dependência entre agentes

O fluxo principal é sequencial.

```text
AGENTE_PACHECO
↓
AGENTE_BENJAMIN
↓
AGENTE_VITOR
↓
AGENTE_MARCO
```

A saída de uma etapa torna-se entrada da próxima somente após aprovação.

---

# 20. Handoffs

A passagem formal entre agentes ocorre por:

```text
handoffs/
```

Arquivos:

```text
01_PACHECO_to_BENJAMIN.md
02_BENJAMIN_to_VITOR.md
03_VITOR_to_MARCO.md
04_MARCO_to_TODOS.md
```

---

# 21. Handoff não é simples aviso

Um handoff deve informar, quando aplicável:

```text
versão da entrada
versão da saída
status
resultados
limitações
issues
bloqueios
decisões
itens congelados
```

---

# 22. Leitura obrigatória

Antes de atuar, todo agente deve consultar:

```text
README.md
AGENTS.md
PROJECT_MAP.md
STATUS.md
config/project.yml
```

Depois deverá consultar seu próprio arquivo.

---

# 23. Leitura específica

Cada agente deverá consultar:

```text
agents/AGENTE_<NOME>.md
```

antes de atuar em sua área.

---

# 24. Instructions

As instruções detalhadas das etapas permanecem em:

```text
instructions/
```

A função é:

```text
agents/
→ comportamento do agente

instructions/
→ procedimento da etapa
```

---

# 25. Analysis

Os cadernos em:

```text
analysis/
```

registram:

```text
execução
análise
validação
interpretação
```

Os arquivos dos agentes não substituem os cadernos analíticos.

---

# 26. Código

A implementação científica deverá ocorrer principalmente em:

```text
R/
```

e, quando apropriado:

```text
scripts/
```

Os arquivos `agents/*.md` não devem conter resultados calculados.

---

# 27. Testes

Os testes reais deverão ser implementados em:

```text
tests/testthat/
```

Os agentes poderão sugerir e implementar testes durante a execução de suas respectivas etapas.

---

# 28. Configurações

Os agentes devem respeitar:

```text
config/project.yml
config/criterios.yml
config/regras_validacao.yml
config/tolerancias.yml
```

Não criar regras paralelas escondidas no código.

---

# 29. Configuração não definida

Se uma configuração necessária estiver:

```text
null
TO_BE_FILLED
NOT_DEFINED
```

o agente não deverá inventar silenciosamente um valor.

Deverá:

```text
identificar necessidade
↓
buscar evidência
↓
definir com justificativa
↓
documentar
```

---

# 30. Decisões metodológicas

Decisões importantes devem ser registradas em:

```text
decisions/
```

O agente não deve criar decisão formal para questões triviais.

---

# 31. Mudança upstream

Se uma etapa aprovada mudar:

```text
nova versão
↓
Boss avalia impacto
↓
etapas downstream afetadas são identificadas
↓
resultados antigos deixam de ser considerados atuais
↓
reexecução
```

---

# 32. Resultados superseded

Resultados substituídos devem receber status:

```text
SUPERSEDED
```

quando apropriado.

---

# 33. Dados brutos

Regra comum para todos os agentes:

```text
data/raw/ = IMUTÁVEL
```

Nenhum agente deverá alterar diretamente os dados originais.

---

# 34. Correções

Toda correção deve possuir:

```text
origem
evidência
regra
implementação reproduzível
registro
```

---

# 35. Resultados antecipados

Enquanto uma etapa não for executada:

```text
RESULTS_STATUS = NOT_GENERATED
```

Nenhum agente deverá preencher resultados hipotéticos.

---

# 36. Métodos guiados pelo vencedor

É proibido:

```text
testar configurações
↓
observar vencedor
↓
escolher método porque produz o vencedor desejado
```

---

# 37. CRITIC

A formulação principal de referência é:

\[
C_j = \sigma_j \sum_k(1-r_{jk})
\]

\[
w_j = \frac{C_j}{\sum_jC_j}
\]

Regra:

```text
1 - r
```

não deve ser substituído silenciosamente por:

```text
1 - |r|
```

---

# 38. TOPSIS

Se os critérios já tiverem sido orientados para:

```text
maior = melhor
```

não realizar nova inversão dos critérios `COST`.

---

# 39. Conformidade

Regra comum:

```text
CONFORMIDADE
≠
RANKING
```

As duas informações devem permanecer disponíveis separadamente.

---

# 40. Pareto

Regra:

```text
PARETO NÃO UTILIZA PESOS
```

A fronteira deve ser utilizada como evidência complementar.

---

# 41. Robustez

Resultados de cenários, sensibilidade ou simulação devem ser interpretados como comportamento dentro das configurações analisadas.

Não como probabilidade real.

---

# 42. Relatório e apresentação

Somente resultados:

```text
APPROVED
```

devem alimentar:

```text
report/final/
presentation/
```

---

# 43. Consistência

Os agentes deverão evitar divergências entre:

```text
analysis/
results/
handoffs/
report/
presentation/
```

Todos devem refletir a mesma execução aprovada.

---

# 44. Integridade científica

Nenhum agente deverá:

```text
ocultar problema
eliminar resultado desfavorável
alterar peso sem registro
trocar critério silenciosamente
editar valor científico manualmente
fabricar dado ausente
```

---

# 45. Rastreabilidade

O objetivo é permitir reconstruir:

```text
conclusão
↓
resultado
↓
método
↓
configuração
↓
dados processados
↓
reconciliação
↓
dados brutos
```

---

# 46. Comunicação entre agentes

Quando um agente precisar de alteração em outra etapa, deverá formular claramente:

```text
problema
localização
evidência
impacto
ação necessária
```

---

# 47. Exemplo de solicitação upstream

```text
REQUEST_ID = TO_BE_FILLED

FROM = AGENTE_VITOR

TO = AGENTE_BENJAMIN

ISSUE = TO_BE_FILLED

IMPACT = TO_BE_FILLED

REQUESTED_ACTION = TO_BE_FILLED
```

Não é obrigatório criar novo arquivo para cada solicitação; poderá ser registrado no mecanismo de trabalho adotado pelo grupo.

---

# 48. Boss como árbitro

Quando existir conflito entre agentes, o Boss deverá avaliar:

```text
fontes
metodologia
decisões anteriores
configurações
impacto downstream
```

Não resolver por preferência pessoal.

---

# 49. Escopo atual

Nesta fase do projeto:

```text
MULTI_AGENT_ARCHITECTURE = BASE_PREPARED

SCIENTIFIC_EXECUTION = NOT_STARTED
```

Os arquivos desta pasta estão sendo preparados como documentação-base.

---

# 50. Estado dos arquivos

```text
AGENTS_ROUTER = BASE_PREPARED

AGENTE_PACHECO = NOT_CONFIGURED

AGENTE_BENJAMIN = NOT_CONFIGURED

AGENTE_VITOR = NOT_CONFIGURED

AGENTE_MARCO = NOT_CONFIGURED

AGENTE_BOSS = NOT_CONFIGURED

REVIEW_PROTOCOL = NOT_CONFIGURED
```

Esses valores deverão ser atualizados à medida que cada arquivo for preenchido.

---

# 51. Princípio final

> Cada agente deve aprofundar uma parte do projeto sem perder a conexão com as demais. A especialização aumenta a qualidade do trabalho; o AGENTE_BOSS garante que as especializações permaneçam consistentes entre si e formem uma única análise científica reproduzível.