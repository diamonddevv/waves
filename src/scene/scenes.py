import pygame

from src import consts
from src.scene import scene

class WorldScene(scene.Scene):
    def __init__(self) -> None:
        super().__init__()

        self.tx_wave = pygame.image.load("asset/texture/wave.png").convert_alpha()
        self.tx_wave = pygame.transform.scale_by(self.tx_wave, 2)

        self.tx_bg_sky = pygame.image.load("asset/texture/sky.png").convert_alpha()
        self.tx_bg_sky = pygame.transform.scale_by(self.tx_bg_sky, 2)
        self.tx_bg_sea = pygame.image.load("asset/texture/sea_depths.png").convert_alpha()
        self.tx_bg_sea = pygame.transform.scale_by(self.tx_bg_sea, 2)

    def draw(self, canvas: pygame.Surface):
        super().draw(canvas)

        self.draw_sea(canvas)

        
    
    def update(self, dt: float):
        pass


    def draw_sea(self, canvas: pygame.Surface):
        iters = consts.CANVAS_DIMS[0] // self.tx_wave.width

        depths_elev = consts.CANVAS_DIMS[1] - self.tx_bg_sea.height

        for i in range(iters):
            canvas.blit(self.tx_bg_sea, (self.tx_wave.width * i, depths_elev))
            canvas.blit(self.tx_wave, (self.tx_wave.width * i, depths_elev - self.tx_wave.height))
            #canvas.blit(self.tx_bg_sky, (self.tx_wave.width * i, 0))