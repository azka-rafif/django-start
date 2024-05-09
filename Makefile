dev:
	python3 ./marmut/manage.py runserver 0.0.0.0:8000

freeze:
	pip freeze > requirements.txt

setup-mac:
	python3 -m venv .venv

setup-win:
	python -m venv .venv

requirements:
	pip install -r requirements.txt