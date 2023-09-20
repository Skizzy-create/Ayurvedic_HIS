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