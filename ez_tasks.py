"""EZ Tasks - Simple task manager"""

import pickle
import time
from os.path import exists
from os import system,name

SAVE_FILE = "task_save.pkl"

class Task:
    """Class for task object.
    
    Attributes:
        name : str
            The task that needs to be completed.
        task_started : bool
            Tracker for if work on the task has started.
        task_completed : bool
            Tracker for if work on the task is completed.
        task_number : int
            Task number assigned by the assigned task list.
        """

    def __init__(self,name: str, task_started=False) -> None:
        """Constructor for Task object"""
        self.name = name
        self.task_started = task_started
        self.task_completed = False
        self.task_number = None
    
    def __repr__(self) -> str:
        return f"{self.name}"

    def get_status(self):
        if not self.task_completed:
            if not self.task_started:
                return "NOT STARTED"
            return "IN PROGRESS"
        return "COMPLETE"

    def start_task(self):
        self.task_started = True

    def complete_task(self):
        self.task_completed = True

    def edit_task(self,new_task):
        self.name = new_task

class TaskList:
    """Class for task list object.
    
    Attributes:
        title : str
            The name of the task list.
        last_task_number : int
            The last task number assigned.
        next_task_number : int
            The next task number to be assigned.
        task_dict : dictionary
            Structure to assign and track tasks on tasklist.
        unassigned_task_number: list
            Sturcture to hold freed task numbers for re-use.
        
    """
    def __init__(self,title) -> None:
        self.title = title
        self.last_task_number = 0
        self.next_task_number = 1
        self.task_dict = {}
        self.unassigned_task_number = []

    def __len__(self):
        return len(self.task_dict)
    
    def __repr__(self) -> str:
        return f"{self.title} task list"
    
    def add_task(self,name):
        """
        Creates a new task and assigns it the next task number. It then
        updates the task numbers and adds it to the task dictionary, which
        holds all the tasks.
        
        Parameters:
            name : str
                The task that you will be creating and need to track.
        """
        new_task = Task(name)
        if self.unassigned_task_number:
            new_task.task_number = self.unassigned_task_number[0]
            self.task_dict[new_task.task_number] = new_task
        else:    
            new_task.task_number = self.next_task_number
            self.last_task_number = new_task.task_number
            self.next_task_number += 1
            self.task_dict[new_task.task_number] = new_task
        
    def list_tasks(self):
        """
        Prints out current tasks on the task list.
        """
        if not self.task_dict:
            return "No tasks created yet!"
        else:
        #(TODO): Update list_tasks to dynamically display tasks.
            print("-"*65)
            print("|Task No.|Task description                   |Task status       |")
            print("-"*65)
            for x in self.task_dict.keys():
                task = self.task_dict[x]
                print("|{:<8}|{:<35}|{:<18}|".format(task.task_number,task.name,task.get_status()))
                print("-"*65)
            print("-"*65)

    def delete_task(self,task_number):
        if self.task_dict[task_number]:
            self.unassigned_task_number.append(task_number)
            del self.task_dict[task_number]
    
    #(TODO): Clearing Tasks in 'COMPLETED' status from the TaskList.

def display_menu():
    print("EZ Tasks Menu:")
    print("1. See current tasks")
    print("2. Create a task")
    print("3. Mark task started")
    print("4. Mark task completed")
    print("5. Edit a task")
    print("6. Delete a task")
    print("7. Quit\n")

def handle_choice(choice):
    if choice == '1':
        if default_tasklist.task_dict:
            default_tasklist.list_tasks()
            time.sleep(3)
            return True
        else:
            print("No tasks created yet!")
            time.sleep(2)
            return True
    elif choice == '2':
        new_task = input("Please enter the task to track: \n")
        default_tasklist.add_task(new_task)
        print("New task created!")
        time.sleep(2)
        return True
    elif choice =='3':
        if default_tasklist.task_dict:
            default_tasklist.list_tasks()
            started_task = input("Which task do you want to mark started: \n")
            if int(started_task) in  default_tasklist.task_dict:
                default_tasklist.task_dict[int(started_task)].start_task()
                print(f"Task {started_task} marked as in progress.")
                time.sleep(3)
                return True
            else:
                print("Please select a valid task.")
                time.sleep(3)
                return True
        else:
            print("No tasks created yet!")
            time.sleep(2)
            return True
    elif choice =='4':
        if default_tasklist.task_dict:
            default_tasklist.list_tasks()
            completed_task = input("Which task do you want to mark completed: \n")
            if int(completed_task) in default_tasklist.task_dict:
                default_tasklist.task_dict[int(completed_task)].complete_task()
                print(f"Task {completed_task} marked as completed.")
                time.sleep(3)
                return True
            else:
                print("Please select a valid task.")
                time.sleep(3)
                return True
        else:
            print("No tasks created yet!")
            time.sleep(2)
            return True
    elif choice == '5':
        if default_tasklist.task_dict:
            default_tasklist.list_tasks()
            task_choice = input("Please select the task you want to update: \n")
            if int(task_choice) in default_tasklist.task_dict:
                updated_task = input("Please enter updated task information: \n")
                default_tasklist.task_dict[int(task_choice)].name = updated_task
                print(f"Task {task_choice} has been updated.")
                time.sleep(3)
                return True
            else:
                print("Please select a valid task.")
                time.sleep(3)
                return True
        else:
            print("No tasks created yet!")
            time.sleep(2)
            return True
    elif choice == '6':
        if default_tasklist.task_dict:
            default_tasklist.list_tasks()
            print("\n")
            task_to_delete = input("Please select the task you want to delete: \n")
            if int(task_to_delete) in default_tasklist.task_dict:
                default_tasklist.delete_task(int(task_to_delete))
                print(f"Task {task_to_delete} has been deleted.")
                time.sleep(3)
                return True
            else:
                print("Please select a valid task.")
                time.sleep(3)
                return True
        else:
            print("No tasks created yet!")
            time.sleep(2)
            return True
    elif choice == '7':
        save_object(default_tasklist)
        return False

def save_object(obj):
    try:
        with open(SAVE_FILE, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
        time.sleep(3)
        return True
#(TODO): Update save_object to run when any operation on a task is completed.

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
        time.sleep(3)
        return True

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == "__main__":

    if not exists(SAVE_FILE):
        default_tasklist = TaskList("TODO")
    else:
        default_tasklist = load_object(SAVE_FILE)

    while True:
        clear()
        display_menu()
        choice = input("Enter your choice: ")

        if not handle_choice(choice):
            break