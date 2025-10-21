import random
import sys

# --- Constantes du jeu ---
PRIX_MIN = 1
PRIX_MAX = 1000
NB_TENTATIVES = 10

def lancer_partie():
    """
    Lance une partie du Juste Prix.
    Génère un nombre aléatoire et demande au joueur de le deviner.
    Retourne un code de statut à la fin de la partie.
    
    Codes de retour :
    - 0 : Victoire (le joueur a trouvé le prix)
    - 1 : Défaite (le joueur a épuisé ses tentatives)
    """
    
    # Génération du prix à trouver
    prix_a_trouver = random.randint(PRIX_MIN, PRIX_MAX)
    
    # Messages d'accueil
    print(f"J'ai choisi un prix entre {PRIX_MIN} et {PRIX_MAX}. Vous avez {NB_TENTATIVES} tentatives pour le trouver.")
    print("Bonne chance !")
    print("-" * 30)

    # Boucle principale du jeu qui itère sur le nombre de tentatives
    for i in range(NB_TENTATIVES):
        # Boucle pour gérer les entrées invalides de l'utilisateur
        while True:
            try:
                proposition_str = input(f"Tentative {i + 1}/{NB_TENTATIVES} - Quelle est votre proposition ? : ")
                proposition = int(proposition_str)
                break # Sort de la boucle si la conversion en nombre est réussie
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")

        # Comparaison de la proposition avec le prix à trouver
        if proposition == prix_a_trouver:
            print(f"\nBravo ! Vous avez trouvé le juste prix qui était bien {prix_a_trouver} !")
            return 0  # Code de retour pour une victoire
        elif proposition < prix_a_trouver:
            print("C'est plus !")
        else: # proposition > prix_a_trouver
            print("C'est moins !")
        
        print() # Ajoute un saut de ligne pour la lisibilité

    # Si la boucle se termine sans que le joueur ait trouvé le prix, c'est une défaite
    print("-" * 30)
    print(f"Dommage, vous avez épuisé vos {NB_TENTATIVES} tentatives.")
    print(f"Le juste prix était : {prix_a_trouver}")
    return 1 # Code de retour pour une défaite

# --- POINT D'ENTRÉE PRINCIPAL ---
# Ce bloc ne s'exécute que si le script est lancé directement
if __name__ == "__main__":
    print("--- Lancement du jeu du Juste Prix ---")
    
    # Appelle la fonction principale du jeu et récupère son résultat
    code_de_retour = lancer_partie()
    
    print(f"--- Fin de la partie. Le programme se termine avec le code {code_de_retour}. ---")
    
    # Termine le script en renvoyant le code de retour au système
    sys.exit(code_de_retour)
