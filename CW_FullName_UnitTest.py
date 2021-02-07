#Christopher Weiner
#CS 362 - HW4 - Full Name Unit Testing
import unittest
import CW_FullName as FN

class TestCaseName(unittest.TestCase):
    def test1(self):
        self.assertEqual(FN.fullName("Chris","Weiner"),"Chris Weiner")
    def test2(self):
        self.assertEqual(FN.fullName(1,"Weiner"), "First names are not numbers")
    def test3(self):
        self.assertEqual(FN.fullName("Chris","Weiner"),"ChrisWeiner")
    def test4(self):
        self.assertEqual(FN.fullName("Chris","Weiner"),"Weiner Chris")
    def test5(self):
        self.assertEqual(FN.fullName("Chris","Weiner"),"Chris")
    def test6(self):
        self.assertEqual(FN.fullName("Chris","Weiner"),"Weiner")
    def test7(self):
        self.assertEqual(FN.fullName("Chris  ","  Weiner"),"Chris Weiner")
    def test8(self):
        self.assertEqual(FN.fullName("     Chris        ","          Weiner          "),"Chris Weiner")
    def test9(self):
        self.assertEqual(FN.fullName("Weiner","Chris"),"Chris Weiner")
    def test10(self):
        self.assertEqual(FN.fullName("Chris",2),"Last names are not numbers")
if __name__ == "__main__": #Using this line from the unittest lecture to display the number of failures in the test
    unittest.main(verbosity=2)