import base_model as bm
import dataset as ds

print(f"Our Model id: {bm.Fine_Tune_adapter.id}")

# num_epochs is the numbr of times you fine tune the model
# more epochs tends to get better results, but you also run a risk of overfitting
num_epochs = 1
count = 0
print("================================================================\n")
print("Fine tuning . . . \n")

while count < num_epochs:
    print(f"Fine-tuning the model, iteration {count + 1}")
    s = 0
    n = 1
    
    for batch in ds.batches:
        print(f"Batch {n} range: {s} : {(s + batch)}")

        # try to fine tune the model with the chunk of samples
        while True:
            try:
                metric = bm.Fine_Tune_adapter.fine_tune(samples=ds.train_dataset[s: + batch])
                print(f"\t Batch {n} Evaluation :", metric)
                break
            except:
                pass

        s += batch
        n += 1
    count = count + 1
