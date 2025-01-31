from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from pymongo import MongoClient
import os
import shutil
from globalvariables import *

# MongoDB connection details
MONGO_URI = ""
DATABASE_NAME = ""  # Update this to match your database name
COLLECTION_NAME = ""  # The collection to fetch data from
print("fetchdata.py loaded successfully")



# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def fetch_data_from_mongo():
    """Fetches data from MongoDB"""
    documents = collection.find({}, {"_id": 0})  # Excluding _id field
    return [doc for doc in documents]

def split_document(document_texts):
    """Splits text into chunks"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=256)
    return splitter.split_text(document_texts)

def get_embeddings_function(model_name):
    """Returns embedding function"""
    return OllamaEmbeddings(model=model_name)

def create_embedding(chunks, modelname):
    """Creates embeddings"""
    embeddingmodel = get_embeddings_function(modelname)
    return embeddingmodel.embed_documents(chunks)

def add_docs(client, chunks):
    """Adds document chunks to ChromaDB"""
    client.add_documents(chunks)

def getclient(collection_name, model_name, directory):
    """Initializes ChromaDB"""
    return Chroma(collection_name=collection_name, embedding_function=get_embeddings_function(model_name), persist_directory=directory)

def process_mongo_data():
    """Processes MongoDB data and stores embeddings"""
    data = fetch_data_from_mongo()
    text_data = " ".join([str(doc) for doc in data])  # Convert documents to a single text block
    chunks = split_document(text_data)

    client = getclient("mongo_collection", MODEL, DB_DIR)  # Store embeddings in ChromaDB
    add_docs(client=client, chunks=chunks)

    del client
    return {"message": "MongoDB data processed and stored in ChromaDB!"}
