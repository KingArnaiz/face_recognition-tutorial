'''
Load pretrain models and create a tensorflow session to run them

@Author: Ronrick Da-ano
'''
import tensorflow as tf


class FaceRecGraph(object):
    def __init__(self):
        self.graph = tf.Graph();
