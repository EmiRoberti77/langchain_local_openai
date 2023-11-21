from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('OPENAI_API_KEY'))
documents = SimpleDirectoryReader('../news').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
r = query_engine.query("how did the pandemic effect business")
print(r)