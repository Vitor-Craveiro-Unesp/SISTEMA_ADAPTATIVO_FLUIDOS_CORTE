FROM rocker/verse:4.5.0

WORKDIR /project

RUN R -q -e "install.packages(c('renv','targets','testthat','readxl','openxlsx2','janitor','naniar','skimr','validate','yaml'), repos='https://cloud.r-project.org')"

COPY renv.lock renv.lock
RUN R -q -e "renv::restore(prompt = FALSE)"

CMD ["R"]
