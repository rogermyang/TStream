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

    src_path = str(sys.argv[1]) # data path
    lines = int(sys.argv[2]) # approximately how many words in text to generate
    ln_break = int(sys.argv[3]) # how many characters before newline in output file
    photo_path = sys.argv[4]
    search_terms = sys.argv[5:]

    tm = {} # transition matrix as a dict
    tknzr = TweetTokenizer()



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

    user = input('Please enter username: ')
    pw = input('Password: ')

    ig = igu.login(user, pw)
    igu.post(ig, photo_path, sample)


if __name__ == '__main__':
    main()