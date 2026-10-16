import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from config import f, A, B, N_BASE, COLOR_CURVA, COLOR_RECT, COLOR_PUNTO, make_axes


def animar(scene):
    #datos para calcular las áreas de los rectángulos.
    n = N_BASE
    dx = (B - A) / n
    muestras = [A + (i + 0.5) * dx for i in range(n)]
    alturas = [f(x) for x in muestras]
    aportes = [h * dx for h in alturas]
    suma = sum(aportes)
    exacta = 14 / 3

    ejes = make_axes().shift(DOWN * 0.5)
    curva = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)
    escena_grafica = VGroup(ejes, curva)
    
    scene.play(Create(ejes), Create(curva), run_time=3)
    scene.wait(5)

    titulo = Text("De la curva a una suma de áreas", font_size=32).to_edge(UP)
    scene.play(Write(titulo), run_time=1.5)
    scene.wait(4)

    #explicamos el primer rectangulo.
    rect_uno = ejes.get_riemann_rectangles(
        curva, x_range=[A, A + dx], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    
    muestra_uno = Dot(ejes.c2p(muestras[0], alturas[0]), color=COLOR_PUNTO)
    
    textos_uno = VGroup(
        Text("Subintervalo: [0, 0.5]", font_size=23),
        Text("Punto medio: x₁* = 0.25", font_size=23),
        Text("Altura: f(0.25) = 1.0625", font_size=23),
        Text("Área = altura por ancho", font_size=23, color=YELLOW),
        Text("f(x₁*) · Δx = 1.0625 · 0.5 = 0.53125", font_size=22),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).to_corner(UR).shift(DOWN * 0.6)
    scene.play(Create(rect_uno), FadeIn(muestra_uno), run_time=2)
    scene.play(Write(textos_uno), run_time=3)
    scene.wait(14)

    explicacion = Text(
        "xᵢ* es el punto muestra de cada subintervalo; aquí elegimos su punto medio.",
        font_size=22, line_spacing=1.2,
    ).to_edge(DOWN).shift(UP * 0.15)
    scene.play(Write(explicacion), run_time=2)
    scene.wait(9)
    scene.play(FadeOut(textos_uno), FadeOut(explicacion), FadeOut(rect_uno), FadeOut(muestra_uno), run_time=1.5)

    #los cuatro rectángulos usan los puntos medios de config.py (n=4)
    rects = ejes.get_riemann_rectangles(
        curva, x_range=[A, B], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    scene.play(Create(rects), run_time=3)
    
    #datos de los cuatro rectangulos
    filas = [
        f"i={i+1}: xᵢ*={muestras[i]:.2f}; altura={alturas[i]:.4f}; área={aportes[i]:.5f}"
        for i in range(n)
    ]
    
    detalle = VGroup(*[Text(linea, font_size=18) for linea in filas]).arrange(
        DOWN, aligned_edge=LEFT, buff=0.12
    ).to_corner(UR).shift(DOWN * 0.55)
    
    encabezado = Text("n = 4: cada término es el área de un rectángulo", font_size=21).next_to(detalle, UP, buff=0.2)
    
    scene.play(Write(encabezado), Write(detalle), run_time=3)
    scene.wait(14)

    formula = MathTex(r"S_n=\sum_{i=1}^{n} f(x_i^*)\,\Delta x", font_size=38).to_edge(DOWN)
    
    suma_txt = Text(
        "S₄ = 0.53125 + 0.78125 + 1.28125 + 2.03125 = 4.625",
        font_size=22,
    ).next_to(formula, UP, buff=0.2)
    
    scene.play(Write(formula), Write(suma_txt), run_time=2.5)
    scene.wait(11)

    #comparamos la suma con el área exacta.
    comparacion = Text(
        "Área exacta = 14/3 ≈ 4.6667. S₄ = 4.625 es una aproximación levemente menor.",
        font_size=21,
    ).to_edge(DOWN)
    
    scene.play(FadeOut(suma_txt), FadeOut(formula), Write(comparacion), run_time=2)
    scene.wait(10)

    scene.play(FadeOut(*scene.mobjects))

class Escena2(Scene):
    def construct(self):
        animar(self)
