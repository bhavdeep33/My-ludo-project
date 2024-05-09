import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Image Using get_rect()")

# Load the image
image = pygame.image.load("Images/Red.png")  # Replace "image.png" with your image file path

# Get the dimensions of the image
image_width, image_height = image.get_size()

# Get the Rect object for the image
image_rect = image.get_rect()

# Set the initial position of the Rect object
image_rect.topleft = (100, 100)  # Example initial position

image = pygame.image.load("Images/Green.png")
image_rect.topleft = (100, 100)

# Movement speed
move_x = 1
move_y = 1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the Rect object (move the image)
    image_rect.x += move_x
    image_rect.y += move_y

    # Check boundaries
    if image_rect.right >= screen_width or image_rect.left <= 0:
        move_x *= -1
    if image_rect.bottom >= screen_height or image_rect.top <= 0:
        move_y *= -1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit (draw) the image onto the screen surface at the specified position
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
