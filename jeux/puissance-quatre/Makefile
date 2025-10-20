CC = gcc
CFLAGS = -Wall -Wextra
TARGET = puissance4
OBJS = main.o fonctions.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c puissance4.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c puissance4.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJS) $(TARGET)

run: $(TARGET)
	./$(TARGET)