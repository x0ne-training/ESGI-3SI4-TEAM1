CC = gcc
CFLAGS = -Wall -Wextra -std=c11

OBJ = main.o quiz.o questions.o

quiz: $(OBJ)
	$(CC) $(CFLAGS) -o quiz $(OBJ)

main.o: main.c quiz.h questions.h
	$(CC) $(CFLAGS) -c main.c

quiz.o: quiz.c quiz.h
	$(CC) $(CFLAGS) -c quiz.c

questions.o: questions.c questions.h quiz.h
	$(CC) $(CFLAGS) -c questions.c

clean:
	rm -f *.o quiz
