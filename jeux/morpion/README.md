# Morpion (Tic-Tac-Toe)

Un jeu de morpion classique en C pour 2 joueurs, avec interface colorée dans le terminal et système de scores.

---

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Règles du jeu](#règles-du-jeu)
- [Structure du projet](#structure-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Commandes Make](#commandes-make)
- [Exemple de partie](#exemple-de-partie)
- [Compilation détaillée](#compilation-détaillée)
- [Dépannage](#dépannage)
- [Contribution](#contribution)

---

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- **GCC** (compilateur C) - version 4.8 ou supérieure
- **Make** (outil de compilation)
- Un terminal supportant les couleurs ANSI :
    - Linux (tous les terminaux)
    - macOS (Terminal, iTerm2)
    - Windows (Git Bash, WSL, Windows Terminal)

### Vérifier les installations

```bash
# Vérifier GCC
gcc --version

# Vérifier Make
make --version
```

---

## Installation

### Méthode 1 : Cloner le dépôt

```bash
# Cloner le projet
git clone https://github.com/x0ne-training/ESGI-3SI4-TEAM1.git

# Aller dans le dossier
cd morpion

# Compiler
make
```

### Méthode 2 : Télécharger le ZIP

1. Téléchargez le projet depuis GitHub
2. Décompressez l'archive
3. Ouvrez un terminal dans le dossier
4. Lancez `make`

---

## Utilisation

### Lancer le jeu

```bash
./morpion
```

### Avec Make

```bash
make run
```

### Compilation manuelle (sans Make)

```bash
gcc -Wall -Wextra main.c fonctions.c -o morpion
./morpion
```

### Sur Windows PowerShell

```powershell
gcc -Wall -Wextra main.c fonctions.c -o morpion
.\morpion
```

---

## Règles du jeu

### Objectif

Aligner **3 symboles identiques** (horizontalement, verticalement ou en diagonale)

### Déroulement

1. Le **joueur X** (rouge) commence toujours
2. Le **joueur O** (bleu) joue ensuite
3. À tour de rôle, chaque joueur choisit une position :
    - Entrez le numéro de **ligne** (1-3)
    - Entrez le numéro de **colonne** (1-3)
4. Le premier qui aligne 3 symboles gagne
5. Si toutes les cases sont remplies sans gagnant : **match nul**

### Après chaque partie

- Les **scores** s'affichent automatiquement
- Possibilité de **rejouer** (o/n)
- Les statistiques sont **conservées** entre les parties

---

## Structure du projet

```
morpion/
│
├── main.c              # Logique principale du jeu
│   └── Boucle de jeu, gestion des tours
│
├── fonctions.c         # Implémentation des fonctions
│   ├── initialiserGrille()
│   ├── afficherGrille()
│   ├── verifierVictoire()
│   ├── grillePleine()
│   ├── demanderRejouer()
│   └── afficherScores()
│
├── morpion.h           # Header file
│   ├── Déclarations des fonctions
│   ├── Définition des constantes
│   └── Variables globales (extern)
│
├── Makefile            # Automatisation compilation
│   ├── all : Compile tout
│   ├── clean : Nettoie
│   └── run : Compile et exécute
│
└── README.md           # Documentation
```

## Fonctionnalités

### Fonctionnalités actuelles

- Grille 3x3 interactive
- Couleurs ANSI (X rouge, O bleu)
- Détection automatique de victoire
- Détection de match nul
- Validation des coups (position + case libre)
- Code propre avec constantes nommées
- Option rejouer après chaque partie
- Compteur de victoires persistant
- Affichage des statistiques
- Compilation avec Make

### Fonctionnalités futures

- Mode contre l'ordinateur (IA)
- Algorithme minimax (IA imbattable)
- Sauvegarde des scores dans fichier
- Historique des parties
- Mode tournoi (meilleur de 3, 5, etc.)
- Grille variable (4x4, 5x5)
- Interface graphique (SDL/ncurses)
- Mode multijoueur réseau

---

## Commandes Make

Le projet utilise un `Makefile` pour simplifier la compilation.

### Commandes disponibles

```bash
# Compiler le projet (crée l'exécutable 'morpion')
make

# Ou explicitement
make all

# Compiler ET exécuter directement
make run

# Nettoyer les fichiers compilés (.o et exécutable)
make clean
```

### Détails du Makefile

```makefile
CC = gcc                    # Compilateur utilisé
CFLAGS = -Wall -Wextra      # Options de compilation
TARGET = morpion            # Nom de l'exécutable
OBJS = main.o fonctions.o   # Fichiers objets nécessaires
```

---

## Exemple de partie

### Démarrage du jeu

```
=== JEU DE MORPION ===

  1   2   3
1   |   |  
  --+---+--
2   |   |  
  --+---+--
3   |   |  

Joueur X, entrez ligne (1-3) : 
```

### Partie en cours

```
  1   2   3
1 O |   |  
  --+---+--
2   | X |  
  --+---+--
3   |   | X

Joueur O, entrez ligne (1-3) : 2
Entrez colonne (1-3) : 1
```

### Fin de partie

```
  1   2   3
1 O | X | X
  --+---+--
2 O | X | O
  --+---+--
3 X | O | X

Joueur X a gagné !

========== SCORES ==========
Joueur X : 3 victoires
Joueur O : 2 victoires
Matchs nuls : 1
============================

Voulez-vous rejouer ? (o/n) : o
```

---

## Compilation détaillée

### Processus de compilation expliqué

Le processus de compilation se fait en 3 étapes :

#### Étape 1 : Prétraitement et compilation en fichiers objets

```bash
# Compiler main.c en main.o
gcc -Wall -Wextra -c main.c

# Compiler fonctions.c en fonctions.o
gcc -Wall -Wextra -c fonctions.c
```

#### Étape 2 : Édition des liens (linking)

```bash
# Lier les fichiers objets pour créer l'exécutable
gcc -Wall -Wextra -o morpion main.o fonctions.o
```

#### Étape 3 : Exécution

```bash
# Linux / macOS / Git Bash
./morpion

# Windows PowerShell
.\morpion
```

### Options de compilation

| Option | Description |
|--------|-------------|
| `-Wall` | Active tous les avertissements standards |
| `-Wextra` | Active des avertissements supplémentaires |
| `-c` | Compile sans lier (crée fichier .o) |
| `-o` | Spécifie le nom du fichier de sortie |

### Compilation en une seule commande

```bash
# Tout en une ligne
gcc -Wall -Wextra main.c fonctions.c -o morpion
```

---

## Dépannage

### Erreur "make: command not found"

**Solution :** Installez Make

```bash
# Ubuntu/Debian
sudo apt install build-essential

# macOS
xcode-select --install

# Windows
# Utilisez WSL ou MinGW
```

Ou compilez manuellement sans Make (voir section Compilation).

### Erreur "morpion.h: No such file or directory"

**Solution :** Vérifiez que tous les fichiers sont dans le même dossier

```bash
ls -l
# Doit afficher : main.c, fonctions.c, morpion.h, Makefile
```

### Les couleurs ne s'affichent pas

**Solution :** Votre terminal ne supporte peut-être pas les codes ANSI

- Windows : Utilisez Git Bash, WSL ou Windows Terminal
- macOS/Linux : Tous les terminaux modernes supportent les couleurs

### Warning "format extra args"

**Solution :** Vérifiez les appels `printf()` dans main.c

```c
// Incorrect
printf("Texte : ", variable);

// Correct
printf("Texte : ");
```

### Boucle infinie après victoire

**Solution :** Vérifiez que les fonctions `verifierVictoire()` et `grillePleine()` utilisent des `return` immédiats et non des variables intermédiaires.

---
