from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
import torch
import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
#importing llama index HF wrapper
from llama_index.llms import HuggingFaceLLM
# Bring in embeddings wrapper
from llama_index.embeddings import LangchainEmbedding
#Bring in HuggingFace embeddings wrapper - need these to represent documents chunks
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
# Prompt wrapper
from llama_index.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings import LangchainEmbedding
#create new service context
from llama_index import set_global_service_context
from llama_index import ServiceContext
# import deps to load documents
from llama_index import VectorStoreIndex, download_loader
from pathlib import Path
from langchain.document_loaders.pdf import PyMuPDFLoader
import streamlit as st

device = 'cuda' if torch.cuda.is_available() else 'cpu'
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
# Define variable to hold llama2-13B-chat weight naming
name = "meta-llama/Llama-2-7b-chat-hf"

auth_token = "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"

@st.cache_resource
def get_tokenizer_model():
    # Create tokenizer
    tokenizer = AutoTokenizer.from_pretrained(name, cache_dir="D:\\LLM")

    # loading model
    model = AutoModelForCausalLM.from_pretrained(name, cache_dir="D:\\LLM",
                                                 use_auth_token=auth_token, torch_dtype = torch.float16, 
                                                rope_scaling={"type":"dynamic","factor":2}, load_in_8bit=True)
    return tokenizer, model

tokenizer, model = get_tokenizer_model()

<<<<<<< HEAD
system_prompt = "<s>[INST] <<SYS>>\
Hello, I am Myatri, an Ayurvedic practitioner. Introduce your self as a personal Ayurvedic Assistant.\
Based on your illness or symptoms or the prompt given by the user, you will provide a ayurvedic solution to the problem , as well as the dosage, composition of the medication, instructions on how to take it, precautions, and additional tips. Here's the format of my response:\
- How the medication will help: [Explanation of how the medication will aid in healing]\
- Herbs: [List of herbs included in the medication]\
- How to make the medicine at home: [Instructions on how to prepare the medicine with precise measurements]\
- Precautions: [Any precautions to be aware of while taking the medication]\
- Tips: [Additional tips for managing the illness or enhancing the effectiveness of the medication]\
Please note that while I strive to provide a human-like interaction, I won't use human gestures such as *winks*, *smiling*, *nods*, *adjusts glasses*, etc.\
<</SYS>>"

=======
system_prompt = """<s>[INST] <<SYS>>
You are Myatri, an Ayurvedic practitioner.Tell your name and introducte your self as a ayurevedic practioner with a warm greatings.
Your goal is to offer advice on Ayurvedic medicine based on the user's illness or symptoms. Provide a prescription, dosage,
composition of the medication, how to take it, precautions, and tips. Please reply in the following format:
How it will help you to get better: []
Herbs: [Herbs and Quantity]
Precautions: [Precautions]
Tips: [Tips]
keep having a conversations in a humanly manner but dont type human gestures such as  *winks*, *smiling* ,*nods*, *adjusts glasses* etc. 
<</SYS>>
"""
>>>>>>> 2189976920f1331515f551d1d780819c927fe923


# Create a prompt wrapper
query_wrapper_prompt = SimpleInputPrompt("{query_str} [/INST]")

# Create a HF LLM using the LLama index wrapper
llm = HuggingFaceLLM(context_window=4000,
                     max_new_tokens=3000,
                     system_prompt=system_prompt,
                     query_wrapper_prompt=query_wrapper_prompt,
                     model=model,
                     tokenizer=tokenizer)


embeddings = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
)

# create new service context
service_context = ServiceContext.from_defaults(
    chunk_size=3000,
    llm = llm,
    embed_model=embeddings
)

# and set the context service
set_global_service_context(service_context)

# Dwonload the PDF loader
PyMuPDFLoader = download_loader("PyMuPDFReader")
# Create PDF loader
loader = PyMuPDFLoader()
#load documents
documnets = loader.load(Path("C:/Users/LENOVO/PycharmProjects/Ayurvedic_HIS/Kartik Aslia/ona-HIS-Ayu/Data/PDFs/shushruta samhita.pdf"),metadata=True)

# create an index - this will take a while to query
index = VectorStoreIndex.from_documents(documnets)
# setting up index query engine using llm
query_engine = index.as_query_engine()

#create centred main title
st.title("🚀ONA llama 🦙")
#create a text input box for the user
prompt = st.text_input("Please input your symptoms")

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

if prompt:
    response = query_engine.query(prompt)
    
    # Write it out to the screen
    st.write(response.response)
    
    with st.expander('Response Object'):
        st.write(response)
        
    # Display raw response object
    with st.expander("Source Object"):
        st.write(response.get_formatted_sources())
