import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Partículas")

NUM_PARTICLES = 50
particles = []

box_size = 500
box_rect = pygame.Rect(WIDTH // 2 - box_size // 2, HEIGHT // 2 - box_size // 2, box_size, box_size)
gravity = 0.1
box_speed = 5

for _ in range(NUM_PARTICLES):
    x = random.randint(box_rect.left + 10, box_rect.right - 10)
    y = random.randint(box_rect.top + 10, box_rect.bottom - 10)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    particles.append({"pos": [x, y], "vel": [vx, vy]})

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_rect.x -= box_speed
    if keys[pygame.K_RIGHT]:
        box_rect.x += box_speed
    if keys[pygame.K_UP]:
        box_rect.y -= box_speed
    if keys[pygame.K_DOWN]:
        box_rect.y += box_speed

    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 0, 0), box_rect, 2)

    for particle in particles:
        particle["vel"][1] += gravity
        particle["pos"][0] += particle["vel"][0]
        particle["pos"][1] += particle["vel"][1]

        if particle["pos"][0] < box_rect.left + 5 or particle["pos"][0] > box_rect.right - 5:
            particle["vel"][0] *= -1
            if particle["pos"][0] < box_rect.left + 5:
                particle["pos"][0] = box_rect.left + 5
            else:
                particle["pos"][0] = box_rect.right - 5

        if particle["pos"][1] < box_rect.top + 5 or particle["pos"][1] > box_rect.bottom - 5:
            particle["vel"][1] *= -1
            if particle["pos"][1] < box_rect.top + 5:
                particle["pos"][1] = box_rect.top + 5
            else:
                particle["pos"][1] = box_rect.bottom - 5

        if (particle["pos"][0] < box_rect.left or 
            particle["pos"][0] > box_rect.right or 
            particle["pos"][1] < box_rect.top or 
            particle["pos"][1] > box_rect.bottom):
            if particle["pos"][0] < box_rect.left or particle["pos"][0] > box_rect.right:
                particle["vel"][0] *= -1
            if particle["pos"][1] < box_rect.top or particle["pos"][1] > box_rect.bottom:
                particle["vel"][1] *= -1

        pygame.draw.circle(screen, (255, 255, 255), (int(particle["pos"][0]), int(particle["pos"][1])), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()