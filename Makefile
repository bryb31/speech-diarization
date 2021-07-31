.PHONY : clean

all : .venv/bin/speech

.venv :
	python3 -m venv .venv

piplist : install
	.venv/bin/pip list

.venv/bin/speech : .venv
	.venv/bin/pip install -e .

.venv/bin/flake8 : .venv/bin/speech
	.venv/bin/pip install flake8

.venv/bin/coverage : .venv/bin/speech
	.venv/bin/pip install coverage


test : .venv/bin/speech .venv/bin/flake8 .venv/bin/coverage
	.venv/bin/pip install pytest
	.venv/bin/flake8 --max-line-length 120 speech
	.venv/bin/coverage run -m pytest

clean :
	rm -rf 