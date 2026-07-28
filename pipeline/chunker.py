"""
Text chunking utilities.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

from configs.settings import CHUNK_SIZE, CHUNK_OVERLAP


def get_text_splitter():
    """
    Create the project's text splitter.
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )


def split_documents(documents):
    """
    Split LangChain Documents into chunks.
    """
    splitter = get_text_splitter()
    return splitter.split_documents(documents)