import pygame
from pygame import image
import pymunk
import numpy as np
import math
import random
import time
import threading

#Start pygame
pygame.init()

#VARS

#Make display
HEIGHT = 600
WITDH = 1000
display = pygame.display.set_mode((WITDH,HEIGHT))

#SET FPS
FPS = 25
SIM_SPACE = 200
SIZE = 1  
AMT = 20
COLIS = False
MIN = 30

justSel = False
auto = False
selected = "r"
planets = []
trail = []
traillen = 100
clock = pygame.time.Clock()

#our pymunk simulation "world" or space
space = pymunk.Space()


#FUNCTIONS
#CONVERT PYGAME CORDS TO PYMUNK CORDS FUNCTION
def convert_cords(point):
    return point[0], HEIGHT-point[1]

def gforce(p1,p2):
    try:
        # Calculate the gravitational force exerted on p1 by p2.
        G = 1 # Change to 6.67e-11 to use real-world values.
        # Calculate distance vector between p1 and p2.
        r_vec = p1.body.position-p2.body.position
        # Calculate magnitude of distance vector.
        r_mag = np.linalg.norm(r_vec)
        # Calcualte unit vector of distance vector.
        r_hat = r_vec/r_mag
        # Calculate force magnitude.
        force_mag = G*p1.shape.mass*p2.shape.mass/r_mag**2
        # Calculate force vector.
        force_vec = -force_mag*r_hat
        
        return force_vec
    except:
        return (0,0)

def collide(arbiter,space,data):
    pass

#CLASS'S
class Ball(): 
    def __init__(self,tag,x,y, vel, mass, coltype,sun_or_ball="Ball", type=""):
        #tag
        self.tag = tag
        #sunorball
        self.sun_or_ball = sun_or_ball
        #type
        self.type = type
        #coltype
        self.coltype = coltype
        #vel
        self.vel = vel
        #A body
        if type == "STATIC":
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        else:
            self.body = pymunk.Body()
        self.body.position = convert_cords((x,y))
        self.body.velocity = vel
        #A shape
        self.shape = pymunk.Circle(self.body,SIZE+(mass*0.1))
        self.shape.density = 1
        self.shape.mass = mass
        self.shape.elasticity = 1
        self.shape.collision_type = coltype
        if COLIS == False:
            self.shape.filter = pymunk.ShapeFilter(group=1)
        #col handler
        self.handler = space.add_collision_handler(1,1)
        self.handler.separate = self.breakUp
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        if self.coltype != 2:
            x,y = convert_cords(self.body.position)
            pygame.draw.circle(display,(255,0,0),(x,y), SIZE+(self.shape.mass*0.1))
        else:
            x,y = convert_cords(self.body.position)
            pygame.draw.circle(display,(255,0,0),(x,y), SIZE+(self.shape.mass*0.1))

    def breakUp(self, arbiter,space,data):
        global planets
        
        pass
    
class Sun(): 
    def __init__(self,tag,x,y, vel, mass, sun_or_ball="Sun", type=""):
        #tag
        self.tag = tag
        #sunorball
        self.sun_or_ball = sun_or_ball
        #A body
        if type == "STATIC":
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        else:
            self.body = pymunk.Body()
        self.body.position = convert_cords((x,y))
        self.body.velocity = vel
        #A shape
        self.shape = pymunk.Circle(self.body,SIZE+(mass*0.1))
        self.shape.density = 1
        self.shape.mass = mass
        self.shape.elasticity = 1
        if COLIS == False:
            self.shape.filter = pymunk.ShapeFilter(group=1)
        #add body and shape to space
        space.add(self.body,self.shape)
    
    def draw(self):
        #show the circle
        x,y = convert_cords(self.body.position)
        pygame.draw.circle(display,(255,255,0),(x,y), SIZE+(self.shape.mass*0.1))

class Button():
    def __init__(self,tag,x,y,img,size):
        self.tag = tag
        width, height = img.get_width(), img.get_height()
        self.img = pygame.transform.scale(img, (int(width*size),int(height*size)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.cliked = False
    
    def draw(self):
        global selected, justSel
        #get mouse pos
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliked == False:
                selected = self.tag
                justSel = True
                

        if pygame.mouse.get_pressed()[0] == 0:
            self.cliked = False

        x,y = (self.rect.x,self.rect.y)
        display.blit(self.img, (x,y))

class Trail():
    global trail
    def __init__(self,tag,x,y, vel, mass, coltype, type=""):
        #tag
        self.tag = tag
        #type
        self.type = type
        #coltype
        self.coltype = coltype
        #vel
        self.vel = vel
        #A body
        if type == "STATIC":
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        else:
            self.body = pymunk.Body()
        self.body.position = convert_cords((x,y))
        self.body.velocity = vel
        #A shape
        self.shape = pymunk.Circle(self.body,SIZE+(mass*0.1))
        self.shape.density = 1
        self.shape.mass = mass
        self.shape.elasticity = 1
        self.shape.collision_type = coltype
        if COLIS == False:
            self.shape.filter = pymunk.ShapeFilter(group=1)
        #add body and shape to space
        space.add(self.body,self.shape)
        timer = threading.Timer(1.0, self.destory)
        timer.start()
    
    def draw(self):
        #show the circle
        if self.coltype != 2:
            x,y = convert_cords(self.body.position)
            pygame.draw.circle(display,(255,255,255),(x,y), SIZE+(self.shape.mass*0.1))
        else:
            x,y = convert_cords(self.body.position)
            pygame.draw.circle(display,(255,255,255),(x,y), SIZE+(self.shape.mass*0.1))

    def destory(self):
        trail.remove(self)


sunbg = pygame.image.load("sunbg.png").convert_alpha()
smbg = pygame.image.load("sunmovebg.png").convert_alpha()
cmbg = pygame.image.load("cusmove.png").convert_alpha()
rbg = pygame.image.load("rbbg.png").convert_alpha()
arbg = pygame.image.load("arbbg.png").convert_alpha()
sunButton = Button("s",10,10,sunbg,0.5)
smButton = Button("sm",10,60,smbg,0.5)
cmButton = Button("cm",10,110,cmbg,0.5)
rButton = Button("r",10,160,rbg,0.5)
arButton = Button("ar",10,210,arbg,0.5)

#GAME FUNCTION
def game():
    global justSel, planets, traillen

    planets = [Ball(i,random.randint(100,WITDH-100),random.randint(100,HEIGHT-100), (random.uniform(-10,10),random.uniform(-10,10)), random.randint(10,50), 1) for i in range(AMT)]
    sun = Sun(len(planets),WITDH/2, HEIGHT/2, (0,0), 100, "Sun", "STATIC")

    planets.append(sun)

    # handlers = [space.add_collision_handler(1,1) for i in range(AMT)]
    # for i, handler in enumerate(handlers):
    #     handler.separate = planets[i].breakUp

    
    while True:
        #check to see if user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if selected == "r" and justSel == False:
                    planets.append(Ball(len(planets)+1, pos[0],pos[1], (random.uniform(-10,10),random.uniform(-10,10)), random.randint(10,50),1))
                if selected == "s" and justSel == False:
                    planets.append(Sun(len(planets)+1,pos[0],pos[1], (0,0), 100,"Sun", "STATIC"))
                if selected == "sm" and justSel == False:
                    mass = int(input("Enter your custom suns mass"))
                    sx = int(input("Enter your customs suns velocity on the X axis"))
                    sy = int(input("Enter your customs suns velocity on the Y axis"))
                    time.sleep(1.5)
                    planets.append(Sun(len(planets)+1,pos[0],pos[1], (sx,sy),mass))
                if selected == "c" and justSel == False:
                    pass
                if selected == "cm" and justSel == False:
                    mass = int(input("Enter your custom planets mass"))
                    sx = int(input("Enter your customs planets velocity on the X axis"))
                    sy = int(input("Enter your customs planets velocity on the Y axis"))
                    time.sleep(1.5)
                    planets.append(Ball(len(planets)+1,pos[0],pos[1], (sx,sy),mass,len(planets)+3))
                if selected == "ar":
                    [planets.append(Ball(i+len(planets)+1,random.randint(100,WITDH-100),random.randint(100,HEIGHT-100), (random.uniform(-10,10),random.uniform(-10,10)), random.randint(10,50),1)) for i in range(AMT)]
                    
                elif justSel == True:
                    justSel = False

        if len(planets) < MIN and auto:
            planets.append(Ball(len(planets)+1,random.randint(100,WITDH-100),random.randint(100,HEIGHT-100), (random.uniform(-10,10),random.uniform(-10,10)), random.randint(10,50),1))

        display.fill((0,0,0))#draw white background

        for ball in planets:
            if ball.sun_or_ball != "Sun":
                x,y = convert_cords(ball.body.position)
                tr = Trail(0,x, y,(0,0),0,1,"STATIC")
                trail.append(tr)


        #move objects & collissions
        for planet1 in planets:
            for planet2 in planets:
                if planet1.tag != planet2.tag:
                    if planet1.body.position[0] < -SIM_SPACE or planet1.body.position[0] > WITDH+SIM_SPACE or planet1.body.position[1] < -SIM_SPACE or planet1.body.position[1] > HEIGHT+SIM_SPACE:
                        t = planet1.tag
                        planets.remove(planet1)
                        for planet in planets:
                            if planet.tag > t:
                                planet.tag -= 1
                        #print("removed:", planet1, "it was as pos:", planet1.body.position, "li is now", planets)
                        break
                    # elif planet1.body.position[0]-planet2.body.position[0] > -10 and planet1.body.position[0]-planet2.body.position[0] < 10 and planet1.body.position[1]-planet2.body.position[1] < 10 and planet1.body.position[1]-planet2.body.position[1] > -10:
                        
                    #     if planet1.sun_or_ball == "Ball":
                    #         #print(planet1.sun_or_ball, planet2.sun_or_ball)
                    #         #find higher mass planet
                    #         if planet1.body.mass > planet2.body.mass and planet1.sun_or_ball != "frag":
                    #             #remove plant 2 and add force to plant1
                                
                    #             p2mass = planet2.body.mass
                    #             p2pos = convert_cords(planet2.body.position)
                    #             force = gforce(planet1, planet2)
                    #             force2 = gforce(planet2,planet1)
                    #             planets.remove(planet2)
                    #             planet1.body.velocity += (force[0]*5, force[1]*5)
                    #             #create 2 fragments each 1/3 of planet2 mass
                    #             planets.append(Ball(len(planets),p2pos[0],p2pos[1]+50, (force2[0],force2[1]) ,p2mass/3, random.randint(10,50), "frag"))
                    #             planets.append(Ball(len(planets),p2pos[0],p2pos[1]-50, (force2[0],force2[1]) ,p2mass/3, random.randint(10,50), "frag"))
                    #             planets.append(Ball(len(planets),p2pos[0]+50,p2pos[1], (force2[0],force2[1]) ,p2mass/3, random.randint(10,50), "frag"))
                               
                    #         elif planet2.sun_or_ball != "frag":
                    #             #remove plant 1 and add force to plant2
                                
                    #             p1mass = planet2.body.mass
                    #             p1pos = convert_cords(planet2.body.position)
                    #             force = gforce(planet1, planet2)
                    #             force2 = gforce(planet2, planet1)
                    #             planets.remove(planet1)
                    #             planet1.body.velocity += (force[0]*5, force[1]*5)
                    #             #create 2 fragments each 1/3 of planet1 mass
                    #             #,tag,x,y, vel, mass, coltype,sun_or_ball="Ball", type=""
                    #             planets.append(Ball(len(planets),p1pos[0],p1pos[1]+50, (force2[0],force2[1]) ,p1mass/3, random.randint(10,50), "frag"))
                    #             planets.append(Ball(len(planets),p1pos[0],p1pos[1]-50, (force2[0],force2[1]) ,p1mass/3, random.randint(10,50), "frag"))
                    #             planets.append(Ball(len(planets),p1pos[0]+50,p1pos[1], (force2[0],force2[1]) ,p1mass/3, random.randint(10,50), "frag"))
                        
                    #     elif planet1.sun_or_ball == "frag":
                    #         t = planet1.tag
                    #         planets.remove(planet1)
                    #         for planet in planets:
                    #             if planet.tag > t:
                    #                 planet.tag -= 1
                    #     elif planet2.sun_or_ball == "frag":
                    #         t = planet2.tag
                    #         planets.remove(planet2)
                    #         for planet in planets:
                    #             if planet.tag > t:
                    #                 planet.tag -= 1
                            

                                

                    #     #print(planet1.body.position[0]-planet2.body.position[0],planet1.body.position[1]-planet2.body.position[1])
                        #planets.remove(planet2)
                    #else:
                        #print(planet1.body.position[1])
                        #time.sleep(1)
                    force = gforce(planet1, planet2)
                    planet1.body.velocity += (force[0]*5, force[1]*5)
                    
    
        #draw objects
        [planet.draw() for planet in planets]
        sunButton.draw()
        smButton.draw()
        cmButton.draw()
        rButton.draw()
        arButton.draw()
        for b in trail:
            b.draw()

        #Update display
        pygame.display.update()
        
        # if len(trail) > traillen*2:
        #     for i in range(traillen):
        #         try:
        #             trail.remove(trail[0])
        #         except:
        #             break

        #FPS TICK
        clock.tick(FPS)
        space.step(1/FPS)

#RUN GAME
game()

pygame.quit()
