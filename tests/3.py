from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

loader = TextLoader('../README.md')
res = loader.load()
print(res)

dirLoader = DirectoryLoader('./news')
docs = dirLoader.load()
print('documents read', len(docs))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=20, length_function=len, add_start_index=True)

texts = text_splitter.split_documents(docs)
print('texts len', len(texts))
print(texts[34])

embedding = OpenAIEmbeddings()
db = Chroma.from_documents(texts, embedding)
retriever = db.as_retriever()

retrieved_response = retriever.invoke("effect of covid in the retail sector")
print(retrieved_response[0].page_content)
