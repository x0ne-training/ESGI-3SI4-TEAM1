# main.py

def gerer_entree():
    print("\nVous êtes à l'entrée sombre d'une grotte.")
    print("Actions possibles : gauche, droite")
    choix = input("> ").lower()
    if choix == "gauche": return "tunnel_venteux"
    if choix == "droite": return "salle_echo"
    return "entrée" # Reste dans la même salle si le choix est invalide

def gerer_tunnel_venteux():
    print("\nLe vent siffle dans ce tunnel étroit.")
    print("Actions possibles : revenir")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    return "tunnel_venteux"

def gerer_salle_echo():
    print("\nVous êtes dans une grande salle. Le moindre bruit crée un écho.")
    print("Actions possibles : revenir, lueur")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    if choix == "lueur": return "impasse"
    return "salle_echo"

# --- Boucle principale ---
position_joueur = "entrée"
while True:
    if position_joueur == "entrée":
        position_joueur = gerer_entree()
    elif position_joueur == "tunnel_venteux":
        position_joueur = gerer_tunnel_venteux()
    elif position_joueur == "salle_echo":
        position_joueur = gerer_salle_echo()
    elif position_joueur == "impasse":
        print("\nC'est une impasse ! L'aventure s'arrête ici.")
        break
    
    # On ajoute une option globale pour quitter
    if position_joueur == "quitter": # Si une fonction renvoyait "quitter"
        break

print("Merci d'avoir joué !")
