import pygame
from settings import *
from levels import *
from brick_functions import *
from random import randrange as rnd

pygame.init()

# pygame objekts
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
block_type = [level0[j][i] for i in range(10) for j in range(4)]

def check_collision_brik(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


def check_collision_wall():
    global dx, dy, ball, paddle
    # left/right collision:
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    # top collision:
    if ball.centery < ball_radius:
        dy = -dy
    # collision paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = check_collision_brik(dx, dy, ball, paddle)

def brik_reaction(brik_type, hit_index):
    if brik_type=='a':
        block_list.pop(hit_index)
        block_type.pop(hit_index)
    if brik_type=='c':
        block_type[hit_index]='a'
    if brik_type=='d':
        block_type[hit_index]='c'

def check_collision_block():
    global FPS, dx, dy
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list[hit_index]
        brik_reaction(block_type[hit_index], hit_index)

        dx, dy = check_collision_brik(dx, dy, ball, hit_rect)
        # # effects
        # hit_rect.inflate_ip(ball.width*3, ball.height * 3)
        # pygame.draw.rect(sc, hit_color, hit_rect)
        # FPS += 2


img = pygame.image.load('D:/school/project/img/fon1.jpeg').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))
    # drawing
    [pygame.draw.rect(sc, brik_color[block_type[color]], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(sc, pygame.Color(((0, 255, 170))), paddle)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
    # ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    check_collision_wall()
    check_collision_block()
    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    # updating
    pygame.display.flip()
    clock.tick(FPS)
