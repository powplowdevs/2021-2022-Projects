import math
from re import S
import pygame as pg
import random
from pygame.constants import HIDDEN
from sklearn.feature_extraction import grid_to_graph

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
ORANGE = (255,215,0)

#vars
target_spot = [0,0]
start = [0,0]
open_grids = []
closed_grids = []

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []

#cost added to diagnal moves
G = 0

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
def draw():
    for row in range(10):
        for column in range(10):
            color = WHITE
            #start
            if grid[row][column] == 1:
                color = GREEN
            #target
            if grid[row][column] == 2:
                color = RED
            #others
            if grid[row][column] == 3:
                color = BLACK
            if grid[row][column] == 4:
                color = WHITE
            if grid[row][column] == 5:
                color = BLUE
            if grid[row][column] == 6:
                color = ORANGE
            pg.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
    
# -------- Path finder logic -----------

open_grids.append(start)

print(f"start: {start}\nend: {target_spot}")
draw()
pg.display.flip()
base_start = start
for i in range(1):
    f_values = []
    xys = []
    for i in range(8):
       # try:
            #dist fromula prob messed up
            if i == 0:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]-1) - (target_spot[1]) ) + ( (start[0]-1) - (target_spot[0]) ) )
                distance += G
                if [start[0]-1,start[1]-1] not in closed_grids:
                    grid[start[0]-1][start[1]-1] = 5
                #print([start[0]-1,start[1]-1], target_spot)
                if [start[0]-1,start[1]-1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]-1,start[1]-1))
            if i == 1:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]-1) - (target_spot[1]) ) + ( (start[0]) - (target_spot[0]) ) )
                if [start[0]-1,start[1]] not in closed_grids:
                 grid[start[0]-1][start[1]] = 5
                #print([start[0]-1,start[1]], target_spot)
                if [start[0]-1,start[1]] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]-1,start[1]))
            if i == 2:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]-1) - (target_spot[1]) ) + ( (start[0]+1) - (target_spot[0]) ) )
                distance += G
                if [start[0]-1,start[1]+1] not in closed_grids:
                    grid[start[0]-1][start[1]+1] = 5 
                #print([start[0]-1,start[1]+1], target_spot)
                if [start[0]-1,start[1]+1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]-1,start[1]+1))
            if i == 3:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]) - (target_spot[1]) ) + ( (start[0]-1) - (target_spot[0]) ) )
                if [start[0],start[1]-1] not in closed_grids:
                    grid[start[0]][start[1]-1] = 5
                #print([start[0],start[1]-1], target_spot)
                if [start[0],start[1]-1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0],start[1]-1))
            if i == 4: 
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]) - (target_spot[1]) ) + ( (start[0]+1) - (target_spot[0]) ) )
                if [start[0],start[1]+1] not in closed_grids:
                    grid[start[0]][start[1]+1] = 5
                #print([start[0],start[1]+1], target_spot)
                if [start[0],start[1]+1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0],start[1]+1))
            if i == 5:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]+1) - (target_spot[1]) ) + ( (start[0]-1) - (target_spot[0]) ) )
                distance += G
                if [start[0]+1,start[1]-1] not in closed_grids:
                    grid[start[0]+1][start[1]-1] = 5
                #print([start[0]+1,start[1]-1], target_spot)
                if [start[0]+1,start[1]-1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]+1,start[1]-1))
            if i == 6:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]+1) - (target_spot[1]) ) + ( (start[0]) - (target_spot[0]) ) )
                if [start[0]+1,start[1]] not in closed_grids:
                    grid[start[0]+1][start[1]] = 5
                #print([start[0]+1,start[1]], target_spot)
                if [start[0]+1,start[1]] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]+1,start[1]))
            if i == 7:
                #if the gird is walkable
                distance = math.sqrt( ( (start[1]+1) - (target_spot[1]) ) + ( (start[0]+1) - (target_spot[0]) ) )
                distance += G
                if [start[0]+1,start[1]+1] not in closed_grids:
                    grid[start[0]+1][start[1]+1] = 5
                #print([start[0]+1,start[1]+1], target_spot)
                if [start[0]+1,start[1]+1] == target_spot:
                    start = target_spot
                    break
                xys.append((start[0]+1,start[1]+1))

            f_values.append(distance)
            print(f_values)
            draw()
            pg.display.flip()
            pg.time.wait(10)
        #except:
        #    pass#close to wall so not every node is open
    if start == target_spot:
        print("HIT")
        grid[base_start[0]][base_start[1]] = 1
        grid[target_spot[0]][target_spot[1]] = 2
        break
    
    #current = f_values.index(min(f_values))
    current = f_values[0]
    for index, value in enumerate(f_values):
        if value <= current:
            current = i
            

    grid[xys[current][0]][xys[current][1]] = 6
   
    closed_grids.append([xys[current][0],xys[current][1]])

    start = [xys[current][0],xys[current][1]]

    draw()
    pg.display.flip()
    pg.time.wait(10)

    



draw()

# Limit to 60 frames per second
clock.tick(60)
# Go ahead and update the screen with what we've drawn.
pg.display.flip()

pg.time.wait(50000)

pg.quit()