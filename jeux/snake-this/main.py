import turtle
import time
import random

# -- CONFIGURATION DU JEU --
delay = 0.1  # Délai pour rafraîchir l'écran et contrôler la vitesse du jeu

# -- SCORES --
score = 0
high_score = 0

# -- CONFIGURATION DE LA FENÊTRE --
wn = turtle.Screen()
wn.title("Jeu Snake")
wn.bgcolor("dark slate gray") # Couleur de fond
wn.setup(width=600, height=600)
wn.tracer(0)  # Désactive les mises à jour automatiques de l'écran pour un contrôle manuel

# -- TÊTE DU SERPENT --
head = turtle.Turtle()
head.speed(0)  # Vitesse d'animation maximale
head.shape("square")
head.color("lime green")
head.penup()  # Ne laisse pas de trace en se déplaçant
head.goto(0, 0)
head.direction = "stop"  # Direction initiale

# -- NOURRITURE --
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("tomato")
food.penup()
food.goto(0, 100) # Position initiale

# Liste pour stocker les segments du corps du serpent
segments = []

# -- AFFICHAGE DU SCORE --
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()  # Masque l'objet turtle, seul le texte sera visible
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# -- FONCTIONS DE MOUVEMENT --
def go_up():
    """Change la direction du serpent vers le haut, si ce n'est pas vers le bas."""
    if head.direction != "down":
        head.direction = "up"

def go_down():
    """Change la direction du serpent vers le bas, si ce n'est pas vers le haut."""
    if head.direction != "up":
        head.direction = "down"

def go_left():
    """Change la direction du serpent vers la gauche, si ce n'est pas vers la droite."""
    if head.direction != "right":
        head.direction = "left"

def go_right():
    """Change la direction du serpent vers la droite, si ce n'est pas vers la gauche."""
    if head.direction != "left":
        head.direction = "right"

def move():
    """Déplace la tête du serpent de 20 pixels dans la direction actuelle."""
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

# -- CONNEXION DES TOUCHES DU CLAVIER --
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# -- BOUCLE PRINCIPALE DU JEU --
while True:
    wn.update()  # Met à jour l'écran à chaque itération

    # 1. Vérifier la collision avec les bords de la fenêtre
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Cacher les segments existants
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Réinitialiser la liste des segments
        segments.clear()

        # Réinitialiser le score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 2. Vérifier la collision avec la nourriture
    if head.distance(food) < 20:
        # Déplacer la nourriture à une position aléatoire
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Ajouter un nouveau segment au serpent
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)
        
        # Augmenter le score
        score += 10
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # 3. Déplacer les segments du corps
    # Itère à l'envers pour que chaque segment suive le précédent
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Déplacer le premier segment à la position de la tête
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    # 4. Déplacer la tête du serpent
    move()

    # 5. Vérifier la collision avec son propre corps
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Cacher les segments
            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()
            
            # Réinitialiser le score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Pause pour contrôler la vitesse du jeu
    time.sleep(delay)

wn.mainloop() # Garde la fenêtre ouverte
