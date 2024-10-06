install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --force-reinstall dist/*.whl

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build