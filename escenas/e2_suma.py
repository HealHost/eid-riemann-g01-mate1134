import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from config import f, A, B, N_BASE, COLOR_CURVA, COLOR_RECT, COLOR_PUNTO, make_axes


def animar(scene):
    # datos para calcular las áreas de los rectángulos
    n = N_BASE
    dx = (B - A) / n
    muestras = [A + (i + 0.5) * dx for i in range(n)]
    alturas = [f(x) for x in muestras]
    aportes = [h * dx for h in alturas]
    suma = sum(aportes)
    exacta = 14 / 3

    # Si el grupo es muy ancho o alto, se achica para que no se salga.
    def en_panel(grupo, y=0.3):
        if grupo.width > 3.7:
            grupo.scale_to_fit_width(3.7)
        if grupo.height > 4.2:
            grupo.scale_to_fit_height(4.2)
        grupo.to_edge(RIGHT, buff=0.25).set_y(y)
        return grupo

    ejes = make_axes().shift(DOWN * 0.5)
    curva = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)

    scene.play(Create(ejes), Create(curva), run_time=3)
    scene.wait(5)

    titulo = Text("De la curva a una suma de áreas", font_size=32).to_edge(UP)
    scene.play(Write(titulo), run_time=1.5)
    scene.wait(4)

    # explicamos el primer rectángulo
    rect_uno = ejes.get_riemann_rectangles(
        curva, x_range=[A, A + dx], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    muestra_uno = Dot(ejes.c2p(muestras[0], alturas[0]), color=COLOR_PUNTO)

    textos_uno = en_panel(VGroup(
        Text(f"Subintervalo: [{A}, {A + dx}]", font_size=22),
        Text(f"Punto medio: x₁* = {muestras[0]}", font_size=22),
        Text(f"Altura: f({muestras[0]}) = {alturas[0]:.4f}", font_size=22),
        Text("Área = altura por ancho", font_size=22, color=YELLOW),
        Text(f"f(x₁*) · Δx = {alturas[0]:.4f} · {dx}", font_size=22),
        Text(f"= {aportes[0]:.5f}", font_size=22),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.16))

    scene.play(Create(rect_uno), FadeIn(muestra_uno), run_time=2)
    scene.play(Write(textos_uno), run_time=3)
    scene.wait(12)

    # la explicación va bajo el título, no sobre los números del eje
    explicacion = Text(
        "xᵢ* es el punto muestra de cada subintervalo; aquí elegimos su punto medio.",
        font_size=22,
    )
    explicacion.scale_to_fit_width(min(explicacion.width, 13))
    explicacion.next_to(titulo, DOWN, buff=0.2)

    scene.play(Write(explicacion), run_time=2)
    scene.wait(9)
    scene.play(FadeOut(textos_uno), FadeOut(explicacion), FadeOut(rect_uno), FadeOut(muestra_uno), run_time=1.5)

    # los cuatro rectángulos usan los puntos medios de config.py (n = 4)
    rects = ejes.get_riemann_rectangles(
        curva, x_range=[A, B], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    scene.play(Create(rects), run_time=3)

    # datos de los cuatro rectángulos
    encabezado = VGroup(
        Text(f"n = {n}: cada término es", font_size=20),
        Text("el área de un rectángulo", font_size=20),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.06)

    filas = VGroup(*[
        VGroup(
            Text(f"i={i+1}:  xᵢ* = {muestras[i]:.2f}", font_size=20),
            Text(f"altura = {alturas[i]:.4f}   área = {aportes[i]:.5f}", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        for i in range(n)
    ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

    detalle = en_panel(VGroup(encabezado, filas).arrange(DOWN, aligned_edge=LEFT, buff=0.25))

    scene.play(Write(detalle), run_time=3)
    scene.wait(25)
    scene.play(FadeOut(detalle), run_time=1)

    # fórmula y suma, en el mismo panel
    formula = MathTex(r"S_n=\sum_{i=1}^{n} f(x_i^*)\,\Delta x", font_size=38)
    suma_txt = VGroup(
        Text(f"S₄ = {aportes[0]:.5f} + {aportes[1]:.5f}", font_size=22),
        Text(f"+ {aportes[2]:.5f} + {aportes[3]:.5f}", font_size=22),
        Text(f"= {suma:.3f}", font_size=22),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
    resumen = en_panel(VGroup(formula, suma_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.4))

    scene.play(Write(resumen), run_time=2.5)
    scene.wait(11)

    # comparamos la suma con el área exacta
    comparacion = en_panel(VGroup(
        Text(f"Área exacta = 14/3 ≈ {exacta:.4f}", font_size=21),
        Text(f"S₄ = {suma:.3f} es una", font_size=21),
        Text("aproximación levemente menor.", font_size=21),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14))

    scene.play(FadeOut(resumen), Write(comparacion), run_time=2)
    scene.wait(10)

    scene.play(FadeOut(*scene.mobjects))

class Escena2(Scene):
    def construct(self):
        animar(self)