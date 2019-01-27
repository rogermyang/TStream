import nltk
from nltk.tokenize import TweetTokenizer
nltk.download("punkt")

import model as md
import ig_utils as igu
import twt_utils as twt


def generate_tweet(creds, search_terms):

    # generate a tweet based on credentials file and a list of hashtags

    tm = {}
    tknzr = TweetTokenizer()

    # login
    twitter = twt.login_oauth1(creds)
    # search for most recent posts with hashtags, make them into a large string
    tweets = twt.tweet_search(twitter, search_terms)
    # create a tokenized list out of the large string of tweets
    corpus = tknzr.tokenize(tweets)
    # generate the transition matrix into tm
    md.build_matrix(corpus, tm)
    # create a sample tweet
    sample = md.sample_tweet(tm, search_terms)
    # then post the tweet
    twt.text_post(twitter, sample)


def generate_ig(src_path, creds, sentence_length, photo_path):

    tm = {}
    tknzr = TweetTokenizer()

    with open(src_path, "r+") as r:
        for line in r:
            corpus = tknzr.tokenize(line)
            md.build_matrix(corpus, tm)


    print("making some text for you...")

    # generate text
    sample = md.sample_sentence(tm, sentence_length)


    # or you could also just post it to instagram

    ig = igu.login(creds)
    # post photo with credentials
    igu.post(ig, photo_path, sample)
