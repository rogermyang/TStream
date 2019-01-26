import numpy as np
import scipy as sp
import pandas as pd
import re
import random
import pykov
import nltk
from nltk.tokenize import TweetTokenizer
nltk.download("punkt")

import generator as md

def main():

    df = pd.read_csv("tweets.csv")
    df_text = df.Text
    tm = {} # transition matrix as a dict
    tknzr = TweetTokenizer()


    for i in range(0, 1000):
        corpus = tknzr.tokenize(df_text[i])
        md.build_matrix(corpus, tm)

    print(md.sample_sentence(tm, 30))

if __name__ == '__main__':
    main()