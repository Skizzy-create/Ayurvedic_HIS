<<<<<<< HEAD
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "tiiuae/falcon-7b-instruct",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    low_cpu_mem_usage=True,
)
tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")


def generate_text(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape)

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )

    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(output_text)

    # Remove Prompt Echo from Generated Text
    cleaned_output_text = output_text.replace(input_text, "")
    return cleaned_output_text


text_generation_interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.inputs.Textbox(label="Input Text"),
    ],
    outputs=gr.inputs.Textbox(label="Generated Text"),
    title="Falcon-7B Instruct",
).launch()
=======
import os
import urllib.request
import gradio as gr
from llama_cpp import Llama


def download_file(file_link, filename):
    # Checks if the file already exists before downloading
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(file_link, filename)
        print("File downloaded successfully.")
    else:
        print("File already exists.")


# Dowloading GGML model from HuggingFace
ggml_model_path = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q6_K.bin"
filename = "llama-2-13b-chat.ggmlv3.q6_K.bin"

download_file(ggml_model_path, filename)


llm = Llama(model_path=filename, n_ctx=512, n_batch=126)


def generate_text(prompt="Who is the CEO of Apple?"):
    output = llm(
        prompt,
        max_tokens=256,
        temperature=0.1,
        top_p=0.5,
        echo=False,
        stop=["#"],
    )
    output_text = output["choices"][0]["text"].strip()

    # Remove Prompt Echo from Generated Text
    cleaned_output_text = output_text.replace(prompt, "")
    return cleaned_output_text


description = "Vicuna-7B"

examples = [
    ["What is the capital of France?", "The capital of France is Paris."],
    [
        "Who wrote the novel 'Pride and Prejudice'?",
        "The novel 'Pride and Prejudice' was written by Jane Austen.",
    ],
    ["What is the square root of 64?", "The square root of 64 is 8."],
]

gradio_interface = gr.Interface(
    fn=generate_text,
    inputs="text",
    outputs="text",
    examples=examples,
    title="Vicuna-7B",
)
gradio_interface.launch()
>>>>>>> 2189976920f1331515f551d1d780819c927fe923
