from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_documents(files):

    docs = []

    for file in files:

        docs.append(
            Document(
                page_content=file["content"],
                metadata={
                    "source": file["path"]
                }
            )
        )

    return docs


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)
