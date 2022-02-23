import pygame
import pymunk
import random

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

class Ball(): 
    def __init__(self,x,y, collision_type, vel):
        #A body
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = vel
        #A shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.density = 1
        self.shape.elasticity = 1
        #collisions
        self.shape.collision_type = collision_type 
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,(255,0,0),(int(x),int(y)), 10)

def collide(arbiter, space, data):
    print("hit!")


#GAME FUNCTION
def game():
    balls = [Ball(random.randint(0,WITDH),random.randint(0,HEIGHT), i+3,(random.uniform(-200,200),random.uniform(-200,200))) for i in range(100)]
    
    #collisions handler
    handler = space.add_collision_handler(1,2) 
    handler.separate = collide

    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255,255,255))#draw white background

        #draw objects
        [ball.draw() for ball in balls]

        #Update display
        pygame.display.update()

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)

#RUN GAME
game()

pygame.quit()