from tests.chapter_2.base import BaseTest


class TestSmokeTest(BaseTest):


    def test_import_tendorflows(self):

        import tensorflow as tf
        import tensorflow.contrib.slim as slim
        import numpy as np

        bandit_arms = [0.2, 0, -0.2, -2]

        num_arms = len(bandit_arms)

        def pullBandit(bandit):
            # 랜덤한 값을 구한다.
            result = np.random.randn(1)

            if result > bandit:
                # 양의 보상을 반환한다.
                return 1

            else:
                # 음의 보상을 반환한다.
                return -1

        tf.reset_default_graph()

        # 네트워크에 피드포워드 부분을 구현한다.

        weights = tf.Variable(tf.ones([num_arms]))
        output = tf.nn.softmax(weights)

        # 학습과정을 구현한다.
        # 보상과 선택된 네트워크에 피드해줌으로써 비용을 계산하고
        # 비용을 이용해 네트워크를 업데이트한다.

        reward_holder = tf.placeholder(shape=[1], dtype=tf.float32)
        action_holder = tf.placeholder(shape=[1], dtype=tf.int32)

