import pygame

from src.scene import scene

class TestScene(scene.Scene):
    def __init__(self) -> None:
        super().__init__()

        self.wave_texture = pygame.image.load("asset/texture/wave.png").convert_alpha()
        self.wave_texture = pygame.transform.scale_by(self.wave_texture, 8)

    def draw(self, canvas: pygame.Surface):
        super().draw(canvas)

        canvas.blit(self.wave_texture, (20, 20))
    
    def update(self, dt: float):
        return super().update(dt)