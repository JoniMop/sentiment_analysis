import tweepy
from textblob import TextBlob
consumer_key = 'BJxeCFqHEWZ7i4vNYB7TNixT2'
consumer_secret = 	'7KiIcK2im611jh5equHRjf2S8GFoJ9ibOCzv2OAZToGc7TO74k'

access_token = '54979064-1gPh0EgRtRU26GL9COdoWlsVim792xUnaEWXBJb3A'
access_token_secret = 'QEDUibSiUQbqJlowLuDt6cR9g1TbTxQfx7HQei3Ccyb3K'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Santa Teresa, Costa Rica')

for tweet in public_tweets:
	print tweet.text
	analysis = TextBlob(tweet.text)
	print analysis.sentiment
