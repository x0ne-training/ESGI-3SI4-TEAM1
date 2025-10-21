# Mastermind

Jeu de Mastermind en C, avec affichage en couleur, historique des tentatives et compteur de scores.

---

## Installation

Cloner le dépôt, se déplacer dans le dossier, puis compiler avec `make` :

```bash
git clone https://github.com/x0ne-training/ESGI-3SI4-TEAM1.git
cd mastermind
make
```

---

## Lancer le jeu

```bash
./mastermind
```

---

## Compiler manuellement

Si vous n'utilisez pas Make :

```bash
gcc -Wall -Wextra main.c fonctions.c -o mastermind
./mastermind
```

---

## Règles du jeu

1. L'ordinateur choisit un **code secret** de 4 couleurs
2. Vous avez **10 tentatives** pour deviner le code
3. Après chaque proposition, vous recevez des indices :
    - **Bien placés** : nombre de couleurs correctes au bon emplacement
    - **Mal placés** : nombre de couleurs correctes mais mal positionnées
4. Gagnez en trouvant le code exact avant la 10ème tentative

---

## Couleurs disponibles

```
1 - Rouge
2 - Vert
3 - Jaune
4 - Bleu
5 - Magenta
6 - Cyan
```

---

## Structure du projet

```
mastermind/
├── main.c          # Logique principale du jeu
├── fonctions.c     # Fonctions (génération, évaluation, affichage)
├── mastermind.h    # Déclarations et constantes
├── Makefile        # Automatisation de la compilation
└── README.md       # Documentation
```

---

## Commandes Make

```bash
make          # Compiler le projet
make run      # Compiler et lancer
make clean    # Nettoyer les fichiers compilés
```

---

## Exemple de partie

```
=== MASTERMIND ===

Devinez le code secret de 4 couleurs !
Vous avez 10 tentatives.

Couleurs disponibles :
1 - Rouge
2 - Vert
3 - Jaune
4 - Bleu
5 - Magenta
6 - Cyan

Tentative 1/10
Entrez votre code (4 chiffres entre 1 et 6) :
Couleur 1 : 1
Couleur 2 : 2
Couleur 3 : 3
Couleur 4 : 4

Votre proposition : R V J B 

Bien places : 1
Mal places : 2

=== HISTORIQUE DES TENTATIVES ===
Tentative 1 : R V J B   -> Bien places: 1, Mal places: 2

Tentative 2/10
...
```

Fin de partie :

```
*** BRAVO ! Vous avez trouve le code secret ! ***
Code secret : R B V J 

========== SCORES ==========
Victoires : 1
Defaites : 0
============================

Voulez-vous rejouer ? (o/n) : 
```

---

## Fonctionnalités

- Code secret généré aléatoirement (4 couleurs parmi 6)
- Couleurs ANSI pour affichage visuel
- Système de feedback (bien placés / mal placés)
- Historique des tentatives avec évaluation
- 10 tentatives maximum
- Compteur de scores (victoires/défaites)
- Option pour rejouer

---

## Auteur

Projet réalisé dans le cadre de l'apprentissage de Git et de la programmation en C.