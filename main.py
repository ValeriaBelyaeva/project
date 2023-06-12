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
ball = Ball()
brick_list = [[Brick(i, j) for i in range(10)] for j in range(4)]


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
        ball.dx, ball.dy = ball.check_collision(paddle)

def check_collision_block():
    global ball, brick_list
    for i in brick_list:
        t = [j.body for j in i]
        hit_index = ball.body.collidelist(t)
        if hit_index != -1:
            hit_rect = i[hit_index]
            if not hit_rect.ruined:
                hit_rect.brik_reaction()
                ball.dx, ball.dy = hit_rect.make_collision(ball)
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))
    # drawing
    [[j.draw(sc) for j in i]for i in brick_list]
    pygame.draw.rect(sc, pygame.Color(((0, 255, 170))), paddle)
    ball.draw(sc)

    #move and collision
    ball.move()
    check_collision_wall()
    check_collision_block()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # updating
    pygame.display.flip()
    clock.tick(FPS)
