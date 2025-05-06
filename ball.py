import pygame

WIDTH = 800
HEIGHT = 600

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_group):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Naras/OneDrive/Desktop/New folder/Python Games/brick_game/ball.png")
        self.image = pygame.transform.scale(self.image,(100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = HEIGHT//2
        self.speed_x = 10
        self.speed_y = 10
        self.score=0
        self.lives=5
    
    def update(self):
        self.rect.y = self.rect.y - self.speed_y
        self.rect.x = self.rect.x - self.speed_x
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1


