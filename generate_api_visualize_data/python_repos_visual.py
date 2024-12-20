import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

repos_dict = r.json()

repos_stars = [star["stargazers_count"] for star in repos_dict["items"]]
repos_names = [repo["name"] for repo in repos_dict["items"]]
repos_links = [
    f"<a href = '{repo['html_url']}'>{repo['name']}</a>" for repo in repos_dict["items"]
]
hover_texts = [
    f"{repo['name']}<br />{repo['description']}" for repo in repos_dict["items"]
]
title = "Most Starred Python Projects on GitHub"
fig = px.bar(
    x=repos_links,
    y=repos_stars,
    labels={"x": "Repo Name", "y": "Star Count"},
    title=title,
    hover_name=hover_texts,
)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20,
)

fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
# fig.show()
fig.write_html("github_starred_repos.html")
