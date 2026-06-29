from app.services.llm_service import ask_repository


def summarize_repository(files):

    docs = []

    for file in files[:8]:

        docs.append(
            type(
                "Doc",
                (),
                {
                    "page_content": file["content"][:2500],
                    "metadata": {"source": file["path"]},
                },
            )
        )

    summary, _ = ask_repository(
        "Explain this repository. Mention its purpose, architecture, important modules, and where a new contributor should start.",
        docs,
    )

    return summary
