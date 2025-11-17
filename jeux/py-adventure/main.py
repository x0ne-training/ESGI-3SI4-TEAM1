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


inventaire = []

salles = {
    "entrée": gerer_entree,
    "tunnel_venteux": gerer_tunnel_venteux,
    "salle_echo": gerer_salle_echo,
}

def gerer_salle_echo():
    print("\nVous êtes dans une grande salle. Le moindre bruit crée un écho.")
    print("Au centre, une vieille CLÉ brille sur un rocher.")
    print("Actions possibles : revenir, lueur, prendre cle")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    if choix == "lueur": return "impasse"
    if choix == "prendre cle":
        if "clé" not in inventaire:
            print("Vous avez pris la clé.")
            inventaire.append("clé")
        else:
            print("Vous avez déjà la clé.")
    return "salle_echo"


def gerer_tunnel_venteux():
    print("\nLe vent siffle. Vous apercevez une FISSURE avec une serrure ancienne.")
    print("Actions possibles : revenir, utiliser cle")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    if choix == "utiliser cle":
        if "clé" in inventaire:
            return "salle_tresor"
        else:
            print("La serrure est solide. Il vous manque la clé.")
            return "tunnel_venteux"
    return "tunnel_venteux"


# --- Boucle principale ---
position_joueur = "entrée"
while True:
    print(f"Inventaire : {inventaire}")

    if position_joueur in salles:
        fonction_salle = salles[position_joueur]
        position_joueur = fonction_salle()
    elif position_joueur == "salle_tresor":
        print("\nLa clé tourne parfaitement. Vous trouvez un coffre rempli d'or ! Vous avez gagné !")
        break
    elif position_joueur == "impasse":
        print("\nC'est une impasse ! L'aventure s'arrête ici.")
        break
    else: # Sécurité au cas où une position serait invalide
        print("Erreur: Le joueur est perdu.")
        break

print("Merci d'avoir joué !")