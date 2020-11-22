import unittest

from LargestOddIntSolution import IsOdd, LargestOf2, LargestOf3, LargestOdd
from fractions import Fraction

class TestLargestOddInt(unittest.TestCase):
    def test_IsOdd_EvenInteger(self):

        integer = 4 
        result = IsOdd(integer)

        # Test a list of whole numbers
        self.assertEqual(result,False)

    def test_IsOdd_OddInteger(self):

        integer = 3 
        result = IsOdd(integer)

        # Test a list of whole numbers
        self.assertEqual(result,True)
        
    def test_IsOdd_NonInteger(self):                                               
        with self.assertRaises(TypeError): 
            IsOdd("hello")

    def test_LargestOf2_a_GreaterThan_b(self):
        a = 2 
        b = 1 
        result = LargestOf2(a, b)
        self.assertEqual(result, a)

    def test_LargestOf2_a_LessThan_b(self):
        a = 1 
        b = 2 
        result = LargestOf2(a, b)
        self.assertEqual(result, b)

    def test_LargestOf3_a_gt_b_and_gt_c(self):
        a = 3 
        b = 2 
        c = 1
        result = LargestOf3(a, b, c)
        self.assertEqual(result, a)

    def test_LargestOf3_a_gt_b_but_lt_c(self):
        a = 2 
        b = 1 
        c = 3
        result = LargestOf3(a, b, c)
        self.assertEqual(result, c)

    def test_LargestOf3_a_lt_b_but_gt_c(self):
        a = 2 
        b = 3 
        c = 1
        result = LargestOf3(a, b, c)
        self.assertEqual(result, b)

    def test_LargestOf3_a_lt_b_and_lt_c(self):
        a = 1 
        b = 2 
        c = 3
        result = LargestOf3(a, b, c)
        self.assertEqual(result, c)

    def test_LargestOdda_b_c_AllOdd(self):
        a = 1 
        b = 3 
        c = 5
        result = LargestOdd(a, b, c)
        self.assertEqual(result, c)
    
    def test_LargestOdd_a_b(self):
        a = 1 
        b = 7 
        c = 4
        result = LargestOdd(a, b, c)
        self.assertEqual(result, b)

    def test_LargestOdd_a_c(self):
        a = 1 
        b = 4 
        c = 7
        result = LargestOdd(a, b, c)
        self.assertEqual(result, c)

    def test_LargestOdd_b_c(self):
        a = 4 
        b = 1 
        c = 7
        result = LargestOdd(a, b, c)
        self.assertEqual(result, c)

    def test_LargestOdd_a(self):
        a = 1 
        b = 4 
        c = 8
        result = LargestOdd(a, b, c)
        self.assertEqual(result, a)

    def test_LargestOdd_b(self):
        a = 4 
        b = 1 
        c = 8
        result = LargestOdd(a, b, c)
        self.assertEqual(result, b)

    def test_LargestOdd_c(self):
        a = 4 
        b = 8 
        c = 1
        result = LargestOdd(a, b, c)
        self.assertEqual(result, c)

    def test_LargestOdd_EvenArgs(self):
        with self.assertRaises(ArithmeticError): 
            LargestOdd(2,4,6)

# This is known as a command line entry point
if __name__ == '__main__':
    unittest.main()

# Another way to test on the commandline is to call the following command
# which runs unittest test on the test module.
# $ python -m unittest test
# $ python -m unittest -v test (verbose)   
# $ python -m unittest discover (tests any file in the folder matching test*.py)

# This allows you to test all the test files in the tests folder
# $ python -m unittest discover -s tests

# lastly if the source code you are testing is not in the root directory but is
# contained in a subdirectory for example a folder like src/ you can tell 
# unittest where to execute the test so that it can import the modules correctly
# with the -t flag
 
# $ python -m unittest discover -s tests -t src
