# Import socket module
import socket			
import time
import os
import pandas as pd
import threading

# Create a socket object
s = socket.socket()				

#VARs
IP = '127.0.0.1'
PORT = 12345

#FILE PATH
file_name = 'G:\My Drive\Programing\Personal scripts\DataBase\Secondary\Data_Backup.csv'

#vars
incremented_backup = False
Server_title = "S"
connected = False
ontask = False
trys = 5

def res_file():
    global file_name
    with open(file_name, 'wb') as f:
        print ('file opened')
        while True:
            data = s.recv(1024)
            print('data=%s', (data))
            if data.decode() == "DONESENDINGFILETOCLINET":
                break
            # write data to a file
            f.write(data)
        f.close()
        print("Server file backup done...")
        handle_res()

def handle_res():
    # receive data from the server and decoding to get the string.
    res = s.recv(1024).decode()

    #LOGIC
    if res == "E":
        print("Server file backup running...")
        res_file()

def closeCon():
    # close the connection
    connected = False
    s.close()	
    show_main_menu()

def connect():
    global trys, connected
    try:
        # connect to the server on local computer
        s.connect((IP, PORT))
        connected = True
        handle_res_t = threading.Thread(target=handle_res)
        handle_res_t.start()
        show_main_menu()
    except:
        if trys > 0:
            trys -= 1
            print(f"Connection atempt failed\nTRYS LEFT: {trys}")
            connect()
        else:
            trys = 5
            print(f"Connection atempt failed, Connection atempts {trys}")
            input("")
            os.system('cls' if os.name == 'nt' else 'clear')
            show_main_menu()

def connectGlobal():
    global IP, PORT

    IP = input("Enter IP to connect to")
    PORT = input("Enter port to connect to")

    # connect to the server on global computer
    s.connect((IP, PORT))
    handle_res()
	
def show_file_head(name):
    data = pd.read_csv(name)
    print(data.head())
    
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    show_main_menu()

def write_to_file(name, data):
    data = pd.DataFrame(data)
    data.to_csv(name, mode='a', index=False, header=False)

def ping():
    os.system(f'ping {IP}')
    input("Press enter to continue")

def show_main_menu():
    global file_name, s, ontask, connected
    
    print("\n")
    print("                    DataBase SIM                   ")
    print("\n")
    print(f"            Connection status: {connected}        ")
    print("\n")
    print("            Select a number on your keyboard       ")
    print("\n")
    print("                                                   ")
    print("               [1]Connect                          ")
    print("               [2]FailOver                         ")
    print("               [3]Backup data                      ")
    print("               [4]View Data                        ")
    print("               [5]Ping connected server            ")
    print("               [6]SHUTDOWN                         ")
    print("\n")

    command = input("Enter a choice ->")

    if command == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        ontask = True
        connect()
    if command == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("function not yet supported")
        show_main_menu()
    if command == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        if Server_title == "P":
            ontask = True
            pass
        else:
            print("The server must be failed over to do this")
            show_main_menu()
        
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
        closeCon()
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

show_main_menu()
