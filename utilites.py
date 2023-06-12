import pygame
from game_objects import Ball, Brick
from settings import GOD_MODE, WIDTH, HEIGHT, PADDLE_W, PADDLE_H, PADDLE_SPEED, FPS


def check_collision_wall(ball, paddle):
    # left/right collision:
    if ball.body.centerx < ball.ball_radius or ball.body.centerx > WIDTH - ball.ball_radius:
        ball.dx = -ball.dx
    # top collision:
    if ball.body.centery < ball.ball_radius:
        ball.dy = -ball.dy
    # collision paddle
    if ball.body.colliderect(paddle) and ball.dy > 0:
        ball.dx, ball.dy = ball.check_collision(paddle)

    if not GOD_MODE:
        return ball.body.centery >= HEIGHT
    else:
        if ball.body.centery >= HEIGHT:
            ball.dy = -ball.dy
        return False


def check_collision_block(ball, brick_list):
    for i in brick_list:
        t = [j.body for j in i]
        hit_index = ball.body.collidelist(t)
        if hit_index != -1:
            hit_rect = i[hit_index]
            if not hit_rect.ruined:
                hit_rect.brik_reaction()
                ball.dx, ball.dy = hit_rect.make_collision(ball)
