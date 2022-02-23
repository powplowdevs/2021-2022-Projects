import random

#unsorted numbers
numbers = [5,3,1,7,4,6,2]

#swaps numbers in a list
def swapPositions(list, pos1, pos2):
     
    # popping both the elements from list
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    
    # inserting in each others positions
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 
     
    return list

#sorts a list
def sort(numbers):
    sorted_list = []

    swaped = False

    for i in range(len(numbers)):
        core = numbers[i]
        #take the core number and compare it to the numbers[i]
        #find the first numbers[i] that is greater then the core 
        #then swap the 2 numbers useing the swapPositions function
    

#sort numbers by calling sorting functions
sort(numbers)