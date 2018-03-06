
from tests.base import BaseTest

import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np


class ContextualBandit(object):

    # 메모리를 아끼기 위해서 __slots__ 사용
    __slots__ = ["state", "bandits", "num_bandits", "num_actions"]

    def __init__(self):
        self.state = 0
        #  밴딧들의 손잡이 목록을 작성. 각 밴딧은 각각 손잡이 4, 2, 1이 최적이다.
        self.bandits = np.array([
            [0.2, 0, -0.0, -5],
            [0.1, -5, 1, 0.25],
            [-5, 5, 5, 5]
        ])

        self.num_bandits = self.bandits.shape[0]
        self.num_actions = self.bandits.shape[1]

    def get_bandit(self):
        #  각각의 에피소드에 대해 랜덤한 상태를 반환
        self.state = np.random.randint(0, len(self.bandits))
        return self.state

    def pull_arm(self, action):
        # 랜덤한 수를 얻는다.
        bandit = self.bandits[self.state.action]
        result = np.random.randn(1)

        if result > bandit:
            # 양 의 보상을 반환한다.
            return 1
        else:
            # 음의 보상을 반환한다.
            return -1


class Agent():

    __slots__ = ["state_in", "state_in_OH", "output", "chosen_action", "reward_holder", "action_holder", "responsible_weight", "loss", "optimizer", "update"]

    def __init__(self, lr, s_size, a_size):
        # 네트워크의 피드포워드 부분, 에이전트는 상태를 받아서 액션을 출력한다.
        self.state_in = tf.placeholder(shape=[1], dtype=tf.int32)
        state_in_OH = slim.one_hot_encoding(self.state_in, s_size)
        output = slim.fully_connected(state_in_OH, a_size, biases_initializer=None, activation_fn=tf.nn.sigmoid, weights_initializer=tf.ones_initializer())

        self.output = tf.reshape(output, [-1])
        self.chosen_action = tf.argmax(self.output, 0)

        # 학습과정을 구현한다.
        # 비용을 계산하기 위해 보상과 선택된 액션을 네트워크에 피드하고,
        # 네트워크를 업데이트하는 데에 이를 이용한다.

        self.reward_holder = tf.placeholder(shape=[1], dtype=tf.float32)
        self.action_holder = tf.placeholder(shape=[1], dtype=tf.int32)

        self.responsible_weight = tf.slice(self.output, self.action_holder, [1])
        self.loss = -(tf.log(self.responsible_weight)* self.reward_holder)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
        self.update = optimizer.minimize(self.loss)



class TestContextBanditTest(BaseTest):

    def test_class_init_test(self):
        res = ContextualBandit()

    def test_context_bandit(self):

        # 텐서플로 그래프를 리셋한다.
        tf.reset_default_graph()

        # 벤딧을 로드한다.
        cBandit = ContextualBandit()

        # 에이전트를 로드한다.

        myAgent = Agent(lr=0.001, s_size=cBandit.num_bandits, a_size=cBandit.num_actions)
