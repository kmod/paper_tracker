run: dev_env
	FLASK_APP=main.py dev_env/bin/flask run

dev_env:
	virtualenv dev_env
	dev_env/bin/pip install -r requirements.txt
