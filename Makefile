.PHONY: docs

all: install clean test lint docs

clean:
	find . -name '*.pyc' | xargs rm

docs:
	cd docs && make clean && make html

flake8:
	flake8 --exclude=migrations src tests

install:
	pip install -e .[docs,test]

isort:
	isort --recursive --check-only --diff src tests

lint: flake8 isort

test:
	py.test tests
