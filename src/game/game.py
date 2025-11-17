import pygame
import math

from src import consts
from src.render import scene
from src.render import camera

from src.game import ocean


class WorldScene(scene.Scene):
    def __init__(self) -> None:
        super().__init__()
        self.ocean_renderer = ocean.OceanRenderer()

    def draw(self, camera: camera.Camera):
        self.ocean_renderer.draw(camera)

        camera.with_zindex(lambda s: pygame.draw.circle(s, 'red', camera.world_to_screen_coords_unpacked(0, 0), 8), zindex=100)
    
    def update(self, dt: float, camera: camera.Camera):
        self.ocean_renderer.update(dt)