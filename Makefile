.PHONY: build run local venv

VENV_NAME?=venv

tag=$(notdir $(CURDIR))
tag_lc=$(shell echo $(tag) | tr A-Z a-z)


build:
	docker build -t $(tag_lc):latest .

run:
	docker run -p 5000:5000 $(ARGS) $(tag_lc):latest

local:
	FLASK_ENV=development $(ARGS) flask run

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate; pip install -r requirements.txt
