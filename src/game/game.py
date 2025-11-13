import pygame
import math

from src import consts
from src.render import scene
from src.render import camera


class WorldScene(scene.Scene):
    def __init__(self) -> None:
        super().__init__()

        self.age = 0.0
        self.s = pygame.image.load('asset/texture/wave.png').convert_alpha()
        self.pos = pygame.Vector2()

    def draw(self, camera: camera.Camera):
        camera.blit(self.s, pygame.Vector2(), scale=8, zindex=1)
        camera.blit(self.s, self.pos, scale=8)
    
    def update(self, dt: float, camera: camera.Camera):
        self.age += dt
        self.pos = pygame.Vector2(math.cos(self.age) * 100, math.sin(self.age) * 100)