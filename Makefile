run:
	python3 -m solver.main

runfix:
	python3 -m solver.main ./boards/npuzzle-3-1.txt
test:
	python3 -m unittest discover -s tests

