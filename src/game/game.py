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

        self.speed = 100

    def draw(self, camera: camera.Camera):
        self.ocean_renderer.draw(camera)

        camera.with_zindex(lambda s: pygame.draw.circle(s, 'red', camera.world_to_screen_coords_unpacked(0, 0), camera.scale_zoom(8)), zindex=100)
    
    def update(self, dt: float, camera: camera.Camera):
        self.ocean_renderer.update(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: camera.focus.y -= self.speed * dt
        if keys[pygame.K_a]: camera.focus.x -= self.speed * dt
        if keys[pygame.K_s]: camera.focus.y += self.speed * dt
        if keys[pygame.K_d]: camera.focus.x += self.speed * dt

        if keys[pygame.K_q]: camera.zoom -= 5 * dt
        if keys[pygame.K_e]: camera.zoom += 5 * dt

        camera.zoom = abs(camera.zoom)

        dims = pygame.Vector2(consts.CANVAS_DIMS) / camera.zoom
        rect = pygame.Rect(dims/2 - camera.focus, dims)
        print(rect)