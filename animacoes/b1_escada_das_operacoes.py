"""Animacao B.1 (Encontro 1): a escada das operacoes.

Desdobra 2^4 na pilha de multiplicacoes e a ultima multiplicacao, 2 . 8,
na soma iterada 8 + 8, exibida como uma grade de 16 quadrados.
"""
from manim import *


class EscadaDasOperacoes(Scene):
    def construct(self):
        pot = MathTex(r"2^{4} = 2 \cdot 2 \cdot 2 \cdot 2")
        self.play(Write(pot)); self.wait()
        prod = MathTex(r"2 \cdot 2 \cdot 2 \cdot 2 = 2 \cdot 8 = 8 + 8")
        self.play(Transform(pot, prod)); self.wait()
        grade = VGroup(*[Square(0.5) for _ in range(16)])
        grade.arrange_in_grid(rows=2, cols=8, buff=0.05).next_to(pot, DOWN, buff=0.8)
        self.play(FadeIn(grade)); self.wait(2)
