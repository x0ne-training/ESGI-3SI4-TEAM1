# Solitaire Pyramide

Jeu de Solitaire Pyramide en C, avec affichage en couleur, compteur de scores et rejouabilité.

---

## Installation

Cloner le dépôt, se déplacer dans le dossier, puis compiler avec `make` :

```bash
git clone https://github.com/x0ne-training/ESGI-3SI4-TEAM1.git
cd solitaire
make
```

---

## Lancer le jeu

```bash
./solitaire
```

---

## Compiler manuellement

Si vous n'utilisez pas Make :

```bash
gcc -Wall -Wextra main.c fonctions.c -o solitaire
./solitaire
```

---

## Règles du jeu

1. Une pyramide de **28 cartes** est disposée sur 7 lignes
2. Retirez des **paires de cartes** dont la somme fait **13**
    - As = 1
    - Valet = 11
    - Dame = 12
    - Roi = 13
3. Les **Rois** (valeur 13) se retirent seuls
4. Une carte est accessible si :
    - Elle est sur la dernière ligne
    - OU les deux cartes en dessous ont été retirées
5. Objectif : **Retirer toutes les cartes de la pyramide**

---

## Structure du projet

```
solitaire/
├── main.c          # Logique principale du jeu
├── fonctions.c     # Fonctions (pyramide, cartes, victoire)
├── solitaire.h     # Déclarations et structures
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
=== SOLITAIRE PYRAMIDE ===

Regles : Retirez des paires de cartes qui font 13
As=1, Valet=11, Dame=12, Roi=13
Les Rois se retirent seuls

              7P  3C  
            9K  AC  RK  
          5T  DT  8P  VC  
        2C  4P  6K  VT  9P  
      3T  RT  5C  8K  2P  10C  
    4K  6P  7C  9T  AT  5P  10T  

1 - Retirer une paire
2 - Retirer un Roi
3 - Abandonner

Votre choix : 1

Premiere carte - Ligne (1-7) : 7
Premiere carte - Colonne (1-7) : 3
Deuxieme carte - Ligne (1-7) : 7
Deuxieme carte - Colonne (1-7) : 5

Paire retiree !
```

Fin de partie :

```
*** BRAVO ! Vous avez gagne ! ***

========== SCORES ==========
Victoires : 1
Defaites : 0
============================

Voulez-vous rejouer ? (o/n) : 
```

---

## Fonctionnalités

- Pyramide de 28 cartes (7 lignes)
- Couleurs ANSI (Rouge pour Cœur/Carreau, Noir pour Pique/Trèfle)
- Mélange aléatoire des cartes
- Vérification automatique des paires (somme = 13)
- Vérification de l'accessibilité des cartes
- Détection automatique de victoire
- Compteur de scores (victoires/défaites)
- Option pour rejouer

---

## Symboles des couleurs

- C = Cœur (rouge)
- K = Carreau (rouge)
- P = Pique (noir)
- T = Trèfle (noir)

---

## Auteur

Projet réalisé dans le cadre de l'apprentissage de Git et de la programmation en C.