from typing import Tuple;

class Puzzle:

    TILE_WALK = 0x00;
    TILE_SLIDE = 0x01;
    TILE_BLOCK = 0x02;

    def __init__(self,
        dims: Tuple[int, int]):

        self.dims = dims;

        # Tiles are initialised as walking tiles
        self._array = [[Puzzle.TILE_WALK for _ in range(self.dims[0])] for _ in range(self.dims[1])];

    def set_tile(self,
        tile_pos: Tuple[int, int],
        v: int) -> None:
        self._array[tile_pos[1]][tile_pos[0]] = v;

    def get_tile(self,
        tile_pos: Tuple[int, int]) -> int:

        return self._array[tile_pos[1]][tile_pos[0]];

    @staticmethod
    def cycle_tile(tile: int):

        if tile == Puzzle.TILE_WALK:
            return Puzzle.TILE_SLIDE;

        elif tile == Puzzle.TILE_SLIDE:
            return Puzzle.TILE_BLOCK;

        elif tile == Puzzle.TILE_BLOCK:
            return Puzzle.TILE_WALK;

        else:
            raise Exception("Unknown tile provided.");
