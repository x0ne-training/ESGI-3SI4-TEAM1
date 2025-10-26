#include <stdio.h>
#include <stdlib.h>
#include "menteur-3000.h"

int main() {
    char reponse[100];
    intro();

    poser_question("As-tu déjà menti à ta mère ?", reponse, 100);
    analyse(reponse);

    poser_question("\nAs-tu déjà mangé quelque chose tombé par terre ?", reponse, 100);
    analyse(reponse);

    poser_question("\nPenses-tu être plus intelligent qu’une IA ?", reponse, 100);
    analyse(reponse);

    verdict();

    printf("\nAppuie sur une touche pour quitter...\n");
    system("pause");
    return 0;
}
