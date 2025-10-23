#include "le-million.h"
#include <string.h>
#include <ctype.h>

static Question questions[MAX_QUESTIONS];
static int questions_count = 0;
static int jokers_used_5050 = 0, jokers_used_phone = 0, jokers_used_audience = 0;

void init_questions(void) {
    // Remplir 15 questions (exemples en français)
    questions_count = 15;

    questions[0] = (Question){
            "Quelle est la capitale de la France ?",
            {"Lyon", "Marseille", "Paris", "Nice"},
            2
    };

    questions[1] = (Question){
            "Quel métal a pour symbole chimique 'Fe' ?",
            {"Fer", "Fluor", "Francium", "Fermium"},
            0
    };

    questions[2] = (Question){
            "Quel est le plus grand océan sur Terre ?",
            {"Atlantique", "Indien", "Arctique", "Pacifique"},
            3
    };

    questions[3] = (Question){
            "Qui a peint la 'Joconde' ?",
            {"Michel-Ange", "Léonard de Vinci", "Raphaël", "Donatello"},
            1
    };

    questions[4] = (Question){
            "Combien de joueurs y a-t-il dans une équipe de football (sur le terrain) ?",
            {"9", "10", "11", "12"},
            2
    };

    questions[5] = (Question){
            "Lequel de ces animaux est un marsupial ?",
            {"Ours", "Kangourou", "Loup", "Dauphin"},
            1
    };

    questions[6] = (Question){
            "Quel élément est nécessaire à la photosynthèse ?",
            {"Azote", "Oxygène", "Carbone", "Lumière"},
            3
    };

    questions[7] = (Question){
            "En informatique, que signifie 'CPU' ?",
            {"Central Processing Unit", "Computer Personal Unit", "Control Protocol Unit", "Central Program Unit"},
            0
    };

    questions[8] = (Question){
            "Quel pays a remporté la Coupe du Monde de football en 2018 ?",
            {"Brésil", "France", "Allemagne", "Espagne"},
            1
    };

    questions[9] = (Question){
            "Quel nombre est premier ?",
            {"21", "29", "27", "33"},
            1
    };

    questions[10] = (Question){
            "Quel est le plus long des fleuves suivants ?",
            {"Seine", "Nil", "Loire", "Taureau"},
            1
    };

    questions[11] = (Question){
            "Quelle planète est la plus proche du Soleil ?",
            {"Vénus", "Mars", "Mercure", "Jupiter"},
            2
    };

    questions[12] = (Question){
            "Qui a écrit 'Le Petit Prince' ?",
            {"Victor Hugo", "Antoine de Saint-Exupéry", "Albert Camus", "Marcel Proust"},
            1
    };

    questions[13] = (Question){
            "Combien de couleurs y a-t-il dans un arc-en-ciel traditionnel ?",
            {"5", "6", "7", "8"},
            2
    };

    questions[14] = (Question){
            "Quelle unité mesure la fréquence ?",
            {"Newton", "Watt", "Hertz", "Pascal"},
            2
    };
}

int get_questions_count(void) {
    return questions_count;
}
    