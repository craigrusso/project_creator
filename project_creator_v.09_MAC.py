#!/usr/bin/env python3
#Copyright 2018 Craig P. Russo | Cr2 Creative 


import os
#from ctypes import windll            #This imports the library to allow for HIDIP Monitors so the text looks clean
from tkinter import filedialog
from tkinter import *
from shutil import copyfile
from tkinter import ttk

#windll.shcore.SetProcessDpiAwareness(2)      # THis is what makes it work on HIDPI Monitors



darkgrey = '#%02x%02x%02x' % (33, 34, 35)  # set your favourite rgb color
boxcolor = '#%02x%02x%02x' % (50, 54, 55) 
buttoncolor = '#%02x%02x%02x' % (70, 104, 185) 

root = Tk()
root.title("CR2 Creative // Project creator v.09")
root.geometry("1420x310+600+200")
root.configure(background=darkgrey)
style = ttk.Style()
style.theme_use('alt')



projPath = ""
projversion = ""
rootPath = ""
templateFile = ""
tempFileFullPath =""
version = 1

heading = Label(root, text="Create your project", font=("arial", 20, "bold","underline"),bg=darkgrey, fg="lightgrey")
heading.pack()



def clear_box(event):
	entry_box.delete(0, END)
	entry_box.config(fg="white")



def get_dirs():
	# This Function Gets the Director path and loads it into the rootPath variable

	global rootPath       #Lets the function know to use the Globa Variables
	global projPath

	
	root.directory = filedialog.askdirectory()      																		 # this loads the directory selection modual
	rootPath = root.directory
	rootPathTrun = (rootPath[:22] + '...' + rootPath[-30:]) if len(rootPath) > 52 else rootPath 							 #Truncates Long Path Names To fit in box
	currentDir = Label(root, text=rootPathTrun, width=55, bg=boxcolor, fg="white",justify="center")
	currentDir.place(x=50, y=157)
	

def clear_selection():
	global tempFileFullPath
	global templateFile

	tempFileFullPath = ""
	templateFile = ""
	currentTemplate = Label(root, text="No template selected", width=55, bg=boxcolor, fg="darkgrey",justify="center")
	currentTemplate.place(x=50, y=100)

def get_template():
	# This function Gets the template Project
	global templateFile
	global tempFileFullPath

	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Premiere files","*.prproj"),("all files","*.*")))
	tempFileFullPath = root.filename
	templateFile = tempFileFullPath.rsplit('/',1)[1]
	currentTemplate = Label(root, text=templateFile, width=55, bg=boxcolor, fg="darkgrey",justify="center")
	currentTemplate.place(x=50, y=100)

	

def create_dirs():
	global rootPath
	global projPath
	global templateFile
	global tempFileFullPath
	global project
	global entry_box
	global projversion
	global version

	if rootPath == "":
		currentDir = Label(root, text="Please select folder", width=55, bg=boxcolor, fg="red",justify="center")
		currentDir.place(x=50, y=157)

	elif str(project.get()) == "" or str(project.get()) == "Please enter project name":

		project = StringVar(value="Please enter project name")
		entry_box = Entry(root, textvariable=project, width=34, bg=boxcolor, fg="red",justify="center")
		entry_box.place(x=355,y=240)
		entry_box.bind("<Button-1>", clear_box)


	else:
		projPath = root.directory + "/" + str(project.get()) 
		
		while os.path.exists(projPath):
			projPath = projPath + "_" + str(version)
			version += 1

		path01 = projPath + '/01_PREMIER_PROJECT'
		path02 = projPath + '/02_AE_PROJECTS'
		path03 = projPath + '/03_AE_RENDERS'
		path04 = projPath + '/04_DELIVERY'
		path05 = projPath + '/05_MUSIC'
		path06 = projPath + '/06_AAFs'
		path07 = projPath + '/07_VOs'
		
		if tempFileFullPath != "":
			os.makedirs(projPath)
			os.makedirs(path01)
			os.makedirs(path02)
			os.makedirs(path03)
			os.makedirs(path04)
			os.makedirs(path05)
			os.makedirs(path06)
			os.makedirs(path07)

			copyfile(tempFileFullPath, path01 + "/" + str(project.get()) + ".prproj")

		else:	
			os.makedirs(projPath)
			os.makedirs(path01)
			os.makedirs(path02)
			os.makedirs(path03)
			os.makedirs(path04)
			os.makedirs(path05)
			os.makedirs(path06)
			os.makedirs(path07)
				
picktemplate = Button(root, text="Please select template", width=20, height=1, bg=buttoncolor,fg=buttoncolor, command=get_template)
picktemplate.place(x=820,y=90)

currentTemplate = Label(root, text="No template selected", width=55, bg=boxcolor, fg="darkgrey",justify="center")
currentTemplate.place(x=50, y=100)

cleartemplate = Button(root, text="Clear template", width=20, height=1, bg=buttoncolor,fg=buttoncolor, command=clear_selection)
cleartemplate.place(x=1120,y=90)

currentDir = Label(root, text="No directory selected", width=55, bg=boxcolor, fg="darkgrey",justify="center")
currentDir.place(x=50, y=157)

pickDir = Button(root, text="Pick Directory", width=20, height=1, bg="black",fg=buttoncolor, command=get_dirs)
pickDir.place(x=820,y=160)

label1 = Label(root, text="Enter project folder name: ", font=("arial",10,),bg=darkgrey, fg="white",justify="center")
label1.place(x=20,y=240)

project = StringVar(value="")
entry_box = Entry(root, textvariable=project, width=34, bg=boxcolor, fg="white",justify="center")      #We need to "Place" the box on a seperat line to be able to work with it later 
entry_box.place(x=355,y=240)                                                                          # If we .place at the end of the main line the var appears as empty to other operators

makedirs = Button(root, text="Create Folders", width=20, height=1, bg="black",fg=buttoncolor, command=create_dirs)
makedirs.place(x=820,y=230)



root.mainloop()