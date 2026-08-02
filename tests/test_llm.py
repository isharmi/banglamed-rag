from generation.llm import generate_answer


question = """
What is hypertension?
"""

answer = generate_answer(question)

print("=" * 60)
print("MODEL ANSWER")
print("=" * 60)
print(answer)