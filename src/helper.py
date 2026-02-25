from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

#extract text from pdf file
def load_pdf_files(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls= PyPDFLoader)
    
    documents = loader.load()
    return documents

from typing import List
from langchain.schema import Document
from langchain_core.documents import Document

#filtering data 
def filter_to_minimal_documents(documents: List[Document]) -> List[Document]:
    #containing only source in metadata and page content 
    minimal_documents = []
    for doc in documents:
        minimal_doc = Document(
            page_content=doc.page_content,
            metadata={
                "source": doc.metadata.get("source", "")
            }
        )
        minimal_documents.append(minimal_doc)
    return minimal_documents

#splitting data into chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap=20)
    text = text_splitter.split_documents(minimal_docs)
    return text

#downloading the embedding model
from langchain.embeddings import HuggingFaceBgeEmbeddings
import torch

def download_embeddings():
    # downlload and return the embedding model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding = HuggingFaceBgeEmbeddings(model_name=model_name)
    return embedding

