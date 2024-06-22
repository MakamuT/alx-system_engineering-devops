#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

from sys import argv
import requests


def top_ten(subreddit):
    """return top ten posts"""
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
    }
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        posts = response.json()
        for post in posts.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title', 'No title'))
    except requests.RequestException as e:
        print("Request failed: ", format(e))
    except ValueError:
        print("Error parsing JSON")
    except Exception as e:
        print("An error ocurred: ", format(e))
