all: format test lint

test: poetry.lock
	poetry run pytest -vv

format: poetry.lock
	# reformat all files
	poetry run black .
	poetry run isort .

lint: poetry.lock
	poetry run flake8

# install the project whenever the pyproject.toml file changes,
# using poetry.lock as an indicator of the last time we updated it
poetry.lock: pyproject.toml
	poetry install
	# update the modification time in case the file doesn't get updated
	touch poetry.lock

dev-setup: ci-setup
	pre-commit install

ci-setup:
	poetry install
