"""Animacao B.2 (Encontro 2): progressao aritmetica e funcao afim."""
from manim import *


class ProgressaoAritmetica(Scene):
    def construct(self):
        eixos = Axes(x_range=[0, 6, 1], y_range=[0, 16, 2])
        self.play(Create(eixos))
        a0, r = 2, 2
        pts = [eixos.coords_to_point(n, a0 + r*n) for n in range(6)]
        for n, p in enumerate(pts):
            ponto = Dot(p, color=YELLOW)
            rotulo = MathTex(f"a_{{{n}}}={a0 + r*n}").scale(0.5).next_to(ponto, UP)
            self.play(FadeIn(ponto), FadeIn(rotulo), run_time=0.5)
        reta = eixos.plot(lambda x: a0 + r*x, x_range=[0, 5], color=BLUE)
        self.play(Create(reta)); self.wait(2)
