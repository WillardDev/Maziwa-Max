import unittest
from model_evaluation import evaluate, extract_instruction_text, extract_response_text

class TestEvaluateFunction(unittest.TestCase):
    def test_extract_instruction_text(self):
        # Test input string containing instruction
        input_string_with_instruction = "<s>### Instruction:\nThis is an instruction.\nResponse:\nThis is a response.</s>"
        expected_instruction = "This is an instruction."
        self.assertEqual(extract_instruction_text(input_string_with_instruction), expected_instruction)

        # Test input string without instruction
        input_string_without_instruction = "<s>Response:\nThis is a response.</s>"
        self.assertIsNone(extract_instruction_text(input_string_without_instruction))

    def test_extract_response_text(self):
        # Test input string containing response
        input_string_with_response = "<s>### Instruction:\nThis is an instruction.\nResponse:\nThis is a response.</s>"
        expected_response = "This is a response."
        self.assertEqual(extract_response_text(input_string_with_response), expected_response)

        # Test input string without response
        input_string_without_response = "<s>### Instruction:\nThis is an instruction.</s>"
        self.assertIsNone(extract_response_text(input_string_without_response))

    
if __name__ == '__main__':
    unittest.main()
