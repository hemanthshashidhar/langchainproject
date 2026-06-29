from app.rag.vector_store import load_vector_store


def retrieve_documents(question, k=5):

    vector_db = load_vector_store()

    results = vector_db.similarity_search_with_score(
        question,
        k=k
    )

    return results
