# importing the module
import tweepy
import os

# personal details

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# post image function
def postImage(filepath):
    media = api.media_upload(filepath)
    text = ""
    api.update_status(status=text, media_ids=[media.media_id])
