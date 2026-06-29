import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="google/gemini-2.5-flash",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.2,
    max_tokens=500,
)


def ask_repository(question, documents):

    context = ""
    sources = []

    for doc in documents:

        source = doc.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

        context += f"""
FILE:
{source}

CONTENT:
{doc.page_content}

"""

    prompt = f"""
You are RepoSage.

You are an expert software engineer.

Answer ONLY using the repository context.

If the answer cannot be found in the repository, say:
"I couldn't find that information in this repository."

Repository Context:

{context}

User Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, sources
