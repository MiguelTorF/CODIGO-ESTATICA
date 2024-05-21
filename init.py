import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para obtener inputs de usuario dentro de un rango usando tkinter
def obtener_input_usuario(mensaje, minimo, maximo):
    while True:
        valor = simpledialog.askfloat("Input", mensaje)
        if valor is None:
            continue
        if minimo <= valor <= maximo:
            return valor
        else:
            messagebox.showerror("Error", f"Por favor, ingrese un valor entre {minimo} y {maximo}.")

# Función para mostrar las coordenadas de los puntos, las fuerzas y el vector unitario en la ventana de ecuaciones
def mostrar_ecuaciones():
    for widget in ecuacion_frame.winfo_children():
        widget.destroy()  # Eliminar widgets anteriores para no superponer ecuaciones

    # Mostrar las coordenadas de los puntos
    coordenadas = [
        (A, 'A'),
        (F, 'F'),
        (E, 'E'),
        (C, 'C'),
        (D, 'D')
    ]

    coord_text = "\n".join([f"{label} = ({p[0]}, {p[1]}, {p[2]})" for p, label in coordenadas])
    coord_label = tk.Label(ecuacion_frame, text=f"Coordenadas de los puntos:\n{coord_text}", justify='left')
    coord_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Mostrar las fuerzas
    fuerzas_text = "Fuerza aplicada en C: 450N hacia abajo en el eje Y"
    fuerzas_label = tk.Label(ecuacion_frame, text=f"Fuerzas:\n{fuerzas_text}", justify='left')
    fuerzas_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Mostrar el cálculo del vector CF, su magnitud y el vector unitario Lambda
    vector_cf_text = f"Vector CF: F - C = ({F[0]} - {C[0]}, {F[1]} - {C[1]}, {F[2]} - {C[2]}) = ({CF[0]}, {CF[1]}, {CF[2]})"
    magnitud_cf_text = f"Magnitud de CF: √(({CF[0]})² + ({CF[1]})² + ({CF[2]})²) = {CF_magnitud:.2f}"
    lambda_cf_text = f"Vector unitario Lambda (CF): CF / |CF| = ({CF[0]} / {CF_magnitud:.2f}, {CF[1]} / {CF_magnitud:.2f}, {CF[2]} / {CF_magnitud:.2f}) = ({lambda_cf[0]:.2f}, {lambda_cf[1]:.2f}, {lambda_cf[2]:.2f})"
    vector_de_text= f"Vector DE: E-D = ({E[0]} - {D[0]}, {E[1]} - {D[1]}, {E[2]} - {D[2]}) = ({ED[0]}, {ED[1]}, {ED[2]})"

    vector_cf_label = tk.Label(ecuacion_frame, text=vector_cf_text, justify='left')
    vector_cf_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    magnitud_cf_label = tk.Label(ecuacion_frame, text=magnitud_cf_text, justify='left')
    magnitud_cf_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    lambda_label = tk.Label(ecuacion_frame, text=lambda_cf_text, justify='left')
    lambda_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Inicializar ventana tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal al inicio

# Obtener valores de y1 y y2
y1 = obtener_input_usuario("Ingrese el valor de y para el punto (0, y, 135) entre -150 y 150 para el punto F:", -150, 150)
y2 = obtener_input_usuario("Ingrese el valor de y para el punto (80, y, 0) entre -150 y 150 para el punto E:", -150, 150)

# Crear frames para organizar la ventana
grafico_frame = tk.Frame(root)
grafico_frame.grid(row=0, column=0, padx=10, pady=10)

ecuacion_frame = tk.Frame(root)
ecuacion_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# Definir las coordenadas de los puntos
A = np.array([0, 0, 0])  # Punto A
F = np.array([0, y1, 135])  # Punto F
E = np.array([80, y2, 0])  # Punto E
C = np.array([80, 0, 135])  # Punto C
D = np.array([80, 0, 90])  # Punto D

# Calcular el vector CF y su magnitud
CF = F - C
CF_magnitud = np.linalg.norm(CF)
# Calcular el vector unitario Lambda de C a F
lambda_cf = CF / CF_magnitud

DE = E - D
DE_magnitud = np.linalg.norm(DE)
# Calcular el vector unitario Lambda de C a F
lambda_de = DE / DE_magnitud

# Mostrar las coordenadas y fuerzas automáticamente
mostrar_ecuaciones()

# Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar puntos adicionales
ax.scatter(A[0], A[1], A[2], color='blue', s=100)  # Punto A (0, 0, 0)
ax.scatter(F[0], F[1], F[2], color='magenta', s=100)  # Punto (0, y, z)
ax.scatter(E[0], E[1], E[2], color='cyan', s=100)  # Punto (x, y, 0)
ax.scatter(C[0], C[1], C[2], color='yellow', s=100)  # Punto (x, 0, z)
ax.scatter(D[0], D[1], D[2], color='orange', s=100)  # Punto (x, 0, z)

# Agregar coordenadas al lado de cada punto
ax.text(A[0], A[1], A[2], f'({A[0]}, {A[1]}, {A[2]})', color='black')
ax.text(F[0], F[1], F[2], f'({F[0]}, {F[1]}, {F[2]})', color='black')
ax.text(E[0], E[1], E[2], f'({E[0]}, {E[1]}, {E[2]})', color='black')
ax.text(C[0], C[1], C[2], f'({C[0]}, {C[1]}, {C[2]})', color='black')
ax.text(D[0], D[1], D[2], f'({D[0]}, {D[1]}, {D[2]})', color='black')

# Dibujar línea desde C a F
ax.plot([C[0], F[0]], [C[1], F[1]], [C[2], F[2]], color='green')

# Dibujar línea desde D a E
ax.plot([D[0], E[0]], [D[1], E[1]], [D[2], E[2]], color='red')

# Agregar vector de 100 unidades hacia abajo en la dirección negativa del eje Y desde C
ax.quiver(C[0], C[1], C[2], 0, -10, 0, color='blue', length=100, normalize=True)
ax.text(C[0], C[1] - 100, C[2], '450N', color='blue', ha='center')  # Etiqueta del vector

# Dibujar planos XY, XZ, YZ positivos y negativos
x = np.linspace(-100, 100, 2)
y = np.linspace(-100, 100, 2)
z = np.linspace(-100, 150, 2)
x, y = np.meshgrid(x, y)
z1, z2 = np.meshgrid(z, z)

ax.plot_surface(x, y, np.zeros_like(x), alpha=0.2, color='grey')  # Plano XY en Z=0
ax.plot_surface(x, np.zeros_like(x), z2, alpha=0.2, color='grey')  # Plano XZ en Y=0
ax.plot_surface(np.zeros_like(y), y, z2, alpha=0.2, color='grey')  # Plano YZ en X=0

# Configuración del gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Esquema del ensamble con cables y carga aplicada')

# Cambiar la dirección de los ejes
ax.invert_xaxis()
ax.invert_yaxis()

# Mostrar el gráfico en la ventana de tkinter
canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.deiconify()  # Mostrar la ventana principal después de configurar los widgets
root.mainloop()
