#!/usr/bin/python3
""" api advanced"""
import requests


def top_ten(subreddit):
    """

    :param subreddit: name of fild
    """
    data = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        print('None')

    else:
        data_dict = data.json()
        for child in data_dict.get("data").get("children"):
            print(child.get("data").get("title"))

