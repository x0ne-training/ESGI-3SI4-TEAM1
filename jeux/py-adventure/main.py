# main.py

def gerer_tunnel_venteux():
    print("\nLe vent siffle dans ce tunnel étroit. Vous apercevez une FISSURE dans le mur.")
    print("Actions possibles : revenir, fissure")
    choix = input("> ").lower()
    if choix == "revenir": return "entrée"
    if choix == "fissure": return "salle_tresor" # Nouvelle salle !
    return "tunnel_venteux"

def afficher_aide():
    print("\n--- AIDE ---")
    print("Commandes générales : 'quitter', 'aide', 'inventaire'")
    print("Actions en jeu : regardez les options affichées (ex: 'gauche', 'prendre cle')")

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
quitter_jeu = False
while not quitter_jeu:
    print(f"Inventaire : {inventaire}")

    if position_joueur in salles:
        fonction_salle = salles[position_joueur]
        # On ne peut pas gérer 'aide'/'quitter' dans les fonctions,
        # donc on le gère avant d'appeler la fonction de salle.
        # C'est une limite de notre design actuel, mais acceptable.
        position_joueur = fonction_salle() # Pour ce commit, on garde la 

print("Merci d'avoir joué !")