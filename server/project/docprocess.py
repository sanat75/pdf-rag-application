from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma

import sys
import os
import shutil
from globalvariables import *

def load_document(file_path):
    docuement_loader = PyPDFLoader(file_path)

    return docuement_loader.load()

def split_document(document):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=256,
    )

    return splitter.split_documents(document)


def get_embeddings_function(model_name):
    return OllamaEmbeddings(model=model_name)



def create_embedding(chunks,modelname:str):
    embeddingmodel = get_embeddings_function(modelname)
    return embeddingmodel.embed_documents(chunks)


def add_docs(client,chunks):
    client.add_documents(chunks)

def getclient(collection_name,model_name,directory):
    return Chroma(collection_name=collection_name,embedding_function=get_embeddings_function(model_name),persist_directory=directory)


def erase(FILE_DIR,DB_DIR):
     
    if os.path.exists(FILE_DIR):
        for item in os.listdir(FILE_DIR):
            item_path = os.path.join(FILE_DIR, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):  # Check for files and symbolic links
                os.remove(item_path)
            elif os.path.isdir(item_path):  # Check for subdirectories
                shutil.rmtree(item_path)
    else:
        return {"error":f"something went wrong while deleting in {FILE_DIR}"}

    if os.path.exists(DB_DIR):
        for item in os.listdir(DB_DIR):
            item_path = os.path.join(DB_DIR, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):  # Check for files and symbolic links
                os.remove(item_path)
            elif os.path.isdir(item_path):  # Check for subdirectories
                shutil.rmtree(item_path)
        # print(f"Cleared all contents from: {DB_DIR}")
    else:
        return {"error":f"something went wrong while deleting in {DB_DIR}"}