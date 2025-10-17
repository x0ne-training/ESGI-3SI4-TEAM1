CC=gcc
CFLAGS=-Wall -Wextra -std=c11
OBJ=main.o fonctions.o ai.o
all: bataille

bataille: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ)

main.o: main.c fonctions.h ai.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c fonctions.h
	$(CC) $(CFLAGS) -c fonctions.c

ai.o: ai.c ai.h fonctions.h
	$(CC) $(CFLAGS) -c ai.c

clean:
	rm -f *.o bataille
