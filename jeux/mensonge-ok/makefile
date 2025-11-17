# Compiler les fichiers .c et générer l'exécutable "mensonge"
CC = gcc
CFLAGS = -Wall -Wextra -std=c11

SRC = main.c functions.c
OBJ = $(SRC:.c=.o)
TARGET = mensonge

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
