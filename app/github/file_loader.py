import os

SUPPORTED = (
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
)


def load_repository(repo_path):

    documents = []

    for root, dirs, files in os.walk(repo_path): 

        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "__pycache__",
                ".venv",
                "node_modules",
            }
        ]

        for file in files:

            if file.endswith(SUPPORTED):

                path = os.path.join(root, file)

                try:

                    with open(path, "r", encoding="utf-8") as f:

                        documents.append(
                            {
                                "path": path,
                                "content": f.read()
                            }
                        )

                except:

                    pass

    return documents
    
