| File          | Responsibility                                   |
| ------------- | ------------------------------------------------ |
| `loader.py`   | Load PDFs and metadata, enrich document metadata |
| `chunker.py`  | Split documents into chunks                      |
| `embedder.py` | Generate embeddings                              |
| `indexer.py`  | Build and save the FAISS index                   |
| `ingest.py`   | Coordinate the entire ingestion pipeline         |
