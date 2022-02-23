#take a input (str) and make a function to do as the input says

#SET UP
tasks = ["add strs", "add ints", "min strs", "min ints", "mul strs", "mul ints", "div strs", "div ints", "sort"]
useVARS = False

print("\n")
print("Welcome to insta code! Enter a command and have a function writen for it just like that.")
print("\n")
print("use the format: a function that will *TASK* *VAR(S)* *OPTINAL OP* then *TASK")
print("\n")
print("TASKS:", tasks)

#SET UP BASE INFO
task = input("You want a function that will: *ENTER A TASK FROM THE LIST ABOVE* ")
useVARSstr = input("Will your function use vars?: yes/no ")

#DEFINE useVARS
if useVARSstr == "yes":
    useVARS = True
else:
    useVARS = False

#HANDLE useVARS = FALSE

#substep: check what out task is
if task != "sort":
    taskOP = task[len(task) - 4:]
    if taskOP == "ints":
        #handle int function
        taskOP = task[:len(task) - 5]
        #find out what we are doing
        if taskOP == "add":
            pass
        elif taskOP == "min":
            pass
        elif taskOP == "mul":
            pass
        elif taskOP == "div":
            pass

    else:
        #handle str function
        taskOP = task[:len(task) - 5]
        #find out what we are doing
        if taskOP == "add":
            pass
        elif taskOP == "min":
            pass
        elif taskOP == "mul":
            pass
        elif taskOP == "div":
            pass

#HANDLE useVARS = TRUE