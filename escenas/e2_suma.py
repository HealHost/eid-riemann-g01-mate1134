import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from config import f, A, B, COLOR_CURVA, make_axes


def animar(scene):
    #ejes y curva de f(x) = x**2 + 1 en el intervalo [A, B]
    ejes = make_axes()
    curva = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)
    scene.play(Create(ejes), Create(curva))
    scene.wait(2)

    scene.play(FadeOut(*scene.mobjects))

class Escena2(Scene):
    def construct(self):
        animar(self)