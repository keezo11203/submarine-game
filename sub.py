import pygame

pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("submarine")

# Define colors
LAND_COLOR = (60, 179, 113) # Dark green
WATER_COLOR = (30, 144, 255) # Dodger blue
SKY_COLOR = (135, 206, 235) # Sky blue


land_rect = pygame.Rect(0, screen_height // 2, screen_width, screen_height // 4)
water_rect = pygame.Rect(0, 0, screen_width, screen_height // 2)
sky_rect = pygame.Rect (0, 0, screen_width, screen_height // 4)
pygame.draw.rect(screen, LAND_COLOR, land_rect)
pygame.draw.rect(screen, WATER_COLOR, water_rect)

# Update the screen
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()