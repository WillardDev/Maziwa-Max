import re
import json
import model_inference as mi
import dataset as ds
from nltk.translate.bleu_score import corpus_bleu
from rouge import Rouge
from langchain.chains import LLMChain
from langchain_community.llms import GradientLLM
from langchain.prompts import PromptTemplate
import os


def compute_rouge_scores(hypotheses, references):
    rouge = Rouge()
    scores = rouge.get_scores(hypotheses, references, avg=True)
    return scores

def compute_bleu_score(target_response, llm_responses):
    # calculate the bleu score
    bleu_score = corpus_bleu([target_response.split()], [llm_responses.split()])
    return bleu_score

def extract_instruction_text(input_string):
    # define th einput pattern
    input_pattern = r'<s>### Instruction:\n(.*?)\n'

    # use re.findall to extract the matching text
    matches = re.findall(input_pattern, input_string, re.DOTALL)

    #return the captured text or None if no match found
    return matches[0] if matches else None

def extract_response_text(input_string):
    # define the input pattern for the response
    response_pattern = r'Response:\n(.*?)</s>'

    # use re.findall to extract the matching text
    matches = re.findall(response_pattern, input_string, re.DOTALL)

    # return the captured text or None if no match found
    return matches[0] if matches else None

def evaluate(sample=None, count=0):
    print("\n=================================== Evaluation =================================== ")
    
    # input_pattern = r'<s>### Instruction:\n(.*?)\n'
    # response_pattern = r'Response:\n(.*?)<s/>'
    bleu_scoreS = []
    rouge_scoreS = []

    if count != 0:
        iteration = count - 1
    else:
        iteration = count

    while iteration >= 0:
        input_query = extract_instruction_text(sample[iteration]["inputs"])
        target_response = extract_response_text(sample[iteration]["inputs"])

        if input_query and target_response is not None:
            print("\n ---------------------------------------------------------------")
            print("INPUT QUERY:\n", input_query)
            print("\nTARGET RESPONSE:\n", target_response)

            llm_responses = mi.llm_chain.run(Instruction=f"{input_query}")
            print("\nLLM RESPONSE:\n", llm_responses)

            rouge_scores = compute_rouge_scores(llm_responses, target_response)

            bleu_score = compute_bleu_score(target_response, llm_responses)
            print("\nBLEU Score:", bleu_score)
            print("ROUGE Scores:")
            print("\tROUGE-1 F1 Score:", rouge_scores["rouge-1"]["f"])
            print("\tROUGE-2 F1 Score:", rouge_scores["rouge-2"]["f"])
            print("\tROUGE-L F1 Score:", rouge_scores["rouge-l"]["f"])
            rouge_scoreS.append((rouge_scores["rouge-1"]["f"], rouge_scores["rouge-2"]["f"], rouge_scores["rouge-l"]["f"]))
            bleu_scoreS.append(bleu_score)

        iteration -= 1

    if count > 0:
        rouge_scores1 = 0
        rouge_scores2 = 0
        rouge_scores3 = 0
        bleu_scoreA = 0

        for i in bleu_scoreS:
            bleu_scoreA += i
        for i in rouge_scoreS:
            rouge_scores1 += i[0]
            rouge_scores2 += i[1]
            rouge_scores3 += i[2]

        print("\nAverageBLEU Score:", bleu_scoreA)
        print(f"Average ROUGE Scores for {count} samples")
        print("\tAverage ROUGE-1 F1 Score:", rouge_scores1 / count)
        print("\tAverage ROUGE-2 F1 Score:", rouge_scores2 / count)
        print("\tAverageROUGE-L F1 Score:", rouge_scores3 / count)

    print("\n ---------------------------------------------------------------")

evaluate(sample=ds.train_dataset, count=3)