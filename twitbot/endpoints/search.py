from twitbot.common.api_configurer import get_api
from twitbot.common.responsehandler.display_response import display_response_for_search
from twitbot.oauth.oauth_configurer import configure_bearer_oauth
import requests


def get_recent_tweets_api():
    return get_api("lookup-tweet")


def search_tweet(query):
    response = requests.get(get_recent_tweets_api(), auth=configure_bearer_oauth, params=query)
    display_response_for_search(response)
    return response
