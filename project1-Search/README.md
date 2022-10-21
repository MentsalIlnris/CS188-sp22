## CS188Project1

### Question1&2

实现 DFS 和 BFS的伪代码及结果

#### 	DFS
![image](https://user-images.githubusercontent.com/92503302/197132272-cc9d9352-46b0-4f24-b3d8-803b840701e8.png)
![image](https://user-images.githubusercontent.com/92503302/197132309-53dddea1-6919-4e48-8a56-545a54fb6ebb.png)

#### 		BFS
![image](https://user-images.githubusercontent.com/92503302/197132357-684d2c4b-d145-4a5e-a56d-50de1676e3e9.png)
![image](https://user-images.githubusercontent.com/92503302/197132403-5b0ccd64-b7ed-42fd-b60c-c38a5c477a28.png)

### Question3:

这道题在前两代题的基础上增加了怪物和路途上的其他食物，程序中表示为一条路上的开销，算法部分只需要在前两题的代码上再考虑一个路途开销问题。糖豆人每次前进，优先选择开销最小而非路程最长的路径。因此，这里存储糖豆人state的数据结构采用最小优先队列。 
![image](https://user-images.githubusercontent.com/92503302/197132478-b1e48ef8-c872-4087-addc-c4ecdc9e6dc5.png)
![image](https://user-images.githubusercontent.com/92503302/197132506-59975c3f-10f4-4b8c-bbe1-2e1a95ebd084.png)
![image](https://user-images.githubusercontent.com/92503302/197132540-f13d3b1b-518b-4314-a190-2e676377070e.png)

### Question4：A*Search

Q4需要实现A*算法以综合考虑启发函数和到达目标点开销的影响因子。Search.py中的aStarSearch中存在一个启发式函数定义heuristic，储存state方法同第三题。利用最小优先队列特性，每次都从队中pop一个最小的cost节点，如果节点没被访问过则访问他。子节点入队时带有一个priority参数，这个参数既估价函数。
![image](https://user-images.githubusercontent.com/92503302/197132620-3bf0a6a4-a822-47e8-9fa5-40f370580da0.png)

### Question5:

这道题需要定义一个problem，原先的problem都是只要到达一个特定的food位置，这里的food有四个，分别在地图的四个对角处。如果state仍然只储存位置信息，push队列时会发生冲突问题，既后续糖豆人将无法到达同一个节点，而实际上为了吃到四个food，重复的路径是必然的。

因此我们将state储存为（当前位置，吃到的food列表），将problem的解决分割为四个子问题，每两次吃food间将不冲突，因为吃过food后，food列表被改变了，此时push的state将是一个全新的系列，不会跟上一次吃food经过的节点冲突。当访问到四个food时，函数结束。
![image](https://user-images.githubusercontent.com/92503302/197132738-54fbc20b-a30a-4933-87b4-2cc746053ae4.png)

### Question6:

Q5中的启发函数heursitc始终返回0.这道题要求写一个恰当的启发函数以增强算法，降低访问的节点数量，提高程序运行速度。这里我采用了两种方法：

方法一：使用state的坐标计算到各个未访问corner的曼哈顿距离，选用最大的曼哈顿距离作为启发式函数值
![image](https://user-images.githubusercontent.com/92503302/197132868-3feb52b5-d1a2-4d56-b336-1e69b9931a21.png)

方法二：使用state的坐标计算到各个未访问corner的曼哈顿距离，将其加和作为启发函数值。情理之中地，这样的到的启发函数值会偏大而过不了test，但是结果达到了理想的500个节点。为了通过测试，这里还是将启发函数值削弱了。可以看到，随着启发函数值的削弱，访问节点数迅速上涨。
![image](https://user-images.githubusercontent.com/92503302/197132925-96b9ab6f-7386-4485-b083-8084a2ac4098.png)

