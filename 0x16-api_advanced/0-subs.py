#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
   """total subscribers"""
   url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
   headers = {"User-Agent": "Mozilla/5.0"}
   try:
       response = requests.get(url, headers=headers, allow_redirects=False)
       if response.status_code == 200:
           data = response.json()
           subscribers = data['data']['subscribers']
           return subscribers
       else:
           return 0
   except requests.RequestException as e:
       print("An error occurred: {}".format(e))
       return 0