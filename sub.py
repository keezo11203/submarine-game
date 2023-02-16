import pygame

pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("submarine")

# Define colors
LAND_COLOR = (60, 179, 113) # Dark green
WATER_COLOR = (0, 0, 128) # Deep blue
SKY_COLOR = (135, 206, 235) # Sky blue

# Draw the land, water, and sky rectangles
water_rect = pygame.Rect(0, screen_height // 3, screen_width, screen_height // 3)
land_rect = pygame.Rect(0, screen_height // 3 * 2, screen_width, screen_height // 3)
sky_rect = pygame.Rect(0, 0, screen_width, screen_height // 3)

pygame.draw.rect(screen, LAND_COLOR, land_rect)
pygame.draw.rect(screen, WATER_COLOR, water_rect)
pygame.draw.rect(screen, SKY_COLOR, sky_rect)

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