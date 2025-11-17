# main.py

def gerer_tunnel_venteux():
    print("\nLe vent siffle dans ce tunnel étroit. Vous apercevez une FISSURE dans le mur.")
    print("Actions possibles : revenir, fissure")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    if choix == "fissure": return "salle_tresor" # Nouvelle salle !
    return "tunnel_venteux"


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
    if position_joueur == "entrée": position_joueur = gerer_entree()
    elif position_joueur == "tunnel_venteux": position_joueur = gerer_tunnel_venteux()
    elif position_joueur == "salle_echo": position_joueur = gerer_salle_echo()
    elif position_joueur == "salle_tresor":
        print("\nDerrière la fissure, vous trouvez un coffre rempli d'or ! Vous avez gagné !")
        break
    elif position_joueur == "impasse":
        print("\nC'est une impasse ! L'aventure s'arrête ici.")
        break

print("Merci d'avoir joué !")
