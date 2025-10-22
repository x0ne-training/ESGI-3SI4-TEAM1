CC=gcc
CFLAGS=-Wall -Wextra -std=c11
OBJ=main.o fonctions.o

all: des.exe

des.exe: $(OBJ)
	$(CC) $(OBJ) -o des.exe

main.o: main.c des.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c des.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f *.o des.exe
