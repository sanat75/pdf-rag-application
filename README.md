# 📄 PDF RAG Application - Document Analysis & Q&A 🔍🤖  

This **Retrieval-Augmented Generation (RAG)** application enables **document analysis and question answering** for **PDF documents** using **ChromaDB embeddings** and **Ollama-based LLMs**.  

The project supports **two modes**:
- **📂 PDF-based processing** → Uses `docprocess.py`
- **🗄️ MongoDB-based processing** → Uses `fetchdata.py`  

---

## 🚀 Features
✅ **PDF Processing** – Extracts text from PDFs, splits them into chunks, and creates embeddings.  
✅ **MongoDB Mode** – Fetches data from MongoDB, generates embeddings, and enables search.  
✅ **ChromaDB Integration** – Stores document embeddings for efficient retrieval.  
✅ **Fast Querying** – Retrieves relevant chunks and uses a language model for answering questions.  
✅ **REST API** – Uses **FastAPI** for document uploads and querying.  
✅ **LLM-Powered Responses** – Uses **Ollama’s LLM** (`llama3.2:1b` by default).  

---

## 🛠️ Tech Stack
| Component       | Technology Used |
|----------------|----------------|
| **Backend**    | FastAPI |
| **Vector Database** | ChromaDB |
| **Embedding Model** | Ollama |
| **Database (Optional)** | MongoDB |
| **Document Processing** | PyPDFLoader (LangChain) |
| **Environment Management** | Python Virtual Environment |

---

## 📂 Project Structure

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/pdf-rag-application.git
cd pdf-rag-application
python -m venv myenv
# Activate (Windows)
myenv\Scripts\activate
# Activate (Mac/Linux)
source myenv/bin/activate
pip install -r requirements.txt
set MONGO_URI="your_mongo_uri"
set DATABASE_NAME="abc"
set COLLECTION_NAME="xyz"
## 👨‍💻 Contributors
- **Sanat Chaudhary** (sanat23122003@gmail.com)
- Open for contributions! 🚀


