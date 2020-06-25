from models import priority_queue as pq

def search(graph, start, goal):
    frontier = pq.PriorityQueue()
    frontier.put(start, 0)
    cameFrom = {}
    costSoFar = {}
    cameFrom[start] = None
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()
        # Early exit condition, optional for Djikstra
        if current == goal:
            break
        for next in graph.neighbors(current):
            newCost = costSoFar[current] + graph.cost(current, next)
            if next not in costSoFar or newCost < costSoFar[next]:
                costSoFar[next] = newCost
                priority = newCost
                frontier.put(next, priority)
                cameFrom[next] = current

    return cameFrom, costSoFar