<p align="center">
  <img src="https://github.com/ather-ops/Amazn-AI/blob/main/Assets/Amazn.png" alt="Amazn AI Banner" width="100%">
</p>

<h1 align="center">Amazn AI</h1>

<p align="center">
  An AI-powered Amazon customer support assistant built with RAG, FAISS, Sentence Transformers, and an agent-based architecture.
</p>

---

## Overview

Amazn AI is an end-to-end **Retrieval-Augmented Generation (RAG)** application designed to provide intelligent assistance for Amazon product discovery and customer-support questions.

Instead of relying only on keyword search, the system uses semantic search to retrieve relevant information from dedicated knowledge bases and uses an AI agent to decide which tool should handle the user's request.

The project currently supports:

* Amazon product search
* Customer-support knowledge retrieval
* Natural-language product queries
* Return and refund-related questions
* Agent-based routing between RAG tools

The project is being developed as a practical AI Engineering project covering the complete workflow from data preparation and embeddings to vector search, RAG, agent orchestration, and deployment.

---

## Features

### 🛍️ Product RAG

* Semantic search over Amazon product data
* Natural-language product queries
* Sentence Transformers embeddings
* FAISS vector similarity search
* Product metadata retrieval
* LLM-generated responses based on retrieved products

Example:

```text
Find the best products under ₹4,000
```

---

### 🎧 Customer Support RAG

A separate support knowledge base is used for customer-service questions.

The support RAG pipeline includes:

* PDF document ingestion
* Page-aware text extraction
* Text cleaning
* Fixed-size chunking with overlap
* Sentence Transformers embeddings
* FAISS vector search
* Retrieved context passed to the LLM

Example:

```text
I got a damaged product. Can I return it?
```

---

### 🤖 AI Agent

A `smolagents` CodeAgent acts as the orchestration layer between the user and the RAG tools.

Currently available tools:

```text
Product Search
     ↓
Product RAG

Support Search
     ↓
Support RAG
```

The agent analyzes the user's request and selects the appropriate tool.

---

## Architecture

```text
                         User
                           │
                           ▼
                    Streamlit Chat UI
                           │
                           ▼
                    smolagents Agent
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Product Search             Support Search
              │                         │
              ▼                         ▼
         Product RAG               Support RAG
              │                         │
              ▼                         ▼
        FAISS Index                FAISS Index
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                      LLM Response
                           │
                           ▼
                          User
```

---

## RAG Pipeline

### Product RAG

```text
Amazon Product Dataset
        ↓
Data Cleaning
        ↓
Product Documents
        ↓
Sentence Transformers
        ↓
Embeddings
        ↓
FAISS Index
        ↓
Semantic Retrieval
        ↓
Retrieved Product Context
        ↓
LLM
        ↓
Answer
```

### Support RAG

```text
Amazon Support PDF
        ↓
Page-aware Text Extraction
        ↓
Text Cleaning
        ↓
Chunking
        ↓
Sentence Transformers
        ↓
Embeddings
        ↓
FAISS Index
        ↓
Semantic Retrieval
        ↓
Retrieved Support Context
        ↓
LLM
        ↓
Answer
```

---

## Tech Stack

### Core

* Python
* Pandas
* NumPy

### RAG

* Sentence Transformers
* FAISS
* PyMuPDF

### AI / LLM

* Groq
* LiteLLM
* smolagents

### Application

* Streamlit

### Development

* Jupyter Notebook
* Git & GitHub

---

## Project Structure

```text
Amazn-AI/
│
├── Assets/
│   └── Amazn.png
│
├── data/
│   ├── raw/
│   │   ├── amazon.csv
│   │   └── Amazon-Support.pdf
│   │
│   └── cleaned/
│       └── amazon_cleaned.csv
│
├── notebooks/
│   ├── product-rag/
│   │   └── EDA.ipynb
│   │
│   └── support-rag/
│       └── Support-RAG.ipynb
│
├── src/
│   ├── agent.py
│   ├── llm.py
│   ├── paths.py
│   └── rag.py
│
├── vector_store/
│   ├── product_index.faiss
│   ├── product_documents.json
│   ├── product_metadata.json
│   ├── support_index.faiss
│   └── support_chunks.json
│
├── app.py
├── README.md
└── requirements.txt
```

---

## Current Project Status

### Completed

* [x] Product dataset exploration
* [x] Product data cleaning
* [x] Product document creation
* [x] Product embeddings
* [x] Product FAISS index
* [x] Product RAG pipeline
* [x] Support PDF extraction
* [x] Support text cleaning
* [x] Support document chunking
* [x] Support embeddings
* [x] Support FAISS index
* [x] Support RAG pipeline
* [x] Product RAG agent tool
* [x] Support RAG agent tool
* [x] smolagents agent routing
* [x] Streamlit application

### In Progress

* [ ] Google Sheets order lookup
* [ ] Order lookup agent tool
* [ ] Multi-tool agent testing
* [ ] Final production deployment improvements

---

## Example Queries

### Product Search

```text
Find the best products under ₹4,000
```

```text
Show me highly rated products for the kitchen
```

### Customer Support

```text
I got a damaged product. Can I return it?
```

```text
How can I return a product?
```

```text
How long does a refund take?
```

---

## Future Architecture

The planned final version will extend the agent with a live, read-only order lookup tool using Google Sheets.

```text
                         User
                           │
                           ▼
                    Streamlit Chat UI
                           │
                           ▼
                    smolagents Agent
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Product RAG        Support RAG       Order Lookup
        │                  │                  │
        ▼                  ▼                  ▼
   Product Data       Support PDF       Google Sheets
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                       LLM Response
```

This will allow Amazn AI to handle questions involving products, customer support, and order information through a single conversational interface.

---

## Project Goal

The goal of Amazn AI is to build a practical **AI Engineering / LLM Engineering application** that demonstrates:

* Data preprocessing
* Document processing
* Embeddings
* Vector databases
* Semantic retrieval
* Retrieval-Augmented Generation
* LLM integration
* Agentic tool calling
* Multi-tool orchestration
* API integration
* Streamlit application development
* AI application deployment

---

## License

This project is released under the MIT License.
