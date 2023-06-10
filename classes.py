import pygame
from settings import *
from levels import *
from random import randrange as rnd


class Brick:
    def __init__(self, i, j):
        self.brick_type = level_map[LV][j][i]
        self.i, self.j = i, j
        self.body = pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50)
        self.ruined = False

    def draw(self, sc):
        pygame.draw.rect(sc, brick_color[self.brick_type], self.body)

    def check_collision(self, ball):
        if ball.dx > 0:
            delta_x = ball.body.right - self.body.left
        else:
            delta_x = self.body.right - ball.body.left
        if ball.dy > 0:
            delta_y = ball.body.bottom - self.body.top
        else:
            delta_y = self.body.bottom - ball.body.top

        if abs(delta_x - delta_y) < 10:
            ball.dx, dy = -ball.dx, -ball.dy
        elif delta_x > delta_y:
            ball.dy = -ball.dy
        elif delta_y > delta_x:
            ball.dx = -ball.dx

        return ball.dx, ball.dy

    def brik_reaction(self, block_list=[]):
        if self.ruined:
            pass
        else:
            if self.brik_type == 'a':
                self.ruined = True
            if self.brik_type == 'c':
                self.brik_type = 'a'
            if self.brik_type == 'd':
                self.brik_type = 'c'
            if self.brik_type == 'e':
                self.ruined = True
                try: block_list[self.i-1][self.j].brik_reaction()
                except:pass
                try: block_list[self.i+1][self.j].brik_reaction()
                except:pass
                try: block_list[self.i][self.j-1].brik_reaction()
                except:pass
                try: block_list[self.i][self.j+1].brik_reaction()
                except:pass



class Ball:
    def __init__(self):
        self.ball_radius = 20
        self.ball_speed = 6
        self.ball_rect = int(self.ball_radius * 2 ** 0.5)
        self.dx, self.dy = 1, -1
        self.body = pygame.Rect(rnd(self.ball_rect, WIDTH - self.ball_rect), HEIGHT // 2, self.ball_rect, self.ball_rect)

    def set_position(self):
        pass

    def set_radius(self, radius):
        self.ball_rect = int(radius * 2 ** 0.5)

    def set_speed(self, speed):
        self.ball_speed = speed

    def draw(self, sc):
        pygame.draw.circle(sc, pygame.Color('white'), self.body.center, self.ball_radius)

    def check_collision(self, paddle):
        if self.dx > 0:
            delta_x = self.body.right - paddle.left
        else:
            delta_x = paddle.right - self.body.left
        if self.dy > 0:
            delta_y = self.body.bottom - paddle.top
        else:
            delta_y = paddle.bottom - self.body.top

        if abs(delta_x - delta_y) < 10:
            self.dx, dy = -self.dx, -self.dy
        elif delta_x > delta_y:
            self.dy = -self.dy
        elif delta_y > delta_x:
            self.dx = -self.dx

        return self.dx, self.dy