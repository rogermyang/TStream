import numpy as np
import scipy as sp
import pandas as pd
import re
import random
import pykov
import nltk
from nltk.tokenize import TweetTokenizer
nltk.download("punkt")


def build_matrix(words, dictionary):

    # takes in list of words and a dictionary
    # will place the words into the dictionary
    # the dictionary is a word and a list of words
    # the list of words being known words that follow from it

    for i in range(0, len(words)):
        word = words[i]

        if i != len(words) - 1:
            next_word = words[i+1]
        else:
            next_word = words[0]

        if word not in dictionary:
                dictionary[word] = []

        dictionary[word].append(next_word)


def sample_sentence(matrix, length, runtime=1000):

    # define relevant pattern
    non_word_pattern = re.compile('\\W+$') # at least one non word character
    end_pattern = re.compile(r'[.?!]\s*')

    sentence = ""
    current_word = random.choice(list(matrix.keys())) # grab a random word to start
    i = 0

    flag = 0
    # need to start a sentence with upper case after all

    # then run it until stability
    while i in range(0, runtime + length) or not re.match(end_pattern, current_word):

        if i == runtime:
            flag = 1

        if i >= runtime and flag == 1:

            # start sentence with a capital word
            if((re.match(non_word_pattern, current_word) or i == runtime) and current_word != ','):
                # if you ended with punctuation
                # then you need to find a capital!
                while not current_word[0].isupper():
                    temp = random.choice(list(matrix.keys()))
                    if(temp[0].isupper()):
                        current_word = temp
                        break # break if you reach a capital

                # append to end of sentence
                # if its the first word no need for a space
                if(sentence == ""):
                    sentence += current_word
                else:
                    sentence += " " + current_word

            # otherwise if it's not the start of a sentence keep going
            else:
                current_word = np.random.choice(matrix[current_word], size=1)[0]

                if(re.match(non_word_pattern, current_word)):
                    sentence += current_word
                else:
                    sentence += " " + current_word

        i += 1

    return sentence