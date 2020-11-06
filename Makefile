all: help

help:
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "ℹ️ Available commands ℹ️"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "⭐️ help                : Show this message"
	@echo "⭐️ clean               : Removes all python cache and temporary files"
	@echo "⭐️ run                 : Runs the application using docker-compose"
	@echo "⭐️ lint                : Lint the source using flake8 codestyle"
	@echo "⭐️ test                : Runs the tests using Docker"
	@echo "⭐️ pre-commit-install  : Install the pre-commit hook"
	@echo "⭐️ pre-commit-run      : Runs the standalone pre-commit routine for checking files"
	@echo "⭐️ update-requirements : Using pip-compile(from pip-tools), update the requirements.txt with fixed version of used libraries"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"

clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +


run:
	@docker-compose up

lint:
	@flake8 .

test: clean
	@docker-compose run --rm app-test python manage.py test

pre-commit-install:
	@pre-commit install

pre-commit-run:
	@pre-commit run --all-files

update-requirements:
	@pip-compile requirements.txt
