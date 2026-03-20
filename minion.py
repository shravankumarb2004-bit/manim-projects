from manim import *

class MyScene(Scene):
    def construct(self):
        text = Text("Hello everyone!")
        self.play(Write(text))