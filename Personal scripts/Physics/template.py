import pygame
import pymunk

#Start pygame
pygame.init()

#Make display
HEIGHT = 500
WITDH = 500
display = pygame.display.set_mode((WITDH,HEIGHT))

#SET FPS
FPS = 50
clock = pygame.time.Clock()

#our pymunk simulation "world" or space
space = pymunk.Space()

#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], WITDH-point[1]

#GAME FUNCTION
def game():
    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        display.fill((255,255,255))#draw white background

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)

#RUN GAME
game()

pygame.quit()