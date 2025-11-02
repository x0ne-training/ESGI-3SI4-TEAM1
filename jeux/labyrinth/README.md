# Escape the Labyrinth

## Description

Escape the Labyrinth est un jeu en console écrit en C où le joueur doit trouver la sortie d’un labyrinthe généré aléatoirement. Vous incarnez un aventurier qui se déplace dans un labyrinthe semé d’obstacles et doit atteindre la sortie avant de perdre toute santé.

## Fonctionnalités

- Labyrinthe généré aléatoirement.
- Déplacement du joueur : Haut (Z), Bas (S), Gauche (Q), Droite (D).
- Collision avec les murs du labyrinthe.
- Affichage du labyrinthe et de la position du joueur.
- Détection de la victoire lorsque le joueur atteint la sortie.
- Possibilité d’ajouter des événements ou objets futurs.

## Structure du projet

labyrinth/
├── main.c # Point d'entrée du jeu
├── game.c # Logique du jeu
├── game.h # Déclarations des fonctions de jeu
├── maze.c # Génération et affichage du labyrinthe
├── maze.h # Déclarations des fonctions du labyrinthe
├── player.c # Gestion du joueur
├── player.h # Déclarations de la structure Player
└── Makefile # Fichier pour compiler le projet


## Compilation

Pour compiler le jeu, exécutez :

```bash
make
./labyrinth
