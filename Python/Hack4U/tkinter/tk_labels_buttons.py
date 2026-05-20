#!/usr/bin/env python3

import tkinter as tk

def presiono_boton():

    print(f"PRESIONARON EL BOTON!")

root = tk.Tk()
root.title("Test")

label_1 = tk.Label(root, text="Este es un label", bg="red")
label_2 = tk.Label(root, text="Este es otro label", bg="blue")
label_3 = tk.Label(root, text="Este es el ultimo label", bg="yellow")

label_1.pack(side=tk.RIGHT, fill=tk.Y)
label_2.pack(fill=tk.BOTH, expand=True)
label_3.pack(fill=tk.BOTH, expand=True)

button_1 = tk.Button(label_2, text="Presioname!", bg="#8A9597", command=presiono_boton)

button_1.pack(side="bottom")

root.mainloop()
