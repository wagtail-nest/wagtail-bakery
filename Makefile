all: install clean test lint

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

flake8:
	flake8 src/

install:
	pip install -e .[test]

isort:
	isort --check-only --diff --recursive src/

lint: flake8 isort

test:
	py.test
