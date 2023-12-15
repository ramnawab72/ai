romania_graph = {'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
                 'Zerind': [('Arad', 75), ('Oradea', 71)],
                 'Timisoara': [('Arad', 118), ('Lugoj', 111)],
                 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
                 'Oradea': [('Zerind', 71), ('Sibiu', 151)],
                 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
                 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
                 'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
                 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
                 'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
                 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
                 'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
                 'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]}


heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Fagaras': 178,
             'Lugoj': 244, 'Mehadia': 241, 'Oradea': 380, 'Pitesti': 98, 'Rimnicu Vilcea': 193,
             'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374}

def a_star(start, goal):
    open_set, came_from, g_score = [(0, start)], {}, {city: float('inf') for city in romania_graph}
    g_score[start] = 0

    while open_set:
        current_cost, current_city = min(open_set)
        open_set.remove((current_cost, current_city))

        if current_city == goal:
            path = []
            while current_city in came_from:
                path.append(current_city)
                current_city = came_from[current_city]
            path.append(start)
            return path[::-1]

        for neighbor, cost in romania_graph[current_city]:
            tentative_g_score = g_score[current_city] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_city
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.append((f_score, neighbor))

    return None  

start_city, goal_city = 'Arad', 'Bucharest'
path = a_star(start_city, goal_city)
print(f"Optimal Path: {path}" if path else "Path not found!")
