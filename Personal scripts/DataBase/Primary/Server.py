#IMPORTS
import socket	
import pandas as pd	
import time
import os
import random
import pyfiglet

# next create a socket object
s = socket.socket()		

# reserve a port on your computer in our
port = 12345			

# Next bind to the port
s.bind(('', port))		

# put the socket into listening mode
s.listen(5)	

#data temp storage list
data_list = []

#FILE PATH
file_name = "G:\My Drive\Programing\Personal scripts\DataBase\Primary\identifying_Information.csv"

#vars
incremented_backup = False
Server_title = "P"
c = None
addr = None
connected = False
ontask = False

#heyyyyyyyyyyy implement a sys to thred incremntal backups to the client side sys. 
# make sure to os ping the cliet side to.


def disconect(c):
    # Close the connection with the client
    c.close()

def connect():
    global c, addr
    # Establish connection with client.
    c, addr = s.accept()	
    os.system('cls' if os.name == 'nt' else 'clear')
    connected = True
    show_main_menu()

def send_msg(msg):
    global c
    # Send msg
    c.send(msg.encode())

def show_file_head(name):
    data = pd.read_csv(name)
    print(data.head())
    
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    show_main_menu()

def write_to_file(name, data):
    data = pd.DataFrame(data)
    data.to_csv(name, mode='a', index=False, header=False)

def ask_for_data():
    global data_list, file_name
    temp_list = []
    name = input("Enter your name -> ")
    temp_list.append(name)
    age = input("Enter your age -> ")
    temp_list.append(age)
    gender = input("Enter your gender -> ")
    temp_list.append(gender)
    ID = random.randrange(1,999)
    temp_list.append(ID)
    
    data_list.append(temp_list)
    write_to_file(file_name, data_list)
    
    #data update sys
    if incremented_backup == False:
        try:
            send_msg("E")
            time.sleep(.5)
            send_file()
        except:
            print("\nWARNING: The server could not contact the backup server\n")
            input("")
    else:
        pass

    print("\n YOUR ID IS %d REMEMBER THIS" %ID)

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    show_main_menu()

def send_file():
    global file_name, c
    f = open(file_name,'rb')
    l = f.read(1024)
    while (l):
       c.send(l)
       l = f.read(1024)
    f.close()
    time.sleep(1)
    send_msg("DONESENDINGFILETOCLINET")

def backup():
    send_msg("E")
    send_file()
    input("Server backed up")
    show_main_menu()

def ping():
    os.system('ping 127.0.0.1')
    input("Press enter to continue")

def backup_settings():
    global incremented_backup
    print(f"Current incremented backup setting is {incremented_backup}") 
    switch_setting_command = input("Would you like to switch this setting? (y/n) ")
    if switch_setting_command == "y":
        incremented_backup = not incremented_backup
        print(f"Current incremented backup setting is {incremented_backup}") 
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_main_menu()
    else:
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_main_menu()

def show_main_menu():
    global file_name, s, addr, ontask

    print("\n")
    print("                    DataBase SIM                   ")
    print("\n")
    print(f"            Connected to {addr}                   ")
    print("            Select a number on your keyboard       ")
    print("\n")
    print("                                                   ")
    print("               [1]Create new account               ")
    print("               [2]FailOver                         ")
    print("               [3]Backup data                      ")
    print("               [4]View Data                        ")
    print("               [5]Ping connected server            ")
    print("               [6]Backup settings                  ")
    print("               [7]SHUTDOWN                         ")
    print("\n")

    command = input("Enter a choice ->")

    if command == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        ask_for_data()
    if command == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("function not yet supported")
        show_main_menu()
    if command == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        backup()
    if command == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        show_file_head(file_name)
    if command == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        ping()
    if command == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        backup_settings()
    if command == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        s.close()
        exit()
    elif not ontask:
        print("Invalid input ogboga")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        show_main_menu()
    elif ontask:
        ontask = False
        os.system('cls' if os.name == 'nt' else 'clear')
        show_main_menu()

ascii_banner = pyfiglet.figlet_format("DataBase SIM")
print(ascii_banner)
print("Waiting for connection...")

while not connected:
    try:
        connect()
    except:
        time.sleep(1)






