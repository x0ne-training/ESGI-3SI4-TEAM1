import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Mini Paint — Python/Tkinter")
    root.geometry('900x600')
    root.mainloop()

canvas = tk.Canvas(root, bg='white', cursor='cross')
canvas.pack(fill=tk.BOTH, expand=True)

def draw(event):
    x, y = event.x, event.y
    r = 3
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='black', outline='black')

canvas.bind('<B1-Motion>', draw)

colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple']
current_color = 'black'

def set_color(c):
    global current_color
    current_color = c

frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.X)
for c in colors:
    tk.Button(frame, bg=c, width=2, command=lambda col=c: set_color(col)).pack(side=tk.LEFT)

canvas.create_oval(x - r, y - r, x + r, y + r, fill=current_color, outline=current_color)

from tkinter import colorchooser

tk.Button(frame, text='Autre couleur', command=lambda: set_color(colorchooser.askcolor()[1])).pack(side=tk.LEFT, padx=5)

