from langchain.chains import LLMChain
from langchain.llms import GradientLLM
from langchain.prompts import PromptTemplate
import gradientai
import os
import base_model as bm

# fine tune adapter.id
Fine_Tune_adapter_ID = bm.Fine_Tune_adapter.id
# print(Fine_Tune_adapter_ID)

# creating a gradientLLM object
llm = GradientLLM(
    model = Fine_Tune_adapter_ID,
    model_kwargs = dict(
        max_generated_token_count = 128, # adjust how your model generates completions
        temperature = 0.7, # randomness
        top_k = 50 # restricts the model to pick from k most likely words,
    ),
)

template = """### Instruction: {Instruction} \n\n### Response:"""
prompt = PromptTemplate(template=template, input_variables=["Instructon"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

Question1 = "How does Clostridial Diseases impact milk production, reproductive performance, and overall well-being in cows?"
Question2 = "what are some of the risk factors associated with lameness in dairy cows?"
Question3 = "How dose lameness impact mill production, reproduction and overall well-being in cows"
Question4 = "What diseases are prevelant in dairy small ruminant, and what managment practice can mitigate their impact "
Question5 = "what specific health managment strategies should be implemented to prevent or treat common cow diseases?"
Question6 = "How do infrastructure, nutrition and human resources play a role in maintaining the health of daily cows?"


# print("Question :\n", Question1)
# Answer = llm_chain.run(Instruction=f"{Question1}")
# print("Answer :\n", Answer, "\n\n")

# print("Question :\n", Question2)
# Answer = llm_chain.run(Instruction=f"{Question2}")
# print("Answer :\n", Answer, "\n\n")

# print("Question :\n", Question3)
# Answer = llm_chain.run(Instruction=f"{Question3}")
# print("Answer :\n", Answer, "\n\n")

# print("Question :\n", Question4)
# Answer = llm_chain.run(Instruction=f"{Question4}")
# print("Answer :\n", Answer, "\n\n")

# print("Question :\n", Question5)
# Answer = llm_chain.run(Instruction=f"{Question5}")
# print("Answer :\n", Answer, "\n\n")

# print("Question :\n", Question6)
# Answer = llm_chain.run(Instruction=f"{Question6}")
# print("Answer :\n", Answer, "\n\n")