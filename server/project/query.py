
from langchain_ollama import ChatOllama,OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_chroma.vectorstores import Chroma
from globalvariables import *

def get_embeddings_function(model_name):
    return OllamaEmbeddings(model=model_name)


def getchatModel(model_name):
    return ChatOllama(model=model_name)

def getChroma(collection_name,model_name,DB_PATH = "chromaDB"):
    return Chroma(collection_name=collection_name,embedding_function=get_embeddings_function(model_name),persist_directory=DB_PATH)



def chatapplicationApi(query:str,collectionName:str,modelName:str,dbpath:str):
    prompt_template = PromptTemplate.from_template(
        """
        Answer the question based on the following context:
        {context}
        Answet the question based on above context : 
        {question}
    """
    )

    chatModel = ChatOllama(model=modelName)

    db = Chroma(collection_name=collectionName,embedding_function=get_embeddings_function(modelName),persist_directory=dbpath)

    results = db.similarity_search_with_score(query)

    context = ""
    for doc,score in results:
        context += doc.page_content
    prompt = prompt_template.invoke({"context":context,"question":query})

    response = chatModel.invoke(prompt)

    del db

    return {'content':response.content,'metadata':response.response_metadata}
