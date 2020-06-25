import os, math, argparse
from pathfinder import pathfinder
from models import graph as G

def main():
    # print('This is an implementation of the several pathfinding algorithms (e.g. Djikstra, A*)')
    parser = argparse.ArgumentParser(description='Simulate sending locational data to the NIMPA server.')
    parser.add_argument('algorithm', type=str, help='Name of the pathfinding algorithm to use')
    parser.add_argument('--start', nargs='+', type=int, dest='start', help='Define the start point on the 2D grid.')
    parser.add_argument('--end', nargs='+', type=int, dest='end', help='Define the end point on the 2D grid.')
    args = parser.parse_args()
    algorithm = args.algorithm
    start = tuple(args.start)
    end = tuple(args.end)
    ''' 
    Calls the pathfinder function
    Input: algorithm to use, start node, end node
    Output: Cost of the Path, List of nodes to pass through
    '''
    # initialize graph
    graph = G.Graph()
    graph.edges = {
        'A' : ['B'],
        'B' : ['A','C','D'],
        'C' : ['A'],
        'D' : ['E','A'],
        'E' : ['B'],
    }
    print(graph)

    # find the shortest path
    # parameters: algorithm, graph, start, end
    # returns the cost of the path
    # and a list of nodes that constitute the shortest path
    cost, path = pathfinder(algorithm=algorithm,start=start,end=end)
    print('cost: ', cost, 'path: ', path)
if __name__ == "__main__":
    main()