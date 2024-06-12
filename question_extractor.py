import re
import dataset as ds
import model_inference as mi


def extract_instruction_text(input_string):
    # define th einput pattern
    input_pattern = r'<s>### Instruction:\n(.*?)\n'

    # use re.findall to extract the matching text
    matches = re.findall(input_pattern, input_string, re.DOTALL)

    #return the captured text or None if no match found
    return matches[0] if matches else None


question = ds.train_dataset[0]["inputs"]
question = extract_instruction_text(question)
print("question :\n\t", question)
answer = mi.llm_chain.run(Instruction=f"{question}")
print("Answer :\n\t", answer)