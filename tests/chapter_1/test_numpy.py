# -*- coding: utf-8 -*-

import numpy as np

from tests.base import BaseTest

class TestNumpyTest(BaseTest):

    def test_numpy(self):
        arr = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

        assert arr.shape[0] == 2 # 전체적으로 2 묶음

        assert arr.shape[1] == 5 # 내부에 5개의 아이템


