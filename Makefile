.PHONY: release

VERSION := $(shell ./setup.py --version)

release:
	git tag v$(VERSION)
	git push origin v$(VERSION)
