import json
import numpy as np
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