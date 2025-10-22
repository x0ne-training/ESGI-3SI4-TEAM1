CC = gcc
CFLAGS = -Wall -Wextra -std=c99

OBJ = main.o game.o utils.o score.o
EXEC = menteur

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJ)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f $(OBJ) $(EXEC)
