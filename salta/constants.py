import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BRONZE = (176, 141, 87)
DBRONZE = (128, 74, 0)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))
STAR1 = pygame.transform.scale(pygame.image.load('assets/star1.png'), (45, 25))
STAR2 = pygame.transform.scale(pygame.image.load('assets/star2.png'), (45, 25))
STAR3 = pygame.transform.scale(pygame.image.load('assets/star3.png'), (45, 25))
STAR4 = pygame.transform.scale(pygame.image.load('assets/star4.png'), (45, 25))
STAR5 = pygame.transform.scale(pygame.image.load('assets/star5.png'), (45, 25))

