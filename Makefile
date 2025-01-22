PYTHON_VERSION=python3.13

test:
	python3 ./jumbles.py
	python3 ./jumbles.py --count=3
	python3 ./jumbles.py --words=3
	python3 ./jumbles.py --count=2 --words=4


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






