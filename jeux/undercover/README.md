# Jeu Undercover avec tirage de cartes

## Description
Jeu de déduction avec tirage de cartes pour déterminer le rôle :
- Citoyen : mot commun
- Undercover : mot proche
- Mr White : mot inconnu

## Règles
1. Chaque joueur tire une carte pour connaître son rôle.
2. Chaque joueur donne un indice sur son mot sans le dire.
3. Vote pour éliminer un joueur suspect.
4. Le joueur éliminé révèle son rôle et son mot.
5. Victoires :
    - Citoyens : tous les Undercover et Mr White éliminés
    - Undercover : restent autant ou plus nombreux que les citoyens
    - Mr White : devine le mot des citoyens après élimination

## Compilation
```bash
make
