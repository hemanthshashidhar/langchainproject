import os
import shutil
import zipfile
import requests

REPO_DIR = "repositories"


def download_repository(repo_url: str):

    repo_url = repo_url.rstrip("/")

    owner = repo_url.split("/")[-2]
    repo = repo_url.split("/")[-1]

    os.makedirs(REPO_DIR, exist_ok=True)

    download_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip"

    zip_path = os.path.join(REPO_DIR, f"{repo}.zip")

    extract_path = os.path.join(REPO_DIR, repo)

    if os.path.exists(extract_path):
        return extract_path

    print("Downloading repository...")

    response = requests.get(download_url)

    response.raise_for_status()

    with open(zip_path, "wb") as f:
        f.write(response.content)

    print("Extracting repository...")

    with zipfile.ZipFile(zip_path) as zip_ref:
        zip_ref.extractall(REPO_DIR)

    extracted = os.path.join(REPO_DIR, f"{repo}-main")

    shutil.move(extracted, extract_path)

    os.remove(zip_path)

    return extract_path
