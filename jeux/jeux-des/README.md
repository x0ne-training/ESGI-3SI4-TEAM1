# Jeu de Dés (Duel) — C

Mini-jeu en C en console : le joueur lance un dé, puis l’ordinateur.  
Le plus grand score gagne la manche. Possibilité de rejouer.

---

## Installation

Cloner le dépôt, se rendre dans le dossier et compiler :

```bash
git clone <url-du-depot>
cd jeu-des
make
```

## Compilation manuelle sans make
gcc -Wall -Wextra main.c fonctions.c -o des.exe
./des.exe
