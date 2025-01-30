

from fastapi.middleware.cors import CORSMiddleware

import docprocess
from query import chatapplicationApi
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import os
import shutil
from globalvariables import *


app = FastAPI()

FILE_DIR = 'data/'
DB_DIR = 'chromaDB'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the specific origin(s) of your frontend for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

@app.post("/uploadpdf/")
async def upload_pdf(file: UploadFile = File(...)):

    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Read the file's contents
    contents = await file.read()

    # Optionally save the PDF to disk
    
    save_path = os.path.join(FILE_DIR,file.filename)
    print('filename :',save_path)
    # save_path = f"uploaded_{file.filename}"
    with open(save_path, "wb") as f:
        f.write(contents)
    file_path = os.path.join(FILE_DIR ,file.filename)
    document = docprocess.load_document(file_path)
    chunks = docprocess.split_document(document)

    client = docprocess.getclient(file.filename,MODEL,DB_DIR)
    docprocess.add_docs(client=client,chunks=chunks)

    del client
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "message": f"PDF file '{file.filename}' uploaded successfully!",
    }




@app.get('/getresult/{filename}/{query}')
def queryengine(filename:str,query:str):
    
    response = chatapplicationApi(query,filename,MODEL,DB_DIR)

    return response

@app.get('/delete')
def deletedata():
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
    

    return {"status":"deleted successfully all the files and directories"}


