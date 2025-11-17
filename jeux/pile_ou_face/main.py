#!/usr/bin/env python3
"""
Jeu : Pile ou Face 🪙
"""
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import random

# --- Fenêtre principale ---
root = tk.Tk()
root.title("Pile ou Face 🪙")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# --- Chargement des images ---
pile_img = ImageTk.PhotoImage(Image.open("pile.png").resize((200, 200)))
face_img = ImageTk.PhotoImage(Image.open("face.png").resize((200, 200)))
win_img = ImageTk.PhotoImage(Image.open("win.png").resize((150, 150)))
lose_img = ImageTk.PhotoImage(Image.open("lose.png").resize((150, 150)))

# --- Variables globales ---
current_side = "pile"
is_animating = False
player_choice = None

# --- Fonctions ---
def choose(choice):
    """Le joueur choisit pile ou face"""
    global player_choice
    if is_animating:
        return
    player_choice = choice
    flip_coin()

def flip_coin():
    """Lance la pièce (démarre l'animation)"""
    global is_animating
    if player_choice is None:
        show_popup("⚠️ Attention", "Choisis PILE ou FACE avant de lancer !")
        return
    is_animating = True
    animate_flip(0)

def animate_flip(step):
    """Fait tourner la pièce sans mouvement vertical"""
    global is_animating, current_side

    total_steps = 50  # nombre d'étapes de l'animation

    # Rotation visuelle (pile ↔ face)
    if step % 3 == 0:  # fréquence du changement de face
        current_side = "face" if current_side == "pile" else "pile"

    # Mise à jour de l'image (rotation simulée)
    canvas.itemconfig(coin_image, image=pile_img if current_side == "pile" else face_img)

    if step < total_steps:
        root.after(40, animate_flip, step + 1)  # vitesse de rotation
    else:
        is_animating = False
        show_result()

def show_result():
    """Affiche le résultat final et ouvre une fenêtre de résultat"""
    global player_choice
    result = random.choice(["pile", "face"])

    # Affiche la vraie face de la pièce
    canvas.itemconfig(coin_image, image=pile_img if result == "pile" else face_img)

    # Vérifie le résultat
    if result == player_choice:
        show_popup("🎉 Gagné !", f"C’était bien {result.upper()} !", win_img)
    else:
        show_popup("😢 Perdu !", f"C’était {result.upper()}...", lose_img)

    player_choice = None  # Réinitialise pour le prochain tour

def show_popup(title, message, image=None):
    """Crée une petite fenêtre popup avec texte et image"""
    popup = Toplevel(root)
    popup.title(title)
    popup.geometry("300x300")
    popup.resizable(False, False)
    popup.configure(bg="#f0f0f0")

    tk.Label(popup, text=title, font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

    if image:
        tk.Label(popup, image=image, bg="#f0f0f0").pack(pady=10)
        popup.image = image  # évite que l’image soit effacée par le garbage collector

    tk.Label(popup, text=message, font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
    tk.Button(popup, text="Fermer", font=("Arial", 12), bg="#0078D7", fg="white",
            command=popup.destroy).pack(pady=10)

# --- Interface principale ---
title = tk.Label(root, text="🎮 Jeu : Pile ou Face", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=20)

canvas = tk.Canvas(root, width=300, height=300, bg="#f0f0f0", highlightthickness=0)
canvas.pack()
coin_image = canvas.create_image(150, 150, image=pile_img)

frame_btn = tk.Frame(root, bg="#f0f0f0")
frame_btn.pack(pady=20)

btn_pile = tk.Button(frame_btn, text="Je choisis PILE 🪙", font=("Arial", 13),
                    bg="#0078D7", fg="white", activebackground="#005A9E",
                    width=14, command=lambda: choose("pile"))
btn_pile.grid(row=0, column=0, padx=10)

btn_face = tk.Button(frame_btn, text="Je choisis FACE 💰", font=("Arial", 13),
                    bg="#0078D7", fg="white", activebackground="#005A9E",
                    width=14, command=lambda: choose("face"))
btn_face.grid(row=0, column=1, padx=10)

root.mainloop()
