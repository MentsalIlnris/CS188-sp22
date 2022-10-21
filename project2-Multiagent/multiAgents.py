# multiAgents.py
# --------------
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
import math

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return childGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        def finish(state,d):
            # 当应该结束递归时放回true
            return state.isWin() or state.isLose() or d == self.depth

        def minChoice(state, d, controllerId):
            if finish(state, d):
                return self.evaluationFunction(state)

            ret = float('inf')
            # 初始最小值为无穷

            # 执行min的一定是鬼魂，考虑这个鬼魂的所有可能路径
            for act in state.getLegalActions(controllerId):
                # print(gameState.getNumAgents())
                if controllerId == gameState.getNumAgents()-1:
                    # ghost值到达了控制器数量值，此时为最后一个鬼魂，下一步进入下一层递归
                    ret = min(ret, maxChoice(state.getNextState(controllerId, act), d + 1))
                else:
                    # 之后还会有应该计算的鬼魂,继续计算min
                    ret = min(ret, minChoice(state.getNextState(controllerId, act), d, controllerId + 1))
                # print(ret)
            return ret

        def maxChoice(state, d):
            if finish(state, d):
                return self.evaluationFunction(state)

            ret = -float('inf')# 初始最大值为负无穷

            for act in state.getLegalActions(0):
                ret = max(ret, minChoice(state.getNextState(0, act), d, 1))
            return ret

        result = None
        maxScore = -float('inf')

        for action in gameState.getLegalActions():
            cac = minChoice(gameState.getNextState(0, action), 0, 1)
            print(f'action{action} ret{cac}')
            # if action == 'West' and cac == -15:
            #     print('!!!!!!!!WARNING!!!!!!!!!!')
            if cac > maxScore:
                maxScore = cac
                result = action
        print(f'success{result}')
        return result


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def finish(state, d):
            return state.isWin() or state.isLose() or d == self.depth

        def minChoice(state, d, controllerId, alpha, beta):
            if finish(state, d):
                return self.evaluationFunction(state)

            value = float('inf')
            # 初始最小值为无穷

            # 执行min的一定是鬼魂，考虑这个鬼魂的所有可能路径
            for act in state.getLegalActions(controllerId):
                if controllerId == gameState.getNumAgents() - 1:
                    # ghost值到达了控制器数量值，此时为最后一个鬼魂，下一步进入下一层递归
                    value = min(value, maxChoice(state.getNextState(controllerId, act), d + 1, alpha, beta))
                else:
                    # 之后还会有应该计算的鬼魂,继续计算min
                    value = min(value, minChoice(state.getNextState(controllerId, act), d, controllerId + 1, alpha, beta))

                # 剪枝
                if value < alpha:
                    # print(f'cut {state} action {act}')
                    return value
                beta = min(beta, value)
            return value

        def maxChoice(state, d, alpha, beta):
            if finish(state, d):
                return self.evaluationFunction(state)

            value = -float('inf')  # 初始最大值为负无穷

            for act in state.getLegalActions(0):
                value = max(value, minChoice(state.getNextState(0, act), d, 1, alpha, beta))

                # 剪枝
                if value > beta:  # value >= beta: error
                    return value
                alpha = max(alpha, value)
            return value

        # 第一层的Max需要记录路径信息，于是独立出来顺便带出action。
        result = None  # 带出action
        maxScore = -float('inf')
        alphaD = -float('inf')
        betaD = float('inf')
        for action in gameState.getLegalActions():
            cac = minChoice(gameState.getNextState(0, action), 0, 1, alphaD, betaD)
            # print(f'action{action} ret{cac}')
            if maxScore < cac:
                maxScore = cac
                result = action

            alphaD = max(alphaD, maxScore)
        # print(f'success{result}')
        return result


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def finish(state, d):
            # 当应该结束递归时放回true
            return state.isWin() or state.isLose() or d == self.depth

        def expChoice(state, d, controllerId):
            if finish(state, d):
                return self.evaluationFunction(state)

            ret = 0
            # 初始0
            cnt = 0

            # 执行min的一定是鬼魂，考虑这个鬼魂的所有可能路径
            for act in state.getLegalActions(controllerId):
                cnt += 1
                # print(gameState.getNumAgents())
                if controllerId == gameState.getNumAgents() - 1:
                    # ghost值到达了控制器数量值，此时为最后一个鬼魂，下一步进入下一层递归
                    ret += maxChoice(state.getNextState(controllerId, act), d + 1)
                else:
                    # 之后还会有应该计算的鬼魂,继续计算min
                    ret += expChoice(state.getNextState(controllerId, act), d, controllerId + 1)
                # print(ret)
            return ret / cnt

        def maxChoice(state, d):
            if finish(state, d):
                return self.evaluationFunction(state)

            ret = -float('inf')  # 初始最大值为负无穷

            for act in state.getLegalActions(0):

                ret = max(ret, expChoice(state.getNextState(0, act), d, 1))
            return ret

        result = None
        maxScore = -float('inf')

        for action in gameState.getLegalActions():
            if action == 'Center' or action == 'Stop':
                continue
            cac = expChoice(gameState.getNextState(0, action), 0, 1)
            # print(f'action{action} ret{cac}')
            if cac > maxScore:
                maxScore = cac
                result = action
        # print(f'success{result}')
        return result

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    GhostStates = currentGameState.getGhostStates()
    ScaredTimes = [ghostState.scaredTimer for ghostState in GhostStates]
    foodPos = currentGameState.getFood().asList()
    ghostPos = [(G.getPosition()[0], G.getPosition()[1]) for G in GhostStates]
    pacmanPos = (currentGameState.getPacmanPosition()[0], currentGameState.getPacmanPosition()[1])

    if currentGameState.isLose():
        return float('-inf')

    if currentGameState.getPacmanPosition() in ghostPos:
        return float('-inf')

    totalScaredTimes = sum(ScaredTimes)
    dangerIdex = 0

    closestFoodDist = sorted(foodPos, key=lambda fDist: util.manhattanDistance(fDist, pacmanPos))
    foodHeuristic = 0
    l = len(closestFoodDist)
    if l == 0:
        foodHeuristic = 500
    else:
        for i in range(0, 30):
            if i >= len(closestFoodDist):
                break
            foodHeuristic += 15/math.pow(manhattanDistance(closestFoodDist[i], pacmanPos), 2)

    # Foods = [manhattanDistance(food, pacmanPos) for food in foodPos]
    # # 求最近的豆豆的距离
    # if len(foodPos) == 0:
    #     foodHeuristic = 500
    # else:
    #     # food的权重
    #     foodHeuristic = 0.5/min(Foods)

    for pos in ghostPos:
        d = manhattanDistance(pos, pacmanPos)
        if d == 1:
            dangerIdex += 200
        elif d == 2:
            dangerIdex += 40
        elif d == 3:
            dangerIdex += 8
        dangerIdex += 1/d
    if foodHeuristic == 0:
        print('warning')
    if len(currentGameState.getCapsules()) < 2:
        foodHeuristic += 50
    ret = currentGameState.getScore() + foodHeuristic - dangerIdex + totalScaredTimes
    return ret



# Abbreviation
better = betterEvaluationFunction
