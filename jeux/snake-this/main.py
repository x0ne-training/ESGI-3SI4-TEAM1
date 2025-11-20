import turtle
import time
import random

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

# Nourriture
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Fonctions de changement de direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Raccourcis clavier
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

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

    # Vérifier la collision avec la nourriture
    if head.distance(food) < 20:
        # Déplacer la nourriture à un endroit aléatoire
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

    move()
    time.sleep(0.1)
