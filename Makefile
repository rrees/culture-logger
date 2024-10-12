
.PHONY: serve deploy

serve:
	pipenv run python runserver.py

deploy:
	flyctl deploy