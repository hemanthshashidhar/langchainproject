import os

from app.github.repository_downloader import download_repository
from app.github.file_loader import load_repository
from app.github.repository_analyzer import analyze_repository

from app.rag.document_processor import (
    create_documents,
    split_documents,
)

from app.rag.vector_store import create_vector_store
from app.rag.retriever import retrieve_documents

from app.services.llm_service import ask_repository
from app.services.repository_summary import summarize_repository


VECTOR_DB = "vector_store/index.faiss"


def index_repository(repo_url: str):

    print("\nDownloading repository...\n")

    repo_path = download_repository(repo_url)

    print("Loading repository...\n")

    files = load_repository(repo_path)

    print(f"Loaded {len(files)} files.\n")

    # -----------------------------
    # Repository Analysis
    # -----------------------------

    analysis = analyze_repository(files)

    print("=" * 70)
    print("📦 Repository Analysis")
    print("=" * 70)

    print(f"\nLanguage : {analysis['language']}")

    print("\nImportant Files:\n")

    for file in analysis["important_files"]:
        print(f"• {file}")

    print("\n" + "=" * 70)

    # -----------------------------
    # AI Repository Summary
    # -----------------------------

    print("\nGenerating AI Repository Summary...\n")

    summary = summarize_repository(files)

    print(summary)

    print("\n" + "=" * 70)

    # -----------------------------
    # Build Vector Database
    # -----------------------------

    print("\nCreating LangChain Documents...")

    documents = create_documents(files)

    print(f"Created {len(documents)} documents.")

    print("\nSplitting Documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("\nBuilding FAISS Vector Database...")

    create_vector_store(chunks)

    print("\n✅ Repository Indexed Successfully!")

    return files


def chat():

    print("\n" + "=" * 70)
    print("💬 RepoSage Chat")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        question = input("\nAsk RepoSage > ")

        if question.lower() == "exit":
            break

        results = retrieve_documents(question)

        docs = [doc for doc, score in results]

        answer, sources = ask_repository(question, docs)

        print("\n" + "=" * 80)
        print(answer)

        print("\nRelevant Files")
        print("-" * 80)

        for source in sources:
            print(source)

        print("=" * 80)


def main():

    print("=" * 80)
    print("🚀 RepoSage - AI Open Source Mentor")
    print("=" * 80)

    if not os.path.exists(VECTOR_DB):

        repo_url = input("\nEnter GitHub Repository URL:\n\n> ").strip()

        index_repository(repo_url)

    else:

        print("\nUsing existing indexed repository.\n")

    chat()

    print("\n👋 Goodbye!\n")


if __name__ == "__main__":
    main()
