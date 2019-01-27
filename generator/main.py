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

def main():

    src_path = str(sys.argv[1]) # data path
    lines = int(sys.argv[2]) # approximately how many words in text to generate
    ln_break = int(sys.argv[3]) # how many characters before newline in output file
    photo_path = sys.argv[4]

    # actually run this
    #'''
    tm = {} # transition matrix as a dict
    tknzr = TweetTokenizer()

    print("generating the dictionary...")

    with open(src_path, "r+") as r:
        for line in r:
            corpus = tknzr.tokenize(line)
            md.build_matrix(corpus, tm)
    #'''

    '''
    # this is for quick use when testing sample sentence functionality
    with open("dict", "r+") as d:
        for line in d:
            tm = eval(line)
    '''

    print("making some text for you...")

    # print to console and print to file
    with open("output", "w+") as f:
        sample = md.sample_sentence(tm, lines)
        print(textwrap.fill(sample, ln_break))
        print(textwrap.fill(sample, ln_break), file=f)


    # or you could also just post it to instagram

    user = input('Please enter username: ')
    pw = input('Password: ')

    browser = webdriver.Chrome("/usr/bin/chromedriver")
    browser.get("https://www.instagram.com/accounts/login")

    userInput = browser.find_elements_by_css_selector('form input')[0]
    pwInput = browser.find_elements_by_css_selector('form input')[1]

    userInput.send_keys(user)
    pwInput.send_keys(pw)
    pwInput.send_keys(Keys.ENTER)

    ig = InstagramAPI(user, pw)
    ig.login()
    ig.uploadPhoto(photo_path, caption=sample)


if __name__ == '__main__':
    main()