from typing import Tuple;
from player import Player;
from player_sprite import PlayerSprite;
from puzzle import Puzzle;
from pygame import Color;
import pygame;
from tile_sprite import TileSprite;

PUZZLE_DIMS = (10, 10);
BG_COLOR = (0, 0, 0);
FRAMERATE = 20;

class MainController:

    def __init__(self,
        window_bg_color: Color,
        puzzle_dims: Tuple[int, int],
        framerate: int):

        pygame.init();

        self.window_dims = TileSprite.tile_pos_to_coords(
            (puzzle_dims[0], puzzle_dims[1])
        );

        self.puzzle_dims = puzzle_dims;
        self.window_bg_color = window_bg_color;
        self.framerate = framerate;

        self.running = False;

    def run(self) -> None:

        self.running = True;

        self.puzzle = Puzzle(self.puzzle_dims);
        self.player = Player(self.puzzle_dims, self.puzzle);

        self.window = pygame.display.set_mode(self.window_dims);
        self.clock = pygame.time.Clock();

        self.tile_sprites = pygame.sprite.Group();
        self.over_tile_sprites = pygame.sprite.Group();

        # Create player sprite
        self.player_sprite = PlayerSprite(BG_COLOR, self.player);
        self.over_tile_sprites.add(self.player_sprite);

        # Create tile spites
        for x in range(self.puzzle.dims[0]):
            for y in range(self.puzzle.dims[1]):
                self.tile_sprites.add(TileSprite(
                    bg_color = BG_COLOR,
                    puzzle = self.puzzle,
                    tile_pos = (x, y)
                ));

        # Run main loop
        self.main_loop();

        # Clean up
        pygame.quit();

    def main_loop(self) -> None:
        
        while self.running:

            # Clock tick
            self.clock.tick(self.framerate);

            # Get dt
            dt = self.clock.get_time();

            # Handle events
            for evt in pygame.event.get():
                self.handle_event(evt);

            # Update sprites
            self.tile_sprites.update(dt = dt);
            self.over_tile_sprites.update(dt = dt);

            # Clear window
            self.window.fill(self.window_bg_color);

            # Draw sprites
            self.tile_sprites.draw(self.window); # Tiles
            self.over_tile_sprites.draw(self.window); # Player

            # Flip display
            pygame.display.flip();

    def handle_event(self,
        evt: pygame.event.Event) -> None:

        if evt.type == pygame.QUIT:
            self.running = False;
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click(pygame.mouse.get_pos());
        elif evt.type == pygame.KEYDOWN:
            self.handle_keydown(evt.key);

    def handle_click(self,
        pos: Tuple[int, int]) -> None:

        # Change state of selected tile

        tile_pos = TileSprite.coords_to_tile_pos(pos);

        old_tile = self.puzzle.get_tile(tile_pos);
        new_tile = Puzzle.cycle_tile(old_tile);

        self.puzzle.set_tile(tile_pos, new_tile);

    def handle_keydown(self,
        key: int) -> None:

        if self.player.move_anim_dir == None:

            if key == pygame.K_w:
                self.player.try_move_up();

            elif key == pygame.K_s:
                self.player.try_move_down();

            elif key == pygame.K_d:
                self.player.try_move_left();

            elif key == pygame.K_a:
                self.player.try_move_right();

            elif key == pygame.K_r:
                self.player.reset_tile_pos();

if __name__ == "__main__":

    controller = MainController(
        window_bg_color = BG_COLOR,
        puzzle_dims = PUZZLE_DIMS,
        framerate = FRAMERATE
    );

    controller.run();