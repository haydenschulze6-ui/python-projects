import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (50, 50))

enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (40, 40))

player_x = 375
player_y = 500

enemies = []

for i in range(7):
    x = random.randint(0, 760)
    y = random.randint(0, 400)
    enemies.append(pygame.Rect(x, y, 40, 40))

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    screen.blit(player, (player_x, player_y))

    for enemy_rect in enemies:
        screen.blit(enemy, (enemy_rect.x, enemy_rect.y))

        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy_rect.x = random.randint(0, 760)
            enemy_rect.y = random.randint(0, 400)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()