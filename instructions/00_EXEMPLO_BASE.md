# 00_EXEMPLO_BASE.md — Modelo de Instrução de Etapa

## 1. Nome da etapa

**ETAPA XX — Nome da etapa**

---

## 2. Responsável principal

**Nome do responsável**

Revisor:

**Nome do revisor**

---

## 3. Objetivo

Descrever de forma clara o que esta etapa precisa produzir.

A etapa deve resolver um problema específico e gerar entregáveis que possam
ser utilizados pela próxima etapa.

---

## 4. Entradas obrigatórias

Listar somente arquivos oficialmente aprovados para uso.

Exemplo:

- `data/processed/base_canonica_v1.rds`
- `config/criterios.yml`
- `handoffs/XX_RESPONSAVEL_A_to_RESPONSAVEL_B.md`

Não utilizar versões alternativas sem registro formal.

---

## 5. Arquivos que podem ser lidos

Exemplo:

- `data/`
- `config/`
- `results/`
- `decisions/`
- `handoffs/`

---

## 6. Arquivos que podem ser alterados

Exemplo:

- `R/responsavel/`
- `analysis/`
- `results/...`
- `report/stages/...`

---

## 7. Arquivos que não podem ser alterados

### Sempre proibido

- `data/raw/`

### Também não alterar silenciosamente

- resultados congelados de etapas anteriores;
- arquivos de decisão já aprovados;
- handoffs já concluídos;
- configurações metodológicas aprovadas em checkpoint.

Caso uma alteração seja necessária, registrar nova decisão.

---

## 8. Procedimentos

Executar na ordem definida.

### Passo 1

Descrever procedimento.

### Passo 2

Descrever procedimento.

### Passo 3

Descrever procedimento.

### Passo 4

Descrever procedimento.

---

## 9. Validações obrigatórias

Antes de considerar a etapa concluída:

- [ ] Entradas corretas utilizadas.
- [ ] Código executado sem erro.
- [ ] Resultados reproduzíveis.
- [ ] Testes relacionados aprovados.
- [ ] Resultados revisados.
- [ ] Nenhuma alteração silenciosa realizada.
- [ ] Decisões metodológicas registradas.
- [ ] Relatório da etapa atualizado.

---

## 10. Resultados esperados

Listar os resultados computacionais.

Exemplo:

```text
results/etapa/
├── resultado_01.csv
├── resultado_02.xlsx
├── tabela_final.csv
└── figura_final.pdf