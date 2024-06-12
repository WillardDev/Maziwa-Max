import unittest
import retrieval_augmented_generation as rag

class TestLLMFunctionality(unittest.TestCase):
    def test_answer_retrieval(self):
        # Test a query related to dairy farming
        query = "What is the recommended breed to rear in Nyanza Province?"
        answer = rag.LLM_Run(query)
        self.assertIsNotNone(answer)
        self.assertIsInstance(answer, str)
        self.assertNotIn("I don't know", answer)  # Check if the answer doesn't contain "I don't know"
        
        # You can add more test cases here to cover different scenarios
    
    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
