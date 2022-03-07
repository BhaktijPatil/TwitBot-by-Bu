from jproperties import Properties
from requests_oauthlib import OAuth1Session


class OAuthConfiguration:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def __init__(self):
        configs = Properties()
        with open('resources/secret.properties', 'rb') as read_prop:
            configs.load(read_prop)
        self.consumer_key = configs.get("API-key").data
        self.consumer_secret = configs.get("API-secret").data
        self.access_token = configs.get("access-token").data
        self.access_token_secret = configs.get("access-token-secret").data

    def createSession(self):
        return OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )
