# Day 8 - Understanding LLM APIs

## 🎯 Learning Objective

Understand how AI applications communicate with Large Language Models using APIs.

---

# What I Learned

- APIs allow applications to communicate with AI models.
- Applications send prompts through APIs.
- APIs return AI-generated responses.
- RAG prepares the prompt before calling the API.
- APIs act as the bridge between applications and LLMs.

---

# Enterprise Example

A Data Engineering AI Assistant retrieves relevant documentation using RAG and then sends the prompt to an LLM through an API.

The API returns the generated answer, which is shown to the user.


---

# Today's Reflection

Today I learned that AI applications do not communicate directly with an LLM. Instead, they use an API that securely sends prompts and receives responses.


--

# API
An API (Application Programming Interface) is a communication layer that allows two applications to exchange information securely.
It receives a request from one application, sends it to another 
application or service, receives the response, and returns it to the requester. In AI applications, 
APIs allow software to communicate with LLMs such as ChatGPT, Claude, or Gemini.


User Question
        │
        ▼
Embedding
        │
        ▼
Vector Database
        │
        ▼
Retrieve Relevant Chunks (RAG)
        │
        ▼
Prompt Builder
        │
        ▼
LLM API
        │
        ▼
LLM
        │
        ▼
Answer

---

# Phase 1: Document Preparation (One Time)

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


# Phase 2: User Question (Every Time)

User Question
        │
        ▼
Tokenizer
        │
        ▼
Embedding
        │
        ▼
Vector Database Search
        │
        ▼
Retrieve Chunks (RAG)
        │
        ▼
Prompt Builder
        │
        ▼
LLM API
        │
        ▼
LLM
        │
        ▼
Answer
