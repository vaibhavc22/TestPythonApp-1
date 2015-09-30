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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    return  DFSStack(problem)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return BFSPriorityQueue(problem)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return CostSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return AStarSearch(problem,heuristic)

def DFSStack(problem):
    from game import Directions
    import util
    import searchNode

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    closedSet=set()
    fringe=util.Stack()
    node= searchNode.searchNode(tuple([problem.getStartState(),"START",0]))
    fringe.push(node)
    foundGoal=False

    while not foundGoal:
        currentNode=fringe.pop()
        if(problem.isGoalState(currentNode.currentState[0])):
            foundGoal=True
            #print('goal!!!!')
            break
        #print("Current: ",currentNode.currentState)
        #print ("umm successors: ", problem.getSuccessors(currentNode.currentState[0]))
        #closedSet.add(currentNode.currentState[0])
        if currentNode.currentState[0] not in closedSet:
            closedSet.add(currentNode.currentState[0])
            for successors in problem.getSuccessors(currentNode.currentState[0]):
                #print("Successor: ",successors)
                #Just undid if successors[0] not in closedSet:
                #Just undid    closedSet.add(successors[0])
                    #print(closedSet)
                newNode=searchNode.searchNode(successors,currentNode)
                fringe.push(newNode)
        #raw_input("Press Enter to continue...")
    return  currentNode.GetDirections()

def BFSPriorityQueue(problem):
    from game import Directions
    import util
    import searchNode
    import Postgres

    #myPG = Postgres.Postgres()

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    closedSet=set()
    fringe=util.PriorityQueue()
    node= searchNode.searchNode(tuple([problem.getStartState(),"START",0]))
    fringe.push(node,node.currentDepth)
    foundGoal=False

    while not foundGoal:
        currentNode=fringe.pop()
        if(problem.isGoalState(currentNode.currentState[0])):
            foundGoal=True
            print('goal!!!!')
            break
        #print("Current: ",currentNode.currentState)
        #print ("umm successors: ", problem.getSuccessors(currentNode.currentState[0]))
        #closedSet.add(currentNode.currentState[0])
        if currentNode.currentState[0] not in closedSet:
            closedSet.add(currentNode.currentState[0])
            for successors in problem.getSuccessors(currentNode.currentState[0]):
            #print("Successor: ",successors)
            #if successors[0] not in closedSet:
                #closedSet.add(successors[0])
                #print(closedSet)
                #myPG.WriteState(successors[0])
                newNode=searchNode.searchNode(successors,currentNode)
                fringe.push(newNode,newNode.currentDepth)
        #raw_input("Press Enter to continue...")
    return  currentNode.GetDirections()

def CostSearch(problem):
    from game import Directions
    import util
    import searchNode

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    closedSet=set()
    fringe=util.PriorityQueue()
    node= searchNode.searchNode(tuple([problem.getStartState(),"START",0]))
    fringe.push(node,node.currentCost)
    foundGoal=False

    while not foundGoal:
        currentNode=fringe.pop()
        if(problem.isGoalState(currentNode.currentState[0])):
            foundGoal=True
            print('goal!!!!')
            break
        #print("Current: ",currentNode.currentState)
        #print ("umm successors: ", problem.getSuccessors(currentNode.currentState[0]))
        #closedSet.add(currentNode.currentState[0])
        if currentNode.currentState[0] not in closedSet:
            closedSet.add(currentNode.currentState[0])
            for successors in problem.getSuccessors(currentNode.currentState[0]):
            #print("Successor: ",successors)
            #if successors[0] not in closedSet:
                #closedSet.add(successors[0])
                #print(closedSet)
                newNode=searchNode.searchNode(successors,currentNode)
                fringe.push(newNode,newNode.currentCost)
        #raw_input("Press Enter to continue...")
    return  currentNode.GetDirections()

def AStarSearch(problem, heuristic):
    from game import Directions
    import util
    import searchNode

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    closedSet=set()
    fringe=util.PriorityQueue()
    node= searchNode.searchNode(tuple([problem.getStartState(),"START",0]),None,heuristic(problem.getStartState(),problem))
    fringe.push(node,node.AStarCost())
    foundGoal=False

    while not foundGoal:
        currentNode=fringe.pop()
        if(problem.isGoalState(currentNode.currentState[0])):
            foundGoal=True
            print('goal!!!!')
            break
        #print("Current: ",currentNode.currentState)
        #print ("umm successors: ", problem.getSuccessors(currentNode.currentState[0]))
        #closedSet.add(currentNode.currentState[0])
        if currentNode.currentState[0] not in closedSet:
            closedSet.add(currentNode.currentState[0])
            for successors in problem.getSuccessors(currentNode.currentState[0]):
            #print("Successor: ",successors)
            #if successors[0] not in closedSet:
                #closedSet.add(successors[0])
                #print(closedSet)
                newNode=searchNode.searchNode(successors,currentNode,heuristic(successors[0],problem))
                fringe.push(newNode,newNode.AStarCost())
        #raw_input("Press Enter to continue...")
    return  currentNode.GetDirections()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
