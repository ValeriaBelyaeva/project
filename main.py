import pygame
from game_objects import Ball, Brick
from settings import GOD_MODE, WIDTH, HEIGHT, PADDLE_W, PADDLE_H, PADDLE_SPEED, FPS
from utilites import check_collision_wall, check_collision_block
from random import randrange as rnd

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('D:/school/project/img/fon1.jpeg').convert()

# values
need_restart = True
lv = 0

# game objects
paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, HEIGHT - PADDLE_H - 10, PADDLE_W, PADDLE_H)
ball = Ball()
brick_list = [[Brick(i, j, lv) for i in range(10)] for j in range(4)]


def restart():
    global paddle, ball, brick_list, lv
    paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, HEIGHT - PADDLE_H - 10, PADDLE_W, PADDLE_H)
    ball = Ball()
    brick_list = [[Brick(i, j, lv) for i in range(10)] for j in range(4)]


def go_to_next_level():
    global lv
    for i in brick_list:
        for j in i:
            if not j.ruined:
                return False
    lv += 1
    restart()


while True:
    if need_restart:
        need_restart = False
        restart()
    go_to_next_level()
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))
    # drawing
    [[j.draw(sc) for j in i] for i in brick_list]
    pygame.draw.rect(sc, pygame.Color(((0, 255, 170))), paddle)
    ball.draw(sc)

    # move and collision
    ball.move()
    need_restart = check_collision_wall(ball, paddle)
    check_collision_block(ball, brick_list)
    key = pygame.key.get_pressed()
    if key[pygame.K_g]:
        GOD_MODE = True
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # updating
    pygame.display.flip()
    clock.tick(FPS)
