#Christopher Weiner
#CS 362 - HW4 - List Average Unit Testing
import unittest
import CW_ListAverage as LA

class TestCaseAverage(unittest.TestCase):
    def test1(self):
        self.assertEqual(LA.listAverage([1,2,3,4,5]),3)
    def test2(self):
        self.assertEqual(LA.listAverage([]),"There are zero elements in the list")
    def test3(self):
        self.assertEqual(LA.listAverage([1,2,3]),2)
    def test4(self):
        self.assertEqual(LA.listAverage([0,0,0,0,0]),0)
    def test5(self):
        self.assertEqual(LA.listAverage("[0,0,0,0,0]"),"Invalid type")
    def test6(self):
        self.assertEqual(LA.listAverage(1),"Invalid type")
if __name__ == "__main__": #Using this line from the unittest lecture to display the number of failures in the test
    unittest.main(verbosity=2)