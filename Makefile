list:
	clear
	@echo "Available commands:"
	@echo "up - Start the project"
	@echo "upd - Start the project in background"
	@echo "build - Build the project"
	@echo "stop - Stop the project"
	@echo "down - Stop and remove the project"
	@echo "restart - Restart the project"
	@echo "make-migrations - Create new migrations based on the changes you have made to your models"
	@echo "migrate - Apply migrations to your database"
	@echo "shell - Run the Python shell"
	@echo "logs - Show logs"
	@echo "create-super-user - Create a superuser"
	@echo "docker-stop-all - Stop all running containers"
	@echo "load-fixtures - Load fixtures"


up:
	clear
	@docker-compose up

upd:
	clear
	@docker-compose up -d

build:
	clear
	@docker-compose build

stop:
	clear
	@docker-compose stop

down:
	clear
	@docker-compose down

restart:
	clear
	@docker-compose restart

make-migrations:
	clear
	@docker-compose run --rm web python manage.py makemigrations

migrate:
	clear
	@docker-compose run --rm web python manage.py migrate

shell:
	clear
	@docker-compose run --rm web python manage.py shell

logs:
	clear
	@docker-compose logs -tf

create-super-user:
	clear
	@docker-compose run --rm web python manage.py createsuperuser

docker-stop-all:
	clear
	docker stop `docker ps -q`
	docker ps

create-schema:
	clear
	@docker-compose run --rm web python manage.py graph_models -a -o schema/schema.png

test:
	clear
	@docker-compose run --rm web python manage.py test

ruff-check:
	clear
	@docker-compose run --rm web ruff check .

ruff-format:
	clear
	@docker-compose run --rm web ruff format .

ruff-fix:
	clear
	@docker-compose run --rm web ruff check --fix .

pre-commit-install:
	clear
	pre-commit install
