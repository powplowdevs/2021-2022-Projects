#Imports for finding urls
import tkinter
import urllib
import json
import urllib.request

#Imports for UI
import tkinter as tk
from tkinter import *
import json, requests
from tkinter.messagebox import showinfo

#Imports to scrape video download, thumbnail, title
from pytube import *
import PIL.Image 
from PIL import ImageTk

#extras
import os
from pytube.helpers import install_proxy
import ast
import io
import time
import threading

#VARS
video_links = []
index = 0
last_title = ""
proxy_use = False
saved_ids = {}

#PROXY
servers = {
  "http": "",
  'https': ""
}

#READ FILE FROM TXT
file = open("savedIDS.txt")
read_content = file.read()
saved_ids = ast.literal_eval(read_content)

#FUCNTIONS
def addProxy(ip, port):
    #proxy settings
    global servers

    servers["http"] = "http://" + ip + ":" + port
    servers["https"] = "https://" + ip + ":" + port

    try:
        install_proxy(servers)
        res = requests.get("https://www.google.com/", proxies=servers)
        showinfo("Proxy", "Sucsessfuly connect to porxy at " + ip + ":" + port)
    
    except:
        showinfo("Proxy", "Sorry but we cant connect to that IP and Port")

def addID(name, cid):
    global saved_ids

    #saveing ids
    saved_ids[name] = cid

    #open file and read
    with open('savedIDS.txt', 'w') as convert_file:
        convert_file.write(json.dumps(saved_ids))

    #save ids in current saved_ids dict
    file = open("savedIDS.txt")
    read_content = file.read()
    saved_ids = ast.literal_eval(read_content)

def get_all_video_in_channel(channel_id):
    global video_links

    #clear video_links
    video_links = []

    #OUR API KEY
    api_key = "---"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    url = first_url
    
    for i in range(1):
        print(url)
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break

def get_video_thumbnail(url):
    #Get thumbnail
    my_video = YouTube(url)
    name = "curtmb.png"

    response = requests.get(my_video.thumbnail_url)
    file = open("curtmb.png", "wb")
    file.write(response.content)
    file.close()

    return name

def get_video_title(url):
    #get title
    my_video = YouTube(url)
    return(my_video.title)

def download_video(url):
    #download video
    my_video = YouTube(url)
    print(my_video)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download() 
    
    #set status
    status.set("Downloaded")

def downlaod_buffer(url):
    #set status
    status.set("Downloading")
    
    download_video(url)

def delete_video():
    global last_title

    #set status
    status.set("Browsing")

    #delete video
    os.remove(last_title.replace(".", "") + ".mp4")

def submit_buffer(name, com, cid):
    global index 
    
    index = 0
    add_videos(name, com, cid)

def add_videos(name, com, cid):
    global main, cthumbnail, index, video_links, last_title, status, saved_ids
    
    #check saved file to grab ids
    if cid in saved_ids.keys():
        cid = saved_ids[cid]
    channel_id = cid
    get_all_video_in_channel(channel_id)

    if com == "n":
        index += 1
        status.set('Browsing')
        add_videos(get_video_thumbnail(video_links[index]), "none", cid)
    elif com == "l":
        index -= 1
        status.set('Browsing')
        add_videos(get_video_thumbnail(video_links[index]), "none", cid)
    else:
        name = get_video_thumbnail(video_links[index]) 
    
    #rezize img
    cthumbnail = PIL.Image.open(name)
    cthumbnail = cthumbnail.resize((535,400), PIL.Image.ANTIALIAS)
    cthumbnail = ImageTk.PhotoImage(cthumbnail)

    #show img
    main.create_image(0,0, anchor=NW, image=cthumbnail) 

    #add title to view
    title = get_video_title(video_links[index])
    vid_title.set(title)
    last_title = title

    
#SET UP UI
app = tk.Tk()
app.geometry("750x500")
app.configure(bg="lightblue")

