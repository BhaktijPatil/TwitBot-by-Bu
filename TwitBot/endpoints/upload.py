from twitbot.common.api_configurer import get_api
from twitbot.common.responsehandler.display_response import display_response_for_tweet
from twitbot.oauth.oauth_configurer import OAuthConfiguration


def create_upload_payload(media, media_category):
    return {'media': media, 'media_category': media_category}


def get_upload_api():
    return get_api("image-upload")


def upload_img(image_loc):
    oauth_config = OAuthConfiguration()
    oauth_session = oauth_config.create_session()
    img_file = open(image_loc, 'rb')
    img_raw = img_file.read()
    response = oauth_session.post(
        get_upload_api(),
        json=create_upload_payload(str(img_raw), 'tweet_image'),
    )
    display_response_for_tweet(response)
    return response
