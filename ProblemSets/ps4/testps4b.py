import unittest
from ps4b import *

class TestMessage(unittest.TestCase):
    # Remember you created an empty dictionary to get the ball rolling an now
    # look where you are! 

    # Class Variables
    message = Message(get_story_string())

    def test_build_shift_ZeroShift(self):
        """
        Test that the build_shift_dict method
        returns a dictionary where its values in order are 
        the ascii_letters because there hasn't been a shift
        """
        # ARRANGE
        shift = 0 
        expected = string.ascii_letters
        # ACT
        shift_dict = TestMessage.message.build_shift_dict(shift)
        # ASSERT
        result = ''
        for val in shift_dict.values():
            result += val
        self.assertEqual(result, expected)

    def test_build_shift_OneShift(self):
        """
        Test that the build_shift_dict method 
        returns a shifted dictionary by 1 so 
        that { 'a': 'b' ... 'Z': 'z'}
        """
        # ARRANGE
        shift = 1 
        alphabet = string.ascii_letters
        expected = alphabet[shift:] + alphabet[0]
        # ACT
        shift_dict = TestMessage.message.build_shift_dict(shift)
        # ASSERT
        result = ''
        for val in shift_dict.values():
            result += val
        self.assertEqual(result, expected)


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
