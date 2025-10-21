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

# Raquette gauche
raquette_gauche = turtle.Turtle()
raquette_gauche.speed(0)
raquette_gauche.shape("square")
raquette_gauche.color("blue")
raquette_gauche.shapesize(stretch_wid=5, stretch_len=1)
raquette_gauche.penup()
raquette_gauche.goto(-350, 0)

# Raquette droite
raquette_droite = turtle.Turtle()
raquette_droite.speed(0)
raquette_droite.shape("square")
raquette_droite.color("red")
raquette_droite.shapesize(stretch_wid=5, stretch_len=1)
raquette_droite.penup()
raquette_droite.goto(350, 0)