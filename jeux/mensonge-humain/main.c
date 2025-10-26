#include <stdio.h>
#include <stdlib.h>
#include "menteur-3000.h"

int main() {
    char reponse[100];
    intro();

    poser_question("1. As-tu deja menti a ta mere ?", reponse, 100);
    analyse(reponse);

    poser_question("\n2. As-tu deja mange quelque chose tombe par terre ?", reponse, 100);
    analyse(reponse);

    poser_question("\n3. As-tu deja triche a un examen ?", reponse, 100);
    analyse(reponse);

    poser_question("\n4. As-tu deja dit 'je suis presque arrive' alors que tu etais encore chez toi ?", reponse, 100);
    analyse(reponse);

    poser_question("\n5. As-tu deja pleure devant un film d'animation ?", reponse, 100);
    analyse(reponse);

    poser_question("\n6. As-tu deja blame ton chien pour une betise que tu as faite ?", reponse, 100);
    analyse(reponse);

    poser_question("\n7. As-tu deja mange tout un paquet de chips seul ?", reponse, 100);
    analyse(reponse);

    poser_question("\n8. As-tu deja envoye un message a la mauvaise personne ?", reponse, 100);
    analyse(reponse);

    poser_question("\n9. As-tu deja fait semblant de comprendre quelque chose sans rien piger ?", reponse, 100);
    analyse(reponse);

    poser_question("\n10. As-tu deja regarde une serie entiere en une journee ?", reponse, 100);
    analyse(reponse);

    poser_question("\n11. As-tu deja parle a ton ordi quand il bugue ?", reponse, 100);
    analyse(reponse);

    poser_question("\n12. As-tu deja invente une excuse debile pour ne pas sortir ?", reponse, 100);
    analyse(reponse);

    poser_question("\n13. As-tu deja espionne ton ex sur les reseaux ?", reponse, 100);
    analyse(reponse);

    poser_question("\n14. As-tu deja mange la nourriture de quelqu'un d'autre au frigo ?", reponse, 100);
    analyse(reponse);

    poser_question("\n15. As-tu deja essaye de chanter sous la douche en te croyant star ?", reponse, 100);
    analyse(reponse);

    poser_question("\n16. As-tu deja ri a une blague que tu n'as pas comprise ?", reponse, 100);
    analyse(reponse);

    poser_question("\n17. As-tu deja pretendu etre malade pour ne pas aller en cours ou au travail ?", reponse, 100);
    analyse(reponse);

    poser_question("\n18. As-tu deja parle tout seul ?", reponse, 100);
    analyse(reponse);

    poser_question("\n19. As-tu deja oublie le nom de quelqu'un juste apres l'avoir rencontre ?", reponse, 100);
    analyse(reponse);

    poser_question("\n20. As-tu deja fait semblant d'etre occupe pour ignorer un appel ?", reponse, 100);
    analyse(reponse);

    verdict();

    printf("\nAppuie sur une touche pour quitter...\n");
    system("pause");
    return 0;
}
