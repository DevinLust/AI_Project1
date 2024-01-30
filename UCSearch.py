# heapq for priority queue
import heapq

GOAL_STATE = [True, True, True, True, True]  # A, B, C, D, P
POWER_INDEX = 4 # Index of the power supply


class Node:

    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

# return the index of a node that has the same state as child, -1 otherwise
def repeatState(heap, child):
    for i in range(len(heap)):
        if heap[i][1].state == child.state:
            return i
    return -1

def UniformCost(initialState, goalState):
    node = Node(state=initialState, parent=None, cost=0)
    explored = []
    heap = []
    heapq.heappush(heap, (node.cost, node))
    while (len(heap) > 0):
        smallest_item = heapq.heappop(heap)
        if (smallest_item[1].state == goalState):
            return smallest_item[1]
        explored.append(smallest_item[1])
        print(smallest_item)
        successors = succ(smallest_item[1].state)
        for nextState in successors:
            child = Node(state=nextState, parent=smallest_item[1], cost=smallest_item[0] + 1)
            if (not (child in heap or child in explored)):
                heapq.heappush(heap, (child.cost, child))
            repeatIdx = repeatState(heap, child)
            if (repeatIdx != -1 and heap[repeatIdx][1].cost > child.cost):
                del heap[repeatIdx]
                heapq.heapify(heap)
                heapq.heappush(heap, (child.cost, child))

    return False


# Provides all next possible states from a current initialState as a list of states
def succ(initialState):
    numFlips = 0
    result = []

    powerLocation = initialState[POWER_INDEX]
    for i in range(POWER_INDEX):
        if (initialState[i] == powerLocation):
            # handles the cases a single robot crosses
            potentialState = initialState.copy()
            potentialState[i] = not potentialState[i]
            potentialState[POWER_INDEX] = not potentialState[POWER_INDEX]
            result.append(potentialState)
            for j in range(i + 1, POWER_INDEX):
                if (initialState[j] == powerLocation):
                    # handles the cases in which pairs cross
                    potentialState = initialState.copy()
                    potentialState[i] = not potentialState[i] 
                    potentialState[j] = not potentialState[j]
                    potentialState[POWER_INDEX] = not potentialState[POWER_INDEX]
                    result.append(potentialState)

    return result


print("hello")
UniformCost([False, False, False, False, False], GOAL_STATE)