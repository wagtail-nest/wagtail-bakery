.PHONY: help all clean install flake8 isort lint test
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'


all: install clean test lint ## Install, test and lint the project.

clean: ## Remove Python file artifacts.
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

install: ## Install dependencies.
	pip install -e .[test]

flake8: ## Run flake8 on the project.
	flake8 src/

isort: ## Run isort on the project.
	isort --check-only --diff --recursive src/

lint: flake8 isort ## Lint the project.

test: ## Test the project.
	py.test
