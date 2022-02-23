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
    scores = []
       
    #if they have the same y
    if start[0] == target_spot[0]:
        print("same y")
        if start[1] > target_spot[1]:
            print("going back")
            while cspot != target_spot:
                cspot[1] -= 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()

        if start[1] < target_spot[1]:
            print("going forward")
            while cspot != target_spot:
                cspot[1] += 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
    #if they have the same x
    elif start[1] == target_spot[1]:
        print("same x")
        if start[0] > target_spot[0]:
            print("going up")
            while cspot != target_spot:
                fast_rout.append("up")
                scores = [999,999,0,999]
                cspot[0] -= 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()

        if start[0] < target_spot[0]:
            print("going down")
            while cspot != target_spot:
                fast_rout.append("down")
                scores = [999,999,999,0]
                cspot[0] += 1
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
          

    #if we are to thr right of the target
    if start[1] > target_spot[1]:
        print("to the right")
        while cspot[1] != target_spot[1]:
            grid[cspot[0]][cspot[1]] = 5
            cspot[1] -= 1
            pg.display.flip()
            time.sleep(.5)
            print(cspot)
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
        
                    
        #if we are under the target
        if cspot[0] > target_spot[0]:
            while cspot[0] != target_spot[0]:
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                cspot[0] -= 1
                print(cspot)
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
            

        #if we are over the target
        if cspot[0] < target_spot[0]:
            while cspot[0] != target_spot[0]:
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                cspot[0] += 1
                time.sleep(.5)
                print(cspot)
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
            


    #if we are to thr left of the target
    if start[1] < target_spot[1]:
        print("to the left")
        while cspot[1] != target_spot[1]:
            grid[cspot[0]][cspot[1]] = 5
            pg.display.flip()
            cspot[1] += 1
            time.sleep(.5)
            print(cspot)
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
            
        #if we are under the target
        if cspot[0] > target_spot[0]:
            while cspot[0] != target_spot[0]:
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                cspot[0] -= 1
                time.sleep(.5)
                print(cspot)
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
            
        #if we are over the target
        if cspot[0] < target_spot[0]:
            while cspot[0] != target_spot[0]:
                grid[cspot[0]][cspot[1]] = 5
                pg.display.flip()
                cspot[0] += 1
                time.sleep(.5)
                print(cspot)
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
            
    
    

    """
    #loop to get scores for each option
    for i in range(4):
        score = 0
        #1 = x
        #0 = y

        #FORWARD
        if i == 0:
            xs = target_spot[1] - (cspot[1] + 1)
            ys = target_spot[0] - cspot[0]

            print(target_spot[1], " - ", (cspot[1] + 1), "=", target_spot[1] - (cspot[1] + 1), "X")
            print(target_spot[0], " - ", cspot[0], "=", target_spot[0] - cspot[0], "Y")

            s = abs((xs+ys))
            print("we are gonna add", s)
            
            if cspot == target_spot:
                s = -999
                found = True
                print("WE GOT A PATH")
                break

            scores.append(s)
        #BACKWARDS
        if i == 1:
            xs = target_spot[1] - (cspot[1] - 1)
            ys = target_spot[0] - cspot[0]
            s = abs((xs+ys))
            print("we are gonna add", s)

            if cspot == target_spot:
                s = -999
                found = True
                print("WE GOT A PATH")
                break


            scores.append(s)
        #UP
        if i == 2:
            xs = target_spot[1] - cspot[1] 
            ys = target_spot[0] - (cspot[0] - 1)
            s = abs((xs+ys))

        

            if cspot == target_spot:
                s = -999
                found = True
                print("WE GOT A PATH")
                break

            scores.append(s)
        #DOWN 
        if i == 3:
            xs = target_spot[1] - cspot[1]
            ys = target_spot[0] - (cspot[0] + 1)
            s = abs((xs+ys))

        

            if cspot == target_spot:
                s = -999
                found = True
                print("WE GOT A PATH")
                break

            scores.append(s)
        
    #get best path out of scores list
    #print(scores)
    best = min(scores)
    print(scores)
    print(best)

    #find out what movement is best
    for i in range(4):
        if scores[i] == best:
            if i == 0:
                bmove = "forward"
                print("f")
                cspot[0] = cspot[0]
                cspot[1] = cspot[1] + 1
                grid[cspot[0]][cspot[1]] = 5
                break
        
            if i == 1:
                bmove = "back"
                print("b")
                cspot[0] = cspot[0]
                cspot[1] = cspot[1] - 1
                grid[cspot[0]][cspot[1]] = 5
                break
        
            if i == 2:
                bmove = "up"
                print("u")
                cspot[0] = cspot[0] - 1
                cspot[1] = cspot[1] 
                grid[cspot[0]][cspot[1]] = 5
                break
        
            if i == 3:
                bmove = "down"
                print("d")
                cspot[0] = cspot[0] + 1
                print(cspot[0] + 1)
                cspot[1] = cspot[1]
                grid[cspot[0]][cspot[1]] = 5 
                break

                
    
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
    
    pg.display.flip()

    print(cspot)
    print(bmove)

    time.sleep(.5)

    #add the movement to the path
    fast_rout.append(bmove)
    """
