from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from configs.settings import EMBEDDING_MODEL


def build_vectorstore(chunks):
    """
    Create a FAISS vector store from LangChain Documents.
    """
    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vectorstore


def save_vectorstore(vectorstore, path="vectorstore"):
    """
    Save the FAISS index locally.
    """
    vectorstore.save_local(path)