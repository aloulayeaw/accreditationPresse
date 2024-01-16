import tweepy

def get_twitter_api():
    consumer_key = 'Rd7iHj3yhLB6ScTz6qJ5TM7tD'
    consumer_secret = 'Cq71WBN6O1a8xBs8AN8WbfH3XBJKo9KuhnI1Xy0qRtripBY110'
    access_token = '1538613596-tmMNzbQFMi34UMAgRdlbEgEhrCfFt6f1kvUfM0r'
    access_token_secret = 'MIqJVxvRauM544KVe3U47MY6MhCDCtDQk9wRjdO46A0Gv'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api
