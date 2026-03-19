from manim import *

class FirstScene(Scene):
    def construct(self):
        text = Text("Hello h World")
        self.play(Write(text))
        self.wait(5)