HEADER = $(shell python --version)
SHELL := /bin/bash
PYTHONP = $(shell python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib() + '/imgproc.py')")

install:
	sudo cp imgproc.py $(PYTHONP)
	
location:
	@echo $(PYTHONP)
	
install-pygame:
	sudo pip install pygame