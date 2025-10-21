CC = gcc
CFLAGS = -Wall -Wextra
TARGET = solitaire
OBJS = main.o fonctions.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c solitaire.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c solitaire.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJS) $(TARGET)

run: $(TARGET)
	./$(TARGET)