CC = gcc
CFLAGS = -Wall -Wextra -std=c11
OBJ = main.o game.o

foret: $(OBJ)
	$(CC) $(CFLAGS) -o foret $(OBJ)

main.o: main.c game.h player.h
	$(CC) $(CFLAGS) -c main.c

game.o: game.c game.h player.h
	$(CC) $(CFLAGS) -c game.c

clean:
	rm -f *.o foret
