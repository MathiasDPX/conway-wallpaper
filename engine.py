import numpy as np
import os
from scipy.signal import convolve2d

class GameOfLife:
    def __init__(self):
        self.board = np.array([])

    def load(self, filename, canvas_size=(10, 10)):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
            self.board = np.array([[int(ch) for ch in line] for line in lines], dtype=np.int8)
        else:
            rows, cols = canvas_size
            self.board = np.zeros((rows, cols), dtype=np.int8)

            self.save(filename)

    def step(self):
        kernel = np.array([[1,1,1],
                           [1,0,1],
                           [1,1,1]], dtype=np.int8)
        neighbor_count = convolve2d(self.board, kernel, mode='same', boundary='fill', fillvalue=0)

        born = (self.board == 0) & (neighbor_count == 3)
        survive = (self.board == 1) & ((neighbor_count == 2) | (neighbor_count == 3))
        self.board[...] = 0
        self.board[born | survive] = 1

    def save(self, filename):
        with open(filename, 'w+') as f:
            for row in self.board:
                f.write(''.join(str(cell) for cell in row) + '\n')
