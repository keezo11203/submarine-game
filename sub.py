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

# Dimensions of the background
water_rect = pygame.Rect(0, screen_height // 3, screen_width, screen_height // 3)
land_rect = pygame.Rect(0, screen_height // 3 * 2, screen_width, screen_height // 3)
sky_rect = pygame.Rect(0, 0, screen_width, screen_height // 3)

# Load the submarine image
submarine_image = pygame.image.load("submarine.png")
submarine = pygame.Surface(submarine_image.get_size())
submarine_rect = submarine_image.get_rect()
submarine_rect.centerx = screen_width // 2
submarine_rect.bottom = screen_height - 10

# Set the initial position of the submarine
submarine_x = screen_width // 2
submarine_y = screen_height // 2

# Set the submarine speed
submarine_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                submarine_rect.centerx -= submarine_speed
            elif event.key == pygame.K_RIGHT:
                submarine_rect.centerx += submarine_speed
            elif event.key == pygame.K_UP:
                submarine_rect.bottom -= submarine_speed
            elif event.key == pygame.K_DOWN:
                submarine_rect.bottom += submarine_speed

    # Draw background
    pygame.draw.rect(screen, LAND_COLOR, land_rect)
    pygame.draw.rect(screen, WATER_COLOR, water_rect)
    pygame.draw.rect(screen, SKY_COLOR, sky_rect)

    # Draw the submarine
    screen.blit(submarine_image, submarine_rect)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
