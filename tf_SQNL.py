#Computationally efficient square based nonlinearity
#to replace the popular computationally expensive Tanh
#For Tensorflow framework

import numpy as np
from scipy import arange
import tensorflow as tf


def tf_sqnl(x): #tensorflow SQNL
    #tf.cond(x>2,lambda: tf.multiply(2,1),lambda:tf.multiply(x,1))
    #tf.cond(tf.less(x,-2),lambda: -2,lambda:tf.multiply(x,1))
    u=tf.clip_by_value(x,-2,2)
    a = u
    b= tf.negative(tf.abs(u))
    wsq = (tf.multiply(a,b))/4.0
    y = tf.add(u,wsq)
    return y

