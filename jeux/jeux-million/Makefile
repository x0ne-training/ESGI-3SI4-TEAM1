CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -O2

OBJ = main.o fonctions.o

all: jeux-million

jeux-million: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ)

main.o: main.c le-million.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c le-million.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJ) jeux-million
