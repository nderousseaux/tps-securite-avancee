LDFLAGS = -m32 -z execstack
CFLAGS = -m32 -O0 -static -g -fno-stack-protector \
	         -mpreferred-stack-boundary=2 -D_FORTIFY_SOURCE=0
  all: testsc
testsc: testsc.o
