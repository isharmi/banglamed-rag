from pipeline.loader import (
    discover_pdfs,
    load_pdf,
    load_metadata,
    enrich_metadata,
)

from pipeline.chunker import split_documents
from pipeline.embedder import embed_chunks

pdf = discover_pdfs()[0]

documents = load_pdf(pdf)

chunks = split_documents(documents)

metadata = load_metadata()

chunks = enrich_metadata(chunks, metadata)

embeddings = embed_chunks(chunks)

print("=" * 60)
print("Embedding Shape")
print("=" * 60)

print(embeddings.shape)

print()

print("First 10 values of first embedding:")

print(embeddings[0][:10])