#!/usr/bin/python3
""" import the request library """

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyApp/0.0.1'}

    try:
        # Make a GET request to the Reddit API for the given subreddit
        response = requests.get(
                f'https://www.reddit.com/r/{subreddit}/about.json',
                headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return the number of subscribers
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the request was not successful, return 0
            return 0
    except (requests.exceptions.RequestException, KeyError):
        # If there was an error making the request or parsing the
        # response, return 0
        return 0
