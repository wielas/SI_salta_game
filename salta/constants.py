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

#image assets
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))

IMG4 = pygame.transform.scale(pygame.image.load('assets/star1.png'), (45, 25))
IMG3 = pygame.transform.scale(pygame.image.load('assets/star2.png'), (45, 25))
IMG2 = pygame.transform.scale(pygame.image.load('assets/star3.png'), (45, 25))
IMG1 = pygame.transform.scale(pygame.image.load('assets/star4.png'), (45, 25))
IMG0 = pygame.transform.scale(pygame.image.load('assets/star5.png'), (45, 25))

IMG9 = pygame.transform.scale(pygame.image.load('assets/moon1.png'), (45, 25))
IMG8 = pygame.transform.scale(pygame.image.load('assets/moon2.png'), (45, 25))
IMG7 = pygame.transform.scale(pygame.image.load('assets/moon3.png'), (45, 25))
IMG6 = pygame.transform.scale(pygame.image.load('assets/moon4.png'), (45, 25))
IMG5 = pygame.transform.scale(pygame.image.load('assets/moon5.png'), (45, 25))

IMG14 = pygame.transform.scale(pygame.image.load('assets/dot1.png'), (45, 25))
IMG13 = pygame.transform.scale(pygame.image.load('assets/dot2.png'), (45, 25))
IMG12 = pygame.transform.scale(pygame.image.load('assets/dot3.png'), (45, 25))
IMG11 = pygame.transform.scale(pygame.image.load('assets/dot4.png'), (45, 25))
IMG10 = pygame.transform.scale(pygame.image.load('assets/dot5.png'), (45, 25))

