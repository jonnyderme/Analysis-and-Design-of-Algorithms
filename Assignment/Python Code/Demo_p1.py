from collections import deque, defaultdict

def feasible_route_exists(graph, start, goal, L):
    V, E = graph
    E_prime = [(u, v) for (u, v, l_e) in E if l_e <= L]
    
    # Build adjacency list for the filtered graph
    adj_list = defaultdict(list)
    for (u, v) in E_prime:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # BFS to check if there's a path from start to goal
    def bfs(start, goal):
        queue = deque([start])
        visited = set([start])
        
        while queue:
            current = queue.popleft()
            if current == goal:
                return True
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    return bfs(start, goal)

# Example usage
V = ['A', 'B', 'C', 'D', 'E']
E = [
    ('A', 'B', 4),
    ('A', 'C', 17),
    ('B', 'C', 3),
    ('B', 'D', 7),
    ('C', 'D', 5),
    ('C', 'E', 10),
    ('D', 'E', 1)
]
graph = (V, E)
start = 'Β'
goal = 'E'
L = 8

if feasible_route_exists(graph, start, goal, L):
    print("There is a feasible route from", start, "to", goal)
else:
    print("There is no feasible route from", start, "to", goal)

