import tkinter as tk
from tkinter import *

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")

        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

        listbox.delete(ANCHOR)

def openTaskfile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        with open("tasklist.txt", 'w') as file:
            file.close()
w = Tk()
w.title("To-Do List")
w.geometry("400x650+400+100")
w.resizable(False, False)
w.configure(bg="#2b2d42")

task_list = []

Image_icon = PhotoImage(file="C:\\Users\\ASUS\\OneDrive\\Desktop\\codsoft\\images\\task.png") 
w.iconphoto(False, Image_icon)

TopImage = PhotoImage(file="C:\\Users\\ASUS\\OneDrive\\Desktop\\codsoft\\images\\topbar.png") 
Label(w, image=TopImage).pack()

dockImage = PhotoImage(file="C:\\Users\\ASUS\\OneDrive\\Desktop\\codsoft\\images\\dock.png")
Label(w, image=dockImage, bg="#2b2d42").place(x=30, y=25)

noteImage = PhotoImage(file="C:\\Users\\ASUS\\OneDrive\\Desktop\\codsoft\\images\\task.png") 
Label(w, image=noteImage, bg="#2b2d42").place(x=300, y=25)

heading = Label(w, text="ALL TASKS", font="Arial 20 bold", fg="white", bg="#2b2d42")
heading.place(x=130, y=25)

frame = Frame(w, width=400, height=50, bg="#edf2f4")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="Helvetica 20", bd=0, bg="#343a40", fg="#ffffff", insertbackground='white') 
task_entry.place(x=10, y=7)

button = Button(frame, text="ADD", font="Helvetica 20 bold", width=6, bg="#ff6f61", fg="white", bd=0, command=addTask)
button.place(x=300, y=0)

frame1 = Frame(w, bd=3, width=700, height=280, bg="#8d99ae")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("Helvetica", 12), width=40, height=16, bg="#343a40", fg="white", cursor="hand2", selectbackground="#ff6f61")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

Scrollbar = Scrollbar(frame1)
Scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=listbox.yview)

openTaskfile()

Delete_icon = PhotoImage(file="C:\\Users\\ASUS\\OneDrive\\Desktop\\codsoft\\images\\delete.png")  
Button(w, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

w.mainloop()
