HEADER = $(shell python --version)
SHELL := /bin/bash
PYTHONP = $(shell python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

all:
	python setup.py build_ext --inplace
	make install
	make clean

install:
	sudo cp imgproc.so $(PYTHONP)

install-pure:
	sudo cp imgproc.py $(PYTHONP)

location:
	@echo $(PYTHONP)
	
install-pygame:
	sudo pip install pygame
	
install-pygame:
	sudo pip install cython

clean:
	rm *.so
	rm *.c
	rm -fr build