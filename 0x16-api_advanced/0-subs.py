#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        return data.get("subscribers", 0)
    except (ValueError, AttributeError):
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: {} subreddit".format(sys.argv[0]))
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        if subscribers >= 0:
            print("OK")
