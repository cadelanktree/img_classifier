#inspired by: https://www.youtube.com/watch?v=iGWbqhdjf2s

#import modules
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
plt.style.use('fivethirtyeight')

#load data
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()



#look at data types of vars
print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))

#Get shape of the arrays
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'frog', 'horse', 'ship', 'truck']
print('The image class is:', classification[y_train[0][0]])

