CC = gcc
CFLAGS = -Wall -Wextra -std=c11

all: qi-patate.exe

qi-patate.exe: main.o fonctions.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c qi-patate.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c qi-patate.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	del /Q *.o *.exe 2>nul || rm -f *.o *.exe
