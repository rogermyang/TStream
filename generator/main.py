from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from InstagramAPI import InstagramAPI
from PIL import Image
import sys
import nltk
import textwrap
from nltk.tokenize import TweetTokenizer
nltk.download("punkt")

import model as md
import ig_utils as igu
import twt_utils as twt

def main():

    ig_flag = int(sys.argv[1])
    # post on instagram or not?

    tm = {} # transition matrix as a dict
    tknzr = TweetTokenizer()

    if ig_flag == 0:
        # post to twitter
        creds = str(sys.argv[2]) # path to credentials file
        search_terms = sys.argv[3:]

        # log in to twitter with oauth1

        twitter = twt.login_oauth1(creds)

        # space to grab tweets

        tweets = twt.tweet_search(twitter, search_terms)

        # then transform them into a matrix
        corpus = tknzr.tokenize(tweets)
        md.build_matrix(corpus, tm)

        # create sample and post
        sample = md.sample_tweet(tm, search_terms)
        twt.text_post(twitter, sample)

    elif ig_flag == 1:
        # post to instagram
        src_path = str(sys.argv[2]) # data path
        lines = int(sys.argv[3]) # approximately how many words in text to generate
        ln_break = int(sys.argv[4]) # how many characters before newline in output file
        creds = str(sys.argv[5])
        photo_path = str(sys.argv[6])

        with open(src_path, "r+") as r:
            for line in r:
                corpus = tknzr.tokenize(line)
                md.build_matrix(corpus, tm)


        print("making some text for you...")

        # print to console and print to file
        with open("output", "w+") as f:
            sample = md.sample_sentence(tm, lines)
            print(textwrap.fill(sample, ln_break))
            print(textwrap.fill(sample, ln_break), file=f)


        # or you could also just post it to instagram

        # grab credentials from creds file
        with open(creds, "r+") as f:
            i = 0
            for line in f:
                if i == 0:
                    user = line
                if i == 1:
                    pw = line
                if i > 1:
                    break
                i += 1

        # login and post

        ig = igu.login(creds)
        igu.post(ig, photo_path, sample)


if __name__ == '__main__':
    main()