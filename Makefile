## This scaffolding allows for an easy to remember convention.
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

test:
	python -m pytest -vv test_hello.py

all: install lint test