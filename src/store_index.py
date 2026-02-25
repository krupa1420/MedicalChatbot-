#load exisiting index
import os
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from src.helper import download_embeddings, filter_to_minimal_documents, load_pdf_files, text_split

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#set the environment variables for Pinecone and OpenAI API keys
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY


from pinecone import Pinecone
pinconeapikey = PINECONE_API_KEY
pc = Pinecone(api_key=pinconeapikey)


#load pdf file
extracted_data = load_pdf_files("/Users/krupa/Documents/Python Projects/LLM/MedicalChatbot-/Data")

#filtering data
minimal_docs = filter_to_minimal_documents(extracted_data)

#chunking data
chunked_data = text_split(minimal_docs)

#embedding model
embedding = download_embeddings() 

#creating databse
index_name = "medicalchabot"
if not pc.has_index(index_name):
    pc.create_index(
                name=index_name,  
                dimension=384, #embedding vector length
                metric="cosine", #similarity metric
                spec =ServerlessSpec(cloud="aws", region="us-east-1")
           )
    
index = pc.Index(index_name)

#store vector embedding in the index
docserach = PineconeVectorStore.from_documents(
    documents = chunked_data, 
    embedding=embedding, 
    index_name=index_name
    )

