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
    player = pygame.draw.rect(screen, "white", [player_x, player_y, 20, 19])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()






