import plotly.express as px
import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers  = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

response_dict = r.json()

repo_dicts = response_dict['items']

repo_name , stars = [], []

for repo in repo_dicts:
    repo_name.append(repo['name'])
    stars.append(repo['stargazers_count'])


title = "Python repos with most stars"
lables = {'x': 'repos', 'y':'Stars'}

fig = px.bar(x = repo_name, y = stars, title=title, labels=lables)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size = 20)

fig.show()