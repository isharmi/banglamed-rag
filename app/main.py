from retrieval.retriever import retrieve
from generation.prompt import build_prompt
from generation.llm import generate


def main():
    print("=" * 60)
    print("Bangla Medical RAG Assistant")
    print("=" * 60)
    print("Type your medical question.")
    print("Type 'exit' or 'quit' to return to the terminal.")
    print()

    while True:
        question = input("You: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        if not question:
            continue

        results = retrieve(question)

        prompt = build_prompt(question, results)

        answer = generate(prompt)

        print("\nAssistant:")
        print("-" * 60)
        print(answer)
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()