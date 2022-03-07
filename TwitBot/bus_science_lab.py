from twitbot.endpoints.search import search_tweet
from twitbot.endpoints.tweet import tweet_plain_text

# Test tweet
# tweet_plain_text("Beep Bop. Test tweet!")

# Tweet custom text
# tweet_plain_text("Just cleaned my code... Will this work?\n\nWe'll find out")

# Search tweet with query
query_params = {'query': '#twitter', 'tweet.fields': 'author_id'}
search_tweet(query_params)
