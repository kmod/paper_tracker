RUN_DEPS := dev_env
dbg: $(RUN_DEPS)
	true
run: $(RUN_DEPS)
	true

dev_env/timestamp: requirements.txt
	virtualenv dev_env -p python3
	dev_env/bin/pip install -r requirements.txt
	touch dev_env/timestamp
dev_env: dev_env/timestamp
