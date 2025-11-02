#ifndef QUIZ_H
#define QUIZ_H

#define MAX_QUESTIONS 10

typedef struct {
    char *question;
    char *options[4];
    int answer; // index de la bonne réponse (0-3)
} Question;

void startQuiz(Question questions[], int numQuestions);

#endif
