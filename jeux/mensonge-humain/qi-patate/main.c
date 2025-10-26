#include <stdio.h>
#include <stdlib.h>
#include "qi-patate.h"

int main() {
    char reponse[100];
    intro();

    poser_questi
    poser_question("4. Est-ce que tu sais faire du jonglage avec des patates ?", reponse, 100);
    analyse(reponse);

    poser_question("5. Quelle est ta couleur de patate preferee ?", reponse, 100);
    analyse(reponse);

    poser_question("6. Peux-tu nommer 3 pays qui commencent par Z ?", reponse, 100);
    analyse(reponse);

    poser_question("7. As-tu deja parle a une patate ?", reponse, 100);
    analyse(reponse);

    poser_question("8. Quelle est ta super puissance secrète ?", reponse, 100);
    analyse(reponse);

    poser_question("9. As-tu deja joue a cache-cache avec un chat ?", reponse, 100);
    analyse(reponse);

    poser_question("10. Combien de secondes peux-tu tenir en apnee ?", reponse, 100);
    analyse(reponse);

    poser_question("11. Peux-tu toucher ton nez avec ta langue ?", reponse, 100);
    analyse(reponse);

    poser_question("12. As-tu deja ecrit une lettre a une patate ?", reponse, 100);
    analyse(reponse);

    poser_question("13. Combien de minutes par jour regardes-tu les nuages ?", reponse, 100);
    analyse(reponse);

    poser_question("14. Peux-tu chanter l'alphabet a l'envers ?", reponse, 100);
    analyse(reponse);

    poser_question("15. As-tu deja reve d'etre une patate ?", reponse, 100);
    analyse(reponse);

    poser_question("16. Combien de secondes peux-tu sauter sur place ?", reponse, 100);
    analyse(reponse);

    poser_question("17. Peux-tu faire un bruit de patate ?", reponse, 100);
    analyse(reponse);

    poser_question("18. As-tu deja joue a l'echelle avec un escargot ?", reponse, 100);
    analyse(reponse);

    poser_question("19. Combien de feuilles de papier peux-tu plier en 1 minute ?", reponse, 100);
    analyse(reponse);

    poser_question("20. Quelle est la meilleure maniere de cuisiner une patate ?", reponse, 100);
    analyse(reponse);

    verdict_final();

    printf("\nAppuie sur une touche pour quitter...\n");
    system("pause");
    return 0;
}
