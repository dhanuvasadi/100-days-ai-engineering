role = "Enterprise Data Engineering AI Assistant"

question = input("Enter your question: ")

context = """
Customer Billing ETL loads data from Oracle
into Snowflake every night.
"""

prompt = f"""
You are a {role}.

Use only the context below.

Context:
{context}

Question:
{question}

Answer clearly.
"""

print("\n----- Generated Prompt -----")
print(prompt)


def build_prompt(role, context, question):

    prompt = f"""
You are a {role}.

Use only the context below.

Context:
{context}

Question:
{question}

Answer clearly.
"""

    return prompt

role = "Enterprise Data Engineering AI Assistant"

question = input("Enter your question: ")

context = """
Customer Billing ETL loads data from Oracle
into Snowflake every night.
"""

final_prompt = build_prompt(role, context, question)

print(final_prompt)