#UI
#--------------------MAIN UI--------------------

vid_title = StringVar()
vid_title.set('Please enter the channle of of your youtuber below...')

vidLabel = tk.Label(app, textvariable=vid_title, bg="lightblue", font=("Airl", 15))
vidLabel.place(relx=0,rely=0)

ytName = tk.Entry(app, width=70)
ytName.place(relx=.01,rely=0.95)

main = tk.Canvas(app, width=535, height=400)
main.place(relx=0.01,rely=0.06) 

cthumbnail = ImageTk.PhotoImage(file="base.png")
main.create_image(0,0, anchor=NW, image=cthumbnail) 

Submit = tk.Button(app, width=14, text="Submit ID", command= lambda *args: submit_buffer(ytName, "none", ytName.get()))
Submit.place(relx=0.6,rely=0.94)

#--------------------MAIN UI--------------------

#--------------------STATUS--------------------

statlab = tk.Label(app, text="Status:", bg="lightblue", font=("Airl", 15))
statlab.place(relx=.85, rely=.05)

status = StringVar()
status.set('Browsing')

statusLabel = tk.Label(app, textvariable=status, bg="lightblue", font=("Airl", 15))
statusLabel.place(relx=.835, rely=.1)

#--------------------STATUS--------------------

#--------------------CONTROLS--------------------

download = tk.Button(app, text="Download video", command= lambda *args: downlaod_buffer(video_links[index]))
download.place(relx=0.4,rely=0.88)

delete = tk.Button(app, text="Delete video", command= lambda *args: delete_video())
delete.place(relx=0.55,rely=0.88)

next = tk.Button(app, width=14, text="Next", command= lambda *args: add_videos(ytName, "n", ytName.get()))
next.place(relx=0.18,rely=0.88)

last = tk.Button(app, width=14, text="Last", command= lambda *args: add_videos(ytName, "l", ytName.get()))
last.place(relx=0.01,rely=0.88)

#--------------------CONTROLS--------------------

#--------------------PROXY--------------------

proxlab = tk.Label(app, text="Proxy:", bg="lightblue", font=("Airl", 15))
proxlab.place(relx=.85, rely=.2)

ipLabel = tk.Label(app, text="IP:", bg="lightblue")
ipLabel.place(relx=.79, rely=.3)

ip_ent = tk.Entry(app)
ip_ent.place(relx=.815, rely=.3)

portLabel = tk.Label(app, text="Port:", bg="lightblue")
portLabel.place(relx=.775, rely=.4)

port_ent = tk.Entry(app)
port_ent.place(relx=.815, rely=.4)

Submitprox = tk.Button(app, width=14, text="Submit proxy", command= lambda *args: addProxy(ip_ent.get(), port_ent.get()))
Submitprox.place(relx=0.83,rely=0.46)

#--------------------PROXY--------------------

#--------------------SAVED IDS--------------------

savelab = tk.Label(app, text="Save an ID:", bg="lightblue", font=("Airl", 15))
savelab.place(relx=.82, rely=.6)

nameLabel = tk.Label(app, text="Name:", bg="lightblue")
nameLabel.place(relx=.75, rely=.7)

name_ent = tk.Entry(app)
name_ent.place(relx=.815, rely=.7)

idLabel = tk.Label(app, text="ID:", bg="lightblue")
idLabel.place(relx=.775, rely=.8)

id_ent = tk.Entry(app)
id_ent.place(relx=.815, rely=.8)

Submitprox = tk.Button(app, width=14, text="Save ID", command= lambda *args: addID(name_ent.get(), id_ent.get()))
Submitprox.place(relx=0.83,rely=0.87)

showids = tk.Button(app, width=14, text="Show saved ID's", command= lambda: showinfo("Saved ID's", saved_ids))
showids.place(relx=0.83,rely=0.93)

#--------------------SAVED IDS--------------------

app.mainloop()
