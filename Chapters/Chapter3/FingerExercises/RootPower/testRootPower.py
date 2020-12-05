import unittest

from RootPowerSolution import ReturnsNthRoot

class TestRootPower(unittest.TestCase):

    def test_ReturnsNthRoot_Existent(self):
        """
        Test ReturnsNthRoot if it exists as an Integer
        """
        x = 9
        n = 2
        result = ReturnsNthRoot(x, n)
        root = 3 
        # Test a list of whole numbers
        self.assertEqual(result, root)
        

    def test_ReturnsNthRoot_NonExistent(self):
        """
        Test ReturnsNthRoot if it exists as an Integer  
        """
        x = 9
        n = 3
        result = ReturnsNthRoot(x, n)
        root = None 
        # Test a list of whole numbers
        self.assertEqual(result, root)

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
