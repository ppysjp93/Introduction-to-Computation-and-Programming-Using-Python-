import unittest
from ps4b import *

class TestMessage(unittest.TestCase):

    # Class Variables
    message = Message(get_story_string())
   

    def test_build_shift_dict_ZeroShift(self):
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

    def test_build_shift_dict_OneShift(self):
        """
        Test that the build_shift_dict method 
        returns a shifted dictionary by 1 so 
        that { 'a': 'b' ... 'Z': 'a'}
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
        self.assertEqual(shift_dict['Z'], 'a')

    def test_build_shift_dict_TenShift(self):
        """
        Test that the build_shift_dict method 
        returns a shifted dictionary by 10 so 
        that { 'a': 'k' ... 'Z': 'j'}
        """
        # ARRANGE
        shift = 10
        alphabet = string.ascii_letters
        expected = alphabet[shift:] + alphabet[0:shift]
        # ACT
        shift_dict = TestMessage.message.build_shift_dict(shift)
        # ASSERT
        result = ''
        for val in shift_dict.values():
            result += val
        self.assertEqual(result, expected)
        self.assertEqual(shift_dict['a'], 'k')

    def test_build_shift_dict_ShiftOutOfRange(self):
        """
        Test that the build_shift_dict method 
        raises exception when shifted out of the range of 0<= shift < 26 
        """
        with self.assertRaises(ValueError) as cm:
                TestMessage.message.build_shift_dict(27)
        
        self.assertEqual('shift out of range', str(cm.exception))

    def test_apply_shift_ZeroShift(self):
        '''
        Returns: the message text (string) in which 
        every character is shifted down the alphabet 
        by the input shift, in this case there is no change to the message text.
        '''
        # ARRANGE
        shift = 0 
        expected = 'Xoqy'
        # ACT
        shift_message_text = TestMessage.message.apply_shift(shift)
        result = shift_message_text.split(' ')[0]
        # ASSERT
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(result, expected)

    def test_apply_shift_OneShift(self):
        '''
        Returns: the message text (string) in which 
        every character is shifted down the alphabet 
        by the input shift, in this case there is no change to the message text.
        '''
        # ARRANGE
        shift = 1 
        expected = 'Yprz'
        # ACT
        shift_message_text = TestMessage.message.apply_shift(shift)
        result = shift_message_text.split(' ')[0]
        # ASSERT
        self.assertEqual(result, expected)

def MessageSuite():
    MessageSuite = unittest.TestSuite()
    MessageSuite.addTest(MessageTest('test_build_shift_dict_ZeroShift'))
    MessageSuite.addTest(MessageTest('test_build_shift_dict_OneShift'))
    MessageSuite.addTest(MessageTest('test_build_shift_dict_TenShift'))
    MessageSuite.addTest(MessageTest('test_build_shift_dict_ShiftOutOfRange'))
    MessageSuite.addTest(MessageTest('test_apply_shift_ZeroShift'))
    MessageSuite.addTest(MessageTest('test_apply_shift_OneShift'))
    return MessageSuite

# This is known as a command line entry point
if __name__ == '__main__':
#    unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(MessageSuite())

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
