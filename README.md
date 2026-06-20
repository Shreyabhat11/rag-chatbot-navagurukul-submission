# 🚀 System Design RAG Assistant

A Retrieval-Augmented Generation (RAG) chatbot built for the AI/ML Hackathon Challenge.

The system ingests large software engineering and system design PDF books, indexes them using open-source embeddings and Qdrant Vector Database, and answers user questions with source citations in real-time.

---

# 📌 Challenge Addressed

## Challenge 1: RAG Chatbot

Build a Retrieval-Augmented Generation (RAG) chatbot that:

- Ingests multiple large PDFs
- Supports OCR for scanned documents
- Uses open-source embeddings
- Uses open-source vector database
- Provides citations
- Responds in real-time
- Supports large-scale document retrieval

---

# 🎯 Project Overview

This project creates a knowledge assistant over a collection of:

- System Design Books
- Software Architecture Books
- Distributed Systems References
- Database Engineering Books

Current Dataset:

| Metric | Value |
|----------|----------|
| PDFs | 46 |
| Domain | System Design |
| Embeddings | BAAI BGE Small |
| Vector Database | Qdrant |
| LLM | Groq Llama |
| Frontend | Streamlit |

---

# 🏗️ Architecture

```text
PDF Books
    │
    ▼
PDF Parsing
(PyMuPDF)
    │
    ▼
OCR
(Tesseract)
    │
    ▼
Text Cleaning
    │
    ▼
Chunking
(500-1000 tokens)
    │
    ▼
Embeddings
(BAAI/bge-small-en-v1.5)
    │
    ▼
Qdrant Vector DB
    │
    ▼
Retriever
    │
    ▼
Context Builder
    │
    ▼
Groq LLM
(Llama)
    │
    ▼
Answer + Citations
    │
    ▼
Streamlit UI
```

---

# ⚙️ Tech Stack

## Document Processing

- PyMuPDF
- Pillow
- Tesseract OCR

## Embeddings

- BAAI/bge-small-en-v1.5

## Vector Database

- Qdrant

## Retrieval

- Dense Vector Search

## LLM

- Groq API
- Llama Models

## Frontend

- Streamlit

## Language

- Python

---

# 📂 Project Structure

```text
rag-chatbot-navagurukul-submission/

├── config/
│   ├── settings.py
│
├── ingestion/
│   ├── pdf_parser.py
│   ├── text_cleaner.py
│   ├── chunker.py
│
├── embeddings/
│   ├── embedder.py
│
├── vectordb/
│   ├── qdrant_manager.py
│
├── retrieval/
│   ├── retriever.py
│
├── rag/
│   ├── pipeline.py
│   ├── prompt_template.py
│
├── llm/
│   ├── groq_client.py
│
├── scripts/
│   ├── ingest_documents.py
│   ├── test_retrieval.py
│   ├── test_rag.py
│   ├── benchmark.py
│
├── ui/
│   ├── app.py
│
├── data/
│   ├── pdfs/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 📚 Features

## PDF Ingestion

Supports:

- Native PDFs
- Scanned PDFs
- Embedded Images

Extraction Methods:

- PyMuPDF
- OCR via Tesseract

---

## Text Processing

- Header/Footer removal
- Whitespace normalization
- Noise reduction

---

## Chunking

Chunk Size:

```python
500
```

Overlap:

```python
100
```

Metadata Stored:

- PDF Name
- PDF ID
- Page Number

---

## Embedding Generation

Model:

```text
BAAI/bge-small-en-v1.5
```

Benefits:

- Open Source
- Fast
- High Retrieval Quality
- CPU Friendly

---

## Vector Search

Database:

```text
Qdrant
```

Supports:

- ANN Search
- Cosine Similarity
- Fast Retrieval

---

## Retrieval Pipeline

```text
User Question
        │
        ▼
Embedding Generation
        │
        ▼
Qdrant Search
        │
        ▼
Top K Chunks
        │
        ▼
Context Building
        │
        ▼
Groq LLM
        │
        ▼
Final Answer
```

---

## Answer Generation

LLM:

```text
Groq Llama
```

Outputs:

- Natural Language Answer
- Citations
- Sources

---

# 🖥️ Streamlit Interface

The application provides:

### Chat Interface

Ask questions naturally.

Example:

```text
What is consistent hashing?
```

---

### Source Citations

Example:

```text
Designing Data Intensive Applications.pdf
Page 226

System Design Interview.pdf
Page 75
```

---

### Retrieval Visualization

Displays:

- Retrieved Chunks
- Source Documents
- Page Numbers

---

### Knowledge Base Statistics

Shows:

- Total PDFs
- Indexed Chunks
- Embedding Model
- Vector Database
- LLM

---

### Response Metrics

Displays:

```text
Response Time
Retrieved Chunks
```

# 📥 Document Ingestion

Place PDFs inside:

```text
data/pdfs/
```

Pipeline:

```text
PDF
 ↓
OCR
 ↓
Chunking
 ↓
Embedding
 ↓
Qdrant
```

---

# 📊 Evaluation

Metrics Tracked:

- Retrieval Quality
- Source Accuracy
- Response Time
- Chunk Coverage

---

# 🎯 Sample Questions

### Distributed Systems

```text
What is consistent hashing?

Explain CAP theorem.

How does leader election work?

What is quorum?
```

### Databases

```text
What is sharding?

Difference between SQL and NoSQL?

Explain indexing.
```

### System Design

```text
How would you design Twitter?

How does Kafka work?

How does a CDN work?
```

---

# 🔒 Open Source Components

| Component | Technology |
|------------|------------|
| OCR | Tesseract |
| Embedding Model | BGE Small |
| Vector Database | Qdrant |
| UI | Streamlit |
| PDF Parsing | PyMuPDF |

---

# ✅ Challenge Requirements Coverage

| Requirement | Status |
|------------|---------|
| Multiple PDFs | ✅ |
| OCR Support | ✅ |
| Chunking | ✅ |
| Metadata Storage | ✅ |
| Open Source Embeddings | ✅ |
| Open Source Vector DB | ✅ |
| Retrieval | ✅ |
| Answer Generation | ✅ |
| Citations | ✅ |
| Streamlit UI | ✅ |
| Retrieval Visualization | ✅ |
| Knowledge Base Stats | ✅ |

---

# 👨‍💻 Author

Built for the AI/ML Hackathon Challenge.

System Design Knowledge Assistant using:

- Retrieval-Augmented Generation (RAG)
- Qdrant Vector Database
- BGE Embeddings
- Groq LLM
- Streamlit

---