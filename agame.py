import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Spaceship properties
spaceship = pygame.Rect(375, 500, 50, 50)  # (x, y, width, height)
spaceship_speed = 5

# Bullet properties
bullet_speed = -7
bullets = []  # List to store active bullets
bullet_width, bullet_height = 5, 10

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fire bullet on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Fire bullet
                bullet = pygame.Rect(
                    spaceship.centerx - bullet_width // 2,
                    spaceship.top,
                    bullet_width,
                    bullet_height,
                )
                bullets.append(bullet)

    # Spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.left > 0:
        spaceship.x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship.right < SCREEN_WIDTH:
        spaceship.x += spaceship_speed

    # Update bullet positions
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.bottom < 0:  # Remove bullet if it goes off-screen
            bullets.remove(bullet)

    # Draw the spaceship
    pygame.draw.rect(screen, WHITE, spaceship)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
