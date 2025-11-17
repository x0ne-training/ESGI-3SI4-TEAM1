CC = gcc
CFLAGS = -Wall -Wextra -std=c11

OBJ = main.o game.o

all: loup_garou

loup_garou: $(OBJ)
	$(CC) $(CFLAGS) -o loup_garou $(OBJ)

main.o: main.c game.h player.h
	$(CC) $(CFLAGS) -c main.c

game.o: game.c game.h player.h
	$(CC) $(CFLAGS) -c game.c

clean:
	rm -f *.o loup_garou
