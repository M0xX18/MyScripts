import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
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

        fig, ax = plt.subplots(figsize=(14, 10))
        plt.subplots_adjust(bottom=0.2)  # Ajusta el espacio en la parte inferior para los controles

        ax.plot(x_vals, y_vals, label='Función original', color='green', linewidth=2)

        colors = cm.viridis(np.linspace(0, 1, grado + 1))
        for i in range(1, grado + 1):
            taylor_expansion = taylor_series_sympy(funcion, punto_evaluacion, i)
            f_taylor_np = sp.lambdify(x, taylor_expansion, "numpy")
            y_taylor_vals = f_taylor_np(x_vals)
            ax.plot(x_vals, y_taylor_vals, label=f'Serie de Taylor (n={i})', color=colors[i], linestyle='--', linewidth=1.5)

        ax.axvline(x=punto_evaluacion, color='red', linestyle='--', label='Punto de evaluación')
        ax.set_title(f"Serie de Taylor para {funcion_str}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)

        # Ajuste automático inicial
        ax.autoscale(enable=True, axis='both', tight=True)
        
        # Función para actualizar los límites
        def update_limits(event=None):
            try:
                xmin, xmax = float(xmin_box.text), float(xmax_box.text)
                ymin, ymax = float(ymin_box.text), float(ymax_box.text)
                ax.set_xlim(xmin, xmax)
                ax.set_ylim(ymin, ymax)
                plt.draw()
            except ValueError:
                pass

        # Botones y cajas de texto para ajustar los límites
        axcolor = 'lightgoldenrodyellow'
        ax_xmin = plt.axes([0.1, 0.05, 0.1, 0.03])
        ax_xmax = plt.axes([0.25, 0.05, 0.1, 0.03])
        ax_ymin = plt.axes([0.4, 0.05, 0.1, 0.03])
        ax_ymax = plt.axes([0.55, 0.05, 0.1, 0.03])
        
        xmin_box = TextBox(ax_xmin, 'X min', initial=str(ax.get_xlim()[0]))
        xmax_box = TextBox(ax_xmax, 'X max', initial=str(ax.get_xlim()[1]))
        ymin_box = TextBox(ax_ymin, 'Y min', initial=str(ax.get_ylim()[0]))
        ymax_box = TextBox(ax_ymax, 'Y max', initial=str(ax.get_ylim()[1]))

        xmin_box.on_submit(update_limits)
        xmax_box.on_submit(update_limits)
        ymin_box.on_submit(update_limits)
        ymax_box.on_submit(update_limits)

        # Botón para restablecer la vista
        reset_ax = plt.axes([0.8, 0.05, 0.1, 0.03])
        reset_button = Button(reset_ax, 'Reset View', color=axcolor, hovercolor='0.975')

        def reset_view(event):
            ax.autoscale(enable=True, axis='both', tight=True)
            plt.draw()
            xmin_box.set_val(str(ax.get_xlim()[0]))
            xmax_box.set_val(str(ax.get_xlim()[1]))
            ymin_box.set_val(str(ax.get_ylim()[0]))
            ymax_box.set_val(str(ax.get_ylim()[1]))

        reset_button.on_clicked(reset_view)

        # Habilitar zoom con la rueda del ratón
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()
            xdata = event.xdata
            ydata = event.ydata
            if event.button == 'up':
                scale_factor = 0.9
            elif event.button == 'down':
                scale_factor = 1.1
            else:
                scale_factor = 1

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * relx])
            ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * rely])
            plt.draw()

            xmin_box.set_val(str(ax.get_xlim()[0]))
            xmax_box.set_val(str(ax.get_xlim()[1]))
            ymin_box.set_val(str(ax.get_ylim()[0]))
            ymax_box.set_val(str(ax.get_ylim()[1]))

        fig.canvas.mpl_connect('scroll_event', zoom)

        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_gui():
    root = tk.Tk()
    root.title("Aplicación de Polinomios de Taylor")
    root.geometry("400x450")
    root.configure(bg='#4d82bc')
    title_label = tk.Label(root, text="Polinomios de Taylor", font=("Arial", 18, "bold"), bg='#4d82bc', fg='#fcffff')
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
    # Pie de página
    footer_frame = tk.Frame(root, bg='#005187')
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    footer_label = tk.Label(footer_frame, text="Integrantes del Grupo:", font=("Arial", 12), bg='#005187', fg='#fcffff')
    footer_label.pack()
    integrantes_text = ("Kenneth Santiago Suárez Mejía  ID 793553\n"
                        "Jhonathan David Gutierrez Meneses ID 787238\n"
                        "Miguel Angel Gamboa Castro  ID 788591\n"
                        "Andrés Eduardo García Bayona ID 798224")

    integrantes_label = tk.Label(footer_frame, text=integrantes_text, bg='#005187', fg='#fcffff', justify="left")
    integrantes_label.pack()
    # Estilo de botones y entradas
    style = ttk.Style()
    style.configure("TButton", borderwidth=0, relief="flat", padding=10)
    style.configure("Rounded.TEntry", borderwidth=2, relief="flat", padding=5)
    for entry in [funcion_entry, grado_entry, punto_entry]:
        entry.configure(style="Rounded.TEntry")
    btn.configure(style="TButton")
    root.mainloop()

if __name__ == "__main__":
    crear_gui()
