.PHONY: test build clean

test:
	pytest

build:
	python -m build

clean:
	rm -rf build dist *.egg-info .pytest_cache
