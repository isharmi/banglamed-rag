from pipeline.loader import (
    discover_pdfs,
    load_pdf,
    load_metadata,
    enrich_metadata,
)

from pipeline.chunker import split_documents
from pipeline.indexer import build_vectorstore, save_vectorstore

pdfs = discover_pdfs()

all_chunks = []

metadata = load_metadata()

for pdf in pdfs:

    docs = load_pdf(pdf)

    chunks = split_documents(docs)

    chunks = enrich_metadata(chunks, metadata)

    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")

vectorstore = build_vectorstore(all_chunks)

save_vectorstore(vectorstore)

print("\n✅ FAISS index created successfully!")