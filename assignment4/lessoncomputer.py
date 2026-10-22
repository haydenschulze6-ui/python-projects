import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mini Sprite Adventure")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

x = 275
y = 175
width = 50
height = 50
speed = 5
color = BLUE

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0, min(x, 600 - width))
    y = max(0, min(y, 400 - height))

    if x == 0 or x == 600 - width or y == 0 or y == 400 - height:
        color = RED
    else:
        color = BLUE

    screen.fill(WHITE)

    pygame.draw.rect(screen, color, (x, y, width, height))

    pygame.draw.rect(screen, BLACK, (x, y, width, height), 3)

    pygame.display.update()
    clock.tick(30)

pygame.quit()