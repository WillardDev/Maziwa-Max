import unittest
import re
import dataset as ds
import response_extractor as rex

class TestExtractResponseText(unittest.TestCase):
    def test_extract_response_text(self):
        # Test input string containing response
        input_string_with_response = "<s>### Instruction:\nThis is an instruction.\nResponse:\nThis is a response.</s>"
        expected_response = "This is a response."
        self.assertEqual(rex.extract_response_text(input_string_with_response), expected_response)

        # Test input string without response
        input_string_without_response = "<s>### Instruction:\nThis is an instruction.</s>"
        self.assertIsNone(rex.extract_response_text(input_string_without_response))

if __name__ == '__main__':
    unittest.main()
