import pygame
class Paddle:
    def __init__(self,width,height):
        self.img = pygame.image.load("C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/13764_133ee6bd77806b6ef7d2d1dc080a2faa-removebg-preview.png")
        self.img = pygame.transform.scale(self.img, (200, 100))
        self.rect = self.img.get_rect()
        self.rect.centerx = width//2
        self.rect.bottom = height
        self.velocity = 10

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x = self.rect.x - self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x = self.rect.x + self.velocity
    
    def draw(self,screen):
        screen.blit(self.img, self.rect)        