CC = gcc
CFLAGS = -Wall -Wextra -std=c11
OBJ = main.o game.o questions.o
TARGET = mini_fifa

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

main.o: main.c game.h questions.h stats.h
	$(CC) $(CFLAGS) -c main.c

game.o: game.c game.h stats.h
	$(CC) $(CFLAGS) -c game.c

questions.o: questions.c questions.h
	$(CC) $(CFLAGS) -c questions.c

clean:
	rm -f $(OBJ) $(TARGET)
