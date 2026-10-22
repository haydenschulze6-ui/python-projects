import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smart Traffic Signal Simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.velocity = 5

    def update(self):
        self.rect.x += self.velocity

car = Car()
all_sprites = pygame.sprite.Group()
all_sprites.add(car)

signal_colour = GREEN

CHANGE_SIGNAL = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_SIGNAL, 3000)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_SIGNAL:
            signal_colour = RED if signal_colour == GREEN else GREEN
            car.image.fill(BLUE if signal_colour == GREEN else RED)

    all_sprites.update()

    if car.rect.right >= 800:
        car.rect.x = 0
        signal_colour = RED if signal_colour == GREEN else GREEN
        car.image.fill(BLUE if signal_colour == GREEN else RED)

    screen.fill(WHITE)

    pygame.draw.rect(screen, GRAY, (0, 280, 800, 80))

    pygame.draw.rect(screen, BLACK, (700, 100, 60, 140))
    pygame.draw.circle(screen, RED, (730, 130), 20)
    pygame.draw.circle(
        screen, signal_colour, (730, 190), 20
    )

    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()