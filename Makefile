TEST_PATH = ./tests
SRC_PATH = ./src
DOCS_PATH = ./docs

.PHONY: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '@' -exec rm -f {} +

lint:
	pylint $(TEST_PATH)/*.py

doc:
	for f in $(TEST_PATH)/*.py ; do \
		pdoc --html "$f" ; \
		mv *.html $(DOCS_PATH) ; \
	done

tests:
	python $(TEST_PATH)/__init__.py
