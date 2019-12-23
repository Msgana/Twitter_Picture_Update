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

# time stamp images before positng to twitter
def timeStamp(filepath):
     # Create our stamp variable
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create time stamp command to have executed
    timestampCommand = "/usr/bin/convert " + completeFilePath + " -pointsize 30 \
    -fill green -annotate +750+700 '" + timestampMessage + "' " + completeFilePath
    # Actually execute the command!
    call([timestampCommand], shell=True)

# post image function
def postImage(filepath):
    media = api.media_upload(filepath)
    text = ""
    api.update_status(status=text, media_ids=[media.media_id])
    

