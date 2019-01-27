from twython import Twython
import requests
import pandas as pad
import numpy as pd


def get_creds(creds_file):
    creds = []
    with open(creds_file, "r+") as f:
        for line in f:
            creds.append(line.strip())
    return creds

def login_oauth1(creds):

    # returns a twython object with oauth1 permissions, allowing you to post
    creds_list = get_creds(creds)
    app_key = creds_list[0]
    app_secret = creds_list[1]
    oauth_key = creds_list[2]
    oauth_secret = creds_list[3]

    twitter = Twython(app_key, app_secret, oauth_key, oauth_secret)

    return twitter


def login_oauth2(creds):

    # returns a twython object that can be used to search through twitter

    creds_list = get_creds(creds)
    app_key = creds_list[0]
    app_secret = creds_list[1]

    twitter = Twython(app_key, app_secret, oauth_version=2)
    access_token = twitter.obtain_access_token()
    twitter = Twython(app_key, access_token=access_token)
    return twitter

def tweet_search(twt, words):

    # basic low volume tweet search
    # takes in a twython object
    # as well as a list of search terms
    # will return a large string
    # has a fixed 10 tweets per page count right now

    ret = ""

    for word in words:
        res = twt.search(q=word, count=10)
        tweets = res['statuses']
        for tweet in tweets:
            ret = ret + " " + tweet['text']


    return ret

def text_post(twt, tweet):

    # text post to twitter with validated oauth object
    twt.update_status(status=tweet)




