import requests


#get_repo_commits("Tirth-Patel903")
def get_repo_commits(user_id):
    # make request to retrieve user's repositories  https://github.com/Tirth-Patel903
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)
    repos_json = repos_response.json()

    # iterate through repositories and retrieve number of commits for each
    result = []
    for repo in repos_json:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        commits_json = commits_response.json()
        num_commits = len(commits_json)
        result.append((repo_name, num_commits))

    return result

repos = get_repo_commits("richkempinski")
for repo in repos:
    print(f"Repo: {repo[0]} Number of commits: {repo[1]}")
