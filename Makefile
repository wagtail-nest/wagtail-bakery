.PHONY: help all clean install format test
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'


all: clean install format test ## Install, format and test the project.

clean: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	rm -rf build dist

install: ## Install dependencies.
	pip install -e .[test]

format: ## Format the code.
	black .
	isort .
	flake8 .

test: ## Test the project.
	pytest --cov

cov:  ## Generate coverage report (manually open htmlcov/index.html in browser)
	pytest --cov --cov-report html
