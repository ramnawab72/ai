import sys

romania_map = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}, 'Zerind': {'Arad': 75, 'Oradea': 71},
               'Timisoara': {'Arad': 118, 'Lugoj': 111}, 'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
               'Oradea': {'Zerind': 71, 'Sibiu': 151}, 'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
               'Fagaras': {'Sibiu': 99, 'Bucharest': 211}, 'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
               'Mehadia': {'Lugoj': 70, 'Drobeta': 75}, 'Drobeta': {'Mehadia': 75, 'Craiova': 120},
               'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
               'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
               'Bucharest': {'Fagaras': 211, 'Pitesti': 101}}

heuristics = {'Arad': 366, 'Zerind': 374, 'Timisoara': 329, 'Sibiu': 253, 'Oradea': 380, 'Lugoj': 244,
               'Fagaras': 176, 'Rimnicu Vilcea': 193, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
               'Pitesti': 100, 'Bucharest': 0}


def rbfs_search(start, goal, path, f_limit):
    if start == goal:
        return path
    successors = sorted(romania_map[start], key=lambda x: romania_map[start][x] + heuristics[x])
    for city in successors:
        new_path, f_value = path + [city], romania_map[start][city] + heuristics[city]
        if f_value <= f_limit:
            result = rbfs_search(city, goal, new_path, min(f_limit, f_value))
            if result:
                return result
    return None

def recursive_best_first_search(start, goal):
    f_limit, path = sys.maxsize, [start]
    while True:
        result = rbfs_search(start, goal, path, f_limit)
        if result:
            return result
        f_limit = sys.maxsize

start_city, goal_city, path = 'Arad', 'Bucharest', recursive_best_first_search('Arad', 'Bucharest')
print(f"Path: {path}\nCost: {sum(romania_map[path[i]][path[i + 1]] for i in range(len(path) - 1))}" if path else "Path not found!")
