# Importing Required Packages
import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
print("=========================== All Libraries are Loaded Succesfully ========================")

# Function to create chunks from text folder
def get_text_chunks(text_folder):
    loader = DirectoryLoader(text_folder, glob = "**/*.txt", loader_cls = TextLoader, loader_kwargs = {'encoding': 'utf-8'})
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

print("===================== Function to Get Text Chunks ================================")

# Function to get the vector store
def get_vector_store(text_chunks):
    embeddings = HuggingFaceBgeEmbeddings(model_name = "all-MiniLM-L6-V2", model_kwargs = {'device':'cpu'})
    vector_store = FAISS.from_documents(text_chunks, embedding = embeddings)
    return vector_store

print("========================== Function to Create Vector Database ====================")