#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
        keras.layers.Flatten( input_shape = (28, 28) ),
        keras.layers.Dense( 128, activation = "relu" ), # rectifier linear unit
        keras.layers.Dense( 10, activation = "softmax" )
        # get probabilities of each class using softmax
        ])

model.compile( optimizer = "adam", loss = "sparse_categorical_crossentropy",
              metrics = [ "accuracy" ] )

# sparse_categorical_crossentropy will calculate how much is lost from output
# neuron. Remember that our output is a 10 multiclass probability. That is
# why it is categorical. Sparse just makes it output integer like 1 or 2 or 3.
# Otherwise it would give one-hot encoded vectors like [1,0,0] or [0,1,0] or
# [0,0,1].

model.fit( train_images, train_labels, epochs = 5 )

# To test accuracy you need to evaluate

# test_loss, test_acc = model.evaluate( test_images, test_labels )

# print("Tested Acc: ", test_acc)

prediction = model.predict( test_images )

for i in range(10):
    plt.grid(False)
    plt.imshow( test_images[i], cmap = plt.cm.binary )
    plt.xlabel( "Actual: " + class_names[test_labels[i]] )
    plt.title( "Prediction: "+ class_names[np.argmax(prediction[i])] )
    # np.argmax will give us the max value in list,
    # hence the predicted class index.
    plt.show()
