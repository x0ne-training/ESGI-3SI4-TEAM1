CC = gcc
CFLAGS = -Wall -Wextra -std=c11

all: menteur-3000.exe

menteur-3000.exe: main.o fonctions.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c menteur-3000.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c menteur-3000.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	del /Q *.o *.exe 2>nul || rm -f *.o *.exe
