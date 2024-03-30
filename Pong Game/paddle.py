import pygame
import sys
from ball import Ball

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 1000
screen_height = 800

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue=	(0,0,255)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong  game")
paddle_width = 15
paddle_height = 90
paddle_speed = 8

# initialize the ball
ball = Ball(screen, white, (screen_width // 2, screen_height // 2), 20, 7, 7)

# left Paddle settings
leftPaddle_x = (screen_width - paddle_width) // 30
leftPaddle_y = (screen_height - paddle_height) // 2

# right Paddle settings
rightPaddle_x = screen_width - paddle_width - (screen_width - paddle_width) // 30
rightPaddle_y = (screen_height - paddle_height) // 2

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        leftPaddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        leftPaddle_y += paddle_speed
        
    # right Paddle settings
    if keys[pygame.K_w]:
        rightPaddle_y -= paddle_speed
    if keys[pygame.K_s]:
        rightPaddle_y += paddle_speed
    
    # Ensure the paddle stays on the screen
    if leftPaddle_y < 0:
        leftPaddle_y = 0
    elif leftPaddle_y + paddle_height > screen_height:
        leftPaddle_y = screen_height - paddle_height
        
    if rightPaddle_y < 0: 
        rightPaddle_y = 0
    elif rightPaddle_y + paddle_height > screen_height:  
        rightPaddle_y = screen_height - paddle_height
    
    # Drawing the paddles
    screen.fill(black)
    pygame.draw.rect(screen, white, (leftPaddle_x, leftPaddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (rightPaddle_x, rightPaddle_y, paddle_width, paddle_height))
    
    # Move the ball
    if ball.x <= leftPaddle_x + paddle_width and leftPaddle_y < ball.y < leftPaddle_y + paddle_height:
        ball.bounce_x()
    if ball.x + ball.size >= rightPaddle_x and rightPaddle_y < ball.y < rightPaddle_y + paddle_height:
        ball.bounce_x()

    # Reset ball position if it goes past the left or right side of the screen
    if ball.x < 0 or ball.x > screen_width:
        ball.reset_position()

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, (leftPaddle_x, leftPaddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (rightPaddle_x, rightPaddle_y, paddle_width, paddle_height))
    ball.draw()

    
    
    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(120)
    
    

# Quit pygame
pygame.quit()
sys.exit()
