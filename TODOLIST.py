#python program to create a todolist using tkinter module for GRAPHICAL USER INTERFACE(GUI)


#importing tkinter module and accesing all function
from tkinter import *
from tkinter import messagebox


#defning a function to add task

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("!!WARNING!!", "Please Enter a Task to Add!")


#defining a function to delete a selected task

def deleteTask():
    try:
        lb.delete(ANCHOR)
    except:
        messagebox.showwarning("!!WARNING!!","Please Select a Task to Delete!")


#giving specifications for TODOLIST window
ws=Tk()
ws.geometry('500x450+500+200')
ws.title('TODOLIST')
ws.config(bg='GREY')
ws.resizable(width=False, height=False)

#creating a frame to display the tasks
frame = Frame(ws)
frame.pack(pady=8)

#giving specification to the frame
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('arial',20),
    background='blue',
    fg='black',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
     )
lb.pack(side=LEFT, fill=BOTH)

#all tasks will be saved here
task_list = []

for item in task_list:
    lb.insert(END, item)

#creating a scrollbar for our frame
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#specification of tasks entering
my_entry = Entry(
    ws,
    font=('arial',20,'bold')
    )

my_entry.pack(pady=10)

#adding the add button and deleting button
button_frame = Frame(ws)
button_frame.pack(pady=8)

#code for add button
addTask_btn = Button(
    button_frame,
    text='ADD TASK',
    font=('arial 18'),
    background='green',
    padx=20,
    pady=10,
    command=newTask
    )
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#code for delete button
delTask_btn = Button(
    button_frame,
    text='DELETE TASK',
    font=('arial 18'),
    background='red',
    padx=20,
    pady=10,
    command=deleteTask
    )
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#using mainloop so the TODOLIST window will appear infinetely
ws.mainloop()