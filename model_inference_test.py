import unittest
from langchain.chains import LLMChain
from langchain.llms import GradientLLM
from langchain.prompts import PromptTemplate
import base_model as bm

class TestLLMChain(unittest.TestCase):
    def setUp(self):
        # Set up the LLMChain object
        Fine_Tune_adapter_ID = bm.Fine_Tune_adapter.id
        llm = GradientLLM(
            model=Fine_Tune_adapter_ID,
            model_kwargs=dict(
                max_generated_token_count=128,
                temperature=0.7,
                top_k=50
            ),
        )
        template = """### Instruction: {Instruction} \n\n### Response:"""
        prompt = PromptTemplate(template=template, input_variables=["Instruction"])
        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

    def test_responses(self):
        questions = [
            "How does Clostridial Diseases impact milk production, reproductive performance, and overall well-being in cows?",
            "what are some of the risk factors associated with lameness in dairy cows?",
            "How dose lameness impact milk production, reproduction and overall well-being in cows?",
            "What diseases are prevalent in dairy small ruminant, and what management practice can mitigate their impact?",
            "what specific health management strategies should be implemented to prevent or treat common cow diseases?",
            "How do infrastructure, nutrition and human resources play a role in maintaining the health of dairy cows?"
        ]

        # Loop through each question and test the response
        for question in questions:
            with self.subTest(question=question):
                answer = self.llm_chain.run(Instruction=question)
                self.assertIsNotNone(answer)
                self.assertNotEqual(answer.strip(), "")  # Ensure the response is not empty

if __name__ == '__main__':
    unittest.main()
