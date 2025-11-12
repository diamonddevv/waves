# (C) DiamondDev, 2025

import pygame

from src import window
from src.scene import scenes

if __name__ == "__main__":
    pygame.init()

    wnd = window.Window(scenes.TestScene)
    wnd.start()