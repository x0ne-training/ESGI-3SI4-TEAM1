# Pierre-Feuille-Ciseaux

Jeu de Pierre-Feuille-Ciseaux en C contre l'ordinateur, avec affichage en couleur, compteur de scores et rejouabilité.

---

## Installation

Cloner le dépôt, se déplacer dans le dossier, puis compiler avec `make` :

```bash
git clone https://github.com/x0ne-training/ESGI-3SI4-TEAM1.git
cd pierre-feuille-ciseaux
make
```

---

## Lancer le jeu

```bash
./pfc
```

---

## Compiler manuellement

Si vous n'utilisez pas Make :

```bash
gcc -Wall -Wextra main.c fonctions.c -o pfc
./pfc
```

---

## Règles du jeu

1. Choisissez entre **Pierre** (1), **Feuille** (2) ou **Ciseaux** (3)
2. L'ordinateur fait son choix aléatoirement
3. Le gagnant est déterminé selon les règles classiques :
    - Pierre bat Ciseaux
    - Ciseaux bat Feuille
    - Feuille bat Pierre
4. Les scores sont conservés entre les parties

---

## Structure du projet

```
pierre-feuille-ciseaux/
├── main.c          # Logique principale du jeu
├── fonctions.c     # Fonctions (choix ordi, résultat, scores)
├── pfc.h           # Déclarations et constantes
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
=== PIERRE-FEUILLE-CISEAUX ===

Choisissez :
1 - Pierre
2 - Feuille
3 - Ciseaux

Votre choix : 1

Vous a choisi : Pierre
Ordinateur a choisi : Ciseaux

Vous avez gagné !

========== SCORES ==========
Vous : 1 victoires
Ordinateur : 0 victoires
Egalites : 0
============================

Voulez-vous rejouer ? (o/n) : o
```

---

## Fonctionnalités

- Choix entre Pierre, Feuille et Ciseaux
- Couleurs ANSI (Pierre bleu, Feuille vert, Ciseaux rouge)
- Ordinateur avec choix aléatoire
- Détermination automatique du gagnant
- Compteur de scores persistant
- Option pour rejouer

---

## Auteur

Projet réalisé dans le cadre de l'apprentissage de Git et de la programmation en C.