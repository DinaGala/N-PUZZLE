PYTHON=python3

all: build run

build:
	$(PYTHON) setup.py build_ext --inplace

run:
	python3 -m solver.main $(file)

test:
	python3 -m unittest discover -s tests

clean:
	rm -rf solutions/* build __pycache__ *.c *.so solver/*.c solver/*.so 

.PHONY: run test clean build all
