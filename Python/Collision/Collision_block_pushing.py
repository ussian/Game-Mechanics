#=====================================================#
# Pygame template - skeleton for a new pygame project #
#=====================================================#


# libaries
import pygame
import random


# Constants
WIDTH = 800
HEIGHT = 800
FPS = 60

SPEEDY = 3
SPEEDX = 3


# Colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

class Ball(pygame.sprite.Sprite):
    # sprite for the Ball
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 1.4, HEIGHT / 1.4)

    def update(self):
        self.rect.x += 0
        # Move to other side of the screen if it goes off to the left or right
        if self.rect.left > WIDTH: # off to the right
            self.rect.right = 0
        if self.rect.right < 0: # off to the left
            self.rect.left = WIDTH
        # Move to other side of the screen if it goes off to the top or bottom
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50)) #size of image
        self.image.fill(GREEN) # fill with the color
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 2, HEIGHT / 2) # Starting Position

    def update(self): # This is run in a loop.

        self.speedy = 0 # These two are used for reseting movement
        self.speedx = 0 # so the sprite stops moving when releasing key.

        keystate = pygame.key.get_pressed() # list of pressed keys (bool)

        if keystate[pygame.K_LEFT]: # Moves left on left arrow click
            self.move(SPEEDX *-1, 0)
        if keystate[pygame.K_RIGHT]: # Moves right on right arrow click
            self.move(SPEEDX, 0)

        if keystate[pygame.K_UP]: # Moves up on up arrow click
            self.move(0, SPEEDY *-1)
        if keystate[pygame.K_DOWN]: # Moves down on down arrow click
            self.move(0, SPEEDY)

        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # Move to other side of the screen if it goes off to the left or right
        if self.rect.left > WIDTH: # off to the right
            self.rect.right = 0
        if self.rect.right < 0: # off to the left
            self.rect.left = WIDTH
        # Move to other side of the screen if it goes off to the top or bottom
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.colliderect(ball.rect):
            if dx > 0: # Moving right; Hit the left side of the wall
                ball.rect.left = self.rect.right
            if dx < 0: # Moving left; Hit the right side of the wall
                ball.rect.right = self.rect.left
            if dy > 0: # Moving down; Hit the top side of the wall
                ball.rect.top = self.rect.bottom
            if dy < 0: # Moving up; Hit the bottom side of the wall
                ball.rect.bottom = self.rect.top


# Initialize pygame and other basics
pygame.init()
pygame.mixer.init()
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the game
pygame.display.set_caption("My Game")
# keeps track of the speed
clock = pygame.time.Clock()


# Sprites
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

ball = Ball()
all_sprites.add(ball)

# Game loop
GameRunning = True
while GameRunning:
    # Keep loop running at the fps speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRunning = False
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
print("after 'pygame.QUIT'")
quit()
