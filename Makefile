.PHONY: release test

VERSION := $(shell ./setup.py --version)

test:
	py.test --cov clinch --cov-report term-missing

release:
	git tag v$(VERSION)
	git push origin v$(VERSION)
