import os

IMPORTANT_FILES = {
    "README.md",
    "README.rst",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "package.json",
    "Dockerfile",
}


def analyze_repository(files):

    important = []

    python_files = 0

    for file in files:

        filename = os.path.basename(file["path"])

        if filename in IMPORTANT_FILES:
            important.append(file["path"])

        if filename.endswith(".py"):
            python_files += 1

    language = "Python" if python_files else "Unknown"

    return {
        "language": language,
        "important_files": important
    }
