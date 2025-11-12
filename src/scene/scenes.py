import pygame

from src.scene import scene

class TestScene(scene.Scene):
    def __init__(self) -> None:
        super().__init__()

    def draw(self, canvas: pygame.Surface):
        return super().draw(canvas)
    
    def update(self, dt: float):
        return super().update(dt)