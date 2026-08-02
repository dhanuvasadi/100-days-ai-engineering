# Day 15 – AI Agents & Tool Routing

## What I Learned

Today I learned that AI Agents do not perform every task themselves.

Instead, they decide which tool should handle a user's request.

## Architecture

User
↓
AI Agent
↓
Choose Tool
↓
Execute Tool
↓
Retrieve Information
↓
Prompt Builder
↓
LLM
↓
Final Answer

## Key Concepts

- AI Agent
- Tool Routing
- Intent Detection
- Workflow Orchestration
- Modular Design

## Key Takeaways

- AI Agents coordinate work rather than doing everything themselves.
- Different user questions require different tools.
- Tool routing makes enterprise AI assistants scalable.
- Separating routing, execution, and prompting creates maintainable systems.


---

# Visual Architecture

                    Enterprise AI Assistant

                          User
                            │
                            ▼
                     AI Agent (Router)
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
    SQL Tool         Airflow Tool      Snowflake Tool
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    Prompt Builder
                            ▼
                           LLM
                            ▼
                     Structured Answer
