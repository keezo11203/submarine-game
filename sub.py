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
submarine_image = pygame.transform.scale(submarine_image, (submarine_image.get_width() // 2, submarine_image.get_height() // 2))
submarine = pygame.Surface(submarine_image.get_size())
submarine_rect = submarine_image.get_rect()
submarine_rect.centerx = screen_width // 2
submarine_rect.bottom = screen_height - 10

# Set the initial position of the submarine
submarine_x = screen_width // 2
submarine_y = screen_height // 2

# Set the submarine speed
submarine_speed = 15

moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # Update the submarine's position
    if moving_left:
        submarine_rect.centerx -= submarine_speed
    if moving_right:
        submarine_rect.centerx += submarine_speed
    if moving_up:
        submarine_rect.bottom -= submarine_speed
    if moving_down:
        submarine_rect.bottom += submarine_speed

    # Keep the submarine on the screen
    if submarine_rect.left < 0:
        submarine_rect.left = 0
    if submarine_rect.right > screen_width:
        submarine_rect.right = screen_width
    if submarine_rect.top < water_rect.bottom:
        submarine_rect.top = water_rect.bottom
    if submarine_rect.bottom > land_rect.top:
        submarine_rect.bottom = land_rect.top

    # Draw the background and the submarine
    pygame.draw.rect(screen, LAND_COLOR, land_rect)
    pygame.draw.rect(screen, WATER_COLOR, water_rect)
    pygame.draw.rect(screen, SKY_COLOR, sky_rect)
    screen.blit(submarine_image, submarine_rect)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
