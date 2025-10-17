#ifndef AI_H
#define AI_H

#include "fonctions.h"

void ai_init(void);
void ai_place_ships(Case p[TAILLE][TAILLE]);
Point ai_choose_shot(Case opponent_view[TAILLE][TAILLE]);
void ai_report_result(Point last, bool hit);

#endif