import unittest

import tensorflow as tf

class BaseTest(tf.test.TestCase):

    def setUp(self):
        print("Let's Start with TensorFlow!")

    def tearDown(self):
        print("Bye TensorFlow")
