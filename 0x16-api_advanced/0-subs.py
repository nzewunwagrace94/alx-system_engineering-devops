#!/usr/bin/python3
""" Module contain number_of_subscribers function that
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subs in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        # "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/imole)"
    }
    results = requests.get(url=url, allow_redirects=False, headers=headers)
    if results.status_code == 404:
        return 0
    return (results.json().get("data").get('subscribers'))
