import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from config import f, A, B, N_BASE, COLOR_CURVA, make_axes

def animar(scene):
    #rango y tamaño de los ejes
    e1_ejes = make_axes().shift(DOWN * 0.5)
    e1_curva = e1_ejes.plot(f, x_range=[A, B], color=COLOR_CURVA)
    e1_region = e1_ejes.get_area(
        e1_curva, x_range=[A, B], color=COLOR_CURVA, opacity=0.3
    )


    scene.play(Create(e1_ejes))
    scene.play(Create(e1_curva))
    scene.play(Create(e1_region))
    scene.wait(6)

    #pregunta central e intervalo [a, b]
    e1_pregunta = Text("¿Cómo se transforma una región bajo una curva en una suma de áreas de rectángulos?", font_size= 20,).to_edge(UP)
    scene.play (Write(e1_pregunta))
    scene.wait(8)

    #rectas verticales punteadas a y b 
    e1_linea_a = e1_ejes.get_vertical_line(e1_ejes.i2gp(A, e1_curva))
    e1_linea_b = e1_ejes.get_vertical_line(e1_ejes.i2gp(B, e1_curva))

    #texto con el intervalo 
    e1_intervalo = MathTex(r"[a,\,b] = [0,\,2]").next_to(e1_pregunta, DOWN)

    scene.play(Create(e1_linea_a), Create(e1_linea_b))
    scene.play(Write(e1_intervalo))
    scene.wait(20)

    #partición n en subintervalos
    e1_n = N_BASE
    e1_dx = (B - A) / e1_n
    e1_xs = [A + i * e1_dx for i in range(e1_n + 1)]  

    #puntos de la partición
    scene.play(FadeOut(e1_pregunta), e1_intervalo.animate.to_edge(UP))

    e1_puntos = VGroup(*[Dot(e1_ejes.c2p(x, 0), color=WHITE) for x in e1_xs])

    #etiquetas de los puntos de la partición

    e1_etiquetas = VGroup(*[MathTex(f"x_{{{i}}}", font_size=34).next_to(e1_puntos[i], DOWN, buff=0.5) for i in range(e1_n + 1)])

    #rectas verticales de la partición
    e1_cortes = VGroup(*[e1_ejes.get_vertical_line(e1_ejes.i2gp(e1_xs[i], e1_curva)) for i in range(1, e1_n)])
   
    scene.play(LaggedStart(*[FadeIn(p) for p in e1_puntos], lag_ratio=0.3))
    scene.play(LaggedStart(*[Write(t) for t in e1_etiquetas], lag_ratio=0.3))
    scene.wait(15)
    scene.play(LaggedStart(*[Create(c) for c in e1_cortes], lag_ratio=0.3))
    scene.wait(15)

    #fórmulas de la partición
    e1_f_dx = MathTex(r"\Delta x = \frac{b-a}{n} = \frac{2-0}{4} = 0{,}5", font_size=34)
    e1_f_xi = MathTex(r"x_i = a + i\,\Delta x", font_size=34)
    e1_formulas = VGroup(e1_f_dx, e1_f_xi).arrange(RIGHT, buff=1)
    e1_formulas.next_to(e1_intervalo, DOWN)

    scene.play(Write(e1_f_dx))
    scene.wait(15)
    scene.play(Write(e1_f_xi))
    scene.wait(15)

    scene.play(FadeOut(*scene.mobjects))
    scene.wait(2)



class Escena1(Scene):
    def construct(self):
        animar(self)

