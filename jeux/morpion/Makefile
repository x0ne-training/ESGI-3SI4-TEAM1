CC = gcc # compilateur
CFLAGS = -Wall -Wextra r # options de compilation
TARGET = morpion # nom de l'exécutable
OBJS = main.o fonctions.o # fichiers objets

all: $(TARGET) # cible principale

$(TARGET): $(OBJS) # création de l'exécutable
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

main.o: main.c morpion.h # compilation de main.c
	$(CC) $(CFLAGS) -c main.c

fonctions.o: fonctions.c morpion.h # compilation de fonctions.c
	$(CC) $(CFLAGS) -c fonctions.c

clean: # suppression des fichiers objets et de l'exécutable
	rm -f $(OBJS) $(TARGET)

run: $(TARGET) # exécution du programme
	./$(TARGET)