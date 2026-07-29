from retrieval.retriever import retrieve
from retrieval.prompt_builder import build_prompt

question = "What drugs are recommended for hypertension?"

docs = retrieve(question)

prompt = build_prompt(question, docs)

print(prompt)