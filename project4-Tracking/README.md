## cs188 project4

### Question1

题意要求我们利用gameState构建贝叶斯网络。具体构建方法可以参考`bayesNet.py`文件。

![image-20220922161737585](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922161737585.png)

可以看到为了构建贝叶斯网络，starterBayesNet构建了variableList、edgeTuplesList、variableDomainsDict。

![image-20220922162040465](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922162040465.png)

利用bayesNet构造函数完成构建。

于题目给出的贝叶斯网络的构建，首先对Ghost0、Ghost1、Pacman的位置进行定义，然后定义Pacman的观测结果，最后将图中所有有向边加入到贝叶斯网络中。

![image-20220922161439815](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922161439815.png)

结果如下：

![](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220920212405080.png)

### Question2

题意要求我们实现一个的条件概率的乘积方法。 `joinFactors` function in `factorOperations.py`接受一个条件概率列表。

![image-20220921225703311](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220921225703311.png)

观察这些例子可以发现，只有在两个乘数中都扮演条件概率角色的条件概率成为了得数的条件概率，其他均变为非条件概率。我们需要利用框架对conditional非条件概率和unconditional条件概率的区分，构建new fector，重新计算概率并将其返回。

需要注意的是条件概率和非条件概率的去重，一开始因为没有考虑到去重问题而不断调试。这里我使用set方法对condition和uncondition集合进行去重：

![image-20220921232959147](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220921232959147.png)

运行结果如下：

![image-20220921225242662](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220921225242662.png)

### Question3

该题需要完成该eliminate函数，实现消除输入变量的功能。首先从输入变量中得到条件变量集和无条件变量集，进行变量消除之后，生成新因子，最后计算概率。变量消除规则示例如下：

![image-20220921232430172](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220921232430172.png)

我们只需要遍历unconditional条件概率并删除其中我们需要eliminate的变量既可，部分代码借用了第二问。为了计算概率，我们遍历原先的factor并将其概率赋给新factor的概率。但注意的是，我们要记录原先所有条件概率并将其加和。



![image-20220922161032081](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922161032081.png)

![image-20220922163057620](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922163057620.png)

![image-20220922163116479](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922163116479.png)

如图所示，W消除后，D重复出现，应该将他们加和，最初的代码中忽略了这一点。

测试结果如下：

![image-20220922163801728](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922163801728.png)

### Question4

这道题要求我们对一个给定的联合概率不断消元，最后得到边缘分布。题目中给定了许多方便的方法：

![image-20220922164801283](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922164801283.png)

joinFactorsByVariable用来连接factor

![image-20220922165013281](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922165013281.png)

eliminationOrder直接为我们制定了我们操作variable的顺序。我们根据这个顺序逐步消元：

![image-20220922193800083](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922193800083.png)

该变量消除算法按照消除顺序迭代隐藏变量，进行连接后消除该变量，直到最后只剩余查询变量和证据变量。既当joinedFactor蕴含的非条件变量等于一时结束循环，获取下一个var进行消元：

![image-20220922193941226](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922193941226.png)

![image-20220922193644642](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922193644642.png)

遍历完所有var，算法结束，此时返回

结果如图：

![image-20220922193738709](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220922193738709.png)





