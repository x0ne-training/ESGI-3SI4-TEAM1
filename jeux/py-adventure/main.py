# main.py
# Un jeu d'aventure textuel simple en Python sans bibliothèques externes.

# --- État du jeu ---
# L'inventaire contient les objets que le joueur a ramassés.
inventaire = []
# La position actuelle du joueur dans le monde du jeu.
position_joueur = "entrée"

# --- Fonctions des Salles ---
# Chaque fonction gère la logique pour une salle spécifique.
# Elle décrit la salle, demande une action au joueur, et retourne sa nouvelle position.

def gerer_entree():
    """Gère la logique pour la salle d'entrée."""
    print("\nVous êtes à l'entrée sombre d'une grotte.")
    print("Un courant d'air froid vient d'un tunnel à votre GAUCHE.")
    print("Un faible écho résonne depuis un chemin à votre DROITE.")
    print("Actions possibles : gauche, droite, quitter")
    
    choix = input("> ").lower()
    
    if choix == "gauche":
        return "tunnel_venteux"
    if choix == "droite":
        return "salle_echo"
    if choix == "quitter":
        return "quitter"
        
    print("Commande invalide.")
    return "entrée" # Reste sur place si le choix est invalide

def gerer_tunnel_venteux():
    """Gère la logique pour le tunnel venteux."""
    print("\nLe vent siffle dans ce tunnel étroit. Vous apercevez une FISSURE dans le mur, fermée par une serrure ancienne.")
    print("Actions possibles : revenir, utiliser cle, quitter")
    
    choix = input("> ").lower()
    
    if choix == "revenir":
        return "entrée"
    if choix == "utiliser cle":
        if "clé" in inventaire:
            return "salle_tresor"
        else:
            print("La serrure est solide. Il vous manque la clé.")
    if choix == "quitter":
        return "quitter"

    print("Commande invalide.")
    return "tunnel_venteux"

def gerer_salle_echo():
    """Gère la logique pour la salle de l'écho."""
    print("\nVous êtes dans une grande salle. Le moindre bruit crée un écho assourdissant.")
    print("Au centre, une vieille CLÉ brille sur un rocher. Au fond, vous voyez une faible LUEUR.")
    print("Actions possibles : revenir, lueur, prendre cle, quitter")
    
    choix = input("> ").lower()
    
    if choix == "revenir":
        return "entrée"
    if choix == "lueur":
        return "impasse"
    if choix == "prendre cle":
        if "clé" not in inventaire:
            print("Vous avez pris la clé.")
            inventaire.append("clé")
        else:
            print("Vous avez déjà la clé.")
    if choix == "quitter":
        return "quitter"
        
    print("Commande invalide.")
    return "salle_echo"

# --- Moteur du jeu ---
# Ce dictionnaire associe les chaînes de caractères des positions aux fonctions qui les gèrent.
salles = {
    "entrée": gerer_entree,
    "tunnel_venteux": gerer_tunnel_venteux,
    "salle_echo": gerer_salle_echo,
}

# --- Boucle Principale ---
print("--- Bienvenue dans l'Aventure de la Grotte Perdue ---")

while True:
    # Affiche l'inventaire au début de chaque tour pour que le joueur sache ce qu'il possède.
    print(f"\nInventaire : {inventaire}")

    # Gère les fins de partie (victoire, défaite, ou si le joueur quitte).
    if position_joueur == "quitter":
        break
    if position_joueur == "salle_tresor":
        print("\nLa clé tourne parfaitement dans la serrure. La fissure s'élargit...")
        print("Derrière, vous trouvez un coffre rempli d'or ! VOUS AVEZ GAGNÉ !")
        break
    if position_joueur == "impasse":
        print("\nLa lueur n'était qu'un reflet sur une paroi humide. C'est une impasse. L'aventure s'arrête ici...")
        break
    
    # Appelle la fonction de la salle actuelle pour obtenir la nouvelle position du joueur.
    if position_joueur in salles:
        fonction_de_la_salle = salles[position_joueur]
        position_joueur = fonction_de_la_salle()
    else:
        # Sécurité au cas où une position invalide serait retournée par une fonction.
        print(f"Erreur : La position '{position_joueur}' est inconnue.")
        break

print("\nMerci d'avoir joué !")
