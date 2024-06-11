import re
import dataset as ds


def extract_response_text(input_string):
    # define the input pattern for the response
    response_pattern = r'Response:\n(.*?)</s>'

    # use re.findall to extract the matching text
    matches = re.findall(response_pattern, input_string, re.DOTALL)

    # return the captured text or None if no match found
    return matches[0] if matches else None

# example usage with one argument
response = ds.train_dataset[0]["inputs"]
response = extract_response_text(response)
print(response)
