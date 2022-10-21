## CS188 project 6

### Question1

题目要求我们完成valueIterationAgent，这个agent接受一个马尔可夫状态并计算其迭代状态。需要我们完成的有三个函数：

1、runValueIteration：主要函数，使当前马尔可夫状态迭代，他会调用下面将要实现的计算QValue的函数，在每个迭代过程中，我们需要遍历当前states的每一个state并记录最大的QValue值，以找到当前决策模型下的最优解。所有value将储存在agent中的values中，方便其他函数进行查询。

![image-20221006143356617](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006143356617.png)

![image-20221006143404014](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006143404014.png)

2、computeActionFromValues

如同函数名称，根据state我们利用该函数计算当前state下最好的action。遍历所有可能action，期望的受益是Qvalue，这个值将由下一个函数计算。

![image-20221006143556665](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006143556665.png)

3、computeQValueFromValues

根据state和action计算QValue并返回的函数。我们遍历mdp模型中的过渡状态概率和受益计算概率加权期望受益并返回这个值，前两个函数通过这个值来判断最优选择。

运行结果：

 ![image-20221006142239844](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006142239844.png)

![image-20221006142224874](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006142224874.png)

![image-20221006143843336](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006143843336.png)

### Question 2

这道题要求我们调整三个参数以改变马尔可夫决策结果。比较简单：

可调参数有三：

answerDiscount：终局得分对决策的影响指数。这个值越高，决策越倾向于选择一条找到更高的终局得分的路线，值越低则终局得分的影响指数低，则agent不考虑终局的得分，所有终局点看起来都差不多。

answerNoise：周围格子对决策的影响指数。这个值越高，agent越考虑因噪声误入危险格子的可能。若周围存在危险格子，agent将不倾向于选择他。这个值越低，agent将愿意冒险。

answerLivingReward：存活对决策的影响指数。这个值越高，agent越倾向于找到一条更远的终局路线。这个值越低，agent将不愿意花长时间去寻找更远路径。

依照这些判断条件不难控制马尔可夫决策导出五种不同的结果。

![image-20221017163933853](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017163933853.png)

![image-20221017163948721](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017163948721.png)

![image-20221006150656648](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221006150656648.png)

### Question 3

本题要求我们实现qlearningAgents.py中的QLearningAgent，其中这些函数等待实现：

getQValue()：返回 Q(state,action)，如果我们从未见过状态或 Q 节点值，则应返回 0.0。
computeValueFromQValues()：返回 max_action Q(state,action)，其中最大值超过合法动作。请注意，如果没有合法操作，即终端状态下的情况，则应返回值 0.0。
computeActionFromQValues()：计算在某种状态下采取的最佳行动。请注意，如果没有法律行为，在终端状态就是这种情况，您应该返回None。
update()：进行Q-Value的更新。

![image-20221017164940670](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017164940670.png)

### Question 4

本题要求我们实现qlearningAgents.py中QLearningAgent中的getAction()：getAction()函数的作用是计算在当前状态下要采取的行动。对于概率self.epsilon，我们应该采取随机行动，否则采取最佳策略行动。

![image-20221017164921119](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017164921119.png)

![image-20221017165347361](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017165347361.png)

### Question 5

运用题中所给的参数设置，在前两个题目的代码下直接运行既可：

![image-20221017170745443](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017170745443.png)

### Question 6

本题要求我们实现qlearningAgents.py中的ApproximateQAgent，其中这些函数等待实现：

getQValue()：返回 Q(state,action)，但是跟之前不同的是，这里要乘上一个featureVector系数

![image-20221017195411557](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017195411557.png)

update()：将weight列表进行更新，使用学习系数和difference

![image-20221017195438039](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017195438039.png)

final():用于调试

![image-20221017192904839](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20221017192904839.png)