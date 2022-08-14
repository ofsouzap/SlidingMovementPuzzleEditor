# Sliding Movement Puzzle Editor

Basic program for editing and testing sliding tile-based movement puzzles.  
(This was made for designing [Pokemon Obsidian](https://github.com/ofsouzap/PokemonObsidian "Github Repo"))

## Dependencies

- pygame

## Controls

- **Mouse click** on a tile to change what type of tile it is
- **WASD** for moving the player (the circle) around the area. The player will slide if they move onto a sliding tile
- **R** to reset the player's position to the top-left

## Tiles

- **Walk tile** is the default, basic tile that can be walked across
- If the player moves onto a **slide tile**, they will be forced to continue moving in the direction they were previously moving until stopped
- **Block tiles** prevent the player from moving into them (and so will stop the player if they slide into one)