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

brush_size = tk.IntVar(value=5)
size_slider = tk.Scale(frame, from_=1, to=30, orient='horizontal', variable=brush_size, label='Taille')
size_slider.pack(side=tk.LEFT, padx=5)

r = brush_size.get()

eraser_on = False

def toggle_eraser():
    global eraser_on
    eraser_on = not eraser_on

tk.Button(frame, text='Gomme', command=toggle_eraser).pack(side=tk.LEFT, padx=5)

color = 'white' if eraser_on else current_color
canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)

history = []
current_stroke = []

def start_draw(event):
    global current_stroke
    current_stroke = []
    draw(event)

def draw(event):
    x, y = event.x, event.y
    r = brush_size.get()
    color = 'white' if eraser_on else current_color
    item = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
    current_stroke.append(item)

def stop_draw(event):
    history.append(current_stroke)

canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', stop_draw)

tk.Button(frame, text='Annuler', command=lambda: [canvas.delete(i) for i in history.pop() if history]).pack(side=tk.LEFT, padx=5)

