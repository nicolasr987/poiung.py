import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load ball image
try:
    ball_image = pygame.image.load("bola.png.jpg")
    ball_rect = ball_image.get_rect()
    ball_rect.center = (screen_width / 2, screen_height / 2)
except pygame.error as e:
    print("Could not load ball image:", e)
    ball_image = None

# Set ball speed
ball_speed = [2, 2]

# Load paddle image
try:
    paddle_image = pygame.image.load("Fundo-Azul .png")
    paddle_rect = paddle_image.get_rect()
    paddle_rect.left = 10
    paddle_rect.centery = screen_height / 2
except pygame.error as e:
    print("Could not load paddle image:", e)
    paddle_image = None

# Set paddle speed
paddle_speed = 5

# Initialize score
score = 0

# Set game as running
running = True

# Main loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if up arrow key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_rect.top -= paddle_speed
    # Check if down arrow key is pressed
    if keys[pygame.K_DOWN]:
        paddle_rect.top += paddle_speed

    # Check if paddle went off screen
    if paddle_rect.top < 0:
        paddle_rect.top = 0
    if paddle_rect.bottom > screen_height:
        paddle_rect.bottom = screen_height

    # Update ball position
    ball_rect.left += ball_speed[0]
    ball_rect.top += ball_speed[1]

    # Check if ball collided with paddle
    if ball_rect.colliderect(paddle_rect):
        ball_speed[0] = -ball_speed[0]
        score += 1

    # Check if ball went off screen
    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_speed[1] = -ball_speed[1]

    # Fill screen with black color
    screen.fill(black)

    # Draw ball on screen
    screen.blit(ball_image, ball_rect)

    # Draw paddle on screen
    screen.blit(paddle_image, paddle_rect)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
