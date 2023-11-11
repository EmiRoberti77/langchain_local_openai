import constants
import os

from pdfminer.high_level import extract_text
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI

def convert_pdf_to_text(pdf_path):
    return extract_text(pdf_path)

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.pdf'):
            text = convert_pdf_to_text(file_path)
            documents.append(text)
        elif filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                documents.append(file.read())
    return documents

os.environ['OPENAI_API_KEY'] = constants.APIKEY
documents = load_documents('data/')

index = VectorstoreIndexCreator().from_documents(documents)

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)
chatHistory = []
query = None
while(True):
  query = input(':>')
  if(query in ['close', 'q', 'quit', 'exit']):
    break
  result = chain({"question":query, "chat_history":chatHistory})
  print(result['answer'])