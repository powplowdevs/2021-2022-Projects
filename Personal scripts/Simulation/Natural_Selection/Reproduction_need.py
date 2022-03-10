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
from re import T
from pygame.locals import *
import pygame
import pygame.display
import random
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from statistics import mode

drawing = False

if drawing:
    #start pygame
    pygame.init()

    #DISPLAY
    SCREEN_SIZE = (1000,500)
    display = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    #COLORS
    RED = (200,0,0)
    BROWN = (165,42,42)
    WHITE = (255,255,255)

    #FONTS
    main_font = pygame.font.SysFont('arial', 13)
    UI_font = pygame.font.SysFont('arial', 20)


#VARS
FPS = 60
MUTATION_CHANCE = 5
SPEED = 0
SIM_TIME = 1000
MAX_DAYS = SIM_TIME/3
REPPRODUCE_FACTOR = 0.1


simulating = True
mouse_amt = 10
tree_amt = mouse_amt*2
mouses = []
trees = []
mouse_die_to_time = False
liveing_mice = mouse_amt
day = 0
days_list = []
liveing_mice_list = []
ntrp = [] #need to reproduce
best_ntrp_list = []
dead_mouse = False
mouse_that_reproduced = 0
tree_hist = []

if drawing:
    #pygame text
    dayt = UI_font.render('Days:' + str(day), True, WHITE)
    population = UI_font.render('Days:' + str(liveing_mice), True, WHITE)

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
    if drawing:
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

def refresh():
    global liveing_mice

    if drawing:
        display.fill((0,0,0))

        dayt = UI_font.render('Days:' + str(day), True, WHITE)
        population = UI_font.render('Pop:' + str(liveing_mice), True, WHITE)

        display.blit(dayt,(0,0))
        display.blit(population,(0,20))
  
        for mouse in mouses:
            mouse.draw()
            mouse.days_alive += 1
            if mouse.days_alive > MAX_DAYS and mouse_die_to_time:
                mouses.remove(mouse)
                liveing_mice -= 1
        for tree in trees:
            tree.draw()  

def main():
    global simulating, mouse_amt, tree_amt, mouses, trees, liveing_mice, day, MAX_DAYS, liveing_mice_list, days_list, ntrp, best_ntrp_list, dead_mouse,drawing,mouse_that_reproduced, tree_hist


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
        try:
            if drawing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        simulating = False

            refresh()
            tick()
            
            #LOGIC
            mouse_alive = False
            for mouse in mouses:
                mouse_alive = False
                for tree in trees:
                    if tree.used == False:
                        #we found a tree
                        mouse.food = 1
                        tree.used = True
                        mouse_alive = True
                        break
                if not mouse_alive:
                    mouses.remove(mouse)
                    liveing_mice -= 1
                   
            #print("day:", day)
            #for tree in trees:
            #    print(tree.used)
            #print("\n")

            for mouse in mouses:
                greed_chance = mouse.need_to_reproduce

                if random.randint(0,10) < greed_chance:
                    #mouse will try to find more food
                    #chance_to_find_food = mouse.strength insted of this we will give the mouse a random tree
                    #if random.randint(0,10) < chance_to_find_food:
                    tree_in_use = find_tree()
                    if tree_in_use.used == False:
                        #we found more food
                        mouse.food = 2
                        ntrp.append(mouse.need_to_reproduce)
                        mouse.need_to_reproduce = 0
                        tree_in_use.used = True
                        continue
                        #this mouse may reporduce at the end of the day
                    else:
                        #the mouse did not find the second piece of food and will die
                        #mouses.remove(mouse)
                        #liveing_mice -= 1
                        continue
                else:
                    #mouse wont try to find more food
                    if mouse.need_to_reproduce < 10:
                        mouse.need_to_reproduce += REPPRODUCE_FACTOR

                if drawing:
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
                    liveing_mice += 1   
                    mouse_that_reproduced += 1
                    #print("Mutation")
                    if random.randint(0,10) < MUTATION_CHANCE:
                        #this mouse will be mutated
                        trait_to_mutate = random.randint(1,2)
                        #print("MUTATION", len((mouses)))
                        if trait_to_mutate == 1:
                            mouses.append(Mouse((len(mouses)*50)+15,450,10,random.randint(int(mouse.need_to_reproduce)-1,int(mouse.need_to_reproduce)+2),4,0))
                        if trait_to_mutate == 2:
                            mouses.append(Mouse((len(mouses)*50)+15,450,10,mouse.need_to_reproduce,random.randint(2,6),0))
                    else:
                        #this mouse wont be mutated5
                        mouse2 = mouse
                        mouses.append(mouse2)
                else:
                    ntrp.append(mouse.need_to_reproduce)
                #if the mouse dose not have 2 food its alredy had its logic applyed
                
            for mouse in mouses:
                mouse.food = 0

            more_trees = random.randint(0,5)
            trees = []
            if more_trees > 3:
                tree_amt += more_trees
                for i in range(tree_amt):
                    x = (i*50)+15
                    y = 50+random.randint(0,150)
                    trees.append(Tree(x,y))
            else:
                tree_amt -= more_trees
                for i in range(tree_amt):
                    x = (i*50)+15
                    y = 50+random.randint(0,150)
                    trees.append(Tree(x,y))

            day += 1
            days_list.append(day)
            liveing_mice_list.append(liveing_mice)
            tree_hist.append(len(trees))
            best_ntrp_list.append(mode(ntrp))
            
            if day == SIM_TIME:
                simulating = False
            if drawing:
                dayt = UI_font.render('Days:' + str(day), True, WHITE)
                population = UI_font.render('Pop:' + str(liveing_mice), True, WHITE)

                display.blit(dayt,(0,0))
                display.blit(population,(0,20))

                pygame.display.update()
                pygame.display.flip()
                clock.tick(FPS)
        except KeyboardInterrupt:
            simulating = False



main()
print("population:", liveing_mice, "Trees pop:", len(trees), "mouse_list", len(mouses), "days:", day, "\n", mouse_that_reproduced," Reproduced")
plt.plot(days_list,liveing_mice_list)
plt.title("Mouse population over x days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Population", fontsize=10)
plt.show()
plt.cla()
plt.plot(days_list, tree_hist)
plt.title("Tree population over x days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Population", fontsize=10)
plt.show()
plt.cla()
plt.plot(days_list,best_ntrp_list)
plt.title("Mouse most common need to reporduce over x days", fontsize=10)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Need to reproduce", fontsize=10)
plt.show()
pygame.quit()























#find our tree
            
                # for i in range(len(trees)):
                #     tree = trees[i]
                    
                #     if tree.used == False:
                #         tree.used = True
                #         if drawing:
                #         #move our mouse to the tree
                #             mouse_base = (mouse.x,mouse.y)
                #             mouse.x = tree.x
                #             mouse.y = tree.y-15
                #         refresh()
                #         tick()
                #         pygame.time.wait(SPEED)
                #         break
                #     if i >= len(trees)-1:
                #         dead_mouse = True
                #         break
                # if dead_mouse:
                #     dead_mouse = False
                #     mouses.remove(mouse)
                #     liveing_mice -= 1
                
                #     break
                