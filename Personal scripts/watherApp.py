import tkinter as tk
from tkinter import *
import json, requests
import threading
import time
from tkinter.messagebox import showinfo

canCall = True
clock = 20
calls = 0

def callClock(max):
    global canCall, calls
    t = 0

    while True:
        if t != max:
            time.sleep(1)
            t += 1
        elif t == max and canCall == False:
            t = 0
            calls = 0
            canCall = True
       
          
def getData(CITY):
    global canCall, calls

    #add to out users calls withing the call time cap
    calls += 1

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "520d977f2380b200471c25d531fdfaeb"

    #our url to send to
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    
    if canCall:
        # HTTP request
        response = requests.get(URL)

    try:
        responsesc = response.status_code
    except:
        responsesc = 400

    # checking the status code of the request
    if responsesc == 200:
        #Stop us from calling
        canCall = False
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']

        #set out city name
        City.set(CITY)

        #add the citys name to a list of all citys 

        History.config(state=NORMAL)
        History.insert("1.0", CITY + "\n")
        History.config(state=DISABLED)
        History.tag_add("right", "1.0", "end")
        
        #adds info to main textbox

        InfoBox.config(state=NORMAL)
        InfoBox.delete("1.0", END)
        InfoBox.insert("end", (f"{CITY:-^30}\n"))
        InfoBox.insert("end", (f"Temperature: {round((temperature - 273.15) * (9/5) + 32 )}\n"))
        InfoBox.insert("end", (f"Humidity: {humidity}\n"))
        InfoBox.insert("end", (f"Pressure: {pressure}\n"))
        InfoBox.insert("end", (f"Weather Report: {report[0]['description']}\n"))
        InfoBox.tag_add("right", "1.0", "end")
        InfoBox.config(state=DISABLED)

        #add city info to our info box with all previous citys
        CityUpdate.config(state=NORMAL)
        CityUpdate.insert("1.0", (f"Weather Report: {report[0]['description']}\n"))
        CityUpdate.insert("1.0", (f"Pressure: {pressure}\n"))
        CityUpdate.insert("1.0", (f"Humidity: {humidity}\n"))
        CityUpdate.insert("1.0", (f"Temperature: {round((temperature - 273.15) * (9/5) + 32 )}\n"))
        CityUpdate.insert("1.0", (f"{CITY:-^30}\n"))
        CityUpdate.tag_add("right", "1.0", "end")
        CityUpdate.config(state=DISABLED)

        
    else:
        #they are eather calling for new data to fast or they are submiting a invalid city name to we let them know
        if calls > 3 and not canCall:
            showinfo("Window", ("Hey, slow down! You can only call once every", clock, "seconds"))
        elif canCall:
            showinfo("Window", "Invalid city name")
    
app = tk.Tk()
app.geometry("550x500")
app.configure(bg="lightblue")

City = StringVar()
City.set('Please enter the name of your city below...')

CityName = tk.Entry(app, width=70)
CityName.place(relx=.01,rely=0.95)

Submit = tk.Button(app, width=14, text="Submit", command= lambda *args: getData(CityName.get()))
Submit.place(relx=0.79,rely=0.94)

History = Text(app, width=10, height=34, font=("Terminal", 10))
History.config(state=DISABLED)
History.place(relx=0.815,rely=0.1)

InfoBox = Text(app, width=50, height=5, bg="blue")
InfoBox.config(state=DISABLED)
InfoBox.place(relx=0.04,rely=0.1)

CityUpdate = Text(app, width=50, height=18, bg="#32BEC3")
CityUpdate.config(state=DISABLED)
CityUpdate.place(relx=0.04,rely=0.325)

CityLabel = tk.Label(app, textvariable=City, bg="lightblue", font=("Airl", 20))
CityLabel.place(relx=0,rely=0)

CallingClock = threading.Thread(target=callClock, args=(clock,))
CallingClock.start()

app.mainloop()