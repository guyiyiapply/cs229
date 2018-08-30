# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:04:21 2018

@author: guyia
"""
#MNIST data set, a collection of 70,000 handwriting samples of the numbers 0-9. Our 
#challenge - to predict which number each handwritten image represents.

#Each image is 28x28 grayscale pixels, so we can treat each image as just a 1D array, 
#or tensor, of 784 numbers. As long as we're consistent in how we flatten each image 
#into an array, it'll still work. 
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#an interactive session in tenserflow, which makes it easier to work with TensorFlow with an iPython
#this removes the need of actually explicitly creating a session and looping within it,
#we want to break up this work across multiple code blocks, so that's how we do that here with an interactive
sess = tf.InteractiveSession()


# mnist is a database, provides 55,000 samples in a training data set, 
#10,000 samples in a test data set, and 5,000 samples in a "validation" data set
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)# one_hot means [0,1,0,0], 1 indicates the number is 1, 0 indicataes the numebr is not here

import matplotlib.pyplot as plt

def display_sample(num):
    #Print the one-hot array of this sample's label
    #train.label is the [0,1,0,0,0,0,0,0,0,0] array of the trainning data, each training data has an array label to present what number the image describes
    print(mnist.train.labels[num]) 
    
    #Print the label converted back to a number
    #argmax(): take the array element with the largest value and display that array element's value
    label = mnist.train.labels[num].argmax(axis=0)
    
    #Reshape the 768 values to a 28x28 image
    image = mnist.train.images[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

#display the image of number.1239    
display_sample(1239)

import numpy as np

images = mnist.train.images[0].reshape([1,784])
for i in range(1, 500):
    images = np.concatenate((images, mnist.train.images[i].reshape([1,784])))
plt.imshow(images, cmap=plt.get_cmap('gray_r'))
plt.show()

#load the input data
input_images = tf.placeholder(tf.float32, shape=[None, 784])#28*28 image, describe in one line
target_labels = tf.placeholder(tf.float32, shape=[None, 10])#label of each image

hidden_nodes = 512#want to decrease to 512 nodes in hidden layer

input_weights = tf.Variable(tf.truncated_normal([784, hidden_nodes]))# give the weights and the bias to input layer
input_biases = tf.Variable(tf.zeros([hidden_nodes]))

hidden_weights = tf.Variable(tf.truncated_normal([hidden_nodes, 10]))#give the same to hidden layer
hidden_biases = tf.Variable(tf.zeros([10]))

#construct y = wx+b
input_layer = tf.matmul(input_images, input_weights)#wx
hidden_layer = tf.nn.relu(input_layer + input_biases)#wx+b for hidden
digit_weights = tf.matmul(hidden_layer, hidden_weights) + hidden_biases # the result from last layer, and calculate wx+b again

#the generated results are compared with the labeled results(real) 
loss_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=digit_weights, labels=target_labels))

#use GD to optimize the result, 0.5 is the step size
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss_function)

#We'll set up a Tensorflow session, and initialize our variables. Next we will train our network in 2000 steps
# (or "epochs") with batches of 100 samples from our training data. At each step, we assign the input_images 
#placeholder to the current batch of training images, and the target_labels placeholder to the current batch 
#of training labels. Once training is complete, we'll measure the accuracy of our model using the accuracy 
#graph we defined above. While measuring accuracy, we assign the input_images placeholder to our test images, 
#and the target_labels placeholder to our test labels.
correct_prediction = tf.equal(tf.argmax(digit_weights,1), tf.argmax(target_labels,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

tf.global_variables_initializer().run()

for x in range(3000):
    batch = mnist.train.next_batch(100)
    optimizer.run(feed_dict={input_images: batch[0], target_labels: batch[1]})
    if ((x+1) % 100 == 0):
        print("Training epoch " + str(x+1))
        print("Accuracy: " + str(accuracy.eval(feed_dict={input_images: mnist.test.images, target_labels: mnist.test.labels})))
        
for x in range(100):
    # Load a single test image and its label
    x_train = mnist.test.images[x,:].reshape(1,784)
    y_train = mnist.test.labels[x,:]
    # Convert the one-hot label to an integer
    label = y_train.argmax()
    # Get the classification from our neural network's digit_weights final layer, and convert it to an integer
    prediction = sess.run(digit_weights, feed_dict={input_images: x_train}).argmax()
    # If the prediction does not match the correct label, display it
    if (prediction != label) :
        plt.title('Prediction: %d Label: %d' % (prediction, label))
        plt.imshow(x_train.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
        plt.show()