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

# 스무스하게 인스톨
pip3 install -r requirements/development.txt

# 적절하게 테스트
pytest -s -v tests/ # test all the cases...

```


### Chapter 1 -> how to use numpy 
```
# 사실 넘파이(numpy)에 대해서는 언급이 없는데, 본인이 기억이 가물가물해서..테스트코드 몇자 넣어봅니다.
# 테스트를 하는 사람중에서 아마 제가 제일 머리가 나쁜듯하네요 :D


```

### Chapter 2 -> Multi_Armd_Bandit

```
+-----------+                      +---------+
|           |                      |         |
|  Action   |--------------------> | Reward  |   멀티암드 벤딧
|           |                      |         |
+-----------+                      +---------+

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

### Chapter 3 -> Context_Bandit

```
+-------+            +--------+                +---------+
|       |            |        |                |         |
|status |  ------>   | Action |--------------> | Reward  |   멀티암드 벤딧
|       |            |        |                |         |
+-------+            +--------+                +---------+
    |                                               *
    |                                               |
    +-----------------------------------------------+
    상태                액션                      보상
                      -------->
```



## Chapter 3 -> Context_Bandit
```

# Chapter 3 Result
Mean reward for each of the 3bandits:[0.   0.   0.25]
Mean reward for each of the 3bandits:[28.75 16.25 34.75]
Mean reward for each of the 3bandits:[66.25 50.5  73.  ]
Mean reward for each of the 3bandits:[105.75  91.75 106.25]
Mean reward for each of the 3bandits:[144.   132.75 142.  ]
Mean reward for each of the 3bandits:[184.25 167.5  175.5 ]
Mean reward for each of the 3bandits:[222.75 203.75 210.25]
Mean reward for each of the 3bandits:[258.   243.5  248.75]
Mean reward for each of the 3bandits:[294.5  283.75 283.5 ]
Mean reward for each of the 3bandits:[328.   329.5  317.75]
Mean reward for each of the 3bandits:[370.   364.   352.25]
Mean reward for each of the 3bandits:[407.   402.   385.75]
Mean reward for each of the 3bandits:[448.   439.5  419.25]
Mean reward for each of the 3bandits:[488.75 477.   454.  ]
Mean reward for each of the 3bandits:[526.5  512.5  489.25]
Mean reward for each of the 3bandits:[570.25 545.25 523.75]
Mean reward for each of the 3bandits:[607.75 582.   562.  ]
Mean reward for each of the 3bandits:[642.5  618.75 601.  ]
Mean reward for each of the 3bandits:[684.   655.75 638.5 ]
Mean reward for each of the 3bandits:[728.   695.   672.25]
The agent thinks action3 for bandit1 is the most promising...
... and it was right!
The agent thinks action1 for bandit2 is the most promising...
... and it was right!
The agent thinks action0 for bandit3 is the most promising...
... and it was right!
Bye TensorFlow




```
