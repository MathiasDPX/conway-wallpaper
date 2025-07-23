import json
import seagull as sg
from seagull import lifeforms as lf

try:
    config:dict = json.load(open("config.json","r", encoding="utf-8"))
except Exception as e:
    print("Unable to load config")
    print(e)
    exit()

scale = config.get("scale", 1)
output_size = config.get("output_size", [256,144])
canva_size = tuple(int(x/scale) for x in output_size)

print(canva_size)

board = sg.Board(size=tuple(canva_size))