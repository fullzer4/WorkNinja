import unittest 
from work_ninja import MyTask

class TestMyTask(unittest.TestCase):
    
    def test_run(self):
        task = MyTask(10)

        result = task.run()

        self.assertEqual(result, 20)
        
    def test_negative(self):
        task = MyTask(-5)
        result = task.run()
        self.assertEqual(result, -10)
        
    def test_zero(self):
        task = MyTask(0)
        result = task.run()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()