import pygame
import math

from src import palette
from src.render import camera

class OceanRenderer():
    def __init__(self) -> None:
        self.w = 1600
        self.color = palette.COLOR_BLUE
        self.seafoam_color = palette.COLOR_SKY_BLUE

        self.age = 0.0
        self.tide = 1.0
        self.current_speed = 5.0

    def draw(self, camera: camera.Camera):
        camera.with_zindex(lambda s: self._camera_drawcall(s, camera))

    def update(self, dt: float):
        self.age += dt

        self.tide = abs(math.sin(self.age * 0.2) * 2)

    def _camera_drawcall(self, s: pygame.Surface, camera: camera.Camera):
        surface_tl = camera.world_to_screen_coords_unpacked(0 - self.w/2, 100)

        pygame.draw.rect(s, self.color, pygame.Rect(
                surface_tl,
                pygame.Vector2(camera.scale_zoom(self.w), camera.scale_zoom(300))
            ))
        
        pygame.draw.lines(
            s, self.seafoam_color, False,
            [surface_tl + pygame.Vector2(camera.scale_zoom(x), camera.scale_zoom(self.tide * math.sin(x + self.age * self.current_speed))) 
             for x in range(0, self.w, 10)],
             width=5
        )