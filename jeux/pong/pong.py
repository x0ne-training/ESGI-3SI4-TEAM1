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

# Assignation des touches
fenetre.listen()
fenetre.onkeypress(raquette_gauche_haut, "z")
fenetre.onkeypress(raquette_gauche_bas, "s")
fenetre.onkeypress(raquette_droite_haut, "Up")
fenetre.onkeypress(raquette_droite_bas, "Down")

# Boucle principale du jeu
while True:
    fenetre.update()

    # Déplacement de la balle
    balle.setx(balle.xcor() + balle.dx)
    balle.sety(balle.ycor() + balle.dy)

    # Bord haut
    if balle.ycor() > 290:
        balle.sety(290)
        balle.dy *= -1

    # Bord bas
    if balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1

    # Balle à droite
    if balle.xcor() > 390:
        balle.goto(0, 0)
        balle.dx *= -1
        score_gauche += 1
        affichage.clear()
        affichage.write(f"Gauche: {score_gauche}  Droite: {score_droite}", align="center", font=("Courier", 24, "normal"))

    # Balle à gauche
    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dx *= -1
        score_droite += 1
        affichage.clear()
        affichage.write(f"Gauche: {score_gauche}  Droite: {score_droite}", align="center", font=("Courier", 24, "normal"))

    # Collision avec raquette droite
    if (340 < balle.xcor() < 350) and (raquette_droite.ycor() - 50 < balle.ycor() < raquette_droite.ycor() + 50):
        balle.setx(340)
        balle.dx *= -1

    # Collision avec raquette gauche
    if (-350 < balle.xcor() < -340) and (raquette_gauche.ycor() - 50 < balle.ycor() < raquette_gauche.ycor() + 50):
        balle.setx(-340)
        balle.dx *= -1