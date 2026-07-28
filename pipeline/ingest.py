from pipeline.loader import (
    discover_pdfs,
    load_pdf,
    load_metadata,
    enrich_metadata,
)

from pipeline.chunker import split_documents
from pipeline.indexer import (
    build_vectorstore,
    save_vectorstore,
)


def ingest():

    print("=" * 60)
    print("Loading metadata...")
    print("=" * 60)

    metadata = load_metadata()

    pdfs = discover_pdfs()

    print(f"\nFound {len(pdfs)} PDF files.\n")

    all_chunks = []

    for pdf in pdfs:

        print(f"Processing: {pdf.name}")

        documents = load_pdf(pdf)

        chunks = split_documents(documents)

        chunks = enrich_metadata(chunks, metadata)

        all_chunks.extend(chunks)

    print("\n")
    print("=" * 60)
    print(f"Total chunks: {len(all_chunks)}")
    print("=" * 60)

    print("\nBuilding FAISS index...")

    vectorstore = build_vectorstore(all_chunks)

    print("Saving vectorstore...")

    save_vectorstore(vectorstore)

    print("\n✅ Ingestion completed successfully!")


if __name__ == "__main__":
    ingest()