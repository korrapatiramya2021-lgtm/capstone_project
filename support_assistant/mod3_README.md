#

Zepto Policy RAG Assistant

Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system for answering questions about Zepto policy documents. The application loads eight policy documents, creates embeddings using the "all-MiniLM-L6-v2" sentence transformer model, stores the embeddings in ChromaDB, and retrieves the most relevant information to answer user queries. A LangGraph workflow routes policy-related questions through retrieval while handling general questions separately. The application exposes a FastAPI endpoint ("POST /ask") that returns responses in a validated JSON format.

---

Architecture

1. Ingestion

- Load all 8 policy documents from the "docs" folder.
- Read the contents of each document.

2. Chunking

- Split each document into fixed-size chunks (500 characters).

3. Embedding

- Generate embeddings for every chunk using:
  - "sentence-transformers/all-MiniLM-L6-v2"

4. Storage

- Store chunk IDs, document text, metadata, and embeddings in a ChromaDB collection named "zepto_policy".

5. Retrieval

- Embed the user query.
- Retrieve the Top-3 most similar chunks from ChromaDB using cosine similarity.

6. Generation

- The LangGraph workflow determines whether retrieval is required.
- In mock mode, the application returns:
  - "Based on the retrieved context: <top retrieved chunk>"
- General questions return:
  - "I can only answer questions about Zepto policies right now."

---

RAG Pipeline

Documents
      │
      ▼
Document Loading
      │
      ▼
Chunking
      │
      ▼
Embeddings (all-MiniLM-L6-v2)
      │
      ▼
ChromaDB
      │
      ▼
LangGraph
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Retrieve   Direct
Answer     Answer
      │
      ▼
JSON Response

---

LangGraph Workflow

Nodes:

1. classify_intent
2. retrieve_and_answer
3. direct_answer

Routing:

- policy_question → retrieve_and_answer
- general_question → direct_answer

---

MOCK_LLM

Default:

MOCK_LLM=1

Behavior:

- Keyword-based intent classification.
- Real ChromaDB retrieval.
- Mock answer generation using the top retrieved chunk.
- General questions return a fixed response.

Optional:

MOCK_LLM=0

Behavior:

- LLM-based intent classification.
- LLM generates grounded answers using the structured prompt.
- Retry validation up to two times if JSON output is invalid.

---

FastAPI Endpoint

POST /ask

Request

{
  "query": "How do I cancel my order?"
}

Response

{
  "answer": "Based on the retrieved context: Orders may be cancelled before dispatch...",
  "sources": [
    "policy1_0",
    "policy1_1",
    "policy2_0"
  ],
  "confidence": 1.0
}

---

Example 1

Request

{
  "query": "How do I cancel my delivery?"
}

Response

{
  "answer": "Based on the retrieved context: ...",
  "sources": [
    "policy3_0",
    "policy3_1",
    "policy5_0"
  ],
  "confidence": 1.0
}

---

Example 2

Request

{
  "query": "Who is the Prime Minister of India?"
}

Response

{
  "answer": "I can only answer questions about Zepto policies right now.",
  "sources": [],
  "confidence": 1.0
}

---

Running the Project

Install dependencies:

pip install -r requirements.txt

Run the ingestion process:

python ingest.py

Run the FastAPI server:

uvicorn main:app --host 0.0.0.0 --port 7860

---

Technologies Used

- Python
- FastAPI
- LangGraph
- ChromaDB
- Sentence Transformers
- all-MiniLM-L6-v2
- Pydantic
