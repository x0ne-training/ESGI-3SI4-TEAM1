# Jeu Undercover en C

## Description
Jeu de déduction inspiré du vrai Undercover. Les joueurs reçoivent des mots secrets selon leur rôle :
- Citoyen : mot commun
- Undercover : mot proche
- Mr White (optionnel) : mot inconnu

## Règles
- Chaque joueur donne un indice sans dire son mot.
- Après la discussion, les joueurs votent pour éliminer quelqu'un.
- Le joueur éliminé révèle son rôle et son mot.
- Les citoyens gagnent si tous les undercovers et Mr White sont éliminés.
- Les undercovers gagnent s'ils restent autant ou plus nombreux que les citoyens.
- Mr White gagne s'il devine le mot des citoyens après avoir été éliminé.

## Compilation
```bash
make
