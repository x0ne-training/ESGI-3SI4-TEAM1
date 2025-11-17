CC = gcc
CFLAGS = -Wall -Wextra -std=c11

SRC = main.c game.c questions.c
OBJ = $(SRC:.c=.o)
EXEC = reigns

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(EXEC)
