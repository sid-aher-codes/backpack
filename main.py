import pygame
import PyQt6

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('/Users/sidaher/Documents/pygames/backpack/images/backpack.png')
#carImg = pygame.transform.scale(carImg, (140,95))


# Image and position of backpack
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if carImg.get_rect().collidepoint(mousePos):
                print("Clicked on the backpack")
        ######################
    ##
    x += x_change
    y += y_change
   ##         
    gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()