dev:
	python3 ./marmut/manage.py runserver

freeze:
	pip freeze > requirements.txt

setup-mac:
	python3 -m venv .venv

setup-win:
	python -m venv .venv

requirements:
	pip install -r requirements.txt