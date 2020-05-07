#!/usr/bin/env python3
#Copyright 2020 Craig P. Russo | Cr2 Creative

import os
import platform

if platform.system() ==  "Windows":
	from ctypes import windll       #This imports the library to allow for HIDIP Monitors so the text looks clean NEEDS TO BE COMMENTED OUT FOR MACOS
	windll.shcore.SetProcessDpiAwareness(2)  # This is what makes it work on HIDPI Monitors NEEDS TO BE COMMENTED OUT FOR MACOS

from tkinter import *
from tkinter import filedialog
from shutil import copyfile

if platform.system() == "Windows":
	darkgrey = '#%02x%02x%02x' % (33, 34, 35)  # set your favourite rgb color
	lightgrey = '#%02x%02x%02x' % (163, 164, 165)  
	boxcolor = '#%02x%02x%02x' % (50, 54, 55) 
	buttoncolor = '#%02x%02x%02x' % (70, 104, 185) 
	buttontext = '#%02x%02x%02x' % (255, 255, 255)
	errortext = '#%02x%02x%02x' % (255, 0, 0)

if platform.system() == "Darwin":
	darkgrey = '#%02x%02x%02x' % (33, 34, 35)  # set your favourite rgb color
	lightgrey = '#%02x%02x%02x' % (163, 164, 165)  
	boxcolor = '#%02x%02x%02x' % (50, 54, 55) 
	buttoncolor = '#%02x%02x%02x' % (70, 104, 185) 
	buttontext = '#%02x%02x%02x' % (0, 0, 0)
	errortext = '#%02x%02x%02x' % (255, 0, 0)

root = Tk()
root.title("CR2 Creative // Project creator v.12")
root.geometry("1220x310+600+200")
root.configure(background=darkgrey)

#Set Global Variables
projPath = ""
projversion = ""
rootPath = ""
templateFile = ""
tempFileFullPath =""
version = 1
fileExt = ""
heading = Label(root, text="Create your project", font=("arial", 20, "bold","underline"),bg=darkgrey, fg="lightgrey")
heading.pack()

#Define all the functions
def clear_box(event):
	entry_box.delete(0, END)
	entry_box.config(fg=buttontext)

def get_dirs():
	# This Function Gets the Directory path and loads it into the rootPath variable

	global rootPath       #Lets the function know to use the Global Variables
	global projPath

	root.directory = filedialog.askdirectory()      																		 # this loads the directory selection modual
	rootPath = root.directory
	rootPathTrun = (rootPath[:22] + '...' + rootPath[-30:]) if len(rootPath) > 52 else rootPath 							 #Truncates Long Path Names To fit in box
	currentDir = Label(root, text=rootPathTrun, width=55, bg=boxcolor, fg=lightgrey,justify="center")
	currentDir.place(x=50, y=167)
	
def clear_selection():
	# This function clears the template file you may have selected
	global tempFileFullPath
	global templateFile

	tempFileFullPath = ""
	templateFile = ""
	currentTemplate = Label(root, text="No template selected", width=55, bg=boxcolor, fg=lightgrey,justify="center")
	currentTemplate.place(x=50, y=100)

def get_template():
	# This function Gets the template Project
	global templateFile
	global tempFileFullPath
	global fileExt

	if platform.system() == "Darwin":
		root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
	else:
		root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Premiere files","*.prproj"),("After Effects","*.aep"),("Photoshop files","*.psd"),("Illustrator files","*.ai"),("all files","*.*")))

	
	tempFileFullPath = root.filename
	templateFile = tempFileFullPath.rsplit('/',1)[1]
	fileExt = os.path.splitext(str(templateFile))
	fileExt = str(fileExt[1])
	currentTemplate = Label(root, text=templateFile, width=55, bg=boxcolor, fg=lightgrey,justify="center")
	currentTemplate.place(x=50, y=100)

def create_dirs():
	#This is the main function that creates all the directories and copies and renames the template file you select
	global rootPath           #Lets the function know to use the Global Variables
	global projPath
	global templateFile
	global tempFileFullPath
	global project
	global entry_box
	global projversion
	global version
	global fileExt

	if rootPath == "":
		currentDir = Label(root, text="Please select folder", width=55, bg=boxcolor, fg=errortext,justify="center")
		currentDir.place(x=50, y=167)

	elif str(project.get()) == "" or str(project.get()) == "Please enter project name":

		project = StringVar(value="Please enter project name")
		entry_box = Entry(root, textvariable=project, width=34, bg=boxcolor, fg=errortext,justify="center")
		entry_box.place(x=255,y=240)
		entry_box.bind("<Button-1>", clear_box)

	else:
		projPath = root.directory + "/" + str(project.get()) 
		
		while os.path.exists(projPath):
			projPath = projPath + "_" + str(version)
			version += 1

