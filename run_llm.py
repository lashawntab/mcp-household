# This logic is responsible for loading a pre-trained language model (Phi-3 mini) and using it to generate text completions given an input prompt.
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Set the default device for tensors to Apple's Metal Performance Shaders ("mps") and use 16-bit floating point precision for efficiency.
torch.set_default_device("mps")
torch.set_default_dtype(torch.float16)

# Define the model checkpoint to be loaded from Hugging Face Hub.
# This is Microsoft's Phi-3 mini instruct-tuned model, specialized for following instructions.
model_name = "microsoft/Phi-3-mini-4k-instruct"

# Initialize the tokenizer, which converts text to tokens that the model can process.
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Determine which device to use for model inference: "mps" (Apple Silicon GPU) if available, otherwise default to "cpu".
device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load the model weights. The model is loaded without using Hugging Face's device map, and moves to the specified device with float16 precision.
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map=None,
    trust_remote_code=False
).to(device=device, dtype=torch.float16)

def run_llm(prompt: str) -> str:
    """
    Given an input prompt (string), this function encodes the input, feeds it to the model,
    and decodes the generated output back to a string.
    """
    # Tokenize the prompt and move the resulting tensors to the model's device.
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    # Generate up to 300 new tokens as the response.
    outputs = model.generate(**inputs, max_new_tokens=150)
    # Decode the generated token IDs to a human-readable string, skipping special tokens.
    # result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    result = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    return result