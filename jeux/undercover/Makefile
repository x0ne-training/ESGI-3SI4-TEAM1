CC = gcc
CFLAGS = -Wall -Wextra -g
SRC = main.c fonctions.c
OBJ = $(SRC:.c=.o)
BIN_DIR = application
TARGET = $(BIN_DIR)/undercover.exe

all: $(TARGET)

$(TARGET): $(OBJ)
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

main.o: main.c undercover.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c undercover.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJ)
	rm -rf $(BIN_DIR)

