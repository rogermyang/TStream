from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from InstagramAPI import InstagramAPI


# some utilities for working with the instagram API
# pretty barebones so far

def get_creds(creds_file):

    # parse key file for user and password and log in with them

    creds = []
    with open(creds_file, "r+") as f:
        for line in f:
            creds.append(line.strip())
    return creds

def login(creds_file):

    # this function will start the session
    # and return a validated ig object

    creds = get_creds(creds_file)
    user = creds[0]
    pw = creds[1]

    # start browser

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

