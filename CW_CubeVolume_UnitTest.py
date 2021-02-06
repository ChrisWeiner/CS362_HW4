#Christopher Weiner
#CS 362 - HW4 - Cube Volume Unit Testing
import unittest
import CW_CubeVolume as CV
import cmath

class TestCaseVolume1(unittest.TestCase):
    def test1(self):
        self.assertEqual(CV.cubeVolume(1.0),1.0)
    def test2(self):
        self.assertEqual(CV.cubeVolume(complex(5,3)),-1)
    def test3(self):
        self.assertEqual(CV.cubeVolume(-1),-1)
    def test4(self):
        self.assertEqual(CV.cubeVolume(3),27)
    def test5(self):
        self.assertEqual(CV.cubeVolume("test"),27)
    def test6(self):
        self.assertEqual(CV.cubeVolume(2),8)

if __name__ == "__main__": #Using this line from the unittest lecture to display the number of failures in the test
    unittest.main(verbosity=2)