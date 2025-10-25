
all: $(TARGET)

$(TARGET): $(OBJ)
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

main.o: main.c petitschevaux.h
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c petitschevaux.h
	$(CC) $(CFLAGS) -c fonctions.c

clean:
	rm -f $(OBJ)
	rm -rf $(BIN_DIR)
