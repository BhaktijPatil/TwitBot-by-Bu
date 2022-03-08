from datetime import datetime, date

from twitbot.endpoints.search import search_tweet, find_tweet_count_distribution
from twitbot.endpoints.upload import upload_img
from twitbot.visualize.data_preprocessor import convert_ukraine_stats_to_df
from twitbot.visualize.seaborn_visualizer import create_ukraine_war_trend_bar_graph
from twitbot.endpoints.tweet import tweet_plain_text


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
    save_loc = 'D:\\Projects\\Pycharm\\TwitBot\\twitbot\\resources\graphs\\ukraine_tweet_trends_' + date.today().strftime(
        "%d-%m-%Y") + '.png'
    create_ukraine_war_trend_bar_graph(ukraine_df, axes_labels, axes, title, save_loc)
    img_upload_response = upload_img(save_loc)


def main():
    visualize_ukraine_invasion_trend()
    # tweet


main()
