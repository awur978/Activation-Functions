import numpy as np
from scipy import arange
import tensorflow as tf

def tf_sqnlsig(x):   #tensorflow SQNLsigmoid
    u=tf.clip_by_value(x,-2,2)
    a = u
    b= tf.negative(tf.abs(u))
    wsq = (tf.multiply(a,b))/4.0
    y = tf.add(tf.multiply(tf.add(u,wsq),0.5),0.5)
    return y
