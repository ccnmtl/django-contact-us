PY_DIRS=contactus
VE ?= ./ve
SYS_PYTHON ?= python3
PY_SENTINAL ?= $(VE)/sentinal
PIP_VERSION ?= 21.0.1
MAX_COMPLEXITY ?= 8
PY_DIRS ?= $(APP)
DJANGO ?= "Django==2.2.13"

FLAKE8 ?= $(VE)/bin/flake8
PIP ?= $(VE)/bin/pip
COVERAGE ?=$(VE)/bin/coverage

all: flake8 coverage

clean:
	rm -rf $(VE)
	find . -name '*.pyc' -exec rm {} \;
	rm -rf node_modules

$(PY_SENTINAL):
	rm -rf $(VE)
	$(SYS_PYTHON) -m venv $(VE)
	$(PIP) install pip==$(PIP_VERSION)
	$(PIP) install --upgrade setuptools
	$(PIP) install "$(DJANGO)"
	$(PIP) install flake8
	$(PIP) install coveralls
	touch $@

test: $(REQUIREMENTS) $(PY_SENTINAL)
	./ve/bin/python runtests.py

flake8: $(PY_SENTINAL)
	$(FLAKE8) $(PY_DIRS) --max-complexity=$(MAX_COMPLEXITY)

coverage: $(PY_SENTINAL)
	$(COVERAGE) run --source=contactus runtests.py

.PHONY: flake8 test coverage clean
