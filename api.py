import requests
import json

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers  = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

response_dict = r.json()

print(f"Total repos : {response_dict["total_count"]}")
print(f"Completed results : {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
print(f"repo returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]

print(f'Selected info abt the repo')
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repo link: {repo_dict['html_url']}")
print(f"Created at: {repo_dict['created_at']}")
print(f"Last Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")