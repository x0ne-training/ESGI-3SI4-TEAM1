import turtle

# Configuration de la fenêtre
wn = turtle.Screen()
wn.title("Jeu Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Tête du serpent
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Boucle principale du jeu
while True:
    wn.update()
