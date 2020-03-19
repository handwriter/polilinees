import pygame
from board import Board
import time
class Lines(Board):
    def __init__(self, width, height, rect, pos, width_w=500, height_w=500):
        super().__init__(width, height, rect, pos)
        self.width_w = width_w
        self.height_w = height_w
        self.screen = pygame.display.set_mode((self.width_w, self.height_w))
        self.count = 0
        self.itog = False
        self.run()

    def render(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                                               self.rect[0], self.rect[1]), 1)
                elif self.board[i][j] == 1:
                    pygame.draw.ellipse(screen, (0, 0, 255),
                                     (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                      self.rect[0], self.rect[1]), 0)
                elif self.board[i][j] == 2:
                    pygame.draw.ellipse(screen, (255, 0, 0),
                                     (i * self.rect[0] + self.pos[0], j * self.rect[1] + self.pos[1],
                                      self.rect[0], self.rect[1]), 0)


    def has_path(self, x1, y1, x2, y2):
        self.need = (x2, y2)
        self.itog = False
        self.board2 = [i for i in self.board]
        self.path = []
        self.bfs(x1, y1, [])
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 4:
                    self.board[i][j] = 0
        for i in self.path:
            self.board[i[1]][i[0]] = 2
            self.render(self.screen)
            pygame.display.flip()
            time.sleep(0.1)
            self.board[i[1]][i[0]] = 0
        return self.itog

    def bfs(self, x, y, path):
        if self.need == (x, y):
            self.itog = True
            self.board2[y][x] = 4
            self.path.extend(path)
            return
        self.board2[y][x] = 4
        d = [j for j in path]
        d.append([x, y])
        if self.check(x - 1, y):
            if self.board2[y][x - 1] != 1 and self.board2[y][x - 1] != 4:
                self.bfs(x - 1, y, d)
        if self.check(x + 1, y):
            if self.board2[y][x + 1] != 1 and self.board2[y][x + 1] != 4:
                self.bfs(x + 1, y, d)
        if self.check(x - 1, y - 1):
            if self.board2[y - 1][x - 1] != 1 and self.board2[y - 1][x - 1] != 4:
                self.bfs(x - 1, y - 1, d)
        if self.check(x, y - 1):
            if self.board2[y - 1][x] != 1 and self.board2[y - 1][x] != 4:
                self.bfs(x, y - 1, d)
        if self.check(x + 1, y - 1):
            if self.board2[y - 1][x + 1] != 1 and self.board2[y - 1][x + 1] != 4:
                self.bfs(x + 1, y - 1, d)
        if self.check(x + 1, y + 1):
            if self.board2[y + 1][x + 1] != 1 and self.board2[y + 1][x + 1] != 4:
                self.bfs(x + 1, y + 1, d)
        if self.check(x, y + 1):
            if self.board2[y + 1][x] != 1 and self.board2[y + 1][x] != 4:
                self.bfs(x, y + 1, d)
        if self.check(x - 1, y + 1):
            if self.board2[y + 1][x - 1] != 1 and self.board2[y + 1][x - 1] != 4:
                self.bfs(x - 1, y + 1, d)

    def check(self, x, y):
        if x < 0 or y < 0:
            return False
        try:
            a = self.board[y][x]
            return True
        except:
            return False

    def run(self):
        pygame.init()
        running = True
        self.screen.fill((0, 0, 0))
        fps = 60
        clock = pygame.time.Clock()
        activated = 0
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.get_cell(pygame.mouse.get_pos()):
                        a = self.get_cell(pygame.mouse.get_pos())
                        if self.board[a[0]][a[1]] == 0:
                            if not activated:
                                self.board[a[0]][a[1]] = 1
                            else:
                                coords = 0
                                for i in range(len(self.board)):
                                    if 2 in self.board[i]:
                                        coords = (i, self.board[i].index(2))
                                if self.has_path(coords[1], coords[0], a[1], a[0]):
                                    self.board[a[0]][a[1]] = 1
                                    activated = 0
                                else:
                                    self.board[coords[0]][coords[1]] = 2
                        elif self.board[a[0]][a[1]] == 1:
                            if not activated:
                                self.board[a[0]][a[1]] = 2
                                activated = 1
                        elif self.board[a[0]][a[1]] == 2:
                            self.board[a[0]][a[1]] = 1
                            activated = 0

            self.render(self.screen)
            pygame.display.flip()
Lines(10, 10, (50, 50), (0, 0))