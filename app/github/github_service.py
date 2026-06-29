from git import Repo
import os

REPO_DIR = "repositories"


def clone_repo(url: str):
    os.makedirs(REPO_DIR, exist_ok=True)

    repo_name = url.split("/")[-1]

    local_path = os.path.join(REPO_DIR, repo_name)

    if not os.path.exists(local_path):
        Repo.clone_from(url, local_path)

    return local_path
