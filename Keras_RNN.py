# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:54:21 2018

@author: guyia
"""

import tensorflow as tf
from tensorflow import keras

print('Loading data...')
#imdb has 5000 training reviews and 25000 testing reviews
#num_words: how many unique words you want to upload to your datasets
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=20000)#20000 indicates the most popular 20000 words in the datasets

print(x_train[0])#the results show numbers, each number indicates an unique word in the num_words(20000 here)

print(y_train[0])#show the review like(1) or dislike(0) the movie


#RNN can blow up very quickly, have to back-propagate through time, so we need a upper bound
#maxlen: we will review the first 80 words of each review
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=80)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=80)

model = tf.keras.models.Sequential()#build up the typology of the network at a time here
model.add(tf.keras.layers.Embedding(20000, 128))#pre_processing, convert the input data into dense vector of some fixed size.
                                                # for here, a dense vec of a fixed size of 20000 words and funnel into 128
#embeddig layer: take the input texual data(has been encoded), convert that into a format, which is suitable for
#imput into my NN
model.add(tf.keras.layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2))#add LSTM
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))#binary classification

# how to optimize and train the model
model.compile(loss='binary_crossentropy',#a ultimately binary problem, "this person like the movie or not"
              optimizer = 'adam',# the best for both worlds for optimizer
              metrics = ['accuracy'])

# 

model.fit(x_train, y_train,
          batch_size=32,
          epochs =15,
          verbose=2,
          validation_data=(x_test,y_test))

score,acc = model.evaluate(x_test,y_test,
                           batch_size=32,
                           verbose=2)

print('test score:',score)
print('accuracy:',acc)

