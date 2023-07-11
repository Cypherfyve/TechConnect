import tkinter as tk

class TodoListApp:
    def __init__(self):
        self.tasks = []


        # Create a Main Window
        self.root = tk.Tk()  # Tk() creates a new window
        self.root.title("Todo List")    


        # Task entry field creation
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(side=tk.LEFT, padx = 5)

    # Add button creation
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task) 
        self.add_button.pack(side = tk.LEFT, padx = 5)

    # Task list creation
        self.task_list = tk.Listbox(self.root)
        self.task_list.pack(side = tk.LEFT, padx = 5)


    # Delete Button Creation
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task) 
        self.delete_button.pack(side = tk.LEFT, padx = 5)

    # Loop 

        self.root.mainloop()


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.task_list.delete(index)       


