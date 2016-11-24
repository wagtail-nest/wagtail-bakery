.PHONY: docs

all: install clean test lint docs

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

docs:
	rm -rf site/ && mkdocs build

flake8:
	flake8 src/

install:
	pip install -e .[docs,test]

isort:
	isort --check-only --diff --recursive src/

lint: flake8 isort

test:
	pytest
