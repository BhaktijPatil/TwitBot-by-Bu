from twitbot.common.api_configurer import get_api
from twitbot.common.responsehandler.display_response import display_response_for_tweet
from twitbot.oauth.oauth_configurer import OAuthConfiguration


def create_basic_payload(text):
    return {"text": text}


def create_image_payload(text, media_id):
    return {"text": text, "media": {"media_ids": [media_id]}}


def get_post_tweet_api():
    return get_api("post-tweet")


def tweet_plain_text(text):
    oauth_config = OAuthConfiguration()
    oauth_session = oauth_config.create_session()
    response = oauth_session.post(
        get_post_tweet_api(),
        json=create_basic_payload(text),
    )
    display_response_for_tweet(response)
    return response


def tweet_img(text, media_id):
    oauth_config = OAuthConfiguration()
    oauth_session = oauth_config.create_session()
    response = oauth_session.post(
        get_post_tweet_api(),
        json=create_image_payload(text, media_id),
    )
    display_response_for_tweet(response)
    return response
