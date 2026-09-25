# ============================================================
# Sistema Adaptativo de Classificação Multicritério
# de Fluidos de Corte
#
# Ambiente-base R do projeto.
#
# IMPORTANTE:
# - este arquivo prepara apenas a infraestrutura;
# - pacotes científicos serão definidos pela equipe;
# - renv será a fonte das dependências R quando implementado;
# - nenhuma análise é executada durante o build.
# ============================================================

FROM rocker/verse:4.5.0

# ------------------------------------------------------------
# Configurações gerais
# ------------------------------------------------------------

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# ------------------------------------------------------------
# Diretório padrão do projeto
# ------------------------------------------------------------

WORKDIR /workspace

# ------------------------------------------------------------
# Copia o repositório para a imagem
# ------------------------------------------------------------

COPY . /workspace

# ------------------------------------------------------------
# Dependências R
#
# NÃO instalar manualmente aqui os pacotes científicos
# enquanto o ambiente renv ainda não estiver definido.
#
# Futuramente, a restauração poderá ser integrada ao
# Docker depois que renv.lock representar o ambiente real.
# ------------------------------------------------------------

# Exemplo FUTURO:
#
# RUN R -e "install.packages('renv')"
# RUN R -e "renv::restore()"
#
# NÃO ATIVAR nesta fase.

# ------------------------------------------------------------
# Pipeline
#
# Não executar targets, testes, relatórios ou análises
# durante a construção da imagem.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Comando padrão
# ------------------------------------------------------------

CMD ["bash"]