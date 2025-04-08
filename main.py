import pygame
from paddle import Paddle
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Smash Game")


paddle = Paddle(WIDTH,HEIGHT)

FPS = 30
clock = pygame.time.Clock()

gameloop = True
while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    paddle.update(event)
    paddle.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()