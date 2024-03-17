import gradio as gr
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

loader = CSVLoader(file_path='myData.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

data = loader.load()

db = FAISS.from_documents(data, embeddings)

def find_similar_things(user_input):
    docs = db.similarity_search(user_input)
    return docs[0], docs[1].page_content

input_text = gr.Textbox(lines=3, label="You: ")
iface = gr.Interface(fn=find_similar_things, inputs=input_text, outputs=["text", "text"], title="Educate Kids", description="Hey, Ask me something & I will give out similar things")
iface.launch()

