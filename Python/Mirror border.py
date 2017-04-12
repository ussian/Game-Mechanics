# libaries
import pygame
import random


# Constants
WIDTH = 600
HEIGHT = 400
FPS = 30

# player speed
SPEEDY = 7
SPEEDX = 7


# Colors in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)


# player
class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, startingPosition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50)) #size of image
        self.image.fill(GREEN) # fill with the color
        self.rect = self.image.get_rect() # converts the "self.image" to a "Rect"

        self.rect.center = startingPosition # Starting Position



    def update(self): # This is run in a loop.

        self.speedy = 0 # These two are used for reseting movement
        self.speedx = 0 # so the sprite stops moving when releasing key.

        self.mirror_border()

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

        if self.rect.left > WIDTH: # move to the other border for each direction
            self.rect.left = 0
        if self.rect.right < 0:
            self.rect.right = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.top = 0
        if self.rect.bottom < 0:
            self.rect.bottom = HEIGHT



    def mirror_border(self): # draws a rectangle with the height/width of the player on the oposite part of the screen
        if self.rect.top < 0:
            pygame.draw.rect(screen, (RED), pygame.Rect((self.rect.x,HEIGHT), (50,self.rect.y)))

        if self.rect.bottom > HEIGHT:
            pygame.draw.rect(screen, (RED), pygame.Rect((self.rect.x,0), (50,self.rect.y - HEIGHT + 50)))

        if self.rect.right > WIDTH:
            pygame.draw.rect(screen, (RED), pygame.Rect((0, self.rect.y), (self.rect.x - WIDTH + 50,50)))

        if self.rect.left < 0:
            pygame.draw.rect(screen, (RED), pygame.Rect((WIDTH, self.rect.y), (self.rect.x, 50)))


    def move(self, dx, dy):
        # Move each axis separately.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


# Initialize pygame and other basics
pygame.init()
pygame.mixer.init()
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the game
pygame.display.set_caption("Mirror border")
# keeps track of the speed
clock = pygame.time.Clock()


# Sprites

all_sprites = pygame.sprite.Group()

player = Player((WIDTH / 1.5, HEIGHT / 2))
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
        # Quit game on hitting escape
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRunning = False


    # Draw / Render
    screen.fill(BLACK)

    all_sprites.update()



    all_sprites.draw(screen)

    # should be ran after everything is drawn
    pygame.display.flip()

pygame.QUIT
print("after 'pygame.QUIT'")
quit()
