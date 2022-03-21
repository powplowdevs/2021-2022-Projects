import PySimpleGUI as sg
import subprocess
import webbrowser
output = ""
amt = 0
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if line.rstrip():
        output += (line.decode().rstrip() + "\n")
msgs = ["Bro why did you run this?", "Its fr an exe file called fun_stuff.exe", "Why did you think this was a good idea?", "I mean your actions need to have consequences..", "Hmm nice programs you haveing running!", "SHOW_LIST", "Would be a shame if i closed all of them...", "3","2","1","BOOM","HAHAHAHA", "I got you!", "jk i would never", "now go on be free and stop running random exes you find online", "...", "you thought you could get off that easy?", "...", "RUN_MANY"]
output = output.replace("Description", "Nice open apps")
for i, value in enumerate(msgs):
    if value == "SHOW_LIST":
        sg.Popup(output,title="R u ok?")
    elif value == "RUN_MANY":
        webbrowser.open('https://cornhub.website/')
        sg.Popup("enjoy (;",title="Ur not ok")
    else:
        sg.Popup(value,title="R u ok?")