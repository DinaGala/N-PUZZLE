PYTHON=python3

all: build run

build:
	$(PYTHON) setup.py build_ext --inplace

run:
	python3 -m solver.main

runfix:
	python3 -m solver.main ./boards/npuzzle-3-1.txt

test:
	python3 -m unittest discover -s tests

clean:
	rm -rf solutions/* build __pycache__ *.c *.so solver/*.c solver/*.so 

.PHONY: run runfix test clean build all
