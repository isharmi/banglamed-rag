def build_prompt(question, results):
    """
    Build a prompt for the LLM using retrieved context.
    """

    context = ""

    for i, (doc, score) in enumerate(results, start=1):
        context += f"""
Context {i}
----------------------------------------
Organization: {doc.metadata.get('organization', 'Unknown')}
Category: {doc.metadata.get('category', 'Unknown')}
Year: {doc.metadata.get('year', 'Unknown')}
Page: {doc.metadata.get('page', 'Unknown')}

{doc.page_content}

"""

    prompt = f"""
You are a helpful medical assistant.

Answer ONLY using the provided medical guidelines.

If the answer cannot be found in the context, say:

"I could not find sufficient information in the provided guidelines."

Always cite the medical evidence from the retrieved context.

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================
"""

    return prompt