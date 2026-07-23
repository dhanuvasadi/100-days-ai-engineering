
# Day 2 - Understanding Tokens

## 🎯 Learning Objective

Understand what tokens are and why they are important when working with Large Language Models.

---

# What I Learned

- LLMs process tokens, not entire paragraphs.
- Tokens are small pieces of text.
- One word can contain multiple tokens.
- Every model has a context window.
- Tokens determine how much information an AI model can process at one time.

---

# Why Tokens Matter

Tokens directly impact:

- Prompt size
- AI cost
- Response quality
- Context limits
- Enterprise AI application design

---

# Real-World Example

An enterprise chatbot cannot send an entire data warehouse or thousands of pages of documentation to an AI model at once.

Instead, it retrieves only the relevant information and sends those tokens to the model to generate an accurate response.


---

Today I learned that AI models do not read information the way humans do. They process small pieces of text called tokens, and every conversation is limited by a context window. This explains why AI engineers need techniques like Retrieval-Augmented Generation (RAG) when building enterprise applications.

# Context


Companies cannot send their entire data warehouse to an LLM because it would exceed the model's context window, be expensive, and include a lot of irrelevant information. Instead, AI applications retrieve only the relevant data needed to answer a user's question and send that smaller context to the model. This approach improves accuracy, reduces cost, and makes responses faster.
