from manim import *
from config import f, A, B, COLOR_CURVA, make_axes

def animar(escena):
    #rango y tamaño de los ejes
    e1_ejes = make_axes()

    e1_curva = e1_ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)

    e1_region = e1_ejes.get_area(e1_curva, x_range=[A, B], color=COLOR_CURVA, opacity=0.3)

    escena.play(Create(e1_ejes))
    escena.play(Create(e1_curva))
    escena.play(Create(e1_region))
    escena.wait(3)

class Escena1(Scene):
    def construct(self):
        animar(self)

#claro cielo pero no exilies a nadie porfavor