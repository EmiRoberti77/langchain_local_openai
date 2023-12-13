from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
embeddings = OpenAIEmbeddings()
text = "Algoritma is a data science school based in Indonesia and Supertype is a data science consultancy with a distributed team of data and analytics engineers."
doc_embeddings = embeddings.embed_documents([text])
print(doc_embeddings)
