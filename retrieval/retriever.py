from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from configs.settings import EMBEDDING_MODEL


def load_vectorstore(path="vectorstore"):
    """
    Load the FAISS vector database.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def retrieve(query, k=5):
    """
    Retrieve the top-k most relevant chunks.
    """
    vectorstore = load_vectorstore()

    results = vectorstore.similarity_search_with_score(
        query,
        k=k
    )

    return results