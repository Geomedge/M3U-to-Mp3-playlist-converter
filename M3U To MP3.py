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
#Menu GUI

text = """V1.0:
- Released Program

Thank You For Supporting My Program!
"""
incompatible = []

#Saves Me The hassle of changing the version number each time separately!
Version = "V1.01"
last_update = 'Last Updated : 15/03/2025'
#Empty Variables
path_list = []
#This just checks if files exists and if not - recreates them
path_start = os.path.expanduser("~")
path_mid = r"\Documents\Geomedge.inc\MP3 Converter"
existing1 = path_start + r"\Documents\Geomedge.inc"
existing = os.path.exists(existing1)
if existing == True:
    print("Pass Geomedge.Inc Folder")
else:
    os.mkdir(existing1)

#This if statement is different!
file = path_start + path_mid
existing = os.path.exists(file)
if existing == True:
    print("Pass", file)
else:
    os.mkdir(file)
path_end = [r"\Theme.txt",r"\Changelog.txt",r"\Font.txt",r"\FontSize.txt",r"\FontEdit.txt"]
for i in range (len(path_end)):
    path = path_start + path_mid + path_end[i]
    path_list.append(path)

#New User Data Generation:
def reset_file(i):
    print("Rebuilding", path_list[i])
    myfile=open(path_list[i], "w")
    match i:
        case 0:
            myfile.write("pink,black,brown,white")
        case 1:
            myfile.write(text)
        case 2:
            myfile.write("none,none,helvetica,helvetica")
        case 3:
            myfile.write("18,12,9,9")
        case 4:
            myfile.write("bold,bold,bold,none")
        case _:
            master = tk.Tk()
            master.withdraw()
            messagebox.showerror("Error - Can't Launch Program", "Error Code 1 - Can't load file!")
            master.destroy()
            quit()
    myfile.close()

#Reading Data For Global Variables
##Verify Files Exist
for i in range(len(path_end)):
    existing = os.path.exists(path_list[i])
    if existing == True:
        print("Pass", path_list[i])
    else:
        print("Fail", path_list[i])
        reset_file(i)
#Ended Checks!

#This just splits the strings - Themes, fonts, font styles etc etc
def Convert(string):
            li = list(string.split(","))
            return li


#Reading + Assigning all the themes accordingly!
def changes():
##Start Reading
    global theme1
    global theme2
    global theme3
    global theme4
    global Title
    global Subtext
    global Button_Txt
    global Credits_Txt
    global changes2
    for i in range(len(path_end)):
        myfile = open(path_list[i], "r")
        a = myfile.read()
        myfile.close()

        match i:
            case 0: #Themes
                theme = Convert(a)
                theme1 = theme[0]
                theme2 = theme[1]
                theme3 = theme[2]
                theme4 = theme[3]
            case 1: #Unused! - This is used for a different program
                changes2 = a
            case 2: #Font
                font1 = Convert(a)
                font11 = font1[0]
                font12 = font1[1]
                font13 = font1[2]
                font14 = font1[3]
            case 3: #Size
                font2 = Convert(a)
                font21 = font2[0]
                font22 = font2[1]
                font23 = font2[2]
                font24 = font2[3]
            case 4: #Extras
                font3 = Convert(a)
                font31 = font3[0]
                font32 = font3[1]
                font33 = font3[2]
                font34 = font3[3]

    Titl = font11 + " " + font21
    Subte = font12 + " " + font22
    Butto = font13 + " " + font23
    Credi = font14 + " " + font24

    #Title
    if font31 == "none":
        Title = Titl
    else:
        Title = Titl + " " + font31
    #SubText
    if font32 == "none":
        Subtext = Subte
    else:
        Subtext = Subte + " " + font32
    #Button Text
    if font33 == "none":
        Button_Txt = Butto
    else:
        Button_Txt = Butto + " " + font33
    #Credits Text
    if font34 == "none":
        Credits_Txt = Credi
    else:
        Credits_Txt = Credi + " " + font34

#Calls the function to assign starter theme
changes()

#Skip to the bottom!

#Pre Set Themes!
def message_1(theme):
    string = "Your theme was changed to " + theme + "."
    print("Users Theme Changed To : ", string)
    changes()

#light mode
def light():
    myfile=open(path_list[0], "w")
    myfile.write("pink,black,brown,white")
    myfile.close()
    message_1("Light Theme")

