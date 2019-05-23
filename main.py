import pygame,random
black = (0,0,0)
white = (255, 255, 255)
screen_width = 700
screen_height = 200
ball_size = 25

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

    def make_ball(self):
        ball = Ball()

        ball.x = random.randrange(ball_size, screen_width - ball_size)
        ball.y = random.randrange(ball_size, screen_height - ball_size)
        ball.color = (
            random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255)
        )
        ball.change_x = random.randrange(-20, -30)
        ball.change_y = random.randrange(-20, -30)

        return ball
