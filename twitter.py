#from more_itertools import consumer
import tweepy

def connect_twitter():
    f = open("twitter_api.txt","r")
    string = f.readline()
    string = f.readline()
    api_key = string.strip()
    string = f.readline()
    string = f.readline()
    api_secret = string.strip()
    string = f.readline()
    string = f.readline()
    bearer_token = string.strip()
    string = f.readline()
    string = f.readline()
    access_token = string.strip()
    string = f.readline()
    string = f.readline()
    access_token_secret = string.strip()
    string = f.readline()
    string = f.readline()
    client_id = string.strip()
    string = f.readline()
    string = f.readline()
    client_secret = string.strip()
    f.close()
#    client = tweepy.Client(
#        consumer_key = api_key , consumer_secret=api_secret , 
#        access_token = access_token , access_token_secret=access_token_secret
#        )

#    auth = tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_secret)
#    auth.set_access_token(access_token, access_token_secret)
#    api = tweepy.API(auth)
    auth = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    return api

api = connect_twitter()
status = "bot test."
api.update_status(status)
api.update_status_with_media(status,"twitter_doc/1.jpg")
