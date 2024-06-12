import os
import json
from gradientai import Gradient
from langchain.chains import LLMChain
from langchain.llms import GradientLLM
from langchain.prompts import PromptTemplate

os.environ['GRADIENT_ACCESS_TOKEN'] = "4k7ZgJFjMZE8O0U3SPyMXnVFni9korHG"
os.environ['GRADIENT_WORKSPACE_ID'] = "8e577a48-b54d-4f28-817e-ca6fe4530478_workspace"

access_token = os.environ["GRADIENT_ACCESS_TOKEN"]
workspace_id = os.environ["GRADIENT_WORKSPACE_ID"]

gradient = Gradient()

print("Available Base Models")
for i in gradient.list_models(only_base=True):
    print("\t", i)

base_model_id = "NousResearch/Nous-Hermes-Llama2-13b"
base_model_name = "nous-hermes2"
base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

print("\nBase Model Chosen :", base_model)

our_finetune_model_name = "llama2-13b/Dairy Farming"
Fine_Tune_adapter = base_model.create_model_adapter(
    name=our_finetune_model_name,
    learning_rate=0.00005,
    rank=8,
)

hyperparameters = {
    "block_size": 1024,
    "model_max_length": 2048,
    "padding": "right",
    "use_flash_attention_2": False,
    "disable_gradient_checkpointing": False,
    "logging_steps": -1,
    "evaluation_strategy": "epoch",
    "save_total_limit": 1,
    "save_strategy": "epoch",
    "auto_find_batch_size": False,
    "mixed_precision": "fp16",
    "epochs": 3,
    "batch_size": 100,
    "warmup_ratio": 0.1,
    "gradient_accumulation": 1,
    "optimizer": "adamw_torch",
    "scheduler": "linear",
    "weight_decay": 0,
    "max_grad_norm": 1,
    "seed": 42,
    "apply_chat_template": False,
    "quantization": "int4",
    "target_modules": "",
    "merge_adapter": False,
    "peft": True,
    "lora_r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05
}

print(f"Base model id                   : {Fine_Tune_adapter.base_model_id}")
print(f"Fine tune model Name            : {Fine_Tune_adapter.name}")
print(f"Fine tune model adapter id      : {Fine_Tune_adapter.id}")

print("\n\n")
print("Size of object in memory, in bytes.", Fine_Tune_adapter.__format__.__sizeof__())
Fine_Tune_adapter.__dict__