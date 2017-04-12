#=====================================================#
# Pygame template - skeleton for a new pygame project #
#=====================================================#


# libaries
import pygame
import random


# Constants
WIDTH = 600
HEIGHT = 400
FPS = 30


# Colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)


# Initialize pygame and other basics
pygame.init()
pygame.mixer.init()
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the game
pygame.display.set_caption("Set Title")
# keeps track of the speed
clock = pygame.time.Clock()


# Sprites
all_sprites = pygame.sprite.Group()

# Game loop
GameRunning = True
while GameRunning:
    # Keep loop running at the fps speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        # Quit game on hitting escape
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRunning = False

    # Update
    all_sprites.update() # This can maybe be on both sides of "screen.fill(BLACK)". i dont quite understand it.

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # should be ran after everything is drawn
    pygame.display.flip()

pygame.QUIT
quit()
