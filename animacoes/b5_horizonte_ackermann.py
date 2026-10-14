"""Animacao B.5 (Encontro 5): o horizonte, a Funcao de Ackermann."""
from manim import *


class HorizonteAckermann(Scene):
    def construct(self):
        defin = VGroup(MathTex(r"A(0, n) = n + 1"),
            MathTex(r"A(m+1, 0) = A(m, 1)"),
            MathTex(r"A(m+1, n+1) = A(m, A(m+1, n))")
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(defin)); self.wait()
        self.play(defin.animate.scale(0.6).to_edge(UP))
        passos = ["A(1, 1)", "A(0, A(1, 0))", "A(0, A(0, 1))", "A(0, 2)", "3"]
        expr = MathTex(passos[0]); self.play(Write(expr))
        for p in passos[1:]:
            self.play(Transform(expr, MathTex(p))); self.wait(0.5)
        fim = MathTex(r"A(4, 2) = 2^{65536} - 3").next_to(expr, DOWN, buff=1)
        nota = Tex(r"19\,729 algarismos").next_to(fim, DOWN)
        self.play(Write(fim), FadeIn(nota)); self.wait(2)