#If it's a Premiere sor After Effects template make the first 3 directory structure
		if fileExt == ".prproj" or fileExt == ".aep" or fileExt == ".aepx":
			path01 = projPath + '/01_PREMIER_PROJECT'
			path02 = projPath + '/02_AE_PROJECTS'
			path03 = projPath + '/03_AE_RENDERS'

#If it's Photoshop or Illustrator make the first 3 directories like this
		elif fileExt == ".psd" or fileExt == ".ai":
			path01 = projPath + '/01_PHOTOSHOP_PROJECTS'
			path02 = projPath + '/02_ILLUSTRATOR_PROJECTS'
			path03 = projPath + '/03_STOCK_FOOTAGE'

#If it's any other kind of file just do the premiere structure
		else:
			path01 = projPath + '/01_PREMIER_PROJECT'
			path02 = projPath + '/02_AE_PROJECTS'
			path03 = projPath + '/03_AE_RENDERS'


		path04 = projPath + '/04_DELIVERY'
		path05 = projPath + '/05_MUSIC'
		path06 = projPath + '/06_AAFs'
		path07 = projPath + '/07_VOs'
		path08 = projPath + '/08_AUDITION_FILES'
		path09 = path08 + '/01_AUDITION_SESSIONS'
		path10 = path08 + '/02_AUDITION_FILES'
		path11 = path08 + '/03_MIX_PRINTS'
		path12 = path01 + '/01_FOOTAGE'

		if tempFileFullPath != "":
			os.makedirs(projPath)
			os.makedirs(path01)
			os.makedirs(path02)
			os.makedirs(path03)
			os.makedirs(path04)
			os.makedirs(path05)
			os.makedirs(path06)
			os.makedirs(path07)
			os.makedirs(path08)
			os.makedirs(path09)
			os.makedirs(path10)
			os.makedirs(path11)
			os.makedirs(path12)

			if fileExt == ".prproj" or fileExt == ".psd":
				copyfile(tempFileFullPath, path01 + "/" + str(project.get()) + fileExt)
			
			elif fileExt == ".aep" or fileExt == ".aepx" or fileExt == ".ai":
				copyfile(tempFileFullPath, path02 + "/" + str(project.get()) + fileExt)

			else:
				copyfile(tempFileFullPath, path01 + "/" + str(project.get()) + fileExt)
			


		else:
			os.makedirs(projPath)
			os.makedirs(path01)
			os.makedirs(path02)
			os.makedirs(path03)
			os.makedirs(path04)
			os.makedirs(path05)
			os.makedirs(path06)
			os.makedirs(path07)
			os.makedirs(path08)
			os.makedirs(path09)
			os.makedirs(path10)
			os.makedirs(path11)
			os.makedirs(path12)


#Build out Interface
picktemplate = Button(root, text="Please select template", width=20, height=1, bg=buttoncolor,fg=buttontext, command=get_template)
picktemplate.place(x=680,y=90)

currentTemplate = Label(root, text="No template selected", width=55, bg=boxcolor, fg=lightgrey,justify="center")
currentTemplate.place(x=50, y=100)

cleartemplate = Button(root, text="Clear template", width=20, height=1, bg=buttoncolor,fg=buttontext, command=clear_selection)
cleartemplate.place(x=920,y=90)

currentDir = Label(root, text="No directory selected", width=55, bg=boxcolor, fg=lightgrey,justify="center")
currentDir.place(x=50, y=167)

pickDir = Button(root, text="Pick Directory", width=20, height=1, bg=buttoncolor,fg=buttontext, command=get_dirs)
pickDir.place(x=680,y=160)

label1 = Label(root, text="Enter project folder name: ", font=("arial",10,),bg=darkgrey, fg=lightgrey,justify="center")
label1.place(x=20,y=240)

project = StringVar(value="")
entry_box = Entry(root, textvariable=project, width=34, bg=boxcolor, fg=lightgrey,justify="center")      #We need to "Place" the box on a seperate line to be able to work with it later 
entry_box.place(x=255,y=240)                                                                           #If we .place at the end of the main line the var appears as empty to other operators

makedirs = Button(root, text="Create Folders", width=20, height=1, bg=buttoncolor,fg=buttontext, command=create_dirs)
makedirs.place(x=680,y=230)

#This is what makes the whole thing run
root.mainloop()
