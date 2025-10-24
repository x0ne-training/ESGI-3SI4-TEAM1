import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Mini Paint — Python/Tkinter")
    root.geometry('900x600')
    root.mainloop()

canvas = tk.Canvas(root, bg='white', cursor='cross')
canvas.pack(fill=tk.BOTH, expand=True)
