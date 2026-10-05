<p align="center">
  <img src="https://github.com/ather-ops/Amazn-AI/blob/main/Assets/Amazn.png" alt="Amazn AI Banner" width="100%">
</p>

<h1 align="center">Amazn AI</h1>

<p align="center">
  An agentic AI customer-support assistant powered by RAG, semantic search, and live order lookup.
</p>

<p align="center">
  Product RAG &nbsp;|&nbsp; Support RAG &nbsp;|&nbsp; Google Sheets Order Lookup &nbsp;|&nbsp; smolagents
</p>

---

## Live Demo

Amazn AI is deployed and available as a live Streamlit application.

Live App: Amazn AI

---

## Overview

Amazn AI is an end-to-end agentic AI application designed to handle Amazon-style product and customer-support queries through multiple specialized tools.

Instead of using a single retrieval pipeline for every question, Amazn AI uses a `smolagents` CodeAgent to determine which tool should handle the user's request.

The current system provides three core capabilities:

1. Product discovery using Product RAG
2. Customer-support assistance using Support RAG
3. Live order information using Google Sheets

The project demonstrates how multiple AI tools can be combined into a single conversational application.

---

## Key Features

### Product RAG

A semantic product-search system built over an Amazon product dataset.

The pipeline includes:

* Product data cleaning
* Product document creation
* Sentence Transformers embeddings
* FAISS vector search
* Semantic retrieval
* LLM-generated responses

Example query:

```text
Find the best products under ₹4,000
```

---

### Support RAG

A dedicated customer-support RAG pipeline built over a 134-page Amazon-style support knowledge base.

The pipeline includes:

* PDF text extraction using PyMuPDF
* Page-aware document processing
* Text cleaning
* Fixed-size chunking with overlap
* Sentence Transformers embeddings
* FAISS similarity search
* Retrieved-context generation

Example queries:

```text
I received a damaged product. Can I return it?
```

```text
How can I return a product?
```

```text
How long does a refund take?
```

The support knowledge base used in this project is a compiled Amazon-style reference document and should not be treated as an official or live Amazon policy source.

---

### Google Sheets Order Lookup

A read-only Google Sheets integration provides live order information to the agent.

The order tool can retrieve information such as:

* Order ID
* Customer name
* Product ID
* Product name
* Order date
* Order status
* Expected delivery
* Payment status
* Delivery address
* Tracking ID

Example:

```text
Where is my order ORD1026?
```

The agent can retrieve the order directly from the connected Google Sheet instead of relying on static RAG data.

---

## Agentic Architecture

The central component of Amazn AI is a `smolagents` CodeAgent.

```text
                         User
                           |
                           v
                    Streamlit Chat UI
                           |
                           v
                    smolagents Agent
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
   Product Search    Support Search    Order Lookup
          |                |                |
          v                v                v
      Product RAG       Support RAG     Google Sheets
          |                |                |
          v                v                v
     FAISS Index       FAISS Index      Live Orders
          |                |                |
          +----------------+----------------+
                           |
                           v
                      LLM Response
                           |
                           v
                          User
```

The agent decides which tool to use based on the user's request.

This allows Amazn AI to move beyond a single-purpose RAG chatbot toward a multi-tool AI system.

---

## Multi-Tool Reasoning

Amazn AI can combine tools when a question requires information from multiple sources.

For example:

```text
Where is order ORD1026 and can I return the product?
```

The agent can use:

```text
Google Sheets
     |
     | Order information
     v
Order Lookup

        +

Support RAG
     |
     | Return information
     v
Support Knowledge Base
```

The retrieved information can then be combined into a single conversational response.

---

## RAG Architecture

### Product RAG

```text
Amazon Product Dataset
        |
        v
Data Cleaning
        |
        v
Product Documents
        |
        v
Sentence Transformers
        |
        v
Embeddings
        |
        v
FAISS Index
        |
        v
Semantic Retrieval
        |
        v
Retrieved Product Context
        |
        v
LLM
        |
        v
Final Response
```

### Support RAG

