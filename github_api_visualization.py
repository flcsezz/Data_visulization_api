import plotly.express as px
import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers  = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

response_dict = r.json()

repo_dicts = response_dict['items']

repo_link , stars , hover_texts= [], [], []



for repo in repo_dicts:
    name = repo['name']
    url = repo['html_url']
    link = f"<a href='{url}'>{name}"
    repo_link.append(link)
    stars.append(repo['stargazers_count'])

    owner = repo['owner']['login']
    description = repo['description']
    hover_text = f'Owner:{owner}<br />Description: {description}'
    hover_texts.append(hover_text)

title = "Python repos with most stars"
lables = {'x':'Repository', 'y':'Stars'}

fig = px.bar(x = repo_link, y = stars, title=title, labels=lables, hover_name=hover_texts,)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size = 20)
fig.update_traces(marker_color = "SteelBlue", marker_opacity = 0.6)

fig.show()