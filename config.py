from manim import *

def f(x):
    return x**2 + 1

#intervalo [a, b]
A = 0
B = 2

N_VALORES = [4, 8, 16]
N_BASE = 4

#colores: curva, rectangulo, punto muestra 
COLOR_CURVA = BLUE
COLOR_RECT = GREEN
COLOR_PUNTO = YELLOW

def make_axes():
    ejes = Axes(
        x_range=[0, 2.5, 0.5],
        y_range=[0, 6, 1],
        x_length=9,
        y_length=5,
        axis_config={"include_numbers": True},
        tips=False,
    )
    return ejes

if __name__ == "__main__":
    exacto = 14 / 3 #referencia
    for n in N_VALORES:
        dx = (B - A) / n
        puntos = [A + (i - 0.5) * dx for i in range(1, n + 1)]
        suma = sum(f(x) * dx for x in puntos)
        print(f"n={n:2d}  dx={dx}  S_n={suma}  error={exacto - suma:.4f}")

#javier por favor no me exilies