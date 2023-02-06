import pygame
from pygame.locals import *
import random
# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)

# Carrega a imagem da bola
ball_image = pygame.image.load("bola.jpg")
ball_rect = ball_image.get_rect()
ball_rect.center = (screen_width / 2, screen_height / 2)

# Define a velocidade da bola
ball_speed = [2, 2]

# Carrega a imagem da raquete
paddle_image = pygame.image.load("paddle.png")
paddle_rect = paddle_image.get_rect()
paddle_rect.left = 10
paddle_rect.centery = screen_height / 2

# Define a velocidade da raquete
paddle_speed = 5

# Inicializa a pontuação
score = 0

# Define o jogo como em andamento
running = True

# Loop principal
while running:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verifica se a tecla para cima foi pressionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_rect.top -= paddle_speed
    # Verifica se a tecla para baixo foi pressionada
    if keys[pygame.K_DOWN]:
        paddle_rect.top += paddle_speed

    # Verifica se a raquete saiu da tela
    if paddle_rect.top < 0:
        paddle_rect.top = 0
    if paddle_rect.bottom > screen_height:
        paddle_rect.bottom = screen_height

    # Atualiza a posição da bola
    ball_rect.left += ball_speed[0]
    ball_rect.top += ball_speed[1]

    # Verifica se a bola colidiu com a raquete
    if ball_rect.colliderect(paddle_rect):
        ball_speed[0] = -ball_speed[0]
        score += 1

    # Verifica se a bola saiu da tela
    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_speed[1] = -ball_speed[1]

    # Preenche a tela com a cor preta
    screen.fill(black)

    # Desenha a bola na tela
    screen.blit(ball_image, ball)
