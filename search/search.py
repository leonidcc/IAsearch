# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def search(problem, fringe):
    initial_state = problem.getStartState()
    initial_actions = []
    initial_candidate = (initial_state, initial_actions)
    fringe.push(initial_candidate)
    closed_set = set()
    while not fringe.isEmpty():
        candidate = fringe.pop()
        state, actions = candidate
        if problem.isGoalState(state):
            return actions
        if state not in closed_set:
            closed_set.add(state)
            candidate_successors = problem.getSuccessors(state)
            candidate_successors = filter(lambda x: x[0] not in closed_set, candidate_successors)
            candidate_successors = map(lambda x: (x[0], actions + [x[1]]), candidate_successors)
            for candidate in candidate_successors:
                fringe.push(candidate)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    return generalSearch(problem, util.Stack())

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    return generalSearch(problem, util.Queue())

def uniformCostSearch(problem):
    "Search the node of least total cost first."
    return generalInformedSearch(problem, util.PriorityQueue(), nullHeuristic)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    return generalInformedSearch(problem, util.PriorityQueue(), heuristic)

def generalSearch(problem, expanded):
    visited = []
    path = []
    expanded.push((problem.getStartState(), path ))
    while not expanded.isEmpty():
        (state, path) = expanded.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited += [state]
            for (successor, motion, _) in problem.getSuccessors(state):
                expanded.push((successor, path + [motion]))

def generalInformedSearch(problem, expanded, heuristic):
    visited = []
    expanded.push((problem.getStartState(), [], 0), 0)
    while not expanded.isEmpty():
        (state, path, cost) = expanded.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited += [state]
            for (successor, direction, nextCost) in problem.getSuccessors(state):
                f = cost + nextCost + heuristic(successor, problem)
                expanded.push((successor, path + [direction], cost + nextCost), f)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch






# ignorar

    # expand = []
    # depthFirstSearchAux( problem.getStartState(), problem, [], expand)
    # return expand
    # return generalSearch(problem, util.Stack(), 0)



# def depthFirstSearchAux( state, problem, visited, expand):
#     if(problem.isGoalState( state )):
#         return True
#     find = False
#     visited+=[state]
#     sus = filter( lambda e: e[0] not in visited , problem.getSuccessors(state))
#     if( sus != []):
#         for s in sus:
#                 expand += [s[1]]
#                 find = depthFirstSearchAux( s[0], problem, visited,expand )
#                 if(find):
#                     return True
#     if(not find):
#         expand.pop()


#     solve = []
#     breadthFirstSearchAux(problem, problem.getSuccessors(problem.getStartState()), [problem.getStartState()],solve)
#     print(solve)
#     return []
#
# def breadthFirstSearchAux(problem, levelNodes,visited,solve):
#     print("level",levelNodes)
#     levelSigNodes = []
#     for node in levelNodes:
#         visited+=[node[0]]
#         solve+=[node]
#         if(problem.isGoalState(node[0])):
#             # print("GANE", padre)
#             return True
#         levelSigNodes += filter( lambda e: e[0] not in visited , problem.getSuccessors(node[0]))
#     # print("level2", levelSigNodes)
#     # print(levelSigNodes,visited)
#
#     return breadthFirstSearchAux(problem, levelSigNodes,visited,solve)
