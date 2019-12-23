# importing the module
import tweepy
import os

# personal details

consumer_key = "3Qm8tyaPvLTUqFWjClX2RqaYJ"
consumer_secret = "QWk1XXxzEVj2G3EsZZiDPYsmFiKfUIBLp4OwbDYzxpAjoZzZgw"
access_token = "1170137990888247296-KvHtelRDcnIlmGbGwpuFt938TT4REf"
access_token_secret = "kPYYDQdsXNp3nFyfIXfb7jTYf2vCQXuy7EDHQuBQlBstQ"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#filepath = "/home/pi/Desktop/sunset-1757593_960_720.jpg"

def postImage(filepath):
    media = api.media_upload(filepath)
    text = ""
    api.update_status(status=text, media_ids=[media.media_id])
