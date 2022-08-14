from typing import Tuple;
from puzzle import Puzzle;

class Player:

    MOVE_TIME = 100;

    DIR_UP = 0x00;
    DIR_RIGHT = 0x01;
    DIR_DOWN = 0x02;
    DIR_LEFT = 0x03;

    def __init__(self,
        bounds: Tuple[int, int],
        puzzle: Puzzle):

        self.tile_pos = [0, 0];

        self._bounds = bounds;

        self.puzzle = puzzle;

        self.move_anim_dir = None;
        self.move_anim_t = 0;

        self.reset_tile_pos();

    def reset_tile_pos(self) -> None:

        if self.move_anim_dir != None:
            raise Exception("Can't reset tile pos when moving.");

        self.tile_pos = [0, 0];

    @staticmethod
    def get_tile_in_direction(start: Tuple[int, int],
        dir: int) -> Tuple[int, int]:
        if dir == Player.DIR_UP:
            return (start[0], start[1] - 1);
        elif dir == Player.DIR_DOWN:
            return (start[0], start[1] + 1);
        elif dir == Player.DIR_RIGHT:
            return (start[0] - 1, start[1]);
        elif dir == Player.DIR_LEFT:
            return (start[0] + 1, start[1]);
        else:
            raise Exception(f"Unknown direction provided: {dir}");

    def start_move_anim(self,
        dir: int) -> None:

        if self.move_anim_dir != None:
            raise Exception("Starting movement animation when one already active.");

        else:
            self.move_anim_dir = dir;
            self.move_anim_t = 0;

    def update_move_anim(self,
        dt: int) -> None:

        if self.move_anim_dir == None:
            return;

        self.move_anim_t += dt;

        if self.get_move_anim_t_fac() >= 1:

            old_move_dir = int(self.move_anim_dir);

            self.end_move_anim();

            # Check if landed on ice and so should keep moving/slide
            if (self.puzzle.get_tile(self.tile_pos) == Puzzle.TILE_SLIDE) and (self.get_can_move_in_dir(old_move_dir)):
                self.start_move_anim(old_move_dir);

    def end_move_anim(self) -> None:

        self.tile_pos = Player.get_tile_in_direction(self.tile_pos, self.move_anim_dir); # Set new position
        self.move_anim_dir = None; # Stop moving

    def get_move_anim_t_fac(self) -> float:

        t = self.move_anim_t / Player.MOVE_TIME;

        if t > 1:
            t = 1;

        return t;

    def get_can_move_in_dir(self,
        dir: int) -> bool:
        if dir == Player.DIR_UP:
            return self.get_can_move_up();
        elif dir == Player.DIR_DOWN:
            return self.get_can_move_down();
        elif dir == Player.DIR_RIGHT:
            return self.get_can_move_right();
        elif dir == Player.DIR_LEFT:
            return self.get_can_move_left();
        else:
            raise Exception("Unknown direction.");

    def get_can_move_up(self) -> bool:
        return (self.tile_pos[1] > 0) and (self.move_anim_dir == None);

    def get_can_move_down(self) -> bool:
        return (self.tile_pos[1] < self._bounds[1] - 1) and (self.move_anim_dir == None);

    def get_can_move_right(self) -> bool:
        return (self.tile_pos[0] > 0) and (self.move_anim_dir == None);

    def get_can_move_left(self) -> bool:
        return (self.tile_pos[0] < self._bounds[0] - 1) and (self.move_anim_dir == None);

    def try_move_up(self) -> None:
        if self.get_can_move_up():
            self.start_move_anim(Player.DIR_UP);

    def try_move_down(self) -> None:
        if self.get_can_move_down():
            self.start_move_anim(Player.DIR_DOWN);

    def try_move_right(self) -> None:
        if self.get_can_move_right():
            self.start_move_anim(Player.DIR_RIGHT);

    def try_move_left(self) -> None:
        if self.get_can_move_left():
            self.start_move_anim(Player.DIR_LEFT);
