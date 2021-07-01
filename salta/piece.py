import pygame.draw
from .constants import RED, WHITE, GREY, SQUARE_SIZE, CROWN, IMG0, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, \
    IMG9, IMG10, IMG11, IMG12, IMG13, IMG14

# TODO: create pieces of specific type
class Piece:
    PADDING = 13
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.id = col//2 + row*5
        self.starting_row = row
        self.starting_col = col
        self.on_place = False

        # FOR PIECE ID
        # pygame.font.init()
        # self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        # self.textsurface = self.myfont.render(str(self.id), False, (0, 0, 0))

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        # drawing image
        if self.id in range(0, 15) and not self.on_place:
            win.blit(eval(f"IMG{self.id}"), (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        elif self.id in range(35, 50) and not self.on_place:
            win.blit(eval(f"IMG{49 - self.id}"), (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        elif self.on_place:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

        # PRINT PIECE ID
        # win.blit(self.textsurface, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