```text
Support PDF
        |
        v
PDF Text Extraction
        |
        v
Text Cleaning
        |
        v
Chunking
        |
        v
Sentence Transformers
        |
        v
Embeddings
        |
        v
FAISS Index
        |
        v
Semantic Retrieval
        |
        v
Retrieved Support Context
        |
        v
LLM
        |
        v
Final Response
```

---

## Technology Stack

### Programming

* Python
* Pandas
* NumPy

### Retrieval and RAG

* Sentence Transformers
* FAISS
* PyMuPDF

### Agent and LLM

* smolagents
* LiteLLM
* Groq

### Google Integration

* gspread
* Google Authentication
* Google Sheets API

### Application

* Streamlit

### Development

* Jupyter Notebook
* Git
* GitHub

---

## Project Structure

```text
Amazn-AI/
|
├── Assets/
|   └── Amazn.png
|
├── data/
|   ├── raw/
|   |   ├── amazon.csv
|   |   └── Amazon-Support.pdf
|   |
|   └── cleaned/
|       └── amazon_cleaned.csv
|
├── notebooks/
|   ├── product-rag/
|   |   └── EDA.ipynb
|   |
|   └── support-rag/
|       └── Support-RAG.ipynb
|
├── src/
|   ├── agent.py
|   ├── llm.py
|   ├── orders.py
|   ├── paths.py
|   └── rag.py
|
├── vector_store/
|   ├── product_index.faiss
|   ├── product_documents.json
|   ├── product_metadata.json
|   ├── support_index.faiss
|   └── support_chunks.json
|
├── app.py
├── README.md
└── requirements.txt
```

---

## Environment Variables

Amazn AI requires environment configuration for the LLM and Google Sheets integration.

```env
GROQ_API_KEY=your_groq_api_key

GOOGLE_CREDENTIALS_PATH=path/to/service-account.json

GOOGLE_SHEET_ID=your_google_sheet_id
```

Google Sheets access is configured with read-only permissions.

Credentials should never be committed to the repository.

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/ather-ops/Amazn-AI.git
cd Amazn-AI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables and Google service-account credentials.

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Development Journey

The project was built incrementally as an AI Engineering learning project.

### Phase 1: Product RAG

* Explored the Amazon product dataset
* Cleaned product data
* Created product documents
* Generated embeddings
* Built a FAISS vector index
* Implemented semantic retrieval
* Connected retrieval with an LLM

### Phase 2: Support RAG

* Loaded the support PDF
* Extracted page-aware text
* Cleaned document content
* Implemented chunking
* Generated embeddings
* Built a support FAISS index
* Implemented support retrieval
* Connected support retrieval with the LLM

### Phase 3: Agentic Architecture

* Introduced `smolagents`
* Created the Product Search tool
* Created the Support Search tool
* Implemented agent-based tool routing
* Added Google Sheets integration
* Created the Order Lookup tool
* Connected all three tools to the agent

### Phase 4: Deployment

* Built the Streamlit chat application
* Configured production dependencies
* Connected Google Sheets securely
* Deployed the application to Streamlit Cloud
* Tested the complete multi-tool workflow

---

## Current Status

Amazn AI is complete and deployed.

```text
Product RAG             Complete
Support RAG             Complete
Google Sheets Tool      Complete
smolagents Agent        Complete
Streamlit Application   Complete
Deployment              Complete
```

The project is now considered a completed end-to-end AI Engineering project.

---

## What This Project Demonstrates

Amazn AI demonstrates practical experience with:

* Data preprocessing
* Document processing
* Embedding generation
* Vector databases
* Semantic search
* Retrieval-Augmented Generation
* LLM integration
* Agentic AI
* Tool calling
* Multi-tool orchestration
* Google API integration
* External data retrieval
* Streamlit application development
* Environment and secret management
* AI application deployment

---

## Future Improvements

Although the current project is complete, possible future improvements include:

* More advanced retrieval and reranking
* Better evaluation of retrieval quality
* Conversation memory
* Structured tool outputs
* Improved agent observability
* Automated evaluation datasets
* More production-grade monitoring

---

## License

This project is released under the MIT License.
