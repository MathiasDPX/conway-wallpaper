import json
from PIL import Image
from engine import GameOfLife

# Setup
try:
    config = json.load(open("config.json", "r", encoding="utf-8"))
except Exception as e:
    print("Unable to load config")
    print(e)
    exit()

scale = config.get("scale", 1)
output_size = config.get("output_size", [256, 144])
canvas_size = tuple(int(x / scale) for x in output_size)
width, height = canvas_size

# Process game
game = GameOfLife()
game.load("board.txt", canvas_size=canvas_size)
game.step()
game.save("board.txt")

# Save image
palette = config.get("palette", [[30,30,30], [0,122,204]])
dead_cell_color = tuple(x for x in palette[0])
live_cell_color = tuple(x for x in palette[1])

img = Image.new("RGB", size=canvas_size, color=dead_cell_color)

for x in range(width-1):
    for y in range(height-1):
        if int(game.board[x][y]):
            img.putpixel((x,y), live_cell_color)

img = img.resize(tuple(x for x in output_size), resample=Image.NEAREST)

img.save("wallpaper.png")