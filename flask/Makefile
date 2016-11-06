RUN_DEPS := dev_env db.sqlite3
dbg: $(RUN_DEPS)
	FLASK_DEBUG=true FLASK_APP=main.py dev_env/bin/flask run
run: $(RUN_DEPS)
	FLASK_APP=main.py dev_env/bin/flask run

dev_env/timestamp: requirements.txt
	virtualenv dev_env
	dev_env/bin/pip install -r requirements.txt
	touch dev_env/timestamp
dev_env: dev_env/timestamp

db.sqlite3: dev_env model.py
	dev_env/bin/python -c "from model import db; db.create_all()"
