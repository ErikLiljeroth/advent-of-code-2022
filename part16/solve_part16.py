import re
from collections import defaultdict
from math import inf as INFINITY
from itertools import product, combinations

def score(flow_rates, chosen_valves):
    """Find the score using the formula in the assignment based on flow rate and time left

    Args:
        flow_rates (dict[str:int]): the flow rates for different valves
        chosen_valves (dict[str:int]): the valves that were chosen to be opened (key) and the time open (val)

    Returns:
        int: the resulting score
    """
    result = 0
    for valve, time_left in chosen_valves.items():
        result += flow_rates[valve] * time_left
    return result

def floyd_warshall(graph):
    """Floyd-Warshall algorithm for finding distances between vertices in a graph

    Args:
        graph (dict[str:list[str]]): a graph showing the connections from a vertex to other vertices

    Returns:
        dict[str:dict[str:int]]: a dictionary consisting of the distance from a vertex to all other vertices
    """
    # Floyd-Warshall algorithm
    # returns distance[Dict[Dict]]
    # distance['AA']['BB'] -> minimum distance from valve AA to BB
    distance = defaultdict(lambda:defaultdict(lambda: INFINITY))
    for cur_node, nodes in graph.items():
        distance[cur_node][cur_node] = 0

        for node in nodes:
            distance[cur_node][node] = 1
            distance[node][node] = 0

    for a,b,c in product(graph, graph, graph):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]
        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance

def solutions(distance, valves, time = 30, cur = 'AA', chosen = {}):
    """Recursive function to find all possible ways to open valves within the time limit.
    Only valves where the flow is >0 are of interest.

    Args:
        distance ([str:dict[str:int]]]): a dictionary consitsting of the distance from a vertex to all other vertices
        valves (list[str]): a list of the valves where the flow rate is >0
        time (int, optional): The time remaining. Defaults to 30.
        cur (str, optional): The current valve. Defaults to 'AA'.
        chosen (dict, optional): the valves that have currently been chosen. Defaults to {}.

    Yields:
        iterator: returns an iterator over the different solutions
    """

    # For all the valves we can currently choose:
    for nxt in valves:
        # 1 min plus to open the valve
        new_time = time - (distance[cur][nxt] + 1)
        # Stop condition for recursion - out of budget
        if new_time <= 0:
            continue
        # dict union
        new_chosen = {**chosen, **{nxt:new_time}}
        # remove nxt from set of valves
        new_valves = valves - {nxt}
        yield from solutions(distance, new_valves, new_time, nxt, new_chosen)
    yield chosen

def main():
    filename = 'input.txt'
    with open(filename, 'r+') as f:
        lines = f.readlines()
    lines = [re.split('[\\s=;,]+', x.strip()) for x in lines]
    graph = {line[1]:line[10:] for line in lines}
    flows = {line[1]:int(line[5]) for line in lines if int(line[5]) != 0} # flows exluding valves with flow 0
    valves = set(flows.keys()) # only visit valves that have flow > 0

    # Part I
    distance = floyd_warshall(graph)
    best = 0
    for choice in solutions(distance, valves):
        cur = score(flows, choice)
        if cur > best:
            best = cur
    print('Answer Part I:',best)

    # Part II
    maxscore = defaultdict(int)
    choices = list(solutions(distance, valves, time = 26))

    for choice in choices:
        k = frozenset(choice)
        s = score(flows, choice)

        if s > maxscore[k]:
            maxscore[k] = s
    best = max(v1+v2 for k1, v1 in maxscore.items() for k2, v2 in maxscore.items() if not k1 & k2)
    print('Answer part II:', best)


if __name__ == '__main__':
    main()