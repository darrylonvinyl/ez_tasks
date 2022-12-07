import unittest
from ez_tasks import Task,TaskList

class TestTask(unittest.TestCase):

    def setUp(self):
        self.a = Task('darryl')
        self.a.date_created = (2022,11,30)

    def test_istask(self):
        self.assertIsInstance(self.a,Task)
        self.assertEqual(self.a.name,'darryl')
        self.assertEqual(self.a.task_started, False)

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
        self.assertEqual(self.a.task_dict[2],"Clean my room")
        self.assertTrue(len(self.a) == 3)

    def tearDown(self):
        return super().tearDown()
        
if __name__ == '__main__':
    unittest.main()