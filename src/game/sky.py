import pygame

from src import palette
from src.render import camera


class SkyRenderer():
    def __init__(self) -> None:
        self.sky_color = palette.COLOR_SILVER

    def update(self, camera: camera.Camera):
        camera.set_bg(self.sky_color)