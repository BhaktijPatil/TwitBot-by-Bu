from twitbot.common.api_configurer import get_api
from twitbot.common.responsehandler.display_response import display_response_for_search
from twitbot.oauth.oauth_configurer import configure_bearer_oauth
import requests


def get_recent_tweets_api():
    return get_api("search-tweet")


def get_tweet_count_api():
    return get_api("tweet-count")


def search_tweet(query):
    response = requests.get(get_recent_tweets_api(), auth=configure_bearer_oauth, params=query)
    display_response_for_search(response)
    return response


def find_tweet_count_distribution(query):
    response = requests.get(get_tweet_count_api(), auth=configure_bearer_oauth, params=query)
    display_response_for_search(response)
    return response


def find_tweet_count(query):
    tweet_count_distribution = find_tweet_count_distribution(query).json()
