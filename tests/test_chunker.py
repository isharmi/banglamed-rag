from pipeline.loader import discover_pdfs, load_pdf
from pipeline.chunker import split_documents

pdfs = discover_pdfs()

# Load only the first PDF for testing
documents = load_pdf(pdfs[0])

print("=" * 60)
print("DOCUMENT")
print("=" * 60)

print(pdfs[0].name)
print(f"Pages: {len(documents)}")

chunks = split_documents(documents)

print()
print("=" * 60)
print("CHUNKS")
print("=" * 60)

print(f"Total chunks: {len(chunks)}")

print()
print("First chunk preview:\n")

print(chunks[0].page_content[:700])

print()
print("Metadata:")

print(chunks[0].metadata)