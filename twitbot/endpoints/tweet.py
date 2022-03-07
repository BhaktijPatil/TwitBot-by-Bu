from twitbot.common.api_configurer import get_api
from twitbot.common.responsehandler.display_response import display_response_for_tweet
from twitbot.oauth.oauth_configurer import OAuthConfiguration


def create_payload(text):
    return {"text": text}


def get_post_tweet_api():
    return get_api("post-tweet")


def tweet_plain_text(text):
    oAuthConfig = OAuthConfiguration()
    oAuthSession = oAuthConfig.create_session()
    response = oAuthSession.post(
        get_post_tweet_api(),
        json=create_payload(text),
    )
    display_response_for_tweet(response)
    return response
