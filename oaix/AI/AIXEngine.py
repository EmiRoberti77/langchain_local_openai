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
from AI.AIXBase import AIXBase

class AIXEngine(AIXBase):
  def __init__(self):
    out(msg='OAIX Engine', color=CR.green, reset=True)
    super().__init__()
    self.embedding = OpenAIEmbeddings()

    self.loader = DirectoryLoader('news', glob="**/*.txt")
    self.documents = self.loader.load()
    print('documents len',len(self.documents))

    self.text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
    self.texts = self.text_splitter.split_documents(self.documents)

    self.vec_store = Chroma.from_documents(self.texts, self.embedding)

    self.qa = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                      chain_type="stuff", 
                                      retriever=self.vec_store.as_retriever())

  def prompt(self, **kwargs):
    input=kwargs['input']
    return self.qa.run(input)
    
