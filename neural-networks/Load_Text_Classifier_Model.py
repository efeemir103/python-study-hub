#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data( \
    num_words = 10000 )

# A dictionary mapping words to an integer index

word_index = data.get_word_index()

word_index = { k:(v+3) for k, v in word_index.items() }
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2 # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

train_data = keras.preprocessing.sequence.pad_sequences( train_data,
                                                        value = \
                                                        word_index["<PAD>"],
                                                        padding="post", 
                                                        maxlen = 250 )

test_data = keras.preprocessing.sequence.pad_sequences( test_data,
                                                        value = \
                                                        word_index["<PAD>"],
                                                        padding="post", 
                                                        maxlen = 250 )

# this function will return the decoded (human readable) reviews  

def decode_review(text):
    return " ".join( [ reverse_word_index.get(i, "?") for i in text ] )

def review_encode(s):
    encoded = [ 1 ]
    
    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)

    return encoded

model = keras.models.load_model("model.h5")

with open("test.txt") as f:
    for line in f.readlines():
        nline = line.replace(",", "") \
                .replace(".", "") \
                .replace("(", "") \
                .replace(")","") \
                .replace(":", "") \
                .replace("!", "") \
                .replace("?", "") \
                .replace("\"", "") \
                .replace("'", "") \
                .strip() \
                .split(" ")
        # or just use
        # import string
        # nline = line.translate(str.maketrans('', '', string.punctuation))
        # to get rid of punctuation
        encode = review_encode(nline)
        encode = keras.preprocessing.sequence.pad_sequences( [encode],
                                                            value = \
                                                            word_index["<PAD>"], 
                                                            padding = "post", 
                                                            maxlen = 250 )
        predict = model.predict(encode)
        print(line)
        print(encode)
        print(predict[0])
