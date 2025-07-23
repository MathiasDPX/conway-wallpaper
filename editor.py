"""
Convert a pixelart to a board
"""

from PIL import Image

img = Image.open("image.png")

width, height = img.size

with open("board.txt", "w+") as f:
    for y in range(height):
        for x in range(width):
            col = img.getpixel((x,y))
            f.write("1" if col == (0,0,0,255) else "0")

        f.write("\n")