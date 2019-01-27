from twython import Twython
import pandas as pad
import numpy as pd


def login(app_key, app_secret):

    # returns a twython object that can be used to search through twitter

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



