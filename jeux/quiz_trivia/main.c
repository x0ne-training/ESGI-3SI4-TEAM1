#include <stdio.h>
#include "quiz.h"
#include "questions.h"

int main() {
    Question questions[MAX_QUESTIONS];
    int numQuestions = getQuestions(questions);

    printf("Bienvenue au Quiz Trivia !\n");
    startQuiz(questions, numQuestions);

    return 0;
}
