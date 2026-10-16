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
    #para f(x)=x**2+1, el área exacta entre A y B se calcula así.
    exacta = (B**3 - A**3) / 3 + (B - A)

    ejes = make_axes().shift(DOWN * 0.5)
    curva = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)
    scene.play(Create(ejes), Create(curva), run_time=3)
    scene.wait(5)

    titulo = Text("De la curva a una suma de áreas", font_size=32).to_edge(UP)
    scene.play(Write(titulo), run_time=1.5)
    scene.wait(4)

    #explicamos el primer rectángulo.
    rect_uno = ejes.get_riemann_rectangles(
        curva, x_range=[A, A + dx], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    
    muestra_uno = Dot(ejes.c2p(muestras[0], alturas[0]), color=COLOR_PUNTO)
    
    textos_uno = VGroup(
        Text(f"Subintervalo: [{A:.1f}, {A + dx:.1f}]", font_size=22),
        Text(f"Punto medio: x₁* = {muestras[0]:.2f}", font_size=22),
        Text(f"Altura: f({muestras[0]:.2f}) = {alturas[0]:.4f}", font_size=22),
        Text("Área = altura por ancho", font_size=23, color=YELLOW),
        Text(f"f(x₁*) · Δx = {alturas[0]:.4f} · {dx:.1f} = {aportes[0]:.5f}", font_size=21),
        Text("x_i* es el punto muestra; aquí usamos el punto medio.", font_size=19),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).to_corner(UL).shift(DOWN * 1.0)
    scene.play(Create(rect_uno), FadeIn(muestra_uno), run_time=2)
    scene.play(Write(textos_uno), run_time=3)
    scene.wait(14)

    scene.wait(9)
    scene.play(FadeOut(textos_uno), FadeOut(rect_uno), FadeOut(muestra_uno), run_time=1.5)

    #mostramos los cuatro rectángulos y los datos de cada uno.
    rects = ejes.get_riemann_rectangles(
        curva, x_range=[A, B], dx=dx,
        input_sample_type="center", color=COLOR_RECT, fill_opacity=0.6,
    )
    scene.play(Create(rects), run_time=3)
    
    filas = [
        f"i={i+1}: x_i*={muestras[i]:.2f}; altura={alturas[i]:.4f}; área={aportes[i]:.5f}"
        for i in range(n)
    ]
    
    detalle = VGroup(*[Text(linea, font_size=18) for linea in filas]).arrange(
        DOWN, aligned_edge=LEFT, buff=0.12
    ).to_corner(UL).shift(DOWN * 1.2)
    
    encabezado = Text(f"n = {n}: cada término es el área de un rectángulo", font_size=20).next_to(detalle, UP, buff=0.2)
    
    scene.play(Write(encabezado), Write(detalle), run_time=3)
    scene.wait(14)

    scene.play(FadeOut(encabezado), FadeOut(detalle))

    formula = MathTex(r"S_n=\sum_{i=1}^{n} f(x_i^*)\,\Delta x", font_size=38).to_corner(UL).shift(DOWN * 1.2)
    
    suma_txt = Text(
        "S₄ = " + " + ".join(f"{aporte:.5f}" for aporte in aportes) + f" = {suma:.3f}",
        font_size=21,
    ).next_to(formula, DOWN, aligned_edge=LEFT, buff=0.2)
    
    scene.play(Write(formula), Write(suma_txt), run_time=2.5)
    scene.wait(11)

    #comparamos la suma con el área exacta.
    comparacion = Text(
        f"Área exacta = {exacta:.4f}. S₄ = {suma:.3f} es una aproximación levemente menor.",
        font_size=20,
    ).to_corner(UL).shift(DOWN * 1.2)
    
    scene.play(FadeOut(suma_txt), FadeOut(formula), Write(comparacion), run_time=2)
    scene.wait(10)

    scene.play(FadeOut(*scene.mobjects))

class Escena2(Scene):
    def construct(self):
        animar(self)
