"""Animacao B.3 (Encontro 3): progressao geometrica e funcao exponencial."""
from manim import *


class ProgressaoGeometrica(Scene):
    def construct(self):
        eixos = Axes(x_range=[0, 6, 1], y_range=[0, 32, 4])
        self.play(Create(eixos))
        a0, q = 1, 2
        pts = [eixos.coords_to_point(n, a0 * q**n) for n in range(6)]
        for n, p in enumerate(pts):
            self.play(FadeIn(Dot(p, color=RED)), run_time=0.5)
        curva = eixos.plot(lambda x: a0 * q**x, x_range=[0, 5], color=GREEN)
        self.play(Create(curva)); self.wait(2)
