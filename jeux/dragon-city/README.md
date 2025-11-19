# Projet Jeux

Ce dépôt contient les fichiers sources de mon projet de jeux en C.

## Arborescence principale

```
jeux/
├── mystere/       # Jeu mystère
│   └── mystere.c
├── menteur/       # Jeu menteur
│   └── ...
├── include/       # Fichiers .h
├── .gitignore     # Ignorer .idea, fichiers temporaires, etc.
└── README.md      # Ce fichier
```

## Compilation

Pour compiler les fichiers C :

```bash
gcc -o nom_du_jeu jeux/mystere/mystere.c
./nom_du_jeu
```

## Git

* `.idea/` est ignoré.
* Utiliser des branches pour chaque fonctionnalité : `git checkout -b feature/nom`.

## Auteur

Lucie HP
