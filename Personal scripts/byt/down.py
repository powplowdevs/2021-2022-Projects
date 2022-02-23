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

url = "https://www.youtube.com/watch?v=SCGmCo2v25k&t=10s"

my_video = YouTube(url)
my_video = my_video.streams.get_highest_resolution()
my_video.download() 
