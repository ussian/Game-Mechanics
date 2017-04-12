
# libaries
import pygame
import random


# Constants
WIDTH = 800
HEIGHT = 800
FPS = 120
SPEEDX = 2
SPEEDY = 1

# Colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50)) #size of image
        self.image.fill(GREEN) # fill with the color
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 2, HEIGHT / 2) # Starting Position

        self.speedy = SPEEDY # These two are used for reseting movement
        self.speedx = SPEEDX # so the sprite stops moving when releasing key.

    def update(self): # This is run in a loop.

        # Dont place "speedy = 8" in here because then every time the
        # loop runs it will set the speed to 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy


        if self.rect.bottom == HEIGHT | self.rect.bottom > HEIGHT:
            self.speedy *= -1

        if self.rect.top == 0 | self.rect.top < 0:
            self.speedy *= -1

        if self.rect.right == WIDTH | self.rect.right > WIDTH:
            self.speedx *= -1

        if self.rect.left == 0 | self.rect.left < 0:
            self.speedx *= -1



        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0


# Initialize pygame and other basics
pygame.init()
pygame.mixer.init()
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the game
pygame.display.set_caption("Border Bounce")
# keeps track of the speed
clock = pygame.time.Clock()


# Sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
GameRunning = True
while GameRunning:
    # Keep loop running at the fps speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False



    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # should be ran after everything is drawn
    pygame.display.flip()

pygame.QUIT
quit()
