RUN_DEPS := dev_env paper_tracker/db_timestamp
run: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py runserver

.PHONY: dump
# dump: db_dump.sql
# db_dump.sql: paper_tracker/db.sqlite3
dump:
	sqlite3 paper_tracker/db.sqlite3 ".output db_dump.sql" ".dump"


paper_tracker/db_timestamp: db_dump.sql
	mv paper_tracker/db.sqlite3 paper_tracker/db.sqlite3_backup
	sqlite3 paper_tracker/db.sqlite3 < db_dump.sql
	touch paper_tracker/db_timestamp

shell: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py shell
makemigrate makemigration makemigrations: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py makemigrations papers
migrate: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py migrate
superuser adminuser admin_user user: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py createsuperuser

dev_env/timestamp: requirements.txt
	virtualenv dev_env -p python3
	dev_env/bin/pip install -r requirements.txt
	touch dev_env/timestamp
dev_env: dev_env/timestamp
