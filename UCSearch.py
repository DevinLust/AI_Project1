# heapq for priority queue
import heapq

goalState = [False, False, False, False, False]  # A, B, C, D, P
POWER_INDEX = 4


class Node:

    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost


def UniformCost(initialState, goalState):
    node = Node(state=initialState, parent=None, cost=0)

    heap = []
    heapq.heappush(heap, (node.cost, node))
    smallest_item = heapq.heappop(heap)

    explored = []


def succ(initialState):

    numFlips = 0

    powerLocation = goalState[POWER_INDEX]
    # for i in range(len(goalState)):


print("hello")