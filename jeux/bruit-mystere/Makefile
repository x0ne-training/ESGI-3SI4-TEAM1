CC = gcc
CFLAGS = -Wall -Wextra

all: bruit

bruit: main.o sounds.o
	$(CC) $(CFLAGS) main.o sounds.o -o bruit

main.o: main.c sounds.h
	$(CC) $(CFLAGS) -c main.c

sounds.o: sounds.c sounds.h
	$(CC) $(CFLAGS) -c sounds.c

clean:
	rm -f *.o bruit
