def build_prompt(question, retrieved_docs):
    """
    Build a grounded prompt for the LLM.
    """

    context = ""

    for i, (doc, score) in enumerate(retrieved_docs, start=1):

        context += f"""
Context {i}
----------------------------------------
Organization: {doc.metadata.get("organization")}
Category: {doc.metadata.get("category")}
Year: {doc.metadata.get("year")}
Page: {doc.metadata.get("page")}

{doc.page_content}

"""

    prompt = f"""
You are a helpful medical assistant.

Answer ONLY using the provided medical guidelines.

If the answer cannot be found in the context,
say:

"I could not find sufficient information in the provided guidelines."

Always be factual.

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