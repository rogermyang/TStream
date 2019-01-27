from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from InstagramAPI import InstagramAPI


# some utilities for working with the instagram API
# pretty barebones so far

def login(user, pw):

    # this function will start the session
    # and return a validated ig object

    browser = webdriver.Chrome("/usr/bin/chromedriver")
    browser.get("https://www.instagram.com/accounts/login")

    userInput = browser.find_elements_by_css_selector('form input')[0]
    pwInput = browser.find_elements_by_css_selector('form input')[1]

    userInput.send_keys(user)
    pwInput.send_keys(pw)
    pwInput.send_keys(Keys.ENTER)

    ig = InstagramAPI(user, pw)
    ig.login()

    return ig


def post(ig, photo_path, text):

    # takes in validated ig object
    # and then posts

    ig.uploadPhoto(photo_path, caption=text)

