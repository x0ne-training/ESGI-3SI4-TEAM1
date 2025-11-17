#include <stdio.h>
#include <stdlib.h>
#include "sounds.h"

int main() {
    int score = 0;
    printf("=== 🔊 JEU DU BRUIT MYSTERE ===\n");
    printf("Devine à quoi correspond le bruit !\n");
    printf("(Réponds avec un mot : ex: chat, voiture, explosion)\n\n");

    score += ask_sound("MIAOUUUUUU !!", "chat");
    score += ask_sound("BROOOOOOMMMM", "voiture");
    score += ask_sound("PLOP SPLATCH", "eau");
    score += ask_sound("BIP BIP BIP BIP", "alarme");
    score += ask_sound("BOUM", "explosion");
