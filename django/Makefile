RUN_DEPS := dev_env
run: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py runserver

shell: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py shell
makemigrations: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py makemigrations papers
migrate: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py migrate
admin_user: $(RUN_DEPS)
	dev_env/bin/python paper_tracker/manage.py createsuperuser

dev_env/timestamp: requirements.txt
	virtualenv dev_env -p python3
	dev_env/bin/pip install -r requirements.txt
	touch dev_env/timestamp
dev_env: dev_env/timestamp
