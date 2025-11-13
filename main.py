# (C) DiamondDev, 2025

import pygame

from src import window
from src.game import game

if __name__ == "__main__":
    pygame.init()

    wnd = window.Window(game.WorldScene)
    wnd.start()