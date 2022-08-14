from typing import Tuple;
from pygame.sprite import Sprite;
from pygame import Color;
import pygame;
from puzzle import Puzzle;

# Width of a single tile in pixels
TILE_WIDTH = 50;

class TileSprite(Sprite):

    COLORS = {
        Puzzle.TILE_WALK: (255, 255, 255),
        Puzzle.TILE_SLIDE: (64, 64, 255)
    };

    BORDER_COLOR = (0, 0, 0);
    BORDER_WIDTH = 1;

    def __init__(self,
        bg_color: Color,
        puzzle: Puzzle,
        tile_pos: Tuple[int, int]):

        super().__init__();

        self.puzzle = puzzle;
        self.tile_pos = tile_pos;

        self.image = pygame.Surface(size = (TILE_WIDTH, TILE_WIDTH));
        self.image.set_colorkey(bg_color);

        self.rect = self.image.get_rect();
        self.rect.x, self.rect.y = TileSprite.tile_pos_to_coords(self.tile_pos);

        self.draw();

    def update(self, *args, **kwargs) -> None:

        super().update(*args, **kwargs);

        self.draw();

    @staticmethod
    def tile_pos_to_coords(tile_pos: Tuple[int, int]) -> Tuple[int, int]:
        return (
            tile_pos[0] * TILE_WIDTH,
            tile_pos[1] * TILE_WIDTH
        );

    @staticmethod
    def coords_to_tile_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
        return (
            pos[0] // TILE_WIDTH,
            pos[1] // TILE_WIDTH
        );

    def set_tile_pos(self,
        tile_pos: Tuple[int, int]) -> None:

        self.tile_pos = tile_pos;

    def get_tile_type(self) -> int:
        return self.puzzle.get_tile(self.tile_pos);

    def draw(self) -> None:

        # Main tile color

        self.image.fill(TileSprite.COLORS[self.get_tile_type()]);

        # Border

        pygame.draw.rect(surface = self.image,
            color = TileSprite.BORDER_COLOR,
            rect = ((0, 0), (self.rect.width, self.rect.height)),
            width = TileSprite.BORDER_WIDTH
        );
