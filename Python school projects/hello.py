import string
import random
import time
from termcolor import colored

#ment to be intro to python... got carried away as i know this language allready

msg = "hello python world"
print(msg)


def password_cracker(password, speed="slow", show=True):
    possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + '!@#$%^&*()_-+=|\":;>.<,/? ' 

    target = password
    at = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
    an = ''

    running = False

    generations = 0

    while not running:
        print("\n")
        if show:
            if at != target:
                for i in range(len(at)):
                    if matched_index[i] != "0":
                        print(colored(at[i], "green"), end ="")
                    else:
                        print(colored(at[i], "red"), end="")
            else:
                print("\n")
                print(colored(at, "green"))
        an = ''
        running = True
        for i in range(len(target)):
            if at[i] != target[i]:
                running = False
                an += random.choice(possibleCharacters)
            else:
                an += target[i]
                matched_index[i] = "1"
        generations += 1
        at = an
        if speed=="slow":
            time.sleep(.001)
        

    print(colored("Target matched! That took " + str(generations) + " generation(s)","yellow"))


matched_index = []
satc = input("Show attempts to crack (y/n): ")
sof =  input("Program speed (slow or fast): ")
password = input("enter a password: ")

for i in range(len(password)):
    matched_index.append("0")

password_cracker(password,sof, *[satc] if satc == "y" else False)