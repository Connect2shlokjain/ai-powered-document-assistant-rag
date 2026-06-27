# 📄 AI-Powered Document Assistant (RAG)

An AI-powered **Retrieval-Augmented Generation (RAG)** application built with **FastAPI**, **React**, **ChromaDB**, and **Groq LLM**.

The application allows users to upload PDF documents, automatically extracts and indexes their content using semantic embeddings, and answers natural language questions with source references using a Retrieval-Augmented Generation (RAG) pipeline.

---

# 🚀 Features

* 📄 PDF Upload
* 📑 PDF Text Extraction using PyMuPDF
* ✂️ Intelligent Document Chunking
* 🧠 Embedding Generation using Sentence Transformers
* 🗂️ ChromaDB Vector Database Integration
* 🔍 Semantic Similarity Search
* 🤖 AI Question Answering using Groq LLM
* 📖 Source References in Responses
* 🕒 Chat History using SQLite
* 🌐 React Frontend
* ⚡ FastAPI REST API
* 📚 Interactive Swagger Documentation
* 🐳 Docker Configuration Included

---

# 🛠 Tech Stack

| Layer            | Technology                               |
| ---------------- | ---------------------------------------- |
| Backend          | FastAPI                                  |
| Frontend         | React + Vite                             |
| PDF Processing   | PyMuPDF (fitz)                           |
| Chunking         | LangChain RecursiveCharacterTextSplitter |
| Embeddings       | sentence-transformers                    |
| Vector Database  | ChromaDB                                 |
| LLM              | Groq (Llama 3)                           |
| Chat History     | SQLite                                   |
| Validation       | Pydantic                                 |
| Containerization | Docker                                   |

---

# 📁 Project Structure

```text
document-assistant/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd document-assistant
```

## Create Virtual Environment

Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv myenv
source myenv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
MODEL_NAME=llama-3.3-70b-versatile

CHROMA_DB_PATH=app/database/chroma_db
COLLECTION_NAME=document_collection

DATABASE_URL=sqlite:///app/database/chat_history.db
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 📌 API Endpoints

| Method | Endpoint  | Description                          |
| ------ | --------- | ------------------------------------ |
| POST   | /upload/  | Upload PDF document                  |
| POST   | /chat/    | Ask questions from uploaded document |
| GET    | /history/ | Retrieve chat history                |
| DELETE | /history/ | Clear chat history                   |

---

# 🔄 RAG Workflow

1. Upload a PDF document.
2. Extract text using PyMuPDF.
3. Split the document into semantic chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Generate embedding for the user query.
7. Retrieve the Top-K relevant chunks.
8. Build contextual prompt.
9. Generate an answer using Groq LLM.
10. Return answer with source references.
11. Save conversation history.

---

# 🐳 Docker

Docker configuration files are included in the repository.

```bash
docker compose up --build
```

> **Note:** Docker configuration is included. Runtime validation and production deployment were not completed before the submission deadline.

---

# 📚 Future Improvements

* DOCX Support
* TXT Support
* Multiple Document Collections
* Authentication
* Streaming Responses
* OCR Support for Scanned PDFs
* Cloud Deployment
* CI/CD Pipeline

---

# 👨‍💻 Author

**Shlok Jain**

AI Engineer | Python Developer | Generative AI | Machine Learning
