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

# Balle
balle = turtle.Turtle()
balle.speed(0)
balle.shape("circle")
balle.color("white")
balle.penup()
balle.goto(0, 0)
balle.dx = 0.2  # vitesse horizontale
balle.dy = 0.2  # vitesse verticale

# Affichage du score
affichage = turtle.Turtle()
affichage.speed(0)
affichage.color("white")
affichage.penup()
affichage.hideturtle()
affichage.goto(0, 260)
affichage.write("Gauche: 0  Droite: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions pour déplacer les raquettes
def raquette_gauche_haut():
    y = raquette_gauche.ycor()
    if y < 250:
        y += 20
    raquette_gauche.sety(y)

def raquette_gauche_bas():
    y = raquette_gauche.ycor()
    if y > -240:
        y -= 20
    raquette_gauche.sety(y)

def raquette_droite_haut():
    y = raquette_droite.ycor()
    if y < 250:
        y += 20
    raquette_droite.sety(y)

def raquette_droite_bas():
    y = raquette_droite.ycor()
    if y > -240:
        y -= 20
    raquette_droite.sety(y)