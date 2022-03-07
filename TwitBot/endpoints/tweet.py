from TwitBot.common.APIConfigurer import getAPI
from TwitBot.oauth.oAuthConfigurer import OAuthConfiguration


def createPayload(text):
    return {"text": text}


def getPostTweetAPI():
    return getAPI("post-tweet")


def displayResponse(response):
    if response.status_code == 201:
        print("Tweet Successful: {} {}".format(response.status_code, response.text))
    else:
        print("Request returned an error: {} {}".format(response.status_code, response.text))


def tweetPlainText(text):
    oAuthConfig = OAuthConfiguration()
    oAuthSession = oAuthConfig.createSession()
    response = oAuthSession.post(
        getPostTweetAPI(),
        json=createPayload(text),
    )
    displayResponse(response)
    return response
