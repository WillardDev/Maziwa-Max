import json

# load the dataset from the JSON file
with open("./dataset/dairy1.json") as f:
    train_dataset = json.load(f)

print("Dataset Size: ", len(train_dataset))

def divide_into_batches(number, chunk_size):
    batches = []
    while number > 0:
        if number >= chunk_size:
            batches.append(chunk_size)
            number -= chunk_size
        else:
            batches.append(number)
            break
    return batches

# divide the dataset into chunks of 100 each
batches = divide_into_batches(len(train_dataset), 100)
print("Batch size")
print(batches)