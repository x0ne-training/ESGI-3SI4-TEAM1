#include <stdio.h>
#include "quiz.h"

void startQuiz(Question questions[], int numQuestions) {
    int score = 0;
    for (int i = 0; i < numQuestions; i++) {
        printf("\nQuestion %d: %s\n", i+1, questions[i].question);
        for (int j = 0; j < 4; j++) {
            printf("%d) %s\n", j+1, questions[i].options[j]);
        }

        int choice;
        printf("Votre réponse (1-4) : ");
        scanf("%d", &choice);

        if (choice - 1 == questions[i].answer) {
            printf("Correct ! ✅\n");
            score++;
        } else {
            printf("Faux ! ❌ La bonne réponse était : %s\n", questions[i].options[questions[i].answer]);
        }
    }
    printf("\nVotre score final : %d/%d\n", score, numQuestions);
}
