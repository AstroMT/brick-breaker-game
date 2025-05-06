import pygame
from paddle import Paddle
from ball import Ball
from bricks import Bricks

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Smash Game")

paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

paddle = Paddle(paddle_group)
ball = Ball(ball_group)
paddle_group.add(paddle)
ball_group.add(ball)



FPS = 30
clock = pygame.time.Clock()


num_rows = 7
num_cols = 7
start_x = 80
start_y = 40
x_space = 100
y_space = 30

for row in range(0, num_rows): 
    for column in range(0, num_cols):
        x =  start_x + column*x_space
        y = start_y + row*y_space
        brick = Bricks(x, y)
        bricks_group.add(brick)


font = pygame.font.Font(None, 36)



gameloop = True
while gameloop:
    screen.fill("black")

    score_text = font.render(f"Score: {ball.score}", True, (255, 255, 255))
    score_textpos = score_text.get_rect(center=(400,15))
    screen.blit(score_text, score_textpos)

    lives_text = font.render(f"Lives: {ball.lives}", True, (240, 255, 255))
    lives_textpos = lives_text.get_rect(center = (740, 575))
    screen.blit(lives_text, lives_textpos)

    pygame.draw.line(screen, "white", (0, 35), (WIDTH, 35), 2)
    pygame.draw.line(screen, "white", (0, HEIGHT-45), (WIDTH, HEIGHT-45), 2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    paddle_group.update(event)
    ball_group.update()
    bricks_group.update()

    paddle_group.draw(screen)
    ball_group.draw(screen)
    bricks_group.draw(screen)

    if pygame.sprite.spritecollide(ball, bricks_group, True):
        ball.score += 10
        ball.speed_y *= -1
    
    if ball.rect.colliderect(paddle.rect):
       ball.speed_y *= -1


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()