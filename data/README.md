# Dados Brutos — `data/raw/`

## Finalidade

Esta pasta contém os arquivos de dados originais utilizados no projeto:

```text
Sistema Adaptativo de Classificação Multicritério de Fluidos de Corte
```

Os arquivos armazenados aqui representam as fontes recebidas pelo grupo e devem ser preservados em seu estado original.

---

# Regra principal

Os arquivos em:

```text
data/raw/
```

são considerados **imutáveis**.

Isso significa que não devem ser:

```text
editados
corrigidos manualmente
sobrescritos
reformatados
reorganizados internamente
```

durante a execução da análise.

---

# Arquivos atualmente presentes

Atualmente esta pasta contém material-fonte como:

```text
ensaio_bancada_alunos (2).xlsx
linkacessodrive.txt
```

A função exata de cada arquivo deverá ser confirmada durante o inventário inicial dos dados.

Nenhuma interpretação científica é antecipada neste README.

---

# Planilha original

O arquivo:

```text
ensaio_bancada_alunos (2).xlsx
```

deverá ser tratado como fonte original de dados.

A estrutura, abas, variáveis, fórmulas, unidades e possíveis inconsistências serão avaliadas posteriormente em:

```text
analysis/01_PACHECO_inventario.qmd
analysis/02_PACHECO_auditoria.qmd
```

---

# Arquivo de acesso

O arquivo:

```text
linkacessodrive.txt
```

deve ser preservado conforme recebido.

Se ele servir como referência para acesso a material externo, sua função deverá ser documentada durante o inventário ou na documentação correspondente.

Não transformar seu conteúdo automaticamente em resultado do projeto.

---

# Fluxo correto

O fluxo esperado é:

```text
data/raw/
↓
inventário
↓
auditoria
↓
reconciliação
↓
data/interim/
↓
base canônica
↓
data/processed/
```

---

# `data/raw/`

Contém:

```text
fonte original
material recebido
arquivos externos de dados
```

---

# `data/interim/`

Conterá futuramente:

```text
dados intermediários
resultados de reconciliação
objetos temporários necessários à pipeline
```

Esses arquivos serão gerados durante a execução do projeto.

---

# `data/processed/`

Conterá futuramente a versão processada e validada dos dados, incluindo a base canônica oficial quando ela for produzida.

---

# Não corrigir a planilha original

Se durante a auditoria for encontrado um valor suspeito, o fluxo correto será:

```text
detectar
↓
registrar
↓
investigar
↓
reconciliar
↓
corrigir por código na versão derivada
```

e não:

```text
abrir Excel
↓
alterar célula
↓
salvar por cima
```

---

# Fórmulas

Fórmulas presentes na fonte original também devem ser preservadas.

Quando necessário, valores derivados importantes poderão ser recalculados independentemente em R durante a auditoria.

---

# Divergências

Se o mesmo conceito aparecer com valores diferentes em fontes ou abas distintas:

```text
nenhum valor deverá ser escolhido silenciosamente
```

A divergência deverá ser documentada e reconciliada.

---

# Dados fornecidos pela professora

Qualquer novo arquivo de dados fornecido pela professora poderá ser armazenado nesta pasta quando representar uma fonte original do projeto.

O arquivo deverá ser preservado conforme recebido.

---

# Renomeação de arquivos

Preferencialmente preservar os nomes originais dos arquivos recebidos.

Caso seja necessário criar um nome padronizado para uso computacional, preservar o original e documentar o mapeamento.

Não renomear arquivos apenas por estética sem necessidade.

---

# Versionamento

Caso uma nova versão de um arquivo seja fornecida posteriormente:

```text
não sobrescrever silenciosamente a versão anterior
```

A relação entre as versões deverá ser documentada.

---

# Git

A inclusão de dados brutos no repositório dependerá da política definida pelo grupo quanto a:

```text
tamanho
licença
privacidade
permissão de distribuição
```

A presença local do arquivo em `data/raw/` não significa automaticamente que ele deve ser publicado no GitHub.

---

# `.gitkeep`

O arquivo:

```text
.gitkeep
```

existe apenas para permitir o versionamento da pasta quando necessário.

Ele deve permanecer vazio.

---

# Responsável inicial

A inspeção e auditoria inicial dos dados é responsabilidade principal de:

```text
Pacheco
```

---

# Estado atual

```text
RAW_DATA_STATUS = AVAILABLE

INVENTORY_STATUS = NOT_EXECUTED

AUDIT_STATUS = NOT_EXECUTED

RECONCILIATION_STATUS = NOT_EXECUTED

CANONICAL_DATA_STATUS = NOT_CREATED
```

---

# Princípio final

> Os dados brutos são a referência histórica do projeto. Toda limpeza, correção ou transformação deve acontecer de forma reproduzível fora desta pasta, mantendo intacta a fonte original.