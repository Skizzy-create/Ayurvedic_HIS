from fastapi import FastAPI
from llama_index import VectorStoreIndex, download_loader
from pathlib import Path
from langchain.document_loaders.pdf import PyMuPDFLoader
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import logging
import sys
from llama_index.llms import HuggingFaceLLM
from llama_index.embeddings import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.prompts.prompts import SimpleInputPrompt
from llama_index import set_global_service_context, ServiceContext
import uvicorn

app = FastAPI()

def setup_index():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    
    name = "meta-llama/Llama-2-7b-chat-hf"
    auth_token = "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"
    
    tokenizer = AutoTokenizer.from_pretrained(name, cache_dir="D:\\LLM")
    model = AutoModelForCausalLM.from_pretrained(name, cache_dir="D:\\LLM",
                                                use_auth_token=auth_token, torch_dtype=torch.float16,
                                                rope_scaling={"type": "dynamic", "factor": 2}, load_in_8bit=True)
    
    system_prompt = "<s>[INST] <<SYS>>\nYou are Myatri, an Ayurvedic practitioner. Tell your name and introduce yourself as an Ayurvedic practitioner with warm greetings.\nYour goal is to offer advice on Ayurvedic medicine based on the user's illness or symptoms. Provide a prescription, dosage, composition of the medication, how to take it, precautions, and tips.\nPlease reply in the following format:\nHow it will help you to get better: [effect on body]\nHerbs: [Herbs and Quantity only]\nPrecautions: [Precautions]\nTips: [Tips]\nKeep having conversations in a humanly manner but don't type human gestures such as *winks*, *smiling*, *nods*, *adjusts glasses*, etc.\n<</SYS>>"
    query_wrapper_prompt = SimpleInputPrompt("{query_str} [/INST]")
    llm = HuggingFaceLLM(context_window=4000,
                        max_new_tokens=3000,
                        system_prompt=system_prompt,
                        query_wrapper_prompt=query_wrapper_prompt,
                        model=model,
                        tokenizer=tokenizer)
    embeddings = LangchainEmbedding(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
    service_context = ServiceContext.from_defaults(chunk_size=3000, llm=llm, embed_model=embeddings)
    set_global_service_context(service_context)
    
    PyMuPDFLoader = download_loader("PyMuPDFReader")
    loader = PyMuPDFLoader()
    documents = loader.load(Path("C:/Users/LENOVO/PycharmProjects/Ayurvedic_HIS/Kartik Aslia/ona-HIS-Ayu/Data/PDFs/shushruta samhita.pdf"), metadata=True)
    
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    
    return query_engine

query_engine = setup_index()

@app.get("/prompt/{prompt_str}")
async def generate_text(prompt: str):
    response = query_engine.query(prompt)
    return {"Prompt" : prompt ,"response" : response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
