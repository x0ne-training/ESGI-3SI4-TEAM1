
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

main.o: main.c memory.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c memory.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJ) $(TARGET)
