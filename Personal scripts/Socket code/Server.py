import socket
import time

serverData = {
    "IDS": [1,2,3,4,5,6,7,8,9],
    "PASSWORDS": [],
    "USER_INFO": [],
}

conn = None
server_socket = None
host = None
port = None
address = None
point = 0

def handleInput():
    global conn, server_socket, host, port, address, point, serverData
    while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            resdata = conn.recv(1024).decode()
            if not resdata:
                pass
            return resdata

def findID(id):
    global conn, server_socket, host, port, address, point, serverData
    for i in range(len(serverData["IDS"])):
        if int(id) == serverData["IDS"][i]:
            return serverData["IDS"][i]
    return "invalid"

 

def serverStart():
    global conn, server_socket, host, port, address, point, serverData
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))#, "IP:", socket.gethostbyname(host))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        resdata = conn.recv(1024).decode()
        if not resdata:
            # if data is not received break
            break
        data = str(resdata)

        #IF THEY WANT TO LOG IN
        if data == "1":
            data = ' Enter ID: '
            conn.send(data.encode())
            data = handleInput()
      
            point = findID(data)

            if point != "invalid":
                li = serverData["IDS"]
                data = ' your id is: ' + str(point)
                conn.send(data.encode())
            else:
                data = ' your id is: INVALID'
                conn.send(data.encode())      

        #IF THEY WANT THERE NAME
        #this boring and i allrady made smth like this im done





    conn.close()  # close the connection


if __name__ == '__main__':
    serverStart()
