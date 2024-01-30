# heapq for priority queue
import heapq

GOAL_STATE = [True, True, True, True, True]  # A, B, C, D, P
POWER_INDEX = 4 # Index of the power supply


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
print(succ([False, False, False, False, False]))