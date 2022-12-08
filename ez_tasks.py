"""EZ Tasks - Simple task manager"""
import datetime

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
        # self.date_created = datetime.datetime.now()
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
        return "TASK COMPLETE"

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
        
    """
    def __init__(self,title) -> None:
        self.title = title
        self.last_task_number = None
        self.next_task_number = 1
        self.task_dict = {}

    def __len__(self):
        return len(self.task_dict)
    
    def __repr__(self) -> str:
        return f"{self.title} task list - ez_tasks"
    
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
        new_task.task_number = self.next_task_number
        self.last_task_number = new_task.task_number
        self.next_task_number += 1
        self.task_dict[new_task.task_number] = new_task
        
    def list_tasks(self):
        """
        Prints out current tasks on the task list.
        """
        print("-"*65)
        print("|Task No.|Task description                   |Task status       |")
        print("-"*65)
        for x in self.task_dict:
            task = self.task_dict[x]
            print("|{:<8}|{:<35}|{:<18}|".format(task.task_number,task.name,task.get_status()))
            print("-"*65)
        print("-"*65)

    #TODO: Delete task

