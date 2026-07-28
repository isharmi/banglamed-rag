"""
Document loading utilities.

Responsibilities:
- Find all PDFs
- Load metadata
- Read PDF documents
"""
from pathlib import Path
import pandas as pd

from langchain_community.document_loaders import PyPDFLoader

from configs.settings import RAW_DATA_DIR, METADATA_FILE


def load_metadata() -> pd.DataFrame:
    """
    Load metadata.csv into a pandas DataFrame.
    """
    return pd.read_csv(METADATA_FILE)


def discover_pdfs() -> list[Path]:
    """
    Recursively discover all PDF files.
    """
    return sorted(RAW_DATA_DIR.rglob("*.pdf"))


def load_pdf(pdf_path: Path):
    """
    Load one PDF and return LangChain Documents.
    """
    loader = PyPDFLoader(str(pdf_path))
    return loader.load()



def enrich_metadata(chunks, metadata_df):
    """
    Attach metadata.csv information to each chunk.
    """

    metadata_lookup = {
        row["filename"]: row
        for _, row in metadata_df.iterrows()
    }

    for chunk in chunks:

        filename = Path(chunk.metadata["source"]).name

        if filename in metadata_lookup:

            row = metadata_lookup[filename]

            chunk.metadata["organization"] = row["source"]
            chunk.metadata["category"] = row["category"]
            chunk.metadata["year"] = int(row["year"])
            chunk.metadata["title"] = row["title"]

    return chunks