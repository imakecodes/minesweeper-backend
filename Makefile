all: help

help:
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "ℹ️ Available commands ℹ️"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "⭐️ help            : Show this message"
	@echo "⭐️ clean           : Removes all python cache and temporary files"
	@echo "⭐️ run             : Runs the application using docker-compose"
	@echo "⭐️ lint            : Lint the source using flake8 codestyle"
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

test:
	@docker-compose run --rm app-test python manage.py test
