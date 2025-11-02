"""
Simple Paint (dessin) en Python avec Tkinter.
Fichier: paint_python.py
Description: application de dessin minimaliste avec palette de couleurs,
curseur de taille de pinceau, gomme, annuler, effacer et sauvegarde.
Dépendances: Python standard (tkinter) + Pillow (pour sauvegarder en PNG si possible).

Exécution: 
    pip install pillow
    python paint_python.py

Écrit en français dans les commentaires pour faciliter la lecture.
"""

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
import io
import os

# PIL est optionnel — sert à convertir PostScript en PNG si disponible
try:
    from PIL import Image
except Exception:
    Image = None


class PaintApp:
    def __init__(self, root):
        self.root = root
        root.title("Mini Paint — Python/Tkinter")

        # layout
        self.controls_frame = tk.Frame(root, padx=5, pady=5)
        self.controls_frame.pack(side=tk.TOP, fill=tk.X)

        self.canvas = tk.Canvas(root, bg='white', cursor='cross')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # état du pinceau
        self.brush_color = '#000000'
        self.brush_size = 5
        self.eraser_on = False

        # historique des traits pour annuler (liste de listes d'IDs)
        self.history = []
        self.current_stroke = []

        # création des contrôles
        self._create_controls()

        # binding souris
        self.canvas.bind('<ButtonPress-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_move)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

        # redimensionnement: on veut garder la toile, rien d'autre à faire

    def _create_controls(self):
        # palette de couleurs rapide
        colors = ['#000000', '#FFFFFF', '#FF0000', '#00AA00', '#0000FF', '#FFFF00', '#FFA500', '#800080']
        for c in colors:
            btn = tk.Button(self.controls_frame, bg=c, width=2, command=lambda col=c: self.set_color(col))
            btn.pack(side=tk.LEFT, padx=1)

        # sélecteur de couleur
        col_btn = tk.Button(self.controls_frame, text='Choisir couleur', command=self.choose_color)
        col_btn.pack(side=tk.LEFT, padx=6)

        # curseur taille
        size_label = tk.Label(self.controls_frame, text='Taille:')
        size_label.pack(side=tk.LEFT, padx=(12,0))
        self.size_slider = tk.Scale(self.controls_frame, from_=1, to=50, orient=tk.HORIZONTAL, command=self.change_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

        # gomme
        self.eraser_btn = tk.Button(self.controls_frame, text='Gomme', command=self.toggle_eraser)
        self.eraser_btn.pack(side=tk.LEFT, padx=6)

        # annuler
        undo_btn = tk.Button(self.controls_frame, text='Annuler', command=self.undo)
        undo_btn.pack(side=tk.LEFT, padx=6)

        # effacer tout
        clear_btn = tk.Button(self.controls_frame, text='Effacer', command=self.clear)
        clear_btn.pack(side=tk.LEFT, padx=6)

        # sauvegarder
        save_btn = tk.Button(self.controls_frame, text='Sauvegarder', command=self.save)
        save_btn.pack(side=tk.LEFT, padx=6)

        # instruction rapide
        instr = tk.Label(self.controls_frame, text='Cliquer-glisser pour dessiner. Utiliser "Choisir couleur" pour plus de couleurs.')
        instr.pack(side=tk.RIGHT)

    # --- événements souris ---
    def on_button_press(self, event):
        self.current_stroke = []
        self.last_x, self.last_y = event.x, event.y

    def on_move(self, event):
        x, y = event.x, event.y
        color = 'white' if self.eraser_on else self.brush_color
        line_id = self.canvas.create_line(self.last_x, self.last_y, x, y,
                                          width=self.brush_size, capstyle=tk.ROUND, smooth=True)
        # appliquer la couleur (création de l'objet n'utilise pas param 'fill' si la couleur blanche apparaît mal)
        self.canvas.itemconfig(line_id, fill=color)
        self.current_stroke.append(line_id)
        self.last_x, self.last_y = x, y

    def on_button_release(self, event):
        if self.current_stroke:
            self.history.append(self.current_stroke)
            self.current_stroke = []

    # --- commandes contrôle ---
    def set_color(self, col):
        self.brush_color = col
        self.eraser_on = False
        self.eraser_btn.config(relief=tk.RAISED)

    def choose_color(self):
        # ouvre le sélecteur natif
        col = colorchooser.askcolor(color=self.brush_color, title='Choisir une couleur')
        if col and col[1]:
            self.set_color(col[1])

    def change_size(self, val):
        try:
            self.brush_size = int(val)
        except Exception:
            pass

    def toggle_eraser(self):
        self.eraser_on = not self.eraser_on
        if self.eraser_on:
            self.eraser_btn.config(relief=tk.SUNKEN)
        else:
            self.eraser_btn.config(relief=tk.RAISED)

    def undo(self):
        if not self.history:
            return
        last = self.history.pop()
        for item in last:
            try:
                self.canvas.delete(item)
            except Exception:
                pass

    def clear(self):
        self.canvas.delete('all')
        self.history.clear()

    def save(self):
        # propose un nom de fichier
        f = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG','*.png'), ('PostScript','*.ps')])
        if not f:
            return

        # on essaye de sauvegarder en PNG si possible via PostScript + Pillow
        # postscript temporaire en mémoire
        try:
            ps = self.canvas.postscript(colormode='color')
        except Exception as e:
            messagebox.showerror('Erreur', f'Impossible de générer PostScript: {e}')
            return

        # Si l'utilisateur a demandé un .ps, on l'écrit et on quitte
        if f.lower().endswith('.ps'):
            try:
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(ps)
                messagebox.showinfo('Sauvegardé', f'Sauvegardé en PostScript: {f}')
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'écrire le fichier: {e}")
            return

        # pour PNG: si PIL est disponible, on convertit
        if Image is None:
            # pas de Pillow: on propose d'enregistrer en .ps à la place
            alt = os.path.splitext(f)[0] + '.ps'
            try:
                with open(alt, 'w', encoding='utf-8') as fh:
                    fh.write(ps)
                messagebox.showwarning('Pillow manquant', f'Pillow n\'est pas installé. J\'ai sauvegardé en PostScript: {alt}\n' +
                                   'Installez Pillow + Ghostscript pour convertir en PNG via ce programme.')
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'écrire le fichier: {e}")
            return

        # conversion via Pillow — cela nécessite fréquemment Ghostscript pour lire le PostScript/EPS
        try:
            import tempfile
            from PIL import Image
            # écrire le PS en fichier temporaire pour que PIL/Ghostscript le lise
            with tempfile.NamedTemporaryFile(delete=False, suffix='.ps') as tmp:
                tmp.write(ps.encode('utf-8'))
                tmp_path = tmp.name

            # ouvrir via Pillow (nécessite Ghostscript pour EPS/PS conversion)
            img = Image.open(tmp_path)
            # rasteriser en taille actuelle du canvas
            # certaines installations rendent l'image plus grande; redimensionner à la taille du canvas
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            img = img.convert('RGBA')
            try:
                img = img.resize((w, h), Image.LANCZOS)
            except Exception:
                pass
            img.save(f, 'PNG')
            os.unlink(tmp_path)
            messagebox.showinfo('Sauvegardé', f'Sauvegardé en PNG: {f}')
        except Exception as e:
            messagebox.showerror('Erreur', f'Échec de conversion en PNG: {e}\n' +
                                 'Le PostScript a été conservé en fichier temporaire si possible.')


if __name__ == '__main__':
    root = tk.Tk()
    # taille initiale raisonnable
    root.geometry('900x600')
    app = PaintApp(root)
    root.mainloop()