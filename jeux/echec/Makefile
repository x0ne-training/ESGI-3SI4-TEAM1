
CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = echecs.exe
OBJS = main.o fonctions.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c echecs.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c echecs.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f *.o $(TARGET)

run: $(TARGET)
	./$(TARGET)