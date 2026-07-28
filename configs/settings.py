"""
Global project configuration.

All configurable values should live here so the rest of the
pipeline stays clean and easy to maintain.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# Data
# ------------------------------------------------------------------

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
METADATA_FILE = PROJECT_ROOT / "data" / "metadata.csv"

# ------------------------------------------------------------------
# Vector Store
# ------------------------------------------------------------------

VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"

# ------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ------------------------------------------------------------------
# Embedding Model
# ------------------------------------------------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"