# Day 14 – AI Tools & Database Connections

## What I Learned

Today I learned that Large Language Models do not automatically know enterprise data.

Instead, my application retrieves information from external systems and then provides that information to the LLM.

## Architecture

User
↓
Application
↓
Database/API
↓
Prompt Builder
↓
LLM
↓
Response

## Key Concepts

- Database Connection
- Tool Calling
- Separation of Responsibilities
- Prompt Enrichment
- AI Workflow

## Key Takeaways

- LLMs do not directly access databases.
- The application retrieves enterprise data.
- Retrieved data is combined with prompts before sending to the LLM.
- Clear separation between data retrieval and AI reasoning improves scalability and maintainability.

---

User asks question

        │

        ▼

Application creates SQL

        │

        ▼

Database executes SQL

        │

        ▼

Returns rows

        │

        ▼

Prompt Builder

        │

        ▼

LLM

        │

        ▼

Human-readable explanation
