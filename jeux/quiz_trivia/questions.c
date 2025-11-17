#include "questions.h"

int getQuestions(Question questions[]) {
    questions[0] = (Question){"Quelle est la capitale de la France?", {"Paris", "Lyon", "Marseille", "Nice"}, 0};
    questions[1] = (Question){"Combien de continents y a-t-il sur Terre?", {"5", "6", "7", "8"}, 2};
    questions[2] = (Question){"Quel est le langage de programmation que vous utilisez maintenant?", {"Python", "C", "Java", "JavaScript"}, 1};
    questions[3] = (Question){"Quelle est la planète rouge?", {"Terre", "Mars", "Jupiter", "Venus"}, 1};
    questions[4] = (Question){"Qui a peint la Joconde?", {"Van Gogh", "Picasso", "Da Vinci", "Monet"}, 2};

    return 5; // nombre de questions
}
