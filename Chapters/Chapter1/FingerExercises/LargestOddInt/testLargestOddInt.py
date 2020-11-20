import unittest

from LargestOddIntSolution import IsOdd
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_IsOdd(self):
        """
        Test IsOdd returns True if an odd integer is passed as its argument
        and return False if an even integer is passed as its argument. 
        If anything but an integer is passed an InvalidArgumentException is 
        called.
        """

        integer = 4 
        result = IsOdd(integer)

        # Test a list of whole numbers
        self.assertEqual(result,True)
        
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
