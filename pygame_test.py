import pygame

pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pygame Test')
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
text = font.render('Hello, Pygame!', True, (255, 255, 255))
text_rect = text.get_rect(center=(200, 150))

# Bloc (rectangle) paramètres
block_x = 180
block_y = 250
block_width = 40
block_height = 40
jumping = False
velocity = 0

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Détecter la barre d'espace
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                velocity = -12  # Vitesse de saut initiale

    # Mécanique de saut
    if jumping:
        block_y += velocity
        velocity += 1  # Gravité
        if block_y >= 250:
            block_y = 250
            jumping = False

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, (0, 255, 0), (block_x, block_y, block_width, block_height))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()