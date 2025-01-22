PYTHON_VERSION=python3.13


.venv.installed:
	$(PYTHON_VERSION) -m venv .venv
	direnv allow
	date > .venv.installed

nothing:
	echo easy

which: 
	which python3
	python3 --version


# force.install:
#	rm -f .installed
install: .venv.installed requirements.txt
	pip install --upgrade pip -q
	pip install -r requirements.txt 
	date > install

clean:
	rm -rf install .venv .venv.installed






