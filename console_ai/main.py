import constants as constants
from constants import console as out
from constants import ColorWrapper as CR
import os

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

os.environ['OPENAI_API_KEY'] = constants.APIKEY
out(msg=constants.LINE_BREAK, color=CR.blue, reset=False)
print('DATA_ROOT', constants.DOCUMENT_ROOT)
print('PERSIST_MODE', constants.PERSIST)
print('PERSIST_ROOT', constants.PERSIST_ROOT)
out(msg=constants.LINE_BREAK, color=CR.blue, reset=True)


if constants.PERSIST and os.path.exists(constants.PERSIST_ROOT):
  out(msg=constants.RESUME_INDEX, color=CR.cyan, reset=True)
  vectorstore = Chroma(persist_directory=constants.PERSIST_ROOT, embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = DirectoryLoader(constants.DOCUMENT_ROOT)
  if constants.PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":constants.PERSIST_ROOT}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)
chatHistory = []
query = None
while(True):
  query = input(constants.INPUT_READY).strip()
  if(query in constants.exitCommands):
    break
  try:
    result = chain({"question":query, "chat_history":chatHistory})
    out(msg=result['answer'], color=CR.green, reset=True)
  except Exception as e:
    out(msg=str(e), color=CR.red, reset=True)
out(msg=constants.EXIT, color=CR.yellow, reset=True)
    
