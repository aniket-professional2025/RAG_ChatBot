# Importing Required Packages
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Loading Environmental Variables
load_dotenv()

print("=============== Importing All Required Libraries =========================")

# Define a function to build the rag chain
def get_rag_chain(vector_store):
    llm = ChatOpenAI(model_name = "gpt-4o", temperature = 0.5)
    prompt = ChatPromptTemplate.from_template("""
        Answer the following question based only on the provided context.
        <context>
        {context}
        </context>
        Question: {input}
            """)
    doc_chain = create_stuff_documents_chain(llm, prompt)
    retriver = vector_store.as_retriever()
    retrieval_chain = create_retrieval_chain(retriver, doc_chain)
    return retrieval_chain

print("================= Function to Get the RAG chain =========================")

# Define Function to get the answer
def get_answer(question, vector_store):
    chain = get_rag_chain(vector_store)
    response = chain.invoke({"input": question})
    return response['answer']

print("================ Function to Get Answer ================")