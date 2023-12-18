from manim import *
from scenes.dynamic import DynamicScene
from pydantic import BaseModel


class CreateCircleParams(BaseModel):
    radius: float = 1.0


class CreateCircle(DynamicScene):
    def construct(self):
        circle = Circle(radius=self.params.radius)
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))


if __name__ == "__main__":
    CreateCircle(params=CreateCircleParams()).render()
