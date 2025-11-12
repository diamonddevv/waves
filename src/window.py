import pygame

from src import consts
from src.scene import scene

class Window():
    def __init__(self, default_scene: type[scene.Scene]) -> None:
        self.window = pygame.window.Window(
            title=consts.TITLE,
            size=consts.WINDOW_DIMS,
            resizable=True
        )

        self.window_surface = self.window.get_surface()
        self.canvas = pygame.Surface(consts.CANVAS_DIMS)

        self.clock = pygame.Clock()
        self.keep_open = False

        self.scene_manager = scene.SceneManager(default_scene)


    def start(self):
        self.keep_open = True
        dt = 0.0

        while self.keep_open:
            self.event(dt)
            self.update(dt)
            self.draw(self.canvas)
            self.window.flip()
            dt = self.clock.tick(consts.TARGET_FRAMERATE) / 1000

            self.window.title = f"{consts.TITLE} | FPS: {self.clock.get_fps():.0f}"


    def draw(self, cvs: pygame.Surface):
        pass

    def update(self, dt: float):
        pass

    def event(self, dt: float):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.keep_open = False