#dark mode
def dark():
    myfile=open(path_list[0], "w")
    myfile.write("#23272a,#7289da,#99aab5,#36393f")
    myfile.close()
    message_1("Dark Theme")

#Hacker mode
def hacker():
    myfile=open(path_list[0], "w")
    myfile.write("#000000,#20C20E,#000000,#20C20E")
    myfile.close()
    message_1("Hacker Theme")

#Mellow
def mellow():
    myfile=open(path_list[0], "w")
    myfile.write("#fceea7,#000000,#fceea7,#000000")
    myfile.close()
    message_1("Mellow Theme")

def exit_app():
    quit()

#Uninstall
def delete():
    for i in range(len[path_list]):
        os.remove(path_list[i])
    os.remove(os.getcwd())
    print("done")


#Confirmation For Uninstalling
def confirm():
    message1 = "Are you sure you want to delete MP3 Converter " + Version + "?"
    command = messagebox.askquestion(title="Are you sure?", message=message1)
    if command == "yes":
        delete()
    elif command == "no":
        settings()


def bug_report():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Bug Fix")
    canvas1 = tk.Canvas(confirm, width=500, height=200, relief='raised', bg = theme1)
    canvas1.pack()

    def callback(url):
        webbrowser.open_new(url)

    title5 = tk.Label(confirm, text="Discord Server", fg="blue", cursor="hand2")
    canvas1.create_window(350, 75, window=title5)
    title6 = tk.Label(confirm, text="Bug Report Form", fg="blue", cursor="hand2")
    canvas1.create_window(150, 75, window=title6)
    canvas1.pack()
    title5.bind("<Button-1>", lambda e: callback("https://discord.gg/QN5HrTAYYs"))
    title6.bind("<Button-1>", lambda e: callback("https://forms.office.com/r/x7Le5d2bbE"))
    
    title = tk.Label(confirm, text='Report Bugs', bg = theme1, fg = theme2)
    title.config(font=(Title))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Select any link below to get started.', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[confirm.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 175, window=button7)


def changelog():
    changelog = tk.Tk()
    changelog.eval('tk::PlaceWindow . centre')
    changelog.title("Changelog")
    canvas1 = tk.Canvas(changelog, width=500, height=400, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(changelog, text='Changelog', bg = theme1, fg = theme2, font=('none 18 bold'))
    canvas1.create_window(250, 25, window=title)



    text_widget = tk.Text(changelog, wrap='word', height=20, width=80,bg = theme1, fg = theme2, font =('segoe UI', 9), borderwidth=0)
    canvas1.create_window(250,200, window = text_widget)
    sample_text = changes2
    text_widget.insert(tk.END, sample_text)
    text_widget.config(state=tk.DISABLED)

    scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    canvas1.create_window(430, 200, window=scrollbar, height=300)

    l2 = tk.Label(changelog, text=last_update, bg = theme1, fg = theme2)
    canvas1.create_window(430, 385, window=l2)
    
    button7 = tk.Button(changelog, text='Back', command=lambda:[changelog.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 385, window=button7)


#Customisation

def font_set3():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Font Extras (Itallics, Bold, etc)', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Extras', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Extras', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Extras', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font Extras', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    

    def get2(var1, var2, var3, var4):
        new = [var1,var2,var3,var4]
        print(new)
        new_list = []
        for i in range(len(new)):
            print(new[i])
            x = new[i].get().lower()
            if x == "none" or x == "bold" or x == "italics":
                new_list.append(x)
            else:  
                print("Invalid Choice")
                string = f"Invalid Choice : {x}, Is not a valid option!"
                messagebox.showerror("Error!", string)
                return False
                
        return new_list




    def theme_switch4():
        new_list = get2(entry5,entry6,entry7,entry8)
        if new_list == False:
            print("Failed!")
            messagebox.showinfo("Didn't Make Changes!", "Font Edit Failed!")
        else:
            myfile=open(path_list[4], "w")
            string = ",".join(new_list) + ","
            myfile.write(string)
            myfile.close()
            messagebox.showinfo("Done!", "Changes To Font Made!")
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch4(), confirm.destroy(), font_set3()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def font_set2():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Font Size', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Size', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Size', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Size', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font Size', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    
    def theme_switch3():
        x5 = entry5.get().lower()
        x6 = entry6.get().lower()
        x7 = entry7.get().lower()
        x8 = entry8.get().lower()
        try:
            x = int(x5)
            x = int(x6)
            x = int(x7)
            x = int(x8)
            myfile=open(path_list[3], "w")
            string = x5 + "," + x6 + "," + x7 + "," + x8 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            confirm.destroy()
            font_set3()
        except:
            messagebox.showerror("Error", "Invalid Characters - Number Input!")

        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch3()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def change_font():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Font Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Change Fonts (Write None If Default Font)', bg = theme1, fg = theme2)
    title.config(font=('none 12 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Title Font (Example : Helvetica)', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Text Font', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Button Font', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Every Other Font', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext)
    canvas1.create_window(250, 225, window=entry8)
    
    def test(x9,x10,x11,x12):
            try:
                test_fonts = [x9,x10,x11,x12]
                print(test_fonts)
                confirm = tk.Tk()
                confirm.title("Test")
                canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
                canvas1.pack()

                title = tk.Label(confirm, text='test')
                for i in range(4):
                    font_test = test_fonts[i] + " 12 bold"
                    print(test_fonts[i])
                    title.config(font=(font_test))
                    canvas1.create_window(250, 25, window=title)
                confirm.withdraw()
                return True
            except:
                confirm.withdraw()
                messagebox.showerror("INVALID FONT!", "Invalid font selected!")
                return False

    def theme_switch2():
        x9 = entry5.get().lower()
        x10 = entry6.get().lower()
        x11 = entry7.get().lower()
        x12 = entry8.get().lower()
        if test(x9,x10,x11,x12) == True:
            myfile=open(path_list[2], "w")
            string = x9 + "," + x10 + "," + x11 + "," + x12 + ","
            myfile.write(string)
            myfile.close()
            messagebox.showinfo(title="Done!", message="Successfully Changed Font!")
            print("Done!")
            font_set2()
        else:
            change_font()
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch2(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[settings(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)


def basic_colour_settings():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Colour Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Colour Settings', bg = theme1, fg = theme2)
    title.config(font=('none 18 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Background colour', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(125, 50, window=title1)

    selected_option1 = tk.StringVar()
    selected_option2 = tk.StringVar()
    selected_option3 = tk.StringVar()
    selected_option4 = tk.StringVar()
    options = ["Black","White","Red","Orange","Pink","Blue","Magenta","Yellow","Cyan","Green"]
    menu_len = len(max(options, key=len)) + 1
    entry5 = tk.OptionMenu(confirm, selected_option1, *options)
    entry5.config(width = menu_len)
    canvas1.create_window(125, 75, window=entry5)

    title2 = tk.Label(confirm, text='Colour of the text', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(375, 50, window=title2)

    entry6 = tk.OptionMenu(confirm, selected_option2, *options)
    entry6.config(width = menu_len)
    canvas1.create_window(375, 75, window=entry6)

    title3 = tk.Label(confirm, text='Background of buttons', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(375, 125, window=title3)

    entry7 = tk.OptionMenu(confirm, selected_option3, *options)
    entry7.config(width = menu_len)
    canvas1.create_window(375, 150, window=entry7)

    title4 = tk.Label(confirm, text='Text Colour of buttons', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(125, 125, window=title4)

    entry8 = tk.OptionMenu(confirm, selected_option4, *options)
    entry8.config(width = menu_len)
    canvas1.create_window(125, 150, window=entry8)




    def theme_switch():
        x13 = selected_option1.get().lower()
        x14 = selected_option2.get().lower()
        x15 = selected_option3.get().lower()
        x16 = selected_option4.get().lower()
        if x13 == "" or x14 == "" or x15 == "" or x16 == "":
            messagebox.showerror("Can't apply changes!", "Please Ensure All Boxes Have Been Selected!")
        else:
            myfile=open(path_list[0], "w")
            string = x13 + "," + x14 + "," + x15 + "," + x16 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            changes()
            messagebox.showinfo("Done!", "Changes Applied")
            quit
        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch(), confirm.destroy(), basic_colour_settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 265, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[colour_settings_menu(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def colour_settings():
    confirm = tk.Tk()
    confirm.eval('tk::PlaceWindow . centre')
    confirm.title("Colour Settings")
    canvas1 = tk.Canvas(confirm, width=500, height=300, relief='raised', bg = theme1)
    canvas1.pack()

    title = tk.Label(confirm, text='Enter Desired Colours!', bg = theme1, fg = theme2)
    title.config(font=('none 10 bold'))
    canvas1.create_window(250, 25, window=title)

    title1 = tk.Label(confirm, text='Input Theme 1 (Background of window)', bg = theme1, fg = theme2)
    title1.config(font=('none 9 bold'))
    canvas1.create_window(250, 50, window=title1)

    entry5 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 75, window=entry5)

    title2 = tk.Label(confirm, text='Input Theme 2 (Text Colour of window)', bg = theme1, fg = theme2)
    title2.config(font=('none 9 bold'))
    canvas1.create_window(250, 100, window=title2)

    entry6 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 125, window=entry6)

    title3 = tk.Label(confirm, text='Input Theme 3 (Background of buttons)', bg = theme1, fg = theme2)
    title3.config(font=('none 9 bold'))
    canvas1.create_window(250, 150, window=title3)

    entry7 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 175, window=entry7)

    title4 = tk.Label(confirm, text='Input Theme 4 (Text Colour of buttons)', bg = theme1, fg = theme2)
    title4.config(font=('none 9 bold'))
    canvas1.create_window(250, 200, window=title4)

    entry8 = tk.Entry(confirm, font=Subtext, width=25)
    canvas1.create_window(250, 225, window=entry8)

    def Colour_Check(test):
        rex = re.compile("^#{1}[0-9]{6}$")
        if rex.match(test):
            return True
        else:
            colour_list = ["black","white","red","orange","pink","blue","magenta","yellow","cyan","green"]
            for i in range(len(colour_list)):
                if colour_list[i] == test:
                    return True
        return False



    def theme_switch():
        #Gets All The Entry Boxes
        x13 = entry5.get().lower()
        x14 = entry6.get().lower()
        x15 = entry7.get().lower()
        x16 = entry8.get().lower()
        #Colour_Check checks for any invalid colours!
        if Colour_Check(x13) == False or Colour_Check(x14) == False or Colour_Check(x15) == False or Colour_Check(x16) == False:
            messagebox.showerror("INVALID COLOUR!", "Invalid colour selected!") 
        else:
            myfile=open(path_list[0], "w")
            string = x13 + "," + x14 + "," + x15 + "," + x16 + ","
            myfile.write(string)
            myfile.close()
            print("Done!")
            changes()
            messagebox.showinfo("Done!", "Changes Made!")

        

    button1 = tk.Button(confirm, text='Change!', command=lambda:[theme_switch(), confirm.destroy(), colour_settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(250, 260, window=button1)

    button7 = tk.Button(confirm, text='Back', command=lambda:[colour_settings_menu(), confirm.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas1.create_window(50, 275, window=button7)

def colour_settings_menu():
    colour = tk.Tk()
    colour.eval('tk::PlaceWindow . centre')
    colour.title("Colour Settings")
    colour.configure(bg = theme1)

    h1 = tk.Label(colour, text='Settings', bg = theme1, fg = theme2)
    h1.config(font=(Title))
    h1.pack()

    frame = tk.Frame(colour, bg=theme1)

    b1 = tk.Button(frame, text='Preset Colour Settings', command=lambda:[basic_colour_settings(), colour.destroy()], bg=theme3, fg= theme4, font=(Button_Txt), width=25, height=1)
    b1.grid(row=0, column=0, padx=5, pady=2)

    b2 = tk.Button(frame, text='Advanced Colour Settings', command=lambda:[colour_settings(), colour.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b2.grid(row=0, column=1, padx=5, pady=2)
    frame.pack(side='top', anchor='center')

    b3 = tk.Button(colour, text='Back', command=lambda:[colour.destroy(), settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    b3.pack(anchor="sw",side=tk.LEFT, padx=5, pady=10)


#Themes
def theme():
    #Fixed
    theme_app = tk.Tk()
    theme_app.title("Theme Settings")
    theme_app.eval('tk::PlaceWindow . centre')
    theme_app.configure(background=theme1)

    h1 = tk.Label(theme_app, text='Select Your Theme', bg = theme1, fg = theme2)
    h1.config(font=(Title))
    h1.pack()
    
    frame = tk.Frame(theme_app, bg=theme1)

    b1 = tk.Button(frame, text='Light Theme', command=lambda:[light(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b1.grid(row=0, column=0, padx=5, pady=2)

    b2 = tk.Button(frame, text='Dark Theme', command=lambda:[dark(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b2.grid(row=0, column=1, padx=5, pady=2)

    b3 = tk.Button(frame, text='Hacker Theme', command=lambda:[hacker(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b3.grid(row=1, column=0, padx=5, pady=2)

    b4 = tk.Button(frame, text='Mellow Theme', command=lambda:[mellow(), theme_app.destroy(), theme()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b4.grid(row=1, column=1, padx=5, pady=2)
    frame.pack(side='top', anchor='center')

    b5 = tk.Button(theme_app, text='Back', command=lambda:[settings(), theme_app.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    b5.pack(anchor="sw",side=tk.LEFT, padx=5, pady=10)


#MP3 Converter app
def converter():
    global l5
    global l8
    root= tk.Tk()
    root.eval('tk::PlaceWindow . centre')
    root.title("MP3 Converter")
    root.configure(bg = theme1)
    root.minsize(600, 500)

    l1 = tk.Label(root, text='MP3 Converter', bg = theme1, fg = theme2)
    l1.config(font=("Segoe UI", "18", "bold"))
    l1.pack(anchor="nw",side=tk.TOP, padx=5, pady=5)


#LOAD Files

    l2 = tk.Label(root, text='Select M3U File:', font="none 12 bold", bg = theme1, fg = theme2)
    l2.pack(side='top', anchor='center', pady=5)

    def b():
        global file_path
        file_path = filedialog.askopenfilename(filetypes={("M3U Files (.m3u)","*.m3u")})
        print(file_path)
        text = "Selected Directory" + file_path
        l5.config(text=text)
        
    b3 = tk.Button(root, text='Select File', command=b, bg = theme3, fg = theme4, font=('helvetica', 9, 'bold'), width=25)
    b3.pack(side='top', anchor='center', pady=5)

    l5 = tk.Label(root, text="NO PATH SELECTED", font=("Segoe UI", "9"), bg = theme1, fg = theme2)
    l5.pack(side='top', anchor='center', pady=5)
    

#SAVE Files

    l7 = tk.Label(root, text='Select Where To Save MP3 Files:', font="none 12 bold", bg = theme1, fg = theme2)
    l7.pack(side='top', anchor='center', pady=5)

    def c():
        global save_path
        pathload = path_start + "/Music"
        save_path = filedialog.askdirectory(mustexist=True, initialdir=pathload)
        textl = "Selected Directory : " + save_path
        l8.config(text=textl)
        
    b4 = tk.Button(root, text='Select Folder', command=c, bg = theme3, fg = theme4, font=('helvetica', 9, 'bold'), width=25)
    b4.pack(side='top', anchor='center', pady=5)

    l8 = tk.Label(root, text="NO PATH SELECTED", font=("Segoe UI", "9"), bg = theme1, fg = theme2)
    l8.pack(side='top', anchor='center', pady=5)



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
            messagebox.showinfo("Completed Task!", f"Errors During Completing Task : {errors}")
                    

    
    b1 = tk.Button(root, text='Convert M3U To Mp3!', command=threading.Thread(target = convert).start, bg = theme3, fg = theme4, font=('helvetica', 9, 'bold'))
    b1.pack(side='top', anchor='center', pady=20)

    progress1 = tk.IntVar()
    progress = ttk.Progressbar(variable=progress1)
    progress.pack(anchor="s", side=tk.BOTTOM, fill="x")
    
    progressl = tk.Label(root, text="Progress : 0.0%", bg = theme1, fg = theme2, font=('Segoe UI', 12))
    progressl.pack(anchor="sw",side=tk.BOTTOM)

    b7 = tk.Button(root, text='Back', command=lambda:[root.destroy(), menu()], bg=theme3, fg=theme4, font=('helvetica', 9, 'bold'), width=10, height=1)
    b7.pack(anchor="sw", side=tk.LEFT, padx=5, pady=10)

    l2 = tk.Label(root, text='Made By Geomedge', bg = theme1, fg = theme2)
    l2.config(font=('helvetica', 9))
    l2.pack(anchor="se",side=tk.RIGHT, padx=5, pady=10)

    root.mainloop()

    


#settings
def settings():
    #Done
    setting = tk.Tk()
    setting.eval('tk::PlaceWindow . centre')
    setting.title("Settings")
    setting.configure(bg = theme1)

    h1 = tk.Label(setting, text='Settings', bg = theme1, fg = theme2)
    h1.config(font=(Title))
    h1.pack(pady=2)

    frame = tk.Frame(setting, bg=theme1)

    b1 = tk.Button(frame, text='Change Fonts', command=lambda:[change_font(), setting.destroy()], bg=theme3, fg= theme4, font=(Button_Txt), width=25, height=1)
    b1.grid(row=0, column=0, padx=5, pady=2)

    b2 = tk.Button(frame, text='Change Theme', command=lambda:[theme(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b2.grid(row=0, column=1, padx=5, pady=2)

    b3 = tk.Button(frame, text='Uninstall Python Scripts', command=lambda:[confirm(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b3.grid(row=1, column=0, padx=5, pady=2)

    b4 = tk.Button(frame, text='Colour settings', command=lambda:[colour_settings_menu(), setting.destroy()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b4.grid(row=1, column=1, padx=5, pady=2)
    frame.pack(side='top', anchor='center')

    b5 = tk.Button(setting, text='Back', command=lambda:[setting.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    b5.pack(anchor="sw",side=tk.LEFT, padx=5, pady=10)


#Credits
def credit():
    credit = tk.Tk()
    credit.eval('tk::PlaceWindow . centre')
    credit.eval('tk::PlaceWindow . centre')
    credit.configure(bg = theme1)
    credit.title("Credits")
    canvas2 = tk.Canvas(credit, width=300, height=100, relief='raised', bg = theme1, bd=0, highlightthickness=0)
    canvas2.pack()

    label1 = tk.Label(credit, text='Made By Geomedge', bg = theme1, fg = theme2)
    label1.config(font=('helvetica', 12, 'bold'))
    canvas2.create_window(150, 25, window=label1)

    label1 = tk.Label(credit, text='Thank you for using the app!', bg = theme1, fg = theme2)
    label1.config(font=('helvetica', 12, 'bold'))
    canvas2.create_window(150, 50, window=label1)
    
    button2 = tk.Button(credit, text='Back', command=lambda:[credit.destroy(), menu()], bg=theme3, fg=theme4, font=(Button_Txt), width=10, height=1)
    canvas2.create_window(50, 85, window=button2)

#Menu
def menu():
    #Finished Menu
    menu = tk.Tk()
    menu.eval('tk::PlaceWindow . centre')
    menu.configure(bg = theme1)
    menu.title("MP3 Converter")
    menu.minsize(500, 200)

    l1 = tk.Label(menu, text='MP3 Converter By Geomedge', bg = theme1, fg = theme2)
    l1.config(font=("Segoe UI", "18", "bold"))
    l1.pack()

    frame = tk.Frame(menu, bg=theme1)

    b1 = tk.Button(frame, text='MP3 Converter', command=lambda:[menu.destroy(), converter()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b1.grid(row=0, column=0, padx=5, pady=2)

    b2 = tk.Button(frame, text='Settings', command=lambda:[menu.destroy(), settings()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b2.grid(row=0, column=1, padx=5, pady=2)

    b3 = tk.Button(frame, text='Changelog', command=lambda:[menu.destroy(), changelog()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b3.grid(row=1, column=0, padx=5, pady=2)

    b4 = tk.Button(frame, text='Report Bug', command=lambda:[menu.destroy(), bug_report()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b4.grid(row=1, column=1, padx=5, pady=2)
    
    b5 = tk.Button(frame, text='Credits', command=lambda:[menu.destroy(), credit()], bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b5.grid(row=2, column=0, padx=5, pady=2)

    b6 = tk.Button(frame, text='Quit', command=exit_app, bg=theme3, fg=theme4, font=(Button_Txt), width=25, height=1)
    b6.grid(row=2, column=1, padx=5, pady=2)
    frame.pack(side='top', anchor='center')

    l2 = tk.Label(menu, text='Made By Geomedge', bg = theme1, fg = theme2)
    l2.config(font=(Credits_Txt))
    l2.pack(anchor="se",side=tk.RIGHT, padx=5, pady=10)

    l3 = tk.Label(menu, text= Version, bg = theme1, fg = theme2)
    l3.config(font=(Credits_Txt))
    l3.pack(anchor="sw",side=tk.LEFT, padx=5, pady=10)
    menu.mainloop()



#Simple Null / Invalid Values Catcher - Resets all preset values if app cannot load (Bit overkill but I can't think of anything else)
try:
    try:
        menu()
    except:
        menu.withdraw()
        for i in range(5):
            reset_file(i)
        #Calls the reset_file function which restarts all files to original state set by me / any other dev
        changes()
        #Calls this function to update all the theme and font values
        menu()
        #Can Load Menu With Default Settings!
except:
    print("Something went really wrong loading this file.")
    print("Error 2 - Can't Load Menu Even After Resetting Files!")
    print(":(")
