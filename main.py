import pygame
import random

pygame.init()

# GAME CONSTANTS(IN RGB):
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 450
HEIGHT = 300


# GAME VARIABLES:
score = 0
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Infinite Runner")
background = "black"
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True

while running:
    timer.tick(fps)
    screen.fill(background)
    floor = pygame.draw.rect(screen, "white", [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, "green", [player_x, player_y, 20, 20])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_LEFT:
                x_change -= 2
            if event.key == pygame.K_RIGHT:
                x_change += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0

    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430


    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()






