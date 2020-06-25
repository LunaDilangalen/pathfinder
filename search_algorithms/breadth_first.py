from models import queue
def search(graph, start):
    # print("TO DO: implement Breadth-First search")
    frontier = queue.Queue()
    frontier.put(start)
    cameFrom = {}
    cameFrom[start] = None

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %s" % str(current))
        for next in graph.neighbors(current):
            if next not in cameFrom:
                frontier.put(next)
                cameFrom[next] = True