from typing import Tuple;
from pygame.sprite import Sprite;
from pygame import Color;
import pygame;
from tile_sprite import TileSprite, TILE_WIDTH;
from player import Player;

class PlayerSprite(Sprite):

    MAIN_COLOR = (255, 0, 0);

    def __init__(self,
        bg_color: Color,
        player: Player):

        super().__init__();

        self.player = player;

        self.image = pygame.Surface(size = (TILE_WIDTH, TILE_WIDTH));
        self.image.set_colorkey(bg_color);

        self.rect = self.image.get_rect();

        self.draw();

    def update(self, *args, **kwargs) -> None:

        super().update(*args, **kwargs);

        self.player.update_move_anim(kwargs["dt"]);

        if self.player.move_anim_dir == None:
            pos = TileSprite.tile_pos_to_coords(self.player.tile_pos);
        else:
            pos = self.get_curr_move_anim_pos();

        self.rect.x, self.rect.y = pos;

        self.draw();

    def get_curr_move_anim_pos(self) -> Tuple[int, int]:

        if self.player.move_anim_dir == None:
            raise Exception("Player not doing move animation.");

        start = TileSprite.tile_pos_to_coords(self.player.tile_pos);
        end = TileSprite.tile_pos_to_coords(Player.get_tile_in_direction(self.player.tile_pos, self.player.move_anim_dir));

        curr = (
            int(start[0] + ((end[0] - start[0]) * self.player.get_move_anim_t_fac())),
            int(start[1] + ((end[1] - start[1]) * self.player.get_move_anim_t_fac()))
        );

        return curr;

    def draw(self) -> None:

        pygame.draw.circle(
            surface = self.image,
            color = PlayerSprite.MAIN_COLOR,
            center = (self.rect.width // 2, self.rect.height // 2),
            radius = self.rect.width // 3
        );

    def set_tile_pos(self,
        tile_pos: Tuple[int, int]):

        self.set_rect_pos(TileSprite.tile_pos_to_coords(tile_pos));
