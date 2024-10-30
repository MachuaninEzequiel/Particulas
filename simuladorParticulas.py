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
    size = random.randint(5, 15)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particles.append({"pos": [x, y], "vel": [vx, vy], "size": size, "color": color})

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

    if keys[pygame.K_g]:  
        gravity += 0.01
    if keys[pygame.K_h]:  
        gravity -= 0.01

    if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS]:  
        box_speed += 1
    if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:  
        box_speed = max(1, box_speed - 1)

    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 0, 0), box_rect, 2)

    for particle in particles:
        particle["vel"][1] += gravity
        particle["pos"][0] += particle["vel"][0]
        particle["pos"][1] += particle["vel"][1]

        if particle["pos"][0] < box_rect.left + particle["size"] or particle["pos"][0] > box_rect.right - particle["size"]:
            particle["vel"][0] *= -1
            if particle["pos"][0] < box_rect.left + particle["size"]:
                particle["pos"][0] = box_rect.left + particle["size"]
            else:
                particle["pos"][0] = box_rect.right - particle["size"]

        if particle["pos"][1] < box_rect.top + particle["size"] or particle["pos"][1] > box_rect.bottom - particle["size"]:
            particle["vel"][1] *= -1
            if particle["pos"][1] < box_rect.top + particle["size"]:
                particle["pos"][1] = box_rect.top + particle["size"]
            else:
                particle["pos"][1] = box_rect.bottom - particle["size"]

        pygame.draw.circle(screen, particle["color"], (int(particle["pos"][0]), int(particle["pos"][1])), particle["size"])

    # Mostrar estadísticas en pantalla
    font = pygame.font.SysFont(None, 36)
    stats_text = f"Gravedad: {gravity:.2f} | Velocidad de Caja: {box_speed}"
    text_surface = font.render(stats_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()