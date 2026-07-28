from sentence_transformers import SentenceTransformer
from configs.settings import EMBEDDING_MODEL

# Load once when the module is imported
model = SentenceTransformer(EMBEDDING_MODEL)


def embed_chunks(chunks):
    """
    Generate embeddings for LangChain chunks.
    """
    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings