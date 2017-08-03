TEST_PATH = ./tests

.PHONY: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '@' -exec rm -f {} +

lint:
	pylint $(TEST_PATH)/*.py

test:
	python $(TEST_PATH)/__init__.py
