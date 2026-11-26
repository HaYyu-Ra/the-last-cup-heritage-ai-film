.PHONY: install validate film clean

install:
	python -m pip install -r requirements.txt

validate:
	python -m pipeline.validate

film: validate
	python -m pipeline.run

clean:
	python -m pipeline.clean
