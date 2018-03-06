# tensorflow_examples_with_test

SetUp
```

# 사실 친절하게 여기 모두 다 나와있다.
# 공홈 참조 https://www.tensorflow.org/install/install_mac

적절하게 설치를 해보자

for python3.x

# let's make env!
pip install --upgrade virtualenv
virtualenv --system-site-packages -p python3 ~/.env/tensor
source ~/.env/tensor/bin/activate


# let's install tensorflow
pip3 install --upgrade tensorflow


```

QuickStart
```
./pytest.sh

```

# Chapter 2 -> multi_armd_bandit

```
+------------+                      +-----------+
|            |                      |           |
|  Action    |--------------------> | Reward    |   멀티암드 벤딧
|            |                      |           |
+------------+                      +-----------+

   액션                                보상
```


```

# Chapter 2 Result

Running reward for the4arms of the bandit:[-1.  0.  0.  0.]
Running reward for the4arms of the bandit:[-1. -7. 11. 12.]
Running reward for the4arms of the bandit:[ -5. -15.  10.  25.]
Running reward for the4arms of the bandit:[-11.  -9.  12.  37.]
Running reward for the4arms of the bandit:[-12.  -8.  16.  51.]
Running reward for the4arms of the bandit:[-17.  -6.  18.  70.]
Running reward for the4arms of the bandit:[-20.  -5.  20.  88.]
Running reward for the4arms of the bandit:[-16. -13.  17. 103.]
Running reward for the4arms of the bandit:[-14.  -9.  22. 112.]
Running reward for the4arms of the bandit:[-16. -17.  25. 125.]
Running reward for the4arms of the bandit:[-18. -12.  27. 140.]
Running reward for the4arms of the bandit:[-22. -11.  33. 159.]
Running reward for the4arms of the bandit:[-27. -15.  37. 178.]
Running reward for the4arms of the bandit:[-32. -13.  35. 191.]
Running reward for the4arms of the bandit:[-36. -17.  40. 206.]
Running reward for the4arms of the bandit:[-39. -20.  36. 226.]
Running reward for the4arms of the bandit:[-35. -20.  38. 238.]
Running reward for the4arms of the bandit:[-38. -16.  40. 259.]
Running reward for the4arms of the bandit:[-44. -15.  42. 272.]
Running reward for the4arms of the bandit:[-45. -14.  41. 289.]

 The agent thinks arm4 is the most promising....
...and it was right
Bye TensorFlow


```
