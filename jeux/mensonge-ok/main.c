#include <stdio.h>
#include "functions.h"

int main(void) {
    printf("=== JEU DU MENSONGE ===\n");
    printf("Regle : reponds OBLIGATOIREMENT le contraire de la verite.\n\n");

    if (!ask("Est-ce que 2+2=4 ?", 1)) return 0;
    if (!ask("Est-ce que les oiseaux sont des poissons ?", 0)) return 0;
    if (!ask("Est-ce que tu es humain ?", 1)) return 0;
    if (!ask("Est-ce qu'une pizza est liquide ?", 0)) return 0;
    if (!ask("Est-ce que tu mens en ce moment ?", 1)) return 0;

    printf("\nTU AS GAGNE !!!\n");
    printf("Tu es officiellement un menteur professionnel.\n");
    return 0;
}
