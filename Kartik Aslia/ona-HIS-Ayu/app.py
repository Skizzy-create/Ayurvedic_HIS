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

# system prompt
system_prompt = """<s>[INST] <<SYS>>
You are Myatri. Tell your name.
your goal is to Offer advice on ayurevedic medicaine based on the illness or the symptoms of the user. <</SYS>>"""


# Create a prompt wrapper
query_wrapper_prompt = SimpleInputPrompt("{query_str} [/INST]")

# Create a HF LLM using the LLama index wrapper
llm = HuggingFaceLLM(context_window=3000,
                     max_new_tokens=2000,
                     system_prompt=system_prompt,
                     query_wrapper_prompt=query_wrapper_prompt,
                     model=model,
                     tokenizer=tokenizer)


embeddings = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
)

# create new service context
service_context = ServiceContext.from_defaults(
    chunk_size=2000,
    min_chunk_overlap=500,  # some reasonable value less than chunk size
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

if prompt:
    response = query_engine.query(prompt)
    #...and write it out to the screen
    st.write(response)
    with st.expander('Response Object'):
        st.write(response)
    # Display raw response object
    with st.expamnder("Source Object"):
        st.write(response.get_formatted_sources())
    
    