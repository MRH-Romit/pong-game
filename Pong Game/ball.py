from random import randint
from paddle import Paddle
import pygame


ball_speed = 10
ball_size=20
ball_color="white"
screen_height=Paddle.screen_height
screen_width=Paddle.screen_width

class Ball:
    def __init__(self, screen, color, initial_position, size, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x, self.y = initial_position
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y

def move(self):
    self.x += self.speed_x
    self.y += self.speed_y
    
    if self.y <= 0 or self.y + self.size >= screen_height:
            self.speed_y *= -1

def draw(self):
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

def bounce_x(self):
    self.speed_x *= -1

def reset_position(self):
    self.x, self.y = screen_width // 2 - self.size // 2, screen_height // 2 - self.size // 2
    self.speed_x *= -1  