# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #递归返回过程构建path，事实证明比较繁琐
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # soup = set()
    # soup.add(problem.getStartState())
    # path = []
    # def dfs(state,step,minStep):
    #     if problem.isGoalState(state):
    #         if step < minStep:
    #             minStep = step
    #             path.clear()
    #             return minStep
    #         else:
    #             return -1
    #     else:
    #         Flag = -1
    #         for successor in problem.getSuccessors(state):
    #             if successor[0] not in soup:
    #                 soup.add(successor[0])
    #                 dfsRet = dfs(successor[0], step + 1, minStep)
    #                 if  dfsRet > 0:
    #                     minStep = dfsRet
    #                     path.append(successor[1])
    #                     Flag = minStep
    #                 soup.remove(successor[0])
    #         return Flag
    #
    # dfs(problem.getStartState(),0,999)
    # return path[::-1]

    # 递归，但是在参数中构建path，每一层递归都有一个当前path
    soup = set()#存储已访问节点
    soup.add(problem.getStartState())
    min=[]
    def dfs(state, step, minCost,path):
        if problem.isGoalState(state):
            if problem.getCostOfActions(path) < minCost:
                minCost = problem.getCostOfActions(path)
                min.clear()
                #更新min以载入新找到的最短路径
                for i in range(len(path)):
                    min.append(path[i])
                return minCost
            else:
                return -1
        else:
            Flag = -1
            for successor in problem.getSuccessors(state):
                if successor[0] not in soup:
                    soup.add(successor[0])
                    path.append(successor[1])
                    dfsRet = dfs(successor[0], step + 1, minCost,path)
                    if dfsRet > 0:#找到到达目标点的路径，记录这个minCost
                        minCost = dfsRet
                        Flag = minCost
                        return minCost#直接return;如果要找最短路径则修改此处不return继续寻找
                    path.pop()
            return Flag

    dfs(problem.getStartState(), 0, 9999,[])
    return min



def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    '''soup = util.Queue()
    soup.push((0, (problem.getStartState(), [])))
    visited = []
    visited.append(problem.getStartState())
    min = []
    minCost = float('inf')
    while not soup.isEmpty():
        cur = soup.pop()
        path = cur[1][1]
        #print(cur)
        if cur[0] >= minCost:
            continue
        elif problem.isGoalState(cur[1][0]) is True:
            #print(cur)
            if cur[0] < minCost:
                #minCost = cur[0]
                min = copy.deepcopy(path)
                #print('find')
                #print(min)
                return min  # 直接返回第一个找到的
            else:
                continue
        else:
            for successor in problem.getSuccessors(cur[1][0]):
                if successor[0] not in visited:
                    p = copy.deepcopy(path)
                    p.append(successor[1])
                    #print(problem.getCostOfActions(p))
                    soup.push((problem.getCostOfActions(p), (successor[0], p)))
                    visited.append(successor[0])
        #print(soup.list)
    return min'''
    current_position = (problem.getStartState(), [])
    possible_nodes = util.Stack()
    visited_nodes = set()
    while not problem.isGoalState(current_position[0]):
        if current_position[0] not in visited_nodes:
            visited_nodes.add(current_position[0])
            children = problem.expand(
                current_position[0])  # Returns child states, a list of tuple(child, action, stepCost)
            for child in children:
                if child[0] not in visited_nodes:
                    possible_nodes.push((child[0], current_position[1] + [child[1]]))
        current_position = possible_nodes.pop()
        # print("current:", current_position)
    return current_position[1]




from queue import PriorityQueue
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """把初始结点放到Frontier集合里面（优先队列）
    重复以下过程直到Frontier变成空的：
    从Frontier里面把带有最小的优先权p（PastCost）的结点取出来
    如果s是终止状态的话，返回整个方案。
    移动s到Explored里面
    对于每个行动s的每一个action：
    得到相应的successor s’ < - Succ(s, a)
    如果s’ 已经在Explored里面的话：continue整个循环
    添加s’到Frontier集合，并且priority是p + cost(s, a)."""
    soup = PriorityQueue()
    soup.put((0,(problem.getStartState(),[])))
    visited = []
    visited.append(problem.getStartState())
    min = []
    minCost = float('inf')
    while not soup.empty():
        cur = soup.get()
        path = cur[1][1]
        #print(cur)
        if cur[0] >= minCost:
            continue
        elif problem.isGoalState(cur[1][0]) is True:
            #print(cur)
            if cur[0] < minCost:
                minCost = cur[0]
                min = copy.deepcopy(path)
                return min#第一个找到的一定为最短路径
            else:
                continue
        else:
            for successor in problem.getSuccessors(cur[1][0]):
                if successor[0] not in visited:
                    p = copy.deepcopy(path)
                    p.append(successor[1])
                    print(problem.getCostOfActions(p))
                    soup.put((problem.getCostOfActions(p),(successor[0],p)))
                    visited.append(successor[0])
            #visited.remove(successor[0])
    return min



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    soup = util.PriorityQueue()
    soup.push((problem.getStartState(), []),0)
    visited = []
    visited.append(problem.getStartState())
    min = []
    #minCost = float('inf')
    while not soup.isEmpty():
        cur = soup.pop()
        path = cur[1]
        #print(cur)
        #print(problem.getCostOfActions(path) + heuristic(cur[0], problem))
        if problem.isGoalState(cur[0]) is True:
            # 第一个找到的一定为最短路径
            min = copy.deepcopy(path)
            return min
        else:
            for successor in problem.getSuccessors(cur[0]):

                if successor[0] not in visited:
                    #print(successor[0])
                    p = copy.deepcopy(path)
                    p.append(successor[1])
                    priority = problem.getCostOfActions(p)+heuristic(successor[0],problem)
                    for index, (n, c, i) in enumerate(soup.heap):
                        if i[0] == successor[0]:
                            if n <= priority:
                                break
                            #print("enter")
                            del soup.heap[index]
                            soup.push((successor[0], p), priority)
                            #soup.heap.append((priority, c, successor[0]))
                            break
                    else:
                        soup.push((successor[0], p), priority)

            visited.append(cur[0])
            #print(soup.heap)
    return min


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
