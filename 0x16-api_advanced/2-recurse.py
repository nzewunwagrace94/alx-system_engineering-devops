#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list: list = [], count=0, after=""):
    """returns the titles of the hot posts of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        # "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/imole)"
    }
    params = {
        "after": after,
        "limit": 100,
        "count": count
    }
    res = requests.get(
        url=url,
        allow_redirects=False,
        headers=headers,
        params=params
        )
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count = count + results.get("dist")

    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, count=count, after=after)
    return hot_list
