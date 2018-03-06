import unittest

import tensorflow as tf

class BaseTest(tf.test.TestCase):

    def setUp(self):
        print("Let's Start with TensorFlow!")
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    def tearDown(self):
        print("Bye TensorFlow")
