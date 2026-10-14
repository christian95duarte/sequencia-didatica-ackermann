"""Animacao B.4 (Encontro 4): linear contra exponencial.

A camera comeca proxima da origem e recua duas vezes, ate que a reta
se achate visualmente sobre o eixo.
"""
from manim import *


class LinearVsExponencial(MovingCameraScene):
    def construct(self):
        eixos = Axes(x_range=[0, 10, 1], y_range=[0, 520, 40])
        self.camera.frame.save_state()
        self.camera.frame.scale(0.3).move_to(eixos.c2p(2.5, 40))
        self.play(Create(eixos))
        linear = eixos.plot(lambda x: 5*x + 5, x_range=[0, 9], color=BLUE)
        expo   = eixos.plot(lambda x: 2**x, x_range=[0, 9], color=GREEN)
        self.play(Create(linear), Create(expo))
        self.play(self.camera.frame.animate.scale(1.8), run_time=2)
        self.play(Restore(self.camera.frame), run_time=2)
        self.wait(2)