#--LOGIC--#

print(fast_rout)        
        
        

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
time.sleep(10)
pg.quit()



"""
 for i in range(4):
        score = 0
        if i == 0: #forward

            if cspot[0] != start[0] and cspot[1] != start[1] and cspot not in scores:
                
                if ((cspot[0] + 1)%10) == 0:
                   
                    cspot[0] = 0
                    look = ((cspot[1] + 1), 0)
                else:
                    
                    look = (cspot[0], cspot[1] + 1)

                #print(look)

                if grid[cspot[0]][cspot[1]] == 3:
                    score += 3
                if grid[cspot[0]][cspot[1]] == 4:
                    scores += 1
                print(score)
                scores.append(score)

            else:
                print(fast_rout, "f")
                found = True

        if i == 1: #backward

            if cspot[0] != start[0] and cspot[1] != start[1] and cspot not in scores:
                
                if (cspot[1] - 1) < 0:
                    cspot[1] = cspot[0]*10
                    look = (cspot[0] - 1, cspot[0])

                if grid[cspot[0]][cspot[1]] == 3:
                    score += 3
                if grid[cspot[0]][cspot[1]] == 4:
                    scores += 1

                print(score,"b")
                scores.append(score)
            else:
                print(fast_rout)
                found = True

        if i == 2: #up

            if cspot[0] != start[0] and cspot[1] != start[1] and cspot not in scores:
            
                look = (cspot[0] - 1, cspot[1])


                if grid[cspot[0]][cspot[1]] == 3:
                    score += 3
                if grid[cspot[0]][cspot[1]] == 4:
                    scores += 1

                print(score, "u")
                scores.append(score)
            else:
                print(fast_rout)
                found = True

        if i == 3: #down

            if cspot[0] != start[0] and cspot[1] != start[1] and cspot not in scores:
                look = (cspot[0] + 1, cspot[1])

                if grid[cspot[0]][cspot[1]] == 3:
                    score += 3
                if grid[cspot[0]][cspot[1]] == 4:
                    scores += 1

                print(score, "d")
                scores.append(score)
            else:
                print(fast_rout)
                found = True

       # print(score)

    print(scores, "ts")
    best = min(scores)

    for i in range(4):
        if scores[i] == best:

            if i == 0:
                if ((cspot[0] + 1)%10) == 0:
                    cspot[0] = 0
                    look = [(cspot[1] + 1), 0]
                    looks = ( (cspot[1] + 1), 0 )
                    
                else:
                    look = [cspot[0], cspot[1] + 1]
                    looks = (cspot[0], cspot[1] + 1)

                
                fast_rout.append(look)
                cspot = looks

            if i == 1:
                if (cspot[1] - 1) < 0:
                    cspot[1] = cspot[0]*10
                    look = [cspot[0] - 1, cspot[0]]
                    looks = (cspot[0] - 1, cspot[0])
                fast_rout.append(look)
                cspot = looks

            if i == 2:
                look = [ cspot[0] - 1, cspot[1] ]
                looks ( cspot[0] - 1, cspot[1] )
                fast_rout.append(look)
                cspot = looks

            if i == 3:
                looks = (cspot[0] + 1, cspot[1])
                fast_rout.append([cspot[0] + 1, cspot[1]])
                cspot = looks
                

"""