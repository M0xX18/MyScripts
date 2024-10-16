import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.cm as cm

def taylor_series_sympy(funcion, a, grado):
    x = sp.symbols('x')
    taylor_expansion = sum([funcion.diff(x, i).subs(x, a) * (x - a)**i / sp.factorial(i) 
                             for i in range(grado + 1)])
    return taylor_expansion

def mostrar_grafica(funcion_str, grado, punto_evaluacion):
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(funcion_str)

        f_np = sp.lambdify(x, funcion, "numpy")
        x_vals = np.linspace(-10, 10, 1000)
        y_vals = f_np(x_vals)

        plt.figure(figsize=(14, 10))
        plt.plot(x_vals, y_vals, label='Función original', color='green', linewidth=2)

        colors = cm.viridis(np.linspace(0, 1, grado + 1))
        for i in range(1, grado + 1):
            taylor_expansion = taylor_series_sympy(funcion, punto_evaluacion, i)
            f_taylor_np = sp.lambdify(x, taylor_expansion, "numpy")
            
            y_taylor_vals = f_taylor_np(x_vals)
            
            if np.isscalar(y_taylor_vals):
                y_taylor_vals = np.full_like(x_vals, y_taylor_vals)
            else:
                y_taylor_vals = np.array(y_taylor_vals)

            plt.plot(x_vals, y_taylor_vals, label=f'Serie de Taylor (n={i})', color=colors[i], linestyle='--', linewidth=1.5)

        plt.axvline(x=punto_evaluacion, color='red', linestyle='--', label='Punto de evaluación')
        plt.title(f"Serie de Taylor para {funcion_str}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.gca().set_aspect('equal', adjustable='box')

        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_gui():
    root = tk.Tk()
    root.title("Aplicación de Polinomios de Taylor")
    root.geometry("400x450")
    root.configure(bg='#4d82bc')

    title_label = tk.Label(root, text="Polinomios de Taylor", font=("Abadi", 25, "bold"), bg='#4d82bc', fg='#fcffff')
    title_label.pack(pady=10)

    tk.Label(root, text="Función (ej: sin(x), x**2):", bg='#4d82bc', fg='#fcffff').pack(pady=(10, 0))
    funcion_entry = ttk.Entry(root, width=30)
    funcion_entry.pack(pady=(0, 10), padx=10)

    tk.Label(root, text="Grado del polinomio (n):", bg='#4d82bc', fg='#fcffff').pack(pady=(10, 0))
    grado_entry = ttk.Entry(root, width=30)
    grado_entry.pack(pady=(0, 10), padx=10)

    tk.Label(root, text="Punto de evaluación (a):", bg='#4d82bc', fg='#fcffff').pack(pady=(10, 0))
    punto_entry = ttk.Entry(root, width=30)
    punto_entry.pack(pady=(0, 10), padx=10)

    btn = ttk.Button(root, text="Mostrar Gráfica", command=lambda: mostrar_grafica(
        funcion_entry.get(), 
        int(grado_entry.get()), 
        float(punto_entry.get())
    ))
    btn.pack(pady=20)

    footer_frame = tk.Frame(root, bg='#005187')
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    footer_label = tk.Label(footer_frame, text="Integrantes del Grupo:", font=("Abadi", 12, "bold"), bg='#005187', fg='#fcffff', justify="center", anchor="center")
    footer_label.pack()

    integrantes_text = ("Kenneth Santiago Suárez Mejía  ID 793553\n"
                        "Jhonathan David Gutierrez Meneses ID 787238\n"
                        "Miguel Angel Gamboa Castro  ID 788591\n"
                        "Andrés Eduardo García Bayona ID 798224")
    
    integrantes_label = tk.Label(footer_frame, text=integrantes_text, font=("Abadi", 10), bg='#005187', fg='#fcffff', justify="center", anchor="center")
    integrantes_label.pack()

    style = ttk.Style()
    style.configure("TButton", borderwidth=0, relief="flat", padding=10)
    style.configure("Rounded.TEntry", borderwidth=2, relief="flat", padding=5)

    for entry in [funcion_entry, grado_entry, punto_entry]:
        entry.configure(style="Rounded.TEntry")

    btn.configure(style="TButton")

    root.mainloop()

if __name__ == "__main__":
    crear_gui()

