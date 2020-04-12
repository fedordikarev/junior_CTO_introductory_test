all: build run local

tag=$(notdir $(CURDIR))
tag_lc=$(shell echo $(tag) | tr A-Z a-z)

build:
	docker build -t $(tag_lc):latest .

run:
	docker run -p 5000:5000 $(ARGS) $(tag_lc):latest

local:
	FLASK_ENV=development flask run
