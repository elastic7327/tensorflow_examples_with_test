
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


class TestContextBanditTest(BaseTest):

    def test_class_init_test(self):
        res = ContextualBandit()

    def test_context_bandit(self):
        pass
