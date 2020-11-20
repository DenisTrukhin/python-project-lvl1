build:
	poetry build

install:
	poetry install

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

lint:
	poetry run flake8 brain_games
