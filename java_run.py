from tkinter import *

from tkinter import messagebox
import os

JavaFileList=[]
javaFileList=[]
def get_file_data():
	javaFileList.clear()
	for file in os.listdir():
	    if file.endswith(".java"):
	        javaFileList.append(file)
def refresh():
	for widget in frame.winfo_children():
		widget.destroy() 
	frame.pack()
	global JavaFileList
	j=1
	for index,i in enumerate(JavaFileList):
		button = Button(frame, text=i, font =
               ('Bebas', 12, 'bold'),fg="green", bg="white", wraplength=300, command=callback(index,None)) 
		deleteBtn =Button(frame ,text = "X",font =
               ('Bebas', 12, 'bold'), fg="red", command=callback(index,"delete"))
		button.grid(row=j, column=0)
		deleteBtn.grid(row=j, column=1)
		j=j+1
		

	


def delete2(args):
	global JavaFileList
	i=0
	r=args+args
	s=args+args+1
	for widget in frame.winfo_children():
		if i==r or i==s:
			widget.destroy()
		i=i+1
	JavaFileList.pop(args)
	refresh()
def onclick2(args):
	global JavaFileList
	command = 'echo ' + JavaFileList[args].strip() + '| clip'
	os.system(command)
def delete(args):
	global JavaFileList
	JavaFileList.pop(args)
	refresh()
def addFunc():
	get_file_data()

root = Tk()      
root.geometry("300x460")
root.bg="white"
root.resizable(False,True)
frame = Frame(root)
frame.pack()
get_file_data()
refresh()



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
    	root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()  