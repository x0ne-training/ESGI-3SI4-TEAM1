import turtle
import time

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

# Fonction de mouvement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Boucle principale du jeu
while True:
    wn.update()
    move()
    time.sleep(0.1)
