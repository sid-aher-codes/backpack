import pygame

class Backpack:
    def __init__(self, game_name, screen_size, background_color):
        #init games
        self.game_name = game_name
        self.screen_size = screen_size
        self.background_color = background_color
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill(background_color)

    def add_image(self, image, location):
        #self.image = image
        #self.location = location
        self.image = pygame.image.load(image)
        self.screen.blit(self.image, location)

        
# Create backpack background screen
bp = Backpack("Backpack", (400,400), (255,255,255))

# Add image to the screen
bp.add_image("/Users/sidaher/Documents/pygames/backpack/images/backpack.png", (0,0))

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:
    # for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

    