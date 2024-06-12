import unittest
from unittest.mock import patch
import re
import dataset as ds
import model_inference as mi
import question_extractor as qe

class TestModelInference(unittest.TestCase):
    def test_extract_instruction_text(self):
        input_string_with_instruction = "<s>### Instruction:\nThis is an instruction.\nResponse:\nThis is a response.</s>"
        expected_instruction = "This is an instruction."
        self.assertEqual(qe.extract_instruction_text(input_string_with_instruction), expected_instruction)

        input_string_without_instruction = "<s>Response:\nThis is a response.</s>"
        self.assertIsNone(qe.extract_instruction_text(input_string_without_instruction))

if __name__ == '__main__':
    unittest.main()
