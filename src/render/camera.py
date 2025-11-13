import pygame
import typing

from src import consts

type _SurfaceOp = typing.Callable[[pygame.Surface], None]
type _BlitParams = tuple[pygame.Surface, pygame.Vector2]
type _Op = _SurfaceOp | _BlitParams

class Camera():

    def __init__(self) -> None:
        self.focus = pygame.Vector2(0, 0)
        self.zoom = 1.0


        self._frame_blits: dict[int, tuple[list[_SurfaceOp], list[_BlitParams]]] = {}

    def world_to_screen_coords(self, world: pygame.Vector2) -> pygame.Vector2:
        pivot = (pygame.Vector2(consts.CANVAS_DIMS) / 2)
        return (world - self.focus) * self.zoom + pivot
    
    def with_zindex(self, op: _SurfaceOp, zindex: int = 0):
        layer = self._frame_blits.get(zindex, ([], []))
        layer[0].append(op)
        self._frame_blits[zindex] = layer

    def with_zindex_blit(self, params: _BlitParams, zindex: int = 0):
        layer = self._frame_blits.get(zindex, ([], []))
        layer[1].append(params)
        self._frame_blits[zindex] = layer

    def blit(self, surface: pygame.Surface, pos: pygame.Vector2, centered: bool = True, scale: float = 1, rotation: float = 0.0, skip_cull: bool = False, zindex: int = 0):

        # resolve transformations
        surface = pygame.transform.scale_by(surface, self.zoom * scale)
        if rotation != 0.0:
            surface = pygame.transform.rotate(surface, -rotation)

        # resolve position
        screen_pos = self.world_to_screen_coords(pos)
        if centered:
            screen_pos = pygame.Vector2(surface.get_rect(center=screen_pos).topleft)

        # add op
        self.with_zindex_blit((surface, screen_pos), zindex=zindex)


    def render(self, canvas: pygame.Surface):
        for zindex in sorted(self._frame_blits, key=lambda k: k):
            layer = self._frame_blits[zindex]
            canvas.blits(layer[1])
            for op in layer[0]:
                op(canvas)

        self._frame_blits = {}