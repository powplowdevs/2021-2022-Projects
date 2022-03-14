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

#This enitre explanation is not at a 100% one to one with what is happening in the code as im playing around
#with rules and varibales to see new data outcomes

#IMPORTS
#pygame imports not needed as we no longer have graphcis for this simulation
#from pygame.locals import *
#import pygame
#import pygame.display
import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from statistics import mode

#this var should be left at false
#before it was here the simulation had graphics 
#unfortonetly if you go back into the git history of this file and run the version with graphics
#the data is unacurate and the code is not properly working
#for this point on you will see lots of code under if drawing statements 
#those pices of code used to be responsible to draw the simulation with pygame
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
MUTATION_CHANCE = 3 #chance out of 10 a mouse will be mutated and have new traits when born
SPEED = 0 #wait time between days should be left at 0 for max speed
SIM_TIME = 1000 #how many days the sim will run (should prob be named sim_days)
MAX_DAYS = SIM_TIME/3 #if mice die to time (see mouse_die_to_time var) then this will control how many days they can live
REPPRODUCE_FACTOR = 0.1 #added to the every mouses need_to_reporduce var every day 


simulating = True #if true sim will run if false sim will stop
mouse_amt = 10 #how many mice sim starts with
tree_amt = mouse_amt*2 #how many trees sim starts with
mouses = [] #list of all mice in sim
trees = [] #list of all trees in sim
mouse_die_to_time = True#if true mice will die after liveing for #MAX_DAYS if false mice wont die to time
mouse_can_starve = True #if true mouse will starve if they dont find food if false they wont die to starvation
liveing_mice = mouse_amt #amount of mice alive curently 
day = 0 #the day we are on curently
days_list = [] #just a list of our days for ex: [1,2,3,4,5,6,...]
liveing_mice_list = []#list of the mice that are alive
ntrp = [] #list of evrey mouses need to reproduce at every day (changes every day)
best_ntrp_list = [] #list of the most common need to reproduce for every day the sim ran
mouse_that_reproduced = 0 #amt of mice that reproduced in total
tree_hist = [] #list of tree population for every day the sim ran

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

#returns random tree
def find_tree():
    global trees
    return trees[random.randint(0,len(trees)-1)]

#updates screen for drawing but not used as we dont draw anymore
def tick():
    if drawing:
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

#handels mice dieing to old age or days alive aslo used for darwing so its not used anymore
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

