#Create a world
#Create a mouse {Need_to_reproduce, strength, food}
#Create a tree {used}
 
#Make a x amt of starting mouse's
#Make an x amt of starting trees
 
#Every day each mouse will go out in search of food and will have a 100% chance to find it
#Once the mouse has obtained a piece of food a chance equal to (Need_to_reproduce/10) will be rolled
#If that chance is positive then the mouse will go looking for another piece of food.
#Note that its not guaranteed that the mouse will get food as there may be none left
#Regardless once the mouse decides to go looking for a second piece of food a random chance will be rolled
#The chance is equal to (strength/10) if the chance is positive then the mouse will go home with 2 food
#If its not it will die
#If the mouse has 2 food at the end of the day it will have a 100% chance to reproduce and its strength will be +1
#If the mouse has 1 food at the end of the day it will have a 0% chance to reproduce and its strength will be +1

#IMPORTS
from tkinter.tix import MAX
import pygame
import pygame.display
import random
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from statistics import mode

#start pygame
pygame.init()

#DISPLAY
display = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()

#COLORS
RED = (200,0,0)
BROWN = (165,42,42)
WHITE = (255,255,255)

#FONTS
main_font = pygame.font.SysFont('arial', 13)

#VARS
FPS = 60
MUTATION_CHANCE = 5
SPEED = 0
MAX_DAYS = 50
REPPRODUCE_FACTOR = 1
SIM_TIME = 500

simulating = True
mouse_amt = 20
tree_amt = mouse_amt*2
mouses = []
trees = []
mouse_die_to_time = True
liveing_mice = mouse_amt
day = 0
days_list = []
liveing_mice_list = []
ntrp = [] #need to reproduce
best_ntrp_list = []

#plot config
plt.style.use("fivethirtyeight")

#CLASS'S
class Mouse():
    def __init__(self,x,y,radius,Need_to_reproduce, strength, food):
        self.x = x
        self.y = y
        self.radius = radius
        self.need_to_reproduce = Need_to_reproduce
        self.strength = strength
        self.food = food
        self.days_alive = 0
    
    def draw(self):
        x,y = self.x, self.y
        pygame.draw.circle(display,RED,(x,y), self.radius)
        display.blit(main_font.render(str(self.need_to_reproduce), True, WHITE), (x-4, y-8))
        
class Tree():
    def __init__(self,x,y,used=False):
        self.x = x
        self.y = y
        self.used = used

    def draw(self):
        x,y = self.x, self.y
        pygame.draw.circle(display,BROWN,(x,y), 10)
        if self.used == False:
            display.blit(main_font.render("1", True, WHITE), (x-4, y-8))
        else:
            display.blit(main_font.render("0", True, WHITE), (x-4, y-8))

        
#FUNCTIONS
def find_tree():
    global trees
    return trees[random.randint(0,len(trees)-1)]

def tick():
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)

def refresh():
    global liveing_mice
    display.fill((0,0,0))
    for mouse in mouses:
        mouse.draw()
        mouse.days_alive += 1
        if mouse.days_alive > MAX_DAYS and mouse_die_to_time:
            mouses.remove(mouse)
            liveing_mice -= 1
    for tree in trees:
        tree.draw()  

def main():
    global simulating, mouse_amt, tree_amt, mouses, trees, liveing_mice, day, MAX_DAYS, liveing_mice_list, days_list, ntrp, best_ntrp_list

    #create mouse's
    for i in range(mouse_amt):
        x = (i*50)+15
        y = 450
        mouses.append(Mouse(x,y,10,random.randint(1,5),4,0))

    #create trees
    for i in range(tree_amt):
        x = (i*50)+15
        y = 50+random.randint(0,150)
        trees.append(Tree(x,y))


    while simulating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulating = False

        refresh()
        tick()
        
        #LOGIC
        for mouse in mouses:
            #find out tree
            index = 0
            while True:
                index += 1
                tree = find_tree()
                if index == len(trees):
                    #mouse could not find food
                    mouses.remove(mouse)
                    liveing_mice -= 1
                    break
                if tree.used == False:
                    tree.used = True
                    #move our mouse to the tree
                    mouse_base = (mouse.x,mouse.y)
                    mouse.x = tree.x
                    mouse.y = tree.y-15
                    refresh()
                    tick()
                    pygame.time.wait(SPEED)
                    break
            
            if index == len(trees):
                break
            #we found a tree
            mouse.strength += 1
            mouse.food = 1
            greed_chance = mouse.need_to_reproduce

            if random.randint(0,10) < greed_chance:
                #mouse will try to find more food
                #chance_to_find_food = mouse.strength insted of this we will give the mouse a random tree
                #if random.randint(0,10) < chance_to_find_food:
                tree_in_use = find_tree()
                if tree_in_use.used == False:
                    #we found more food
                    mouse.food = 2
                    #mouse.need_to_reproduce = 1
                    #this mouse may reporduce at the end of the day
                else:
                    #the mouse did not find the second piece of food and will die
                    try:
                        mouses.remove(mouse)
                        liveing_mice -= 1
                    except:
                        break
            else:
                #mouse wont try to find more food
                if mouse.need_to_reproduce < 10:
                    mouse.need_to_reproduce += REPPRODUCE_FACTOR

            mouse.x = mouse_base[0]
            mouse.y = mouse_base[1]
            refresh()
            tick()
            pygame.time.wait(SPEED)

        #the day has ended so lets regenerate the forest and reproduce the mice
        for tree in trees:
            tree.used = False
        for mouse in mouses:
            if mouse.food == 2:
                #make new mouse with a chance to be mutated  
                liveing_mice+= 1   
                if random.randint(0,10) < MUTATION_CHANCE:
                    #this mouse will be mutated
                    trait_to_mutate = random.randint(1,2)
                    #print("MUTATION", len((mouses)))
                    if trait_to_mutate == 1:
                        mouses.append(Mouse((len(mouses)*50)+15,450,10,random.randint(mouse.need_to_reproduce-1,mouse.need_to_reproduce+2),4,0))
                    if trait_to_mutate == 2:
                        mouses.append(Mouse((len(mouses)*50)+15,450,10,mouse.need_to_reproduce,random.randint(2,6),0))
                else:
                    #this mouse wont be mutated5
                    mouse2 = mouse
                    mouses.append(mouse2)
            #if the mouse dose not have 2 food its alredy had its logic applyed
            ntrp.append(mouse.need_to_reproduce)

        day += 1
        days_list.append(day)
        liveing_mice_list.append(liveing_mice)
        best_ntrp_list.append(mode(ntrp))
        if day == SIM_TIME:
            simulating = False
        pygame.display.update()
        pygame.display.flip()
        #clock.tick(FPS)
        print(day)

main()
plt.plot(days_list,liveing_mice_list)
plt.show()
plt.cla()
plt.plot(days_list,best_ntrp_list)
plt.show()
pygame.quit()