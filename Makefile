TEST_PATH = ./tests

.PHONY: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '@' -exec rm -f {} +

lint:
	pylint $(TEST_PATH)/*.py

docs:
	pdoc --html src/*.py
	pdoc --html tests/*.py
	mv ./*.html docs/

test:
	python $(TEST_PATH)/__init__.py
