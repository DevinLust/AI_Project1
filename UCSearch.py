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
        notCrossed = ""
        crossed = ""
        for i in range(len(self.state)):
            if (self.state[i] == True):
                match i:
                    case 0:
                        crossed = crossed + "A"
                    case 1:
                        crossed = crossed + "B"
                    case 2:
                        crossed = crossed + "C"
                    case 3:
                        crossed = crossed + "D"
                    case 4:
                        crossed = crossed + "P"
                    case _:
                        print("Good people don\'t end up here")
            else:
                match i:
                    case 0:
                        notCrossed = notCrossed + "A"
                    case 1:
                        notCrossed = notCrossed + "B"
                    case 2:
                        notCrossed = notCrossed + "C"
                    case 3:
                        notCrossed = notCrossed + "D"
                    case 4:
                        notCrossed = notCrossed + "P"
                    case _:
                        print("Good people don\'t end up here")
        return "state: [not crossed: (" + notCrossed + "), crossed: (" + crossed + ")], cost: " + str(self.cost)

# return the index of a node that has the same state as child, -1 otherwise


def repeatState(heap, child):
    for i in range(len(heap)):
        if heap[i].state == child.state:
            return i
    return -1


def UniformCost(initialState, goalState):
    nodeCount = 0
    node = Node(state=initialState, parent=None, cost=0)
    explored = []
    heap = []
    heapq.heappush(heap, node)
    print("Heap: " + str(heap))  # debug print

    solution = None
    while (len(heap) > 0 and not solution):
        smallest_item = heapq.heappop(heap)  # the heap stores nodes
        print("Expanded Node: " + smallest_item.to_String())  # debug print
        nodeCount += 1
        if (smallest_item.state == goalState):
            solution = smallest_item
            continue
        explored.append(smallest_item)
        successors = succ(smallest_item)
        for child in successors:
            repeatIdx = repeatState(heap, child)
            repeatExplored = repeatState(explored, child)
            if (repeatIdx == -1 and repeatExplored == -1):
                heapq.heappush(heap, child)
            elif (repeatIdx != -1 and heap[repeatIdx].cost > child.cost):
                del heap[repeatIdx]
                heapq.heapify(heap)
                heapq.heappush(heap, child)

    return solution, nodeCount


# Provides all next possible states from a current initialState as a list of states
def succ(initialNode):
    numFlips = 0
    result = []

    powerLocation = initialNode.state[POWER_INDEX]
    for i in range(POWER_INDEX):
        if (initialNode.state[i] == powerLocation):
            # handles the cases a single robot crosses
            potentialState = initialNode.state.copy()
            potentialState[i] = not potentialState[i]
            potentialState[POWER_INDEX] = not potentialState[POWER_INDEX]
            node = Node(state=potentialState, parent=initialNode,
                        cost=TIMES[str(i)] + initialNode.cost)
            result.append(node)
            for j in range(i + 1, POWER_INDEX):
                if (initialNode.state[j] == powerLocation):
                    # handles the cases in which pairs cross
                    potentialState = initialNode.state.copy()
                    potentialState[i] = not potentialState[i]
                    potentialState[j] = not potentialState[j]
                    potentialState[POWER_INDEX] = not potentialState[POWER_INDEX]
                    node = Node(state=potentialState, parent=initialNode,
                                cost=max(TIMES[str(i)], TIMES[str(j)]) + initialNode.cost)
                    result.append(node)

    return result


def printSolutionPath(solution):
    if (solution != None):
        printSolutionPath(solution.parent)
        print(solution.to_String())
    else:
        print("Solution:")


solution, nodeCount = UniformCost(
    [False, False, False, False, False], GOAL_STATE)
if (solution != None):
    printSolutionPath(solution)
else:
    print("No solution")

print("Nodes expanded: " + str(nodeCount))