#main sim function
def main():
    #global vars
    global simulating, mouse_amt, tree_amt, mouses, trees, liveing_mice, day, MAX_DAYS, liveing_mice_list, days_list, ntrp, best_ntrp_list,drawing,mouse_that_reproduced, tree_hist, mouse_can_starve

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

    #loop that runs for every day
    while simulating:
        #we use try so that the user can use the KeyboardInterrupt to stop the program and stil get the data up to the last day the loop ran at 
        try:
            if drawing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        simulating = False

            refresh()
            #tick() #not needed as we dont draw
            
            #LOGIC
            #the day has just started and every mouse needs to get a new tree
            #we will run a loop for every single mouse and find it a tree 
            #we make sure that every mouse has food or died trying before we move on
            #start our loop for every mouse
            for mouse in mouses:
                #first of we assume that the mouse is dead and found no food
                mouse_alive = False
                #lets run a loop to check every tree till we find a unused onw
                for tree in trees:
                    if tree.used == False:
                        #we found a tree
                        #add one food to the mouse
                        mouse.food = 1
                        #Make this tree used
                        tree.used = True
                        #let the code know this mouse will live
                        mouse_alive = True
                        break
                if not mouse_alive:
                    #this mouse could not find a tree so that means they where all used so we kill it
                    mouses.remove(mouse)
                    liveing_mice -= 1   

            #now lets implement the logic to reproduce and mutate mice
            for mouse in mouses:
                #the chance the mice will go out looking for more food and try to reproduce
                greed_chance = mouse.need_to_reproduce

                #role the chance
                if random.randint(0,10) < greed_chance:
                    #mouse will try to find more food
                    #chance_to_find_food = mouse.strength insted of this we will give the mouse a random tree for now
                    #pick a random tree
                    tree_in_use = find_tree()
                    #check if the tree has been used
                    if tree_in_use.used == False:
                        #we found more food
                        #add food to mouse
                        mouse.food = 2
                        #add our need_to_reproduce to list
                        ntrp.append(mouse.need_to_reproduce)
                        #make this mouse not want to reproduce as much now as it just did
                        mouse.need_to_reproduce = 0
                        #make this tree used
                        tree_in_use.used = True
                        continue
                        #this mouse may reporduce at the end of the day
                    else:
                        #the mouse did not find the second piece of food and will die if they are allowed to starve
                        if mouse_can_starve:
                            mouses.remove(mouse)
                            liveing_mice -= 1
                        continue
                else:
                    #mouse wont try to find more food at all so we will make it want to reproduce more next time
                    if mouse.need_to_reproduce < 10:
                        mouse.need_to_reproduce += REPPRODUCE_FACTOR

                if drawing:
                    mouse.x = mouse_base[0]
                    mouse.y = mouse_base[1]

                refresh()
                #tick() #not needed as we dont draw

            #the day has ended so lets regenerate the forest and reproduce the mice
                
            #reproduce mice
            for mouse in mouses:
                #check to see if mouse can reproduce
                if mouse.food == 2:
                    #if the mouse can reproduce we make new mouse with a chance to be mutated  
                    #also add to our data vars
                    liveing_mice += 1   
                    mouse_that_reproduced += 1
    
                    #role chance for mouse to be mutated #TO DO! ~ implement stregth into chance of mice muateing...
                    if random.randint(0,10) < MUTATION_CHANCE:
                        #this mouse will be mutated
                        trait_to_mutate = random.randint(1,2)
                        #pick what trait to mutate
                        if trait_to_mutate == 1:
                            mouses.append(Mouse((len(mouses)*50)+15,450,10,random.randint(int(mouse.need_to_reproduce)-1,int(mouse.need_to_reproduce)+2),4,0))
                        if trait_to_mutate == 2:
                           mouses.append(Mouse((len(mouses)*50)+15,450,10,mouse.need_to_reproduce,random.randint(int(mouse.strength)-1,int(mouse.strength)+2),0))
                    else:
                        #this mouse wont be mutated
                        mouse2 = mouse
                        mouses.append(mouse2)
                else:
                    #add more to our data cars
                    ntrp.append(mouse.need_to_reproduce)

                #if the mouse dose not have 2 food its then it had its logic done before this

            #reset all mice    
            for mouse in mouses:
                mouse.food = 0

            #regenerate forest and add or remove trees
            more_trees = random.randint(0,5)#amt of trees we will add or remove
            trees = []#reset tree list
            
            #logic to remove or add trees
            if more_trees > 3:
                tree_amt += more_trees
                if tree_amt > 100:
                    tree_amt = 100
                for i in range(tree_amt):
                    x = (i*50)+15
                    y = 50+random.randint(0,150)
                    trees.append(Tree(x,y))
            else:
                tree_amt -= more_trees
                if tree_amt > 100:
                    tree_amt = 100
                for i in range(tree_amt):
                    x = (i*50)+15
                    y = 50+random.randint(0,150)
                    trees.append(Tree(x,y))

            #add to out data vars and update the day
            day += 1
            days_list.append(day)
            liveing_mice_list.append(liveing_mice)
            tree_hist.append(len(trees))
            best_ntrp_list.append(mode(ntrp))

            #check to see if we should stop
            if day == SIM_TIME:
                simulating = False

            #more drawing stuff we dont use
            if drawing:
                dayt = UI_font.render('Days:' + str(day), True, WHITE)
                population = UI_font.render('Pop:' + str(liveing_mice), True, WHITE)

                display.blit(dayt,(0,0))
                display.blit(population,(0,20))

                pygame.display.update()
                pygame.display.flip()
                clock.tick(FPS)

        #if the user stops the program mid simulation we will still be able to show them the data we collected so far
        except KeyboardInterrupt:
            simulating = False


#run main loop
main()
#plot and display data
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
#pygame.quit()