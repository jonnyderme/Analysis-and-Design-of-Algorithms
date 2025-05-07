from collections import deque

def feasible_route(V, E, s, t, L):
    # Step 1: Filter the edges
    E_prime = [(u, v) for (u, v, l) in E if l <= L]
    
    # Create adjacency list for the modified graph G'
    adj = {v: [] for v in V}
    for (u, v) in E_prime:
        adj[u].append(v)
        adj[v].append(u)
    
    # Step 2: Use BFS to check connectivity from s to t
    def bfs(start, goal):
        queue = deque([start])
        visited = set()
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            if node == goal:
                return True
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
    
    return bfs(s, t)




# Define the graph
V = ['A', 'B', 'C', 'D', 'E', 'G', 'F']
E = [
    ('A', 'B', 4),
    ('A', 'C', 8),
    ('A', 'D', 7), 
    ('B', 'A', 4),
    ('B', 'E', 12),
    ('C', 'A', 8),
    ('C', 'D', 10),
    ('C', 'F', 12),
    ('D', 'A', 7), 
    ('D', 'C', 7), 
    ('D', 'E', 3),
    ('E', 'B', 12),
    ('E', 'D', 3),
    ('E', 'G', 9),
    ('F', 'C', 12),
    ('F', 'G', 5),
    ('G', 'E', 9),
    ('G', 'F', 5)

]
s = 'A'
t = 'G'
L = 5 

ret = feasible_route(V, E, s, t, L)

# # Check if there is a feasible route
if feasible_route(V, E, s, t, L):
    print(f"There is a feasible route from {s} to {t} with mileage constraint {L}.")
else:
    print(f"There is no feasible route from {s} to {t} with mileage constraint {L}.")
