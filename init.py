import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog, messagebox

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

# Inicializar ventana tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Obtener valores de y1 y y2
y1 = obtener_input_usuario("Ingrese el valor de y para el punto (0, y, 135) entre -100 y 100:", -100, 100)
y2 = obtener_input_usuario("Ingrese el valor de y para el punto (80, y, 0) entre -100 y 100:", -100, 100)

P1 = np.array([0, y1, 135])  # Punto adicional 1
P2 = np.array([80, y2, 0])  # Punto adicional 2
P3 = np.array([80, 0, 135])  # Punto adicional 3
P4 = np.array([80, 0, 90])  # Punto adicional 4

# Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar puntos adicionales
ax.scatter(P1[0], P1[1], P1[2], color='magenta', s=100)  # Punto (0, y, z)
ax.scatter(P2[0], P2[1], P2[2], color='cyan', s=100)  # Punto (x, y, 0)
ax.scatter(P3[0], P3[1], P3[2], color='yellow', s=100)  # Punto (x, 0, z)
ax.scatter(P4[0], P4[1], P4[2], color='orange', s=100)  # Punto (x, 0, z)

# Agregar coordenadas al lado de cada punto
ax.text(P1[0], P1[1], P1[2], f'({P1[0]}, {P1[1]}, {P1[2]})', color='black')
ax.text(P2[0], P2[1], P2[2], f'({P2[0]}, {P2[1]}, {P2[2]})', color='black')
ax.text(P3[0], P3[1], P3[2], f'({P3[0]}, {P3[1]}, {P3[2]})', color='black')
ax.text(P4[0], P4[1], P4[2], f'({P4[0]}, {P4[1]}, {P4[2]})', color='black')

# Dibujar línea desde P3 a P1
ax.plot([P3[0], P1[0]], [P3[1], P1[1]], [P3[2], P1[2]], color='green')

# Dibujar línea desde P4 a P2
ax.plot([P4[0], P2[0]], [P4[1], P2[1]], [P4[2], P2[2]], color='red')

# Agregar vector de 10 unidades hacia abajo en la dirección negativa del eje Y desde P3
ax.quiver(P3[0], P3[1], P3[2], 0, -10, 0, color='blue', length=100, normalize=True)
ax.text(P3[0], P3[1] - 100, P3[2], '450N', color='blue', ha='center')  # Etiqueta del vector

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

# Función para rotar el gráfico según la tecla presionada
def on_key(event):
    if event.key == 'x':
        ax.view_init(elev=0, azim=0)
    elif event.key == 'y':
        ax.view_init(elev=0, azim=90)
    elif event.key == 'z':
        ax.view_init(elev=90, azim=0)
    elif event.key == '3':
        ax.view_init(elev=30, azim=45)
    plt.draw()

# Registrar el evento del teclado
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
