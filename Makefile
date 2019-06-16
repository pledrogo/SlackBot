test:
	@echo "run tests"
	py.test --verbose tests
run:
	@echo "run server"
	pip3 install -r requirements.txt
	flask run