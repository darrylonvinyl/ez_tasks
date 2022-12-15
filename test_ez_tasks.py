import unittest
from ez_tasks import Task,TaskList

class TestTask(unittest.TestCase):

    def setUp(self):
        # Task not started
        self.a = Task("Wash the car")
   
    def test_istask(self):
        self.assertIsInstance(self.a,Task)
        self.assertEqual(self.a.name,"Wash the car")
        self.assertEqual(self.a.task_started, False)
    
    def test_getstatus(self):
        self.b = Task("Clean the dishes")
        self.c = Task("Take out the trash")
        # Task marked in progress
        self.b.start_task()
        # Task marked completed
        self.c.complete_task()
        self.assertEqual(self.a.get_status(), "NOT STARTED")
        self.assertEqual(self.b.get_status(), "IN PROGRESS")
        self.assertEqual(self.c.get_status(), "TASK COMPLETE")
    
    def test_edittask(self):
        self.assertEqual(self.a.name,"Wash the car")
        self.a.edit_task("Wash the Prius")
        self.assertEqual(self.a.name, "Wash the Prius")

    def tearDown(self):
        return super().tearDown()
        
class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.a = TaskList('Weekend')

    def test_istasklist(self):
        self.assertIsInstance(self.a,TaskList)
        self.assertEqual(self.a.title, 'Weekend')
        self.assertEqual(self.a.task_dict,{})

    def test_addtask(self):
        self.a.add_task("Replace air filter for HVAC")
        self.a.add_task("Clean my room")
        self.a.add_task("Wash the dishes")
        self.assertEqual(self.a.task_dict[2].name,"Clean my room")
        self.assertTrue(len(self.a) == 3)
    
    def test_list_task(self) -> None:
        print("\n")
        self.a.add_task("Replace air filter for HVAC")
        self.a.add_task("Clean my room")
        self.a.add_task("Wash the dishes")
        self.a.list_tasks()

    def test_listtasknonecreated(self):
        self.assertEqual(self.a.list_tasks(),"No tasks created yet!")

    def test_deletetask(self):
        self.a.add_task("Replace air filter for HVAC")
        self.a.add_task("Clean my room")
        self.a.add_task("Wash the dishes")
        self.a.delete_task(2)
        self.assertTrue(len(self.a) == 2)
        self.a.list_tasks()

    def test_listtasknonecreated(self):
        self.assertTrue(not self.a.task_dict)
        self.assertEqual(self.a.list_tasks(), "No tasks created yet!")

    def tearDown(self):
        return super().tearDown()
        
if __name__ == '__main__':
    unittest.main()