from datetime import datetime, date

from twitbot.common.databasehandler.database_connector import connect_img_db
from twitbot.common.databasehandler.image_db_operations import add_entry_video_game_image_dataset
from twitbot.endpoints.search import search_tweet, find_tweet_count_distribution
from twitbot.endpoints.upload import upload_img
from twitbot.imagerecognition.google_vision import detect_labels
from twitbot.visualize.data_preprocessor import convert_ukraine_stats_to_df
from twitbot.visualize.seaborn_visualizer import create_ukraine_war_trend_bar_graph
from twitbot.endpoints.tweet import tweet_plain_text

# Welcome to Bu's Science Lab. I write my trash code here.

# Test tweet
# tweet_plain_text("Beep Bop. Test tweet!")

# Tweet custom text
# tweet_plain_text("Just cleaned my code... Will this work?\n\nWe'll find out")

# Queries
# query = {'query': '#twitter', 'tweet.fields': 'author_id'}

# Search tweet with query
# search_tweet(ukraine_query)

# Count tweet with query
# find_tweet_count_distribution(ukraine_query)
# find_tweet_count_distribution(ukraine_war_query)

# Function to generate graph showing number of tweets relating to Ukraine in the last week


def visualize_ukraine_invasion_trend():
    ukraine_query = {'query': 'entity:ukraine lang:en', 'granularity': 'day'}
    ukraine_df = convert_ukraine_stats_to_df(find_tweet_count_distribution(ukraine_query).json())
    axes_labels = ["Date", "Tweet Count"]
    axes = ["date", "tweet_count"]
    title = 'No. of Ukraine related tweets over the week'
    save_loc = 'D:\\Projects\\Pycharm\\TwitBot\\twitbot\\resources\\graphs\\ukraine_tweet_trends_' + date.today().strftime(
        "%d-%m-%Y") + '.png'
    create_ukraine_war_trend_bar_graph(ukraine_df, axes_labels, axes, title, save_loc)
    img_upload_response = upload_img(save_loc)


def find_war_trends():
    trending_entities = ['Ukraine', 'Russia', 'Putin', 'Zelensky', 'NATO', 'UN']
    trending_entities_tweet_count_map = []
    for entity in trending_entities:
        generic_war_trends_query = {'query': entity, 'granularity': 'day'}
        tweet_count = find_tweet_count_distribution(generic_war_trends_query).json().get('meta').get(
            'total_tweet_count')
        trending_entities_tweet_count_map.append([entity, tweet_count])

    tweet = "Over the last week, the words Ukraine, Russia, Putin, Zelensky, NATO, UN appeared in tweets many millions of times.\nHere's the exact count:"
    hashtags = "#Ukraine #Analysis"
    for entity_tweet_count in trending_entities_tweet_count_map:
        tweet += "\n" + entity_tweet_count[0] + ":" + "{:,}".format(entity_tweet_count[1])
    tweet += "\n" + hashtags
    tweet_plain_text(tweet)

def main():
    pass
    # find_war_trends()
    # visualize_ukraine_invasion_trend()


main()
