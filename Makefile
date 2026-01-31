install:
	uv sync

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

update_lang:
	django-admin makemessages -l ru

compile_lang:
	django-admin compilemessages

start-server:
	python manage.py runserver

lint:
	ruff check

migrate:
	python manage.py makemigrations
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --no-input

test:
	uv run python manage.py test

test-cov:
	uv run pytest --cov=task_manager --cov-report=term --cov-report=xml

clear-cache:
	find . -type d \( -name '__pycache__' -o -name '.pytest_cache' -o -name '.ruff_cache' \) -exec rm -r {} +
