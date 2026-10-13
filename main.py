from manim import *

#por fa creen la funcion animar
from escenas.e1_particion import animar as e1_animar
from escenas.e2_suma import animar as e2_animar
from escenas.e3_cierre import animar as e3_animar

class VideoCompleto(Scene):
    def construct(self):
        e1_animar(self)
        e2_animar(self)
        e3_animar(self)