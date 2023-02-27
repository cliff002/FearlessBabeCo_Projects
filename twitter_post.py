import tweepy

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# create an instance of the Twitter API client
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_to_twitter(listing):
    # compose the tweet message
    tweet = f"New listing on Etsy: {listing['title']} - {listing['url']}"

    # post the tweet
    api.update_status(tweet)
