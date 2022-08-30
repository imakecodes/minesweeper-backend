all: help

help:
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "ℹ️ Comandos disponíveis ℹ️"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "⭐️ help               : Exibe esta mensagem"
	@echo "⭐️ run                : Executa a aplicação fora do docker"
	@echo "⭐️ run-worker         : Executa Celery"
	@echo "⭐️ blue               : Executa blue"
	@echo "⭐️ isort              : Executa isort"
	@echo "⭐️ docker-run         : Levanta toda a aplicação utilizando Docker"
	@echo "⭐️ docker-run-app     : Levanta apenas a aplicação utilizando Docker"
	@echo "⭐️ docker-run-worker  : Levanta apenas o Celery utilizando Docker"
	@echo "⭐️ shell              : Acessa o shell do Django"
	@echo "⭐️ makemigrations     : Gera as novas migrações de banco"
	@echo "⭐️ migrate            : Executa as novas migrações de banco"
	@echo "⭐️ collectstatic      : Atualiza os arquivos estáticos no bucket"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"

run:
	@poetry run python manage.py runserver 0.0.0.0:7788

celery:
	@poetry run celery -A app worker -l INFO --concurrency=2 -Q default -E

docker-run:
	@docker-compose up

docker-run-app:
	@docker-compose up app

docker-run-worker:
	@docker-compose up worker

shell:
	@poetry run python manage.py shell

makemigrations:
	@poetry run python manage.py makemigrations

migrate:
	@poetry run python manage.py migrate

collectstatic:
	@poetry run python manage.py collectstatic

blue:
	@poetry run blue .

isort:
	@poetry run isort .
