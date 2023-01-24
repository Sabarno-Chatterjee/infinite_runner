import pygame
import random

pygame.init()

# GAME CONSTANTS(IN RGB):
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 450
HEIGHT = 300

# GAME VARIABLES:
score = 0
with open("high_score.txt") as game_data:
    high_score = game_data.read()
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1
obstacles = [300, 450, 600]
obstacle_speed = 2

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Infinite Runner")
background = BLACK
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True
active = True

while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        instruction_text1 = font.render(f"Space Bar To Start", True, WHITE, BLACK)
        screen.blit(instruction_text1, (150, 50))
        instruction_text2 = font.render(f"Space Bar Jumps. Left/Right Moves", True, WHITE, BLACK)
        screen.blit(instruction_text2, (80, 90))
    score_text = font.render(f"Score: {score}", True, WHITE, BLACK)
    screen.blit(score_text, (100, 250))
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE, BLACK)
    screen.blit(high_score_text, (250,250))
    floor = pygame.draw.rect(screen, "white", [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, GREEN, [player_x, player_y, 20, 20])
    obstacle0 = pygame.draw.rect(screen, ORANGE, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, RED, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, YELLOW, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                active = True
                player_x = 50
                score = 0
                obstacles = [300, 450, 600]
        if event.type == pygame.KEYDOWN and active:
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
    for obstacle in range(len(obstacles)):
        if active:
            obstacles[obstacle] -= obstacle_speed
            if obstacles[obstacle] < -20:
                obstacles[obstacle] = random.randint(470, 570)
                score += 1
                # Check for high_Score and collision with obstacle:
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False
                if score > int(high_score):
                    high_score = score
                    with open("high_score.txt", mode="w") as game_data:
                        game_data.write(str(high_score))

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
