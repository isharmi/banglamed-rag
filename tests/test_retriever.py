from retrieval.retriever import retrieve

query = "What drugs are recommended for hypertension?"

results = retrieve(query)

print("=" * 60)
print("QUESTION")
print("=" * 60)
print(query)

print("\n")

print("=" * 60)
print("TOP RESULTS")
print("=" * 60)

for i, (doc, score) in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 60)

    print("Score:", score)

    print("Organization:", doc.metadata.get("organization"))
    print("Category:", doc.metadata.get("category"))
    print("Year:", doc.metadata.get("year"))
    print("Page:", doc.metadata.get("page"))

    print("\nPreview:\n")

    print(doc.page_content[:500])