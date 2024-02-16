import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Load image (make sure it has an alpha channel, like a PNG)
image = pygame.image.load("./assets/images/BattleField_background.png").convert_alpha()

# Set desired transparency (0 is fully transparent, 255 is fully opaque)
transparency = 128  # Adjust this value for desired transparency

# Create a transparent surface with the same size as the image
transparent_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)

# Fill the transparent surface with the desired transparency level
transparent_surface.fill((0, 0, 0, transparency))

# Blit the image onto the transparent surface
image.blit(transparent_surface, (0, 0))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the image with transparency
    screen.blit(image, (100, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()