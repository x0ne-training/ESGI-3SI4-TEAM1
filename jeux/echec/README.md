# Jeu d'Échecs en C

Un jeu d'échecs simple en ligne de commande, sans interface graphique.

## Structure du projet

```
echecs.h          - Déclarations et structures
fonctions.c       - Implémentation des fonctions
main.c            - Boucle principale du jeu
Makefile          - Compilation automatique
echecs.exe        - Exécutable
```

## Compilation

```bash
make
```

## Exécution

```bash
./echecs.exe
# ou
make run
```

## Comment jouer

- Les **Blancs** (majuscules) commencent: P T C F D R
- Les **Noirs** (minuscules): p t c f d r
- Format de coup: `e2 e4` (position départ + position arrivée)
- Notation: colonnes a-h, lignes 1-8
- Tapez `q` pour quitter

## Exemple de partie

```
  a b c d e f g h
8 t c f d r f c t 8
7 p p p p p p p p 7
6 . . . . . . . . 6
5 . . . . . . . . 5
4 . . . . . . . . 4
3 . . . . . . . . 3
2 P P P P P P P P 2
1 T C F D R F C T 1
  a b c d e f g h

Joueur Blancs (majuscules)

Votre coup: e2 e4
```

## Règles implémentées (simplifiées)

- Mouvements de base de toutes les pièces
- Capture du roi = victoire
- Pas de roque, en passant, ou promotion
- Pas de vérification d'échec/échec et mat

## Nettoyage

```bash
make clean
```