ARCH := $(shell getconf LONG_BIT)
CC=gcc
CFLAGS=-I. -I../vlfeat-0.9.20
LIBS_64=-L../vlfeat-0.9.20/bin/glnxa64 -lvl
LIBS_32=-L../vlfeat-0.9.20/bin/glnx86 -lvl
LIBS=$(LIBS_$(ARCH))
ALL = vlfeat_wrapper.so

all: $(ALL)

clean:
	rm -rf vlfeat_wrapper.so __pycache__ *~

vlfeat_wrapper.so: fishervector_wrapper.c gmm_wrapper.c dsift_wrapper.c
	$(CC) -shared -fPIC -o $@ $^ $(CFLAGS) $(LIBS)


