build:
	docker compose build

test:
	docker compose run --rm r Rscript -e "testthat::test_dir('tests/testthat')"

pipeline:
	docker compose run --rm r Rscript -e "targets::tar_make()"

audit:
	docker compose run --rm r Rscript scripts/run_audit.R

report:
	docker compose run --rm r Rscript scripts/render_all.R
