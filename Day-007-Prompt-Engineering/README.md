# Day 7 - Prompt Engineering

## 🎯 Learning Objective

Understand how well-designed prompts improve AI responses in enterprise applications.

---

# What I Learned

- A prompt is an instruction given to an AI model.
- Better prompts produce better responses.
- Enterprise applications often use hidden system prompts.
- Prompt engineering reduces hallucinations.
- Prompts define role, context, and output format.

---

# Enterprise Example

An Enterprise Data Engineering AI Assistant builds a structured prompt before sending the user's question to the LLM.

The prompt includes retrieved documentation, instructions, and the expected response format.


---

# Today's Reflection

Prompt engineering is not about asking better questions as a user. It is about designing clear instructions that help AI generate accurate, consistent, and trustworthy responses.


---

# Prompt

A prompt is a structured instruction that tells the AI what task to perform,
who the target audience is, what context or reference documents to use, and how the output should be formatted. A well-designed prompt helps the AI generate more accurate, relevant, and consistent responses.

---

# 🏗️ Your AI Assistant Architecture


Company Documents
        │
        ▼
Preprocessing
        │
        ▼
Chunking
        │
        ▼
Embeddings
        │
        ▼
Vector Database
        │
        ▼
User Question
        │
        ▼
Embedding
        │
        ▼
Retrieve Chunks (RAG)
        │
        ▼
Prompt Builder
        │
        ▼
LLM
        │
        ▼
Final Answer



---

There are actually two different embedding operations:

During ingestion (one time)

Document

↓

Chunk

↓

Embedding

↓

Vector Database

During a user query (every question)


User Question

↓

Embedding

↓

Vector Search

↓

Relevant Chunks

↓

Prompt Builder

↓

LLM API

↓

LLM

↓

Answer

