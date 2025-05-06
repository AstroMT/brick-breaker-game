import pygame
from random import randint


class Bricks(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        bricks = ["C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/brick_blue.png", 
                  "C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/brick_red.png", 
                  "C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/brick_yellow.png"]
        self.image = pygame.image.load(bricks[randint(0,2)])
        self.image = pygame.transform.scale(self.image, (80, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)

