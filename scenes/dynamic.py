from pydantic import BaseModel
from manim import Scene


class DynamicScene(Scene):
    def __init__(self, params: BaseModel, **kwargs):
        super().__init__(**kwargs)
        self.params = params
