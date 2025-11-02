#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "questions.h"

Question getRandomQuestion() {
    static Question questions[] = {
        {
            "Le peuple réclame plus de nourriture.",
            "Distribuer des réserves (+Peuple, -Richesse)",
            "Refuser (-Peuple, +Richesse)",
            {0, -10, 0, +15},
            {0, +10, 0, -15}
        },
        {
            "L'Église veut construire une cathédrale.",
            "Financer le projet (+Foi, -Richesse)",
            "Refuser (-Foi, +Richesse)",
            {0, -15, +20, 0},
            {0, +10, -20, 0}
        },
        {
            "L’armée demande plus de ressources.",
            "Accorder (+Pouvoir, -Richesse)",
            "Refuser (-Pouvoir, +Richesse)",
            {+15, -10, 0, 0},
            {-15, +10, 0, 0}
        },
        {
            "Une famine touche les campagnes.",
            "Aider les paysans (+Peuple, -Richesse)",
            "Ignorer (-Peuple, +Richesse)",
            {0, -15, 0, +20},
            {0, +10, 0, -25}
        }
    };

    
}
