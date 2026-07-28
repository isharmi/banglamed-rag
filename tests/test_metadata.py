from pipeline.loader import (
    discover_pdfs,
    load_pdf,
    load_metadata,
    enrich_metadata,
)

from pipeline.chunker import split_documents

pdf = discover_pdfs()[0]

documents = load_pdf(pdf)

chunks = split_documents(documents)

metadata = load_metadata()

chunks = enrich_metadata(chunks, metadata)

print("=" * 60)
print("FIRST CHUNK")
print("=" * 60)

print(chunks[0].metadata)