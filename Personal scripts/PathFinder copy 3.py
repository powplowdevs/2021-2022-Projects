from os import cpu_count, lstat, stat, terminal_size
import sys
import os
from typing import Collection, Text
import pygame as pg
import random
import time
import math

from pygame.constants import HIDDEN

def main():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)
    target_spot = [0,0]
    start = [0,0]
    # This sets the WIDTH and HEIGHT of each grid location
    #og size is 20,20
    WIDTH = 20
    HEIGHT = 20
    
    # This sets the margin between each cell
    #og 5
    MARGIN = 2
    rows, cols = 24, 24
    
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(rows):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(cols):
            grid[row].append(0)  # Append a cell
    
    #color grid

    #add enviroment blocks
    for i in range(len(grid)):
        block_state = random.randint(3, 5)

        x = random.randint(1,rows - 1)
        y = random.randint(1,cols - 1)

        if block_state == 3 or 4:
            grid[y][x] = 3
        else:
            grid[y][x] = 5

    #add start and end blocks 
    for i in range(2):
        x = random.randint(1,rows - 1)
        y = random.randint(1,cols - 1)

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
    #og size is 255,255
    WINDOW_SIZE = [500, 500]
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
    for row in range(rows):
        for column in range(cols):
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
    last = ""
    print(cspot, "start")
    print(target_spot, "target")
    fast_rout = []

    #--LOGIC--#

    #HEYYYYYYYYYYYYY
    #The code can handle hiting a wall while its going strignht and the x or y and aligned with the target
    #we may be able to fix this by make the code aslo go forward or backwards every time it goes right or left
    #and make the code go right or left every time it goes forward or backwards
    #but only do this when is handling a collistion!!!

    #ok so what i jut said up there porb wont work
    #i hope u rember ur soultion from pe class!

    #if they dont have the same y or x

    while not found:
        while cspot != target_spot:
            #if we are not allredy set on the y

            if cspot[0] > target_spot[0]:
                #UP
                if grid[cspot[0]-1][cspot[1]] != 3:  
                    cspot[0] -= 1
                    grid[cspot[0]][cspot[1]] = 5
                    pg.display.flip()
                else:
                    print("we hit a wall 1")
                    if grid[cspot[0]][cspot[1] - 1] != 3 and last != "f" and last != "b" and (cspot[1] - 1) != cols:
                        print("lets go back 1 and our last was", last , cspot)
                        cspot[1] -= 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        last = "b"
                    elif grid[cspot[0]][cspot[1] + 1] != 3 and last != "b" and (cspot[1] + 1) != cols:
                        print("lets go forward and our last was", last , cspot)
                        cspot[1] += 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        last = "f"
                    else:
 
                        #up
                        if grid[cspot[0] - 1][cspot[1]]:
                            cspot[0] -= 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go up and our last was", last , cspot)
                            last = "u"
                        #down
                        if grid[cspot[0] + 1][cspot[1]]:
                            cspot[0] += 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go down and our last was", last , cspot)
                            last = "d"

                
            elif cspot[0] < target_spot[0]:
                #DOWN
                if grid[cspot[0]+1][cspot[1]] != 3:  
                    cspot[0] += 1
                    grid[cspot[0]][cspot[1]] = 5
                    pg.display.flip()
                else:
                    if grid[cspot[0]][cspot[1] + 1] != 3 and last != "f" and (cspot[1] + 1) != cols:
                        cspot[1] += 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go forward and our last was", last , cspot)
                        last = "f"
                    elif grid[cspot[0]][cspot[1] - 1] != 3 and last != "f" and (cspot[1] - 1) != cols:
                        cspot[1] -= 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go back 2 and our last was", last , cspot)
                        last = "b"
                    else:
                       
                        #up
                        if grid[cspot[0] - 1][cspot[1]]:
                            cspot[0] -= 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go up and our last was", last , cspot)
                            last = "u"
                        #down
                        if grid[cspot[0] + 1][cspot[1]]:
                            cspot[0] += 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go down and our last was", last , cspot)
                            last = "d"


                
            grid[cspot[0]][cspot[1]] = 5
            pg.display.flip()

            if cspot[1] > target_spot[1]:
                #LEFT
                if grid[cspot[0]][cspot[1] - 1] != 3:  
                    cspot[1] -= 1
                    grid[cspot[0]][cspot[1]] = 5
                    pg.display.flip()
                else:
                    print("we hit a wall 2")
                    if grid[cspot[0]-1][cspot[1]] != 3 and last != "d" and last != "u" and (cspot[0] - 1) != cols:
                        cspot[0] -= 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go up and our last was", last , cspot)
                        last = "u"
                    elif grid[cspot[0] + 1][cspot[1]] != 3 and last != "u" and (cspot[0] + 1) != cols:
                        cspot[0] += 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go down and our last was", last , cspot)
                        last = "d"
                    else:
                        #foward
                        if grid[cspot[0]][cspot[1] + 1]:
                            cspot[1] += 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go forward and our last was", last , cspot)
                            last = "f"
                        #back
                        if grid[cspot[0]][cspot[1] - 1]:
                            cspot[1] -= 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go back and our last was", last , cspot)
                            last = "b"
                       
        
            elif cspot[1] < target_spot[1]:
                #RIGHT
                if grid[cspot[0]][cspot[1] + 1] != 3:  
                    cspot[1] += 1
                    grid[cspot[0]][cspot[1]] = 5
                    pg.display.flip()
                else:
                    print("we hit a wall 3", last)
                    if grid[cspot[0]-1][cspot[1]] != 3 and last != "d" and last != "u" and (cspot[0] - 1) != cols:
                        cspot[0] -= 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go up 2 and our last was", last , cspot)
                        last = "u"
                    elif grid[cspot[0] + 1][cspot[1]] != 3 and last != "u" and (cspot[0] + 1) != cols:
                        cspot[0] += 1
                        grid[cspot[0]][cspot[1]] = 5
                        pg.display.flip()
                        print("lets go down and our last was", last , cspot)
                        last = "d"
                    else:
                        #foward
                        if grid[cspot[0]][cspot[1] + 1]:
                            cspot[1] += 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go forward and our last was", last , cspot)
                            last = "f"
                        #back
                        if grid[cspot[0]][cspot[1] - 1]:
                            cspot[1] -= 1
                            grid[cspot[0]][cspot[1]] = 5
                            pg.display.flip()
                            print("lets go back and our last was", last , cspot)
                            last = "b"
                        
     
                
                    

            time.sleep(.1)
            for row in range(rows):
                for column in range(cols):
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

        found = True


    #--LOGIC--#
    print(fast_rout)        
    

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

    pg.quit()

for i in range(100):
    main()