from search_algorithms import a_star
from search_algorithms import breadth_first 
from search_algorithms import djikstra

def pathfinder(algorithm='a_star', start=None, end=None):
    path = []
    cost = 0
    graph = [] # placeholder data structure
    if (algorithm == 'a_star'):
        a_star.search(graph, start) 
    elif (algorithm == 'breadth_first'):
        breadth_first.search(graph, start)
    elif (algorithm == 'djikstra'):
        djikstra.search(graph, start)
    else:
        print("No implementation of search algorithm")
    # print(algorithm, start, end) 
    return (cost, path)