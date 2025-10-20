# Puissance 4

Jeu de Puissance 4 en C pour 2 joueurs en local, avec affichage en couleur, compteur de scores et rejouabilité.

---

## Installation

Cloner le dépôt, se déplacer dans le dossier, puis compiler avec `make` :

```bash
git clone https://github.com/x0ne-training/ESGI-3SI4-TEAM1.git
cd puissance4
make
```

---

## Lancer le jeu

```bash
./puissance4
```

---

## Compiler manuellement

Si vous n'utilisez pas Make :

```bash
gcc -Wall -Wextra main.c fonctions.c -o puissance4
./puissance4
```

---

## Règles du jeu

1. Le joueur **Rouge** (R) commence
2. Le joueur **Jaune** (J) joue ensuite
3. Choisissez une colonne (1-7) pour placer votre jeton
4. Le jeton tombe en bas de la colonne choisie
5. Le premier qui aligne **4 jetons** gagne (horizontal, vertical, diagonal)
6. Les scores sont conservés entre les parties

---

## Structure du projet

```
puissance4/
├── main.c          # Logique principale du jeu
├── fonctions.c     # Fonctions (affichage, victoire, scores)
├── puissance4.h    # Déclarations et constantes
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

Démarrage :

```
=== JEU DE PUISSANCE 4 ===

  1   2   3   4   5   6   7
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+

Joueur R, choisissez une colonne (1-7) : 
```

Fin de partie :

```
  1   2   3   4   5   6   7
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   | J |   |   |   |   |
|   |   | R | J |   |   |   |
|   | J | R | R | J |   |   |
| J | R | R | R | J | J |   |
+---+---+---+---+---+---+---+

Joueur Rouge a gagné !

========== SCORES ==========
Joueur Rouge : 2 victoires
Joueur Jaune : 1 victoires
Matchs nuls : 0
============================

Voulez-vous rejouer ? (o/n) : 
```

---

## Fonctionnalités

- Grille 7x6 interactive
- Couleurs ANSI (Rouge et Jaune)
- Détection automatique de victoire (4 alignés)
- Détection de match nul
- Validation des colonnes
- Les jetons tombent par gravité
- Compteur de scores persistant
- Option pour rejouer

---
