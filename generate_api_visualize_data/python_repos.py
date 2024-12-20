import requests


# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
# url += '?q=sort:stars+stars:>=0'

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())

print(f'Total repositories: {response_dict["total_count"]}')
print(f'Complete results: {not response_dict["incomplete_results"]}')

# Explore the information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[-1]
print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print("\n\tName:", repo_dict["name"])
    print("\tOwner:", repo_dict["owner"]["login"])
    print("\tStars:", repo_dict["stargazers_count"])
    print("\tRepository:", repo_dict["html_url"])
    print("\tCreated:", repo_dict["created_at"])
    print("\tUpdated:", repo_dict["updated_at"])
    print("\tDescription:", repo_dict["description"])
