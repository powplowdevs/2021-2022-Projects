import random
import math 

# distances moved = 1 x
# And evolution = 1 y

# (x+y) * 1 = iq


x = random.randint(0,23531) #pick number between 0 and population of fairfax virginia
y = 0 #as spaceyon said y=x alsways but ill make it 0 for now 


#REMEMBER X IS DEFINED FIRST AND Y = X

def calculateIQ(x,y):
    
    add = x+y

    ans = add * 1

    return ans



#runs sumuation 100 times 
for i in range(100):
    x = random.randint(0,23531) 
    y = x
    print("The IQ of your rocks is", calculateIQ(x,y))