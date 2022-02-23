import cv2
import numpy as np
#import turtle
import time
import PIL
from PIL import Image
import datetime
import pygame as pg
import sys

from pygame.constants import HIDDEN

print(datetime.datetime.now())

""" 
man = turtle

man.speed()
man.penup()
man.goto(-660, 200)
man.pendown()
turtle.hideturtle()

"""


pg.init()

img = PIL.Image.open("G:\My Drive\Programing\Personal scripts\GigaChad.jpg")

RBG_img = img.convert("1")

widthi, heighti = img.size

print(widthi,heighti)

x = 0
y = 0

num = 0

screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
screen.fill((255, 255, 255))
clock = pg.time.Clock()

height = widthi
width = heighti
size = 1
color = (255, 255, 255)
new_color = (0, 0, 0)

rectangles = []

for ys in range(height):
    for xs in range(width):
        rect = pg.Rect(xs * (size+1), ys * (size+1), size, size)
        # The grid will be a list of (rect, color) tuples.
        rectangles.append((rect, color))


for i in range(width*height):

    num += 1

    rect = pg.Rect(x * (size+1), y - 5 * (size+1), size, size)
    
    cop = RBG_img.getpixel((x,y))

    x += 1

    if num == 300:
        pg.display.flip()
        clock.tick(99990)  
        #time.sleep(.5)
        num = 0  
         
        

    if x > (widthi- 1):
        y += 1
        x = 0

   
    if cop == 0:
        pg.draw.rect(screen, (0,0,0), rect)
    else:
        pg.draw.rect(screen, (255,255,255), rect)
    
for rect, color in rectangles:
    pg.draw.rect(screen, color, rect)
    pg.display.flip()
    clock.tick(0)


screen.fill((255, 255, 255))

# Now draw the rects. You can unpack the tuples
# again directly in the head of the for loop.
for rect, color in rectangles:
    pg.draw.rect(screen, color, rect)

pg.display.flip()
clock.tick(30)

time.sleep(1000)



"""

for i in range(width*height):
   
    cop = RBG_img.getpixel((x,y))
    

    if cop == 0:
        turtle.tracer(1, 0)
        man.color("black")
        man.forward(2.5)     
    else:
        turtle.tracer(1, 0)
        man.color("white")
        man.forward(2.5)

    x += 1
    
    if x > (width-1):
        y+=1
        man.speed()
        man.penup()
        man.goto(-660, (200 - y))
        man.pendown()
        x = 0

turtle.update()
print("done at",datetime.datetime.now())
input("Press Enter to END...")

"""