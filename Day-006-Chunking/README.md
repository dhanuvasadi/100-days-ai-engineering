# Day 6 - Understanding Chunking

## 🎯 Learning Objective

Understand how chunking improves document retrieval in RAG systems.

---

# What I Learned

- Large documents are split into smaller chunks.
- Each chunk receives its own embedding.
- Smaller chunks improve retrieval accuracy.
- Chunk overlap preserves context.
- Chunking reduces unnecessary token usage.

---

# Enterprise Example

A Data Engineering AI Assistant splits SQL scripts, ETL documentation, and runbooks into logical sections before generating embeddings.

This allows the system to retrieve only the most relevant information.


---

# Today's Reflection

Today I learned that chunking is not just splitting documents into smaller pieces. It is about preserving meaning while making retrieval more accurate and efficient.



---
# Why is chunking important for RAG?

Chunking helps RAG retrieve the most relevant part of a document instead of the entire document. By splitting large documents into logical sections,
each section gets its own embedding. This improves retrieval accuracy, reduces unnecessary token usage, and provides better context for the LLM.
Notice how we included:

Accuracy ✅
Tokens ✅
Context ✅
Logical sections ✅


---
# 🏗️ Our AI Assistant Is Growing

Company Documents
        │
        ▼
Chunk Documents ✅
        │
        ▼
Create Embeddings ✅
        │
        ▼
Store in Vector Database ✅
        │
        ▼
User Question
        │
        ▼
Retrieve Best Chunks (RAG) ✅
        │
        ▼
LLM Generates Answer ✅
