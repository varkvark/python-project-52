build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

clear-cache:
	find . -type d \( -name '__pycache__' -o -name '.pytest_cache' -o -name '.ruff_cache' \) -exec rm -r {} +
