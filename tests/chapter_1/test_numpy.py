# -*- coding: utf-8 -*-

import numpy as np

from tests.base import BaseTest

class TestNumpyTest(BaseTest):

    def test_numpy(self):
        arr = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]])

        assert arr.shape[0] == 4 # 전체적으로 2 묶음

        assert arr.shape[1] == 5 # 내부에 5개의 아이템

        print(np.random.randn(1))

        # assert np.random.randn(1) in range(1000)

        num_bandits = 4
        num_actions = 3

        total_rewards = np.zeros([num_bandits, num_actions])
        """
        rewards =>
        array([[0., 0., 0.],
               [0., 0., 0.],
               [0., 0., 0.],
               [0., 0., 0.]])
        """

        res = np.mean(arr, axis=1)
        """
        # 평균 구하는
        [3. 3. 1. 2.]
        """
        print(res)
