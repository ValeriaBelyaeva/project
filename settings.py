# display settings
WIDTH, HEIGHT = 1200, 800
FPS = 60

# paddle settings
paddle_w = 330
paddle_h = 35
paddle_speed = 15

# ball settings
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
dx, dy = 1, -1

brik_color = {
    'a':(255, 255, 255),  # standard brick
    'b':(150, 150, 150),  # unbroken briсk
    'c':(0, 0, 255),  # 2hp briсk
    'd':(0, 0, 100)  # 3hp briсk
}