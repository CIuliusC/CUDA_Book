# -*- coding: utf-8 -*-
"""TF_HelloWorld.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1igJxTEGp8HdLlEzGIMa_hVrGtnCOO7F0
"""

import tensorflow as tf

print(tf.__version__)

message = tf.constant('Hello World')

print(message)

tf.print(message)