import turtle

# Configuration de la fenêtre
fenetre = turtle.Screen()
fenetre.title("Pong by Rayane")
fenetre.bgcolor("black")
fenetre.setup(width=800, height=600)
fenetre.tracer(0)  # désactive les mises à jour automatiques

# Score
score_gauche = 0
score_droite = 0