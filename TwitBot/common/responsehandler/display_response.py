def display_success(response):
    print("Tweet Successful: {} {}".format(response.status_code, response.text))


def display_error(response):
    print("Request returned an error: {} {}".format(response.status_code, response.text))


def display_response_for_tweet(response):
    if response.status_code == 201:
        display_success(response)
    else:
        display_error(response)


def display_response_for_search(response):
    if response.status_code == 200:
        display_success(response)
    else:
        display_error(response)