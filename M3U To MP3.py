#All The Imports:
import shutil
import time
import os
import tkinter as tk
from tkinter import messagebox, ttk
from os import system
import webbrowser
import threading
import re
from tkinter import filedialog
import sys
from SAUIGeo import SAU

sauvernr = "1.03.5"
version = "V1.04.2"
sauver = "SAU" + str(sauvernr)
release_date = "26/04/2026"

incompatible = []
path_start = os.path.expanduser("~")
SAU.check()
var = SAU.start()
print(var)
default = var[0]
button = var[1]
combo = var[2]
cred = var[3]
scale = var[4]
title = var[5]
window_ui = var[6]

def openlink(link):
    link_list = ["https://github.com/Geomedge/M3U-to-Mp3-playlist-converter", "https://forms.office.com/r/x7Le5d2bbE", "https://discord.gg/QN5HrTAYYs"]
    webbrowser.open(link_list[link])

def version_info():
    ver_win = tk.Tk()
    ver_win.minsize(250, 100)
    ver_win.title("Version")
    ver_win.config(background="#333")

    l1 = tk.Label(ver_win, text="Version Information", **title)
    l1.pack(side="top", anchor="nw")

    l2 = tk.Label(ver_win, text=f"{version}", **cred)
    l2.pack(side="top")

    l3 = tk.Label(ver_win, text=f"{sauver}", **cred)
    l3.pack(side="top")

    l4 = tk.Label(ver_win, text=f"Release Date : {release_date}", **cred)
    l4.pack(side="top")


#MP3 Converter app
def converter():
    global l5
    global l8
    root= tk.Tk()
    root.eval('tk::PlaceWindow . centre')
    root.title("MP3 Converter")
    root.configure(background='#333')
    root.minsize(500, 425)

    l1 = tk.Label(root, text='MP3 Converter', **title)
    l1.pack(anchor="nw",side=tk.TOP, padx=2, pady=2)

    #MENU BAR
    menubar = tk.Menu(root, **window_ui)

    #File Settings
    filemenu = tk.Menu(menubar, tearoff=0, **cred)
    filemenu.add_command(label="Exit", command=root.quit)

    #Settings
    settingsmenu = tk.Menu(menubar, tearoff=0, **cred)

#Theme Menu
    thememenu = tk.Menu(settingsmenu, tearoff=0, **cred)
    thememenu.add_command(label="Light", command=lambda:[SAU.set(0)])
    thememenu.add_command(label="Dark", command=lambda:[SAU.set(1)])
    thememenu.add_command(label="Mellow", command=lambda:[SAU.set(2)])
    thememenu.add_command(label="Hacker", command=lambda:[SAU.set(3)])

    #Theme Settings
    settingsmenu.add_cascade(label="Choose Theme (Experimental)", menu=thememenu)

    #Help Menu
    helpmenu = tk.Menu(menubar, tearoff=0, **cred)
    helpmenu.add_command(label="Open Discord Support Page", command=lambda:[openlink(2)])
    helpmenu.add_command(label="Open Github Page", command=lambda:[openlink(0)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Report Bugs", command=lambda:[openlink(1)])
    helpmenu.add_separator()
    helpmenu.add_command(label="Version", command=lambda:[version_info()])
    
    #Menubar Itself
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Settings", menu=settingsmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    

    root.config(menu=menubar)

#LOAD Files
    f1 = tk.Frame(root, bg="#111")

    l2 = tk.Label(f1, text='Select M3U File:', **default)
    l2.pack(side='top', anchor='nw', pady=2)

    def b():
        global file_path
        file_path = filedialog.askopenfilename(filetypes={("M3U Files (.m3u)","*.m3u")})
        print(file_path)
        text = "Selected Directory : " + file_path
        l5.config(text=text)
        messagebox.showinfo("M3U file warning", "Ensure this file is in the correct absolute path.\nCheck Github readme for more info!")
        
    b3 = tk.Button(f1, text='Select File', command=b, **button)
    b3.pack(side='top', anchor='center', pady=2, padx=160)

    l5 = tk.Label(f1, text="NO PATH SELECTED", **cred)
    l5.config(background="#111")
    l5.pack(side='top', anchor='center', pady=2)

    f1.pack(side='top', anchor='center', pady=5)

#SAVE Files
    f2 = tk.Frame(root, bg="#111")

    l7 = tk.Label(f2, text='Select Save Location:', **default)
    l7.pack(side='top', anchor='nw', pady=2)

    def c():
        global save_path
        pathload = path_start + "/Music"
        save_path = filedialog.askdirectory(mustexist=True, initialdir=pathload)
        textl = "Selected Directory : " + save_path
        l8.config(text=textl)
        messagebox.showinfo("Save folder warning", "This folder is to store the final music files not to load them!\nEnsure your folder is empty!")
        
    b4 = tk.Button(f2, text='Select Export Folder', command=c, **button)
    b4.pack(side='top', anchor='center', pady=2, padx=150)

    l8 = tk.Label(f2, text="NO PATH SELECTED", **cred)
    l8.config(background="#111")
    l8.pack(side='top', anchor='center', pady=2)

    f2.pack(side='top', anchor='center', pady=5)


    def convert():
        notcopied = save_path + "/Not-copied.txt"
        file = open(notcopied, "wb")
        file.write("Not Copied \n".encode('utf-8', 'ignore'))
        file.close()
        os.makedirs(save_path, exist_ok=True)
        i = 1
        global errors
        errors = 0
        with open(file_path, 'r', encoding="utf8") as file:
            a = len(file.readlines())
        file.close()
        with open(file_path, 'r', encoding="utf8") as file:
            for line in file:
                i += 1
                c_progress = i/a
                c_progresss = c_progress*100
                c_progresss = round(c_progresss, 1)
                if c_progresss > 100:
                    c_progresss = 100
                progressl.config(text=f"Current Progress : {c_progresss}%")
                progress1.set(c_progresss)
                line = line.strip()
                if line and not line.startswith('#'):
                    directory = os.path.dirname(file_path)
                    if "../" in line:
                        line = line.replace("../", "")
                        line = line.replace("3432-3330/", "") 
                        line = line.replace("890E-2AB0/", "")
                        line = line.replace("/../", "")
                        directory = os.path.dirname(directory)
                    line = directory + "/" + line
                    try:
                        shutil.copy(line, save_path)
                        print(f"Copied {line}")
                    except:
                        errors += 1
                        incompatible.append(line)
                        file = open(notcopied, "ab")
                        line = line + "\n"
                        file.write(line.encode('utf-8', 'ignore'))
                        file.close()
            if errors == 0:
                messagebox.showinfo("Completed Task!", f"Task finished successfully!\nCheck {save_path} for your playlist!")
            else:
                messagebox.showinfo("Completed Task!", f"Errors During Completing Task : {errors}\nPlease ensure M3U file is in the correct path and not corrupted!\nCheck '{save_path}/notcopied.txt'")
                    

    
    b1 = tk.Button(root, text='Convert M3U To Mp3!', command=threading.Thread(target = convert).start, **button)
    b1.pack(side='top', anchor='center', pady=5)

    progress1 = tk.IntVar()
    progress = ttk.Progressbar(variable=progress1)
    progress.pack(anchor="s", side=tk.BOTTOM, fill="x")
    
    credit = tk.Label(root, text="Made By Geomedge", **cred)
    credit.pack(side='left', anchor='sw', padx=5, pady=5)

    progressl = tk.Label(root, text="Progress : 0.0%", **default)
    progressl.config(background='#333')
    progressl.pack(anchor="se",side='right')

    root.mainloop()

converter()