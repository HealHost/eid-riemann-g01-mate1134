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

    etiqueta = Text("Área exacta:", font_size=32)
    exacto = MathTex(r"\frac{14}{3} \approx 4.6667")
    grupo = VGroup(etiqueta, exacto).arrange(RIGHT, buff=0.3)
    grupo.next_to(texto, DOWN)

    scene.play(Write(grupo))
    scene.wait(3)

    scene.play(FadeOut(*scene.mobjects))

    # Momento 5: respuesta a la pregunta central
    titulo = Text("Respuesta a la pregunta central", font_size=36, color=YELLOW)
    lineas = VGroup(
        Text("1. Dividimos el intervalo en n partes iguales.", font_size=28),
        Text("2. En cada parte levantamos un rectángulo", font_size=28),
        Text("    con la altura de la curva.", font_size=28),
        Text("3. Sumamos las áreas de todos los rectángulos.", font_size=28),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    formula = MathTex(r"S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x")
    cierre = Text("Con más rectángulos, la suma se acerca al área exacta.", font_size=28)

    todo = VGroup(titulo, lineas, formula, cierre).arrange(DOWN, buff=0.45)
    todo.scale_to_fit_width(min(todo.width, 12))   # evita que se salga de la pantalla

    scene.play(Write(titulo))
    for parte in (lineas, formula, cierre):
        scene.play(Write(parte))
        scene.wait(1)
    scene.wait(3)

    scene.play(FadeOut(*scene.mobjects))      # limpia al terminar

        # Momento 6: créditos
    titulo_cred = Text("Créditos", font_size=40, color=YELLOW)
    lineas_cred = VGroup(
        Text("Integrantes: Sakin Contreras, Kevin Inalaf, Javier Gutiérrez", font_size=24),
        Text("Fuente 1: COMPLETAR", font_size=24),
        Text("Fuente 2: COMPLETAR", font_size=24),
        Text("Manim Community v0.22.0, documentación oficial", font_size=24),
        Text("Uso de IA: Claude (Anthropic) y otras IAs, para estructura del proyecto", font_size=24),
        Text("y apoyo en código.", font_size=24),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

    creditos = VGroup(titulo_cred, lineas_cred).arrange(DOWN, buff=0.5)
    creditos.scale_to_fit_width(min(creditos.width, 12))

    scene.play(Write(titulo_cred))
    scene.play(FadeIn(lineas_cred))
    scene.wait(4)
    scene.play(FadeOut(*scene.mobjects))


class Escena3(Scene):
    def construct(self):
        animar(self)