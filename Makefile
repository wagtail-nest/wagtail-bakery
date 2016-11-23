.PHONY: docs

all: install clean test lint docs

clean:
	find . -name '*.pyc' | xargs rm

docs:
	cd docs && make clean && make html

flake8:
	flake8 src/ tests/

install:
	pip install -e .[docs,test]

isort:
	isort --check-only --diff --recursive src/ tests/

lint: flake8 isort

test:
	python -m py.test tests/
