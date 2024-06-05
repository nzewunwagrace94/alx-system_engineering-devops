#!/usr/bin/python3
""" Module contain top_ten function that queries the Reddit API and prints
 the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the title of the top 10 hot posts of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        # "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/imole)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(
        url=url,
        allow_redirects=False,
        headers=headers,
        params=params
        )
    if res.status_code == 404:
        print('None')
        return
    results = res.json().get("data").get("children")
    for i in results:
        print(i.get("data").get("title"))


if __name__ == "__main__":
    import sys

    top_ten(sys.argv[1])
