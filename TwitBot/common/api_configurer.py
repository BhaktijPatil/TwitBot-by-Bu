from jproperties import Properties


def get_api(api_name):
    configs = Properties()
    with open('D:/Projects/Pycharm/TwitBot/twitbot/resources/api.properties', 'rb') as read_prop:
        configs.load(read_prop)
    return configs.get(api_name).data
