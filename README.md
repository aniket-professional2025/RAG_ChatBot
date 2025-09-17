# RAG_ChatBot
This repository contains the process of building a chatbot using RAG (Retrieval Augmented Generation) using the Hawaii Wild Fire data available on GitHub

### Deatils:
In this project, when the `app.py` file is run from the CLI using the code `streamlit run app.py`, the dataset will be chuncked into different parts. After partition all the text inside those .txt file will be converted into vector databases. This will happen each time the code is run. 

After this, when the user will ask anything, it will search the vector databases that are created and the RAG agent will answer the question. 

The dataset that is used in this RAG ChatBot project is fetched from the github repo: <https://github.com/poloclub/Fine-tuning-LLMs>
