import requests

def fetch_repo_data(repo_url):
    """
    Takes a GitHub repository URL and returns important repo data
    """
    # Example: https://github.com/user/repo
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner = parts[0]
    repo = parts[1]

    base_api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_info = requests.get(base_api).json()
    languages = requests.get(f"{base_api}/languages").json()
    commits = requests.get(f"{base_api}/commits").json()

    readme_response = requests.get(
        f"{base_api}/readme",
        headers={"Accept": "application/vnd.github.v3.raw"}
    )

    readme_text = readme_response.text if readme_response.status_code == 200 else ""

    return {
        "name": repo_info.get("name"),
        "description": repo_info.get("description"),
        "stars": repo_info.get("stargazers_count"),
        "languages": list(languages.keys()),
        "commit_count": len(commits),
        "readme": readme_text
    }
