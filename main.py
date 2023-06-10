import pygame
from classes import Ball, Brick
from settings import *
from levels import *
from brick_functions import *
from random import randrange as rnd

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('D:/school/project/img/fon1.jpeg').convert()

# game objekts
paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, HEIGHT - PADDLE_H - 10, PADDLE_W, PADDLE_H)
# paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
ball = Ball()
block_list = [[Brick(i, j) for i in range(10)] for j in range(4)]


def check_collision_wall():
    global ball, paddle
    # left/right collision:
    if ball.body.centerx < ball.ball_radius or ball.body.centerx > WIDTH - ball.ball_radius:
        ball.dx = -ball.dx
    # top collision:
    if ball.body.centery < ball.ball_radius:
        ball.dy = -ball.dy
    # collision paddle
    if ball.body.colliderect(paddle) and ball.dy > 0:
        dx, dy = ball.check_collision(paddle)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))
    # drawing
    [[j.draw(sc) for j in i]for i in block_list]
    pygame.draw.rect(sc, pygame.Color(((0, 255, 170))), paddle)
    ball.draw(sc)
    # ball movement
    ball.body.x += ball.ball_speed * ball.dx
    ball.body.y += ball.ball_speed * ball.dy
    check_collision_wall()
    [[j.check_collision(ball) for j in i] for i in block_list]
    ball.check_collision(paddle)
    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # updating
    pygame.display.flip()
    clock.tick(FPS)
