
import pygame
import time
class Board:
    def __init__(self, width, height, rect, pos):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.rect = rect
        self.pos = pos

    def set_view(self, rect):
        self.rect = rect

    def get_cell(self, pos):
        x = (pos[0] - self.pos[0]) // self.rect[0]
        y = (pos[1] - self.pos[1]) // self.rect[1]
        if x > self.height - 1 or y > self.width - 1 or x < 0 or y < 0:
            return False
        return x, y

    def checker(self, numb):
        if numb == 1:
            return 0
        return 1

    def re_checker(self, x, y):
        try:
            var = self.board[x][y]
            return var
        except:
            return 0

    def on_click(self, pos):
        self.board[pos[0]][pos[1]] = self.checker(self.board[pos[0]][pos[1]])

    def get_click(self, pos):
        if self.get_cell(pos):
            self.on_click(self.get_cell((pos[0], pos[1])))