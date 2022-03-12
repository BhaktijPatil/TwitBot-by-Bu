import json

from twitbot.common.api_configurer import get_api
from twitbot.oauth.oauth_configurer import OAuthConfiguration, configure_bearer_oauth, configure_bearer_oauth_for_upload


def create_upload_payload(media, media_category):
    return {'media': media, 'media_category': media_category}


def get_upload_api():
    return get_api('image-upload')


def upload_img(image_loc):
    oauth_config = OAuthConfiguration()
    oauth_session = oauth_config.create_session()

    files = {'media': open(image_loc, 'rb')}
    response = oauth_session.post(get_upload_api(), files=files)

    if response.status_code != 200:
        print('image app fail: %s', response.text)
        exit()

    return json.loads(response.text)['media_id']
