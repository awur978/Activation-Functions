'''
This is version 2 which is much faster than version 1
This is an activation function called SQLU (Square Linear Unit), a replacement for the fast and accurate
ELU (Exponential Linear Unit). This new function eliminates the use of exponential function and can
achieve the same accuracy and sometimes better but at a very fast convergence speed in times of wall clock. 
Mathematically, exponent terms are very expensive and requires a call to higher libraries and can't be 
implemented directly on hardware without the use of LUT or some approximation techniques. 
Eliminating this term in an activation function is guaranteed to speed up the NN model training
'''
#In this code, I implemented the new function using tensorflow, I implemented both the forward function and its derivative. Even though tensorflow will do autodifferentiation, just feel like doing both. The graph of the activation function is plotted as well
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops
from scipy import arange
import matplotlib.pyplot as plt
import keras

def tf_sqlu(x):
    u=tf.clip_by_value(x,-2,200)
    a = u
    alpha = 1.0
    t = alpha*(a + (a*a)/4.0) 
    cond = tf.greater(a,tf.constant(0.0))
    return tf.where(cond, a, t)

'''
        
with tf.Session() as sess:
    start = -8
    limit = 8
    delta = 0.1
    x=tf.range(start, limit, delta)
    #x = tf.constant([1.1])
    y = tf_sqlu(x)
    #tf.initialize_all_variables().run()
    tf.global_variables_initializer().run()

    #print(y.eval())
    plt.plot(x.eval(),y.eval())
    plt.grid(True)
    plt.show()
'''