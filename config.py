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