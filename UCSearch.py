# heapq for priority queue
import heapq

GOAL_STATE = [True, True, True, True, True]  # A, B, C, D, P
POWER_INDEX = 4  # Index of the power supply

TIMES = {"0": 1, "1": 2, "2": 5, "3": 10}


class Node:

    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def to_String(self):
        return "state: " + str(self.state) + ", cost: " + str(self.cost)

# return the index of a node that has the same state as child, -1 otherwise


def repeatState(heap, child):
    for i in range(len(heap)):
        if heap[i].state == child.state:
            return i
    return -1


def UniformCost(initialState, goalState):
    node = Node(state=initialState, parent=None, cost=0)
    explored = []
    heap = []
    heapq.heappush(heap, node)
    print("Heap: " + str(heap))  # debug print
    while (len(heap) > 0):
        smallest_item = heapq.heappop(heap)  # the heap stores nodes
        print("Expanded Node: " + smallest_item.to_String())  # debug print
        if (smallest_item.state == goalState):
            return smallest_item
        explored.append(smallest_item)
        successors = succ(smallest_item.state)
        for nextState in successors:
            child = Node(state=nextState, parent=smallest_item,
                         cost=smallest_item.cost + 1)
            repeatIdx = repeatState(heap, child)
            if (not (repeatIdx != -1 or child in explored)):
                heapq.heappush(heap, child)
            elif (repeatIdx != -1 and heap[repeatIdx].cost > child.cost):
                del heap[repeatIdx]
                heapq.heapify(heap)
                heapq.heappush(heap, child)

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


UniformCost([False, False, False, False, False], GOAL_STATE)
