from __future__ import annotations
import pygame


class SceneManager():
    def __init__(self, default: type[Scene]) -> None:
        self.current = default()


    def draw_current(self, canvas: pygame.Surface):
        self.current.draw(canvas)

    def update_current(self, dt: float):
        self.current.update(dt)

    def change(self, scene: type[Scene]):
        self.current = scene()


class Scene():
    def __init__(self) -> None:
        pass

    def draw(self, canvas: pygame.Surface):
        pass

    def update(self, dt: float):
        pass