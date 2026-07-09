test:
	python -m unittest discover tests

run:
	python mini-projects/expense_tracker.py

lint:
	python -m py_compile mini-projects/*.py