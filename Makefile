install:
	uv sync --all-groups

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

update_lang:
	uv run django-admin makemessages -l ru

compile_lang:
	uv run django-admin compilemessages

start-server:
	uv run python manage.py runserver

lint:
	uv run ruff check

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

test:
	uv run python manage.py test

test-cov:
	uv run pytest --cov=task_manager --cov-report=term --cov-report=xml

clear-cache:
	find . -type d \( -name '__pycache__' -o -name '.pytest_cache' -o -name '.ruff_cache' \) -exec rm -r {} +
