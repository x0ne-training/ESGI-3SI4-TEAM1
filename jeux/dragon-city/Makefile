CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -O2
OBJS = main.o functions.o
TARGET = dragon_mini

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c functions.h
	$(CC) $(CFLAGS) -c main.c

functions.o: functions.c functions.h
	$(CC) $(CFLAGS) -c functions.c

clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: all clean
