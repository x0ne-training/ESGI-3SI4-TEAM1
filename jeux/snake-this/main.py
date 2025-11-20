import turtle

# Configuration de la fenêtre
wn = turtle.Screen()
wn.title("Jeu Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Désactive les mises à jour de l'écran

# Boucle principale du jeu
while True:
    wn.update()
