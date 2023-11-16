from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from constants import console as out
from constants import ColorWrapper as CR
import constants
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
embedding = OpenAIEmbeddings()

loader = DirectoryLoader('news', glob="**/*.txt")
documents = loader.load()
print('documents len',len(documents))

text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

vec_store = Chroma.from_documents(texts, embedding)

qa = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                 chain_type="stuff", 
                                 retriever=vec_store.as_retriever())

def query(q:str)->None:
  out(msg=f"Query: {q}", color=CR.green, reset=True)
  out(msg=f"Answer: {qa.run(q)}", color=CR.yellow, reset=True)

user_input = None
while(True):
  user_input = input(':>')
  if user_input in constants.exitCommands:
    break
  query(user_input)

out(msg=constants.EXIT, color=CR.blue, reset=True)












