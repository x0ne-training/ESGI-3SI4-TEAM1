CC = gcc
CFLAGS = -Wall -Wextra -std=c99
OBJ = main.o game.o utils.o score.o
EXEC = menteur.exe

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	del /F /Q $(OBJ) $(EXEC)