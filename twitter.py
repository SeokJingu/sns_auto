#from more_itertools import consumer
from ast import Num
from tempfile import tempdir
from isort import file
import tweepy
import random
import time
from datetime import datetime



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
    auth = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def read_doc(file_name):
    file = open("twitter_doc/"+str(file_name)+".txt","r", encoding='utf-8')
    status = file.read()
    file.close()
    return status

def twitter_post():
    api = connect_twitter()
    random_num = random.randrange(1,19)
    doc_num = str(random_num)
    status = read_doc(doc_num)
    picture_file = "twitter_doc/"+doc_num+".jpg"
    api.update_status_with_media(status,picture_file)

def main():
    current_time = datetime.now()
    old_hour = current_time.minute
    while True:
        current_time = datetime.now()
        if current_time.hour != old_hour :
            twitter_post()
        old_hour = current_time.minute

main()

