import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Smash Game")

paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

paddle = Paddle(paddle_group)
ball = Ball(ball_group)
paddle_group.add(paddle)
ball_group.add(ball)


FPS = 30
clock = pygame.time.Clock()

gameloop = True
while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    paddle_group.update(event)
    ball_group.update()

    paddle_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()