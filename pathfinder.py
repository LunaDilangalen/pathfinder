from search_algorithms import a_star
from search_algorithms import breadth_first 
from search_algorithms import djikstra

def pathfinder(algorithm='a_star', graph=None, start=None, end=None):
    path = []
    cost = 0
    if (algorithm == 'a_star'):
        a_star.search(graph, start) 
    elif (algorithm == 'breadth_first'):
        breadth_first.search(graph, start)
        # breadth_first.search(graph, start='A')
    elif (algorithm == 'djikstra'):
        djikstra.search(graph, start)
    else:
        print("No implementation of search algorithm")
    return (cost, path)