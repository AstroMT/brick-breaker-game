import pygame

WIDTH = 800
HEIGHT = 600

class Paddle(pygame.sprite.Sprite):
    def __init__(self, ball_group):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/13764_133ee6bd77806b6ef7d2d1dc080a2faa-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT
        self.velocity = 10
        self.ball_group = ball_group

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x = self.rect.x - self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x = self.rect.x + self.velocity
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)        