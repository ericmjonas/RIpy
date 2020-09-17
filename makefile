

test: all

clean:
	rm -Rf *.so build

all: clean
	python setup.py build_ext --inplace
#	python test.py
