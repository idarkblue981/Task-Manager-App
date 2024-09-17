import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo


# Global Task List
tasks = []
completed_tasks = []

# Functions for Buttons
def help_panel():
    help_panel_text = """
To add a new task, enter the task name in the input field and then click "Add Task".

To remove a task, select the task and click "Remove Task".
To remove all tasks, click "Remove All Tasks".

To mark a task as complete, select the task and click "Complete Task".
To mark all tasks as complete, click "Complete All Tasks".

To see a list of all tasks, click "List All Tasks".
To see a list of completed tasks, click "List Completed Tasks".
To see a list of uncompleted tasks, click "List Uncompleted Tasks".

To see how many tasks you have, click "Count All Tasks".
To see how many completed tasks you have, click "Count Completed Tasks".
To see how many uncompleted tasks you have, click "Count Uncompleted Tasks".

To see the help panel, click "Help".
To exit, click "Exit".
"""
    showinfo("Help Panel", help_panel_text)

def add_task():
    task = input_field.get()
    if task:
        tasks.append(task)
        input_field.delete(0, tk.END)
        update_task_list()
    else:
        showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_index = selected[0]
        task = tasks[task_index]
        tasks.remove(task)
        if task in completed_tasks:
            completed_tasks.remove(task)
        update_task_list()
    else:
        showwarning("Selection Error", "Please select a task to remove.")

def remove_all_tasks():
    if tasks:
        tasks.clear()
        completed_tasks.clear()
        update_task_list()
    else:
        showwarning("Error", "No tasks to remove.")

def complete_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected[0])
        if task not in completed_tasks:
            completed_tasks.append(task)
        update_task_list()
    else:
        showwarning("Selection Error", "Please select a task to mark as complete.")

def complete_all_tasks():
    completed_tasks.clear()
    completed_tasks.extend(tasks)
    update_task_list()

def list_completed_tasks():
    task_listbox.delete(0, tk.END)
    for task in completed_tasks:
        task_listbox.insert(tk.END, task + " (Completed)")

def list_uncompleted_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if task not in completed_tasks:
            task_listbox.insert(tk.END, task)

def count_all_tasks():
    showinfo("Task Count", f"Total tasks: {len(tasks)}")

def count_completed_tasks():
    showinfo("Completed Task Count", f"Completed tasks: {len(completed_tasks)}")

def count_uncompleted_tasks():
    uncompleted_count = len(tasks) - len(completed_tasks)
    showinfo("Uncompleted Task Count", f"Uncompleted tasks: {uncompleted_count}")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if task in completed_tasks:
            task_listbox.insert(tk.END, task + " (Completed)")
        else:
            task_listbox.insert(tk.END, task)

# Window Setup
window = tk.Tk()
window.title("Task Manager App")
window.geometry("800x600")
window.resizable(False, False)

# Frames
main_frame = ttk.Frame(window)
buttons_frame = ttk.Frame(window)
bottom_frame = ttk.Frame(window)

main_frame.place(x = 0, y = 0, relwidth = 0.6, relheight = 0.9)
buttons_frame.place(relx = 0.6, y = 0, relwidth = 0.4, relheight = 0.9)
bottom_frame.place(x = 0, rely = 0.9, relwidth = 1, relheight = 0.1)

# Widgets
# Main Frame
input_field = ttk.Entry(main_frame, width = 60)
add_button = ttk.Button(main_frame, text = "Add Task", command = add_task)
task_listbox = tk.Listbox(main_frame, width = 70, height = 30)

main_frame.grid_columnconfigure(0, weight = 1)
main_frame.grid_columnconfigure(2, weight = 1)

input_field.grid(column = 1, row = 0, pady = 25)
add_button.grid(column = 2, row = 0, pady = 25)
task_listbox.grid(column = 1, row = 1, columnspan = 2, pady = 25)

# Buttons Frame
buttons_frame.grid_columnconfigure(0, weight = 1)
buttons_frame.grid_columnconfigure(1, weight = 1)

for row in range(6):
    buttons_frame.grid_rowconfigure(row, weight = 1)

remove_task_button = ttk.Button(buttons_frame, text = "Remove Task", command = remove_task)
remove_all = ttk.Button(buttons_frame, text = "Remove All Tasks", command = remove_all_tasks)

complete_task_button = ttk.Button(buttons_frame, text = "Complete Task", command = complete_task)
complete_all = ttk.Button(buttons_frame, text = "Complete All Tasks", command = complete_all_tasks)

list_all = ttk.Button(buttons_frame, text = "List All Tasks", command = lambda: update_task_list())
list_completed = ttk.Button(buttons_frame, text = "List Completed Tasks", command = list_completed_tasks)
list_uncompleted = ttk.Button(buttons_frame, text = "List Uncompleted Tasks", command = list_uncompleted_tasks)

count_all = ttk.Button(buttons_frame, text = "Count All Tasks", command = count_all_tasks)
count_completed = ttk.Button(buttons_frame, text = "Count Completed Tasks", command = count_completed_tasks)
count_uncompleted = ttk.Button(buttons_frame, text = "Count Uncompleted Tasks", command = count_uncompleted_tasks)

help_button = ttk.Button(buttons_frame, text = "Help", command = help_panel)
exit_button = ttk.Button(buttons_frame, text = "Exit", command = lambda: window.destroy())

remove_task_button.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)
remove_all.grid(column = 1, row = 0, sticky = "nsew", padx = 5, pady = 5)

complete_task_button.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)
complete_all.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady = 5)

list_all.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)
list_completed.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)
list_uncompleted.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)

count_all.grid(column = 1, row = 2, sticky = "nsew", padx = 5, pady = 5)
count_completed.grid(column = 1, row = 3, sticky = "nsew", padx = 5, pady = 5)
count_uncompleted.grid(column = 1, row = 4, sticky = "nsew", padx = 5, pady = 5)

help_button.grid(column = 0, row = 5, sticky = "nsew", padx = 5, pady = 5)
exit_button.grid(column = 1, row = 5, sticky = "nsew", padx = 5, pady = 5)

# Bottom Frame
bottom_label = ttk.Label(bottom_frame, text = "A Paul Jimon Production\nArad, Romania\n2024", anchor = "center", justify = "center")
bottom_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)


# Run
if __name__ == "__main__":
    window.mainloop()