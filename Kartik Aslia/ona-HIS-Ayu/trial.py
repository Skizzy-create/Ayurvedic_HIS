# Import streamlit for app dev
import streamlit as st

# Import transformer classes for generaiton
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
# Import torch for datatype attributes 
import torch
# Import the prompt wrapper...but for llama index
from llama_index.prompts.prompts import SimpleInputPrompt
# Import the llama index HF Wrapper
from llama_index.llms import HuggingFaceLLM
# Bring in embeddings wrapper
from llama_index.embeddings import LangchainEmbedding
# Bring in HF embeddings - need these to represent document chunks
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
# Bring in stuff to change service context
from llama_index import set_global_service_context
from llama_index import ServiceContext
# Import deps to load documents 
from llama_index import VectorStoreIndex, download_loader
from pathlib import Path

# Define variable to hold llama2 weights naming 
name = "meta-llama/Llama-2-7b-chat-hf"
# Set auth token variable from hugging face 
auth_token = "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"

@st.cache_resource
def get_tokenizer_model():
    # Create tokenizer
    tokenizer = AutoTokenizer.from_pretrained(name, cache_dir="D:\\LLM", use_auth_token=auth_token)

    # Create model
    model = AutoModelForCausalLM.from_pretrained(name, cache_dir="D:\\LLM"
                            , use_auth_token=auth_token, torch_dtype=torch.float16, 
                            rope_scaling={"type": "dynamic", "factor": 2}, load_in_8bit=True) 

    return tokenizer, model
tokenizer, model = get_tokenizer_model()

# Create a system prompt 
system_prompt = """<s>[INST] <<SYS>>
You are Myatri, an Ayurvedic practitioner.Tell your name and introducte your self as a ayurevedic practioner with a warm greatings.
Your goal is to offer advice on Ayurvedic medicine based on 
the user's illness or symptoms. Provide a prescription, dosage, composition of the medication, how to 
take it, precautions, and tips. Please reply in the following format:
How it will help you to get better
Herbs: [Herbs]
Precautions: [Precautions]
Tips: [Tips]
keep having a conversations in a humanly manner but dont type human gestures such as  *winks*, *smiling* ,*nods*, *adjusts glasses* etc. 
<</SYS>>
"""

# Throw together the query wrapper
query_wrapper_prompt = SimpleInputPrompt("{query_str} [/INST]")

# Create a HF LLM using the llama index wrapper 
llm = HuggingFaceLLM(context_window=4096,
                    max_new_tokens=256,
                    system_prompt=system_prompt,
                    query_wrapper_prompt=query_wrapper_prompt,
                    model=model,
                    tokenizer=tokenizer)

# Create and dl embeddings instance  
embeddings=LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
)

# Create new service context instance
service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embeddings
)
# And set the service context
set_global_service_context(service_context)

# Dwonload the PDF loader
PyMuPDFLoader = download_loader("PyMuPDFReader")
# Create PDF loader
loader = PyMuPDFLoader()
#load documents
documnets = loader.load(Path("C:/Users/LENOVO/PycharmProjects/Ayurvedic_HIS/Kartik Aslia/ona-HIS-Ayu/Data/PDFs/ayurvedic solution for diseases.pdf"),metadata=True)

# Create an index - we'll be able to query this in a sec
index = VectorStoreIndex.from_documents(documnets)
# Setup index query engine using LLM 
query_engine = index.as_query_engine()

# Create centered main title 
st.title("🚀ONA llama 🦙")
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')

# If the user hits enter
if prompt:
    response = query_engine.query(prompt)
    # ...and write it out to the screen
    st.write(response.response)

    # Display raw response object
    with st.expander('Response Object'):
        st.write(response.response)
    # Display source text
    with st.expander('Source Text'):
        st.write(response.get_formatted_sources())

