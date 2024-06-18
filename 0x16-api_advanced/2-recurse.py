#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords
"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """a list of titles of all hot posts on subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
       "User-Agent": "0x16-api_advanced:project:\
                     v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    try:
        results = response.json().get("data")
    except ValueError:
        print("Error: Invalid JSON response")
        print("Response content:", response.content)
        return None

    after = results.get("after")
    count += reaults.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
