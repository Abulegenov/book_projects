import requests
import json
from operator import itemgetter

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
status_code = 0

while status_code != 200:
    r = requests.get(url=url)
    print("Status code", r.status_code)
    status_code = r.status_code

# print(r.text)
submission_ids = r.json()
# response_dict = dict(r)
# print(type(response_dict))
# response_string = json.dumps(response_dict, indent=4)
# print(type(response_string))
submission_dicts = []

for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"],
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Disucssion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
