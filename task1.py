#TO-DO LIST

#TASK 1

#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

import tkinter as tk

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a selected task from the list
def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

# Create the main window
app = tk.Tk()
app.title("To-Do List")

# Create and configure the task entry field
task_entry = tk.Entry(app, width=40)
task_entry.pack()

# Create and configure the Add Task button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Create and configure the Remove Task button
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Create and configure the task list
task_list = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
task_list.pack()

# Run the application
app.mainloop()
