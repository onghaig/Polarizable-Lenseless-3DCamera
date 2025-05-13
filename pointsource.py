#point source creator: Gavin

import pygame
import sys

#Pygame acts as a window to display our point source:
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode
width, height = screen.get_size()  # Get the actual screen size
pygame.display.set_caption("Point Source Display")

#Define colors: (e.g white, blue, etc?)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

## Set the position and size of the point source (can make functions to automate this later)
point_radius = 5  # Radius of the point source (pixels)
point_x = width // 2  # Center of the screen (X position)
point_y = height // 2  # Center of the screen (Y position)

# Main loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen with a black background

    # Draw the point source as a WHITE circle at the center
    pygame.draw.circle(screen, WHITE, (point_x, point_y), point_radius)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # User clicks anywhere
            running = False

    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()