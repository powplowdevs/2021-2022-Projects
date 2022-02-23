from os import cpu_count, stat, terminal_size
import sys
from typing import Text
import pygame as pg
import random
import time
import math

from pygame.constants import HIDDEN

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
target_spot = [0,0]
start = [0,0]
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
#color grid

#add enviroment blocks
for i in range(len(grid)):
    block_state = random.randint(3, 5)

    x = random.randint(1,9)
    y = random.randint(1,9)

    if block_state == 3:
        grid[y][x] = 3
    else:
        grid[y][x] = 4

#add start and end blocks 
for i in range(2):
    x = random.randint(1,9)
    y = random.randint(1,9)

    if i == 0:
        grid[y][x] = 1
        start[0] = y
        start[1] = x
    elif i == 1:
        target_spot[0] = y
        target_spot[1] = x 
        grid[y][x] = 2


# Initialize pg
pg.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pg.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pg.display.set_caption("PATH FINDING")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pg.time.Clock()
 
# -------- Main Program Loop -----------

# Set the screen background
screen.fill(BLACK)

# Draw the grid
for row in range(10):
    for column in range(10):
        color = WHITE
        #start
        if grid[row][column] == 1:
            color = GREEN
        #target
        if grid[row][column] == 2:
            color = RED
        if grid[row][column] == 3:
            color = BLACK
        if grid[row][column] == 4:
            color = WHITE
        if grid[row][column] == 5:
            color = BLUE
        pg.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
 
# Limit to 60 frames per second
clock.tick(60)
# Go ahead and update the screen with what we've drawn.
pg.display.flip()
 
#----OUR LOGIC FOR PATH FINDER------#
found = False
cspot = start
print(cspot, "start")
print(target_spot, "target")
fast_rout = []

#--LOGIC--#

#HEYYYYYYYYYYYYY
#why dont we just figure out if our stat is on the left or right of the target
#then align the x and align the y?
#lmao

#if they dont have the same y or x

while not found:
    #if we are not allredy set on the y
    if cspot[0] > target_spot[0]:

        while cspot[0] != target_spot[0]:
            cspot[0] -= 1
            grid[cspot[0]][cspot[1]] = 5
            pg.display.flip()
            time.sleep(.5)
          
            for row in range(10):
                for column in range(10):
                    color = WHITE
                    #start
                    if grid[row][column] == 1:
                        color = GREEN
                    #target
                    if grid[row][column] == 2:
                        color = RED
                    if grid[row][column] == 3:
                        color = BLACK
                    if grid[row][column] == 4:
                        color = WHITE
                    if grid[row][column] == 5:
                        color = BLUE
                    pg.draw.rect(screen,
                                        color,
                                        [(MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT])
    
    elif cspot[0] < target_spot[0]:
      
        while cspot[0] != target_spot[0]:
            cspot[0] += 1
            grid[cspot[0]][cspot[1]] = 5
            pg.display.flip()
            time.sleep(.5)
          
            for row in range(10):
                for column in range(10):
                    color = WHITE
                    #start
                    if grid[row][column] == 1:
                        color = GREEN
                    #target
                    if grid[row][column] == 2:
                        color = RED
                    if grid[row][column] == 3:
                        color = BLACK
                    if grid[row][column] == 4:
                        color = WHITE
                    if grid[row][column] == 5:
                        color = BLUE
                    pg.draw.rect(screen,
                                        color,
                                        [(MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT])
    
    if cspot[0] == target_spot[0]:
        grid[cspot[0]][cspot[1]] = 5
        pg.display.flip()

        if cspot[1] > target_spot[1]:
  
            while cspot[1] != target_spot[1] + 1:
                cspot[1] -= 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                time.sleep(.5)
              
                for row in range(10):
                    for column in range(10):
                        color = WHITE
                        #start
                        if grid[row][column] == 1:
                            color = GREEN
                        #target
                        if grid[row][column] == 2:
                            color = RED
                        if grid[row][column] == 3:
                            color = BLACK
                        if grid[row][column] == 4:
                            color = WHITE
                        if grid[row][column] == 5:
                            color = BLUE
                        pg.draw.rect(screen,
                                            color,
                                            [(MARGIN + WIDTH) * column + MARGIN,
                                            (MARGIN + HEIGHT) * row + MARGIN,
                                            WIDTH,
                                            HEIGHT])
        
        elif cspot[1] < target_spot[1]:
     
            while cspot[1] != target_spot[1] - 1:
                cspot[1] += 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                time.sleep(.5)
              
                for row in range(10):
                    for column in range(10):
                        color = WHITE
                        #start
                        if grid[row][column] == 1:
                            color = GREEN
                        #target
                        if grid[row][column] == 2:
                            color = RED
                        if grid[row][column] == 3:
                            color = BLACK
                        if grid[row][column] == 4:
                            color = WHITE
                        if grid[row][column] == 5:
                            color = BLUE
                        pg.draw.rect(screen,
                                            color,
                                            [(MARGIN + WIDTH) * column + MARGIN,
                                            (MARGIN + HEIGHT) * row + MARGIN,
                                            WIDTH,
                                            HEIGHT])
        







#--LOGIC--#
print(fast_rout)        
 

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
time.sleep(10)
pg.quit()
