from __future__ import annotations
import pygame

from src.render import camera

class UiContainer():
    def __init__(self) -> None:
        self.elements: dict[int, UiElement] = {}
        self._next_index = 0

    def draw(self, camera: camera.Camera):
        for idx in self.elements:
            self.elements[idx].draw(camera)

    def update(self, dt: float, camera: camera.Camera):
        for idx in self.elements:
            self.elements[idx].update(dt, camera)

    def add(self, element: UiElement) -> int:
        self.elements[self._next_index] = element
        self._next_index += 1
        return self._next_index - 1
    
    def remove(self, idx: int):
        del self.elements[idx]


class UiElement():
    def __init__(self) -> None:
        pass

    def draw(self, camera: camera.Camera):
        pass

    def update(self, dt: float, camera: camera.Camera):
        pass