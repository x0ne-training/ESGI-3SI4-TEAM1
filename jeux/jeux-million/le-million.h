#ifndef LE_MILLION_H
#define LE_MILLION_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_CHOICES 4
#define MAX_QUESTIONS 15

typedef struct {
    const char *question;
    const char *choices[MAX_CHOICES];
    int correct; // 0..3
} Question;

// accès aux questions
void init_questions(void);
int get_questions_count(void);
const Question* get_question(int idx);

// jokers
int joker_5050(int qidx, int out_choices[]); // remplit out_choices avec 2 indices valides (dont la bonne)
void joker_phone(int qidx);
void joker_audience(int qidx);

// utilitaires
int ask_user_choice(const Question *q, int removed_mask); // removed_mask: bits 0..3: si bit 1 => choix retiré
void print_question(const Question *q, int removed_mask);

#endif // LE_MILLION_H
