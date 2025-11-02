CC=gcc
CFLAGS=-Wall -Wextra -std=c11

OBJ=main.o game.o maze.o player.o

labyrinth: $(OBJ)
	$(CC) $(CFLAGS) -o labyrinth $(OBJ)

main.o: main.c game.h maze.h player.h
	$(CC) $(CFLAGS) -c main.c

game.o: game.c game.h player.h maze.h
	$(CC) $(CFLAGS) -c game.c

maze.o: maze.c maze.h player.h
	$(CC) $(CFLAGS) -c maze.c

player.o: player.c player.h
	$(CC) $(CFLAGS) -c player.c

clean:
	rm -f *.o labyrinth
