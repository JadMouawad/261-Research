from manim import *

class TestLatex(Scene):
    def construct(self):
        t = MathTex(r"\frac{a}{b} = c")
        self.add(t)
        self.wait() 