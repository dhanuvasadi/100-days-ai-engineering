# Day 4 - Understanding Vector Databases

## 🎯 Learning Objective

Understand why AI applications use vector databases to perform semantic search.

---

# What I Learned

- Embeddings are stored in vector databases.
- Vector databases search by meaning.
- They calculate similarity between embeddings.
- They are optimized for semantic search.
- They are a key part of RAG systems.

---

# Enterprise Example

A Data Engineering AI Assistant stores SQL scripts, ETL jobs, documentation, and data dictionaries as embeddings in a vector database.

When a user asks a question, the application retrieves the most relevant documents before sending them to the LLM.

---

# Today's Reflection

Today I learned that vector databases do not replace SQL databases. Instead, they complement them by enabling AI to search information based on meaning rather than exact keywords.

---

# Vector DB

A relational database is optimized for structured queries using indexes, joins, and filters. A vector database is optimized for semantic similarity search by comparing embeddings and finding the nearest neighbors.
