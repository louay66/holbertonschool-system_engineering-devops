#!/usr/bin/python3
""" api advanced"""
import requests


def number_of_subscribers(subreddit):
    """
    :param subreddit: name of fild
    """

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        return 0
    data_dict = data.json()
    return data_dict["data"]["subscribers"]
