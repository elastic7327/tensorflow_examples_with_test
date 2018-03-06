import unittest

import tensorflow as tf

class BaseTest(tf.test.TestCase):

    def setUp(self):
        print("Let's Start with TensorFlow!")

        # *******************************************************************************************
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        # Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
        # issue solution
        # *******************************************************************************************

    def tearDown(self):
        print("Bye TensorFlow")
