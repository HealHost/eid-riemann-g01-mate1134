import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from config import f, A, B, N_VALORES, COLOR_CURVA, COLOR_RECT, make_axes


def animar(scene):
    ejes = make_axes().shift(DOWN * 0.5)
    curva = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)
    scene.play(Create(ejes), Create(curva))

    # Momento 1 a 3: n=4, 8, 16
    rects = None
    texto = None
    for n in N_VALORES:
        dx = (B - A) / n
        suma = sum(f(A + (i + 0.5) * dx) * dx for i in range(n))
        rects_nuevo = ejes.get_riemann_rectangles(
            curva, x_range=[A, B], dx=dx,
            input_sample_type="center",
            color=COLOR_RECT, fill_opacity=0.6,
        )
        texto_nuevo = MathTex(rf"n = {n},\quad \Delta x = {dx},\quad S_n = {suma}").to_edge(UP)

        if rects is None:
            scene.play(Create(rects_nuevo), Write(texto_nuevo))
        else:
            scene.play(
                ReplacementTransform(rects, rects_nuevo),
                ReplacementTransform(texto, texto_nuevo),
            )
        rects = rects_nuevo
        texto = texto_nuevo
        scene.wait(2)

    scene.play(FadeOut(*scene.mobjects))


class Escena3(Scene):
    def construct(self):
        animar(self)