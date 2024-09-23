#!/usr/bin/python3
"""Defines a function that prints the titles of
the first 10 hot posts listed for a given subreddit.
"""


import requests as rq


def top_ten(subreddit):
    """If not a valid subreddit, print None
    else prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced"
    }
    params = {
        "limit": 10
    }
    response = rq.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c["data"]["title"]) for c in results["children"]]