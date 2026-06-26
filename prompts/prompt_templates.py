def get_prompt(context, question, prompt_type="Role Prompt"):

    if prompt_type == "Role Prompt":

        return f"""
You are an experienced Business Consultant.

Use ONLY the provided context to answer.

If the answer is not found, reply:
"I couldn't find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Return the answer in this format:

Summary:
...

Key Points:
• ...
• ...

Recommendation:
...
"""

    elif prompt_type == "Chain of Thought":

        return f"""
You are an expert Business Consultant.

Think step by step before answering.

1. Understand the question.
2. Find relevant information from the context.
3. Explain clearly.
4. Give the final answer.

Context:
{context}

Question:
{question}
"""

    elif prompt_type == "Few Shot":

        return f"""
Example 1

Question:
What is the leave policy?

Answer:
Employees receive 20 paid leave days annually.

---------------------

Example 2

Question:
What are office timings?

Answer:
Office timings are 9 AM to 6 PM.

---------------------

Now answer this question.

Context:
{context}

Question:
{question}
"""

    elif prompt_type == "Zero Shot":

        return f"""
Answer the following question using ONLY the given context.

Context:
{context}

Question:
{question}
"""

    else:

        return f"""
Context:
{context}

Question:
{question}
"""