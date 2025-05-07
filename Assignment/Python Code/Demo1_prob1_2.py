from collections import deque

def get_unique_edge_lengths(graph):
    edge_lengths = set()
    for u in graph:
        for v, length in graph[u]:
            edge_lengths.add(length)
    return sorted(edge_lengths)

def is_feasible_route(graph, s, t, L):
    # Create subgraph G_L with edges <= L
    G_L = {v: [] for v in graph}
    for u in graph:
        for v, length in graph[u]:
            if length <= L:
                G_L[u].append((v, length))
                G_L[v].append((u, length))
    
    # BFS to check reachability and track the path
    queue = deque([(s, [s])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == t:
            return True, path
        if current not in visited:
            visited.add(current)
            for neighbor, _ in G_L[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return False, []

def minimum_fuel_capacity_with_route(graph, s, t):
    # Step 1: Extract and sort unique edge lengths
    edge_lengths = get_unique_edge_lengths(graph)
    
    # Step 2: Binary search over the sorted edge lengths
    low, high = 0, len(edge_lengths) - 1
    final_path = []
    while low < high:
        mid = (low + high) // 2
        feasible, path = is_feasible_route(graph, s, t, edge_lengths[mid])
        if feasible:
            high = mid
            final_path = path
        else:
            low = mid + 1
    
    # Final check to confirm the route for the last value of low
    feasible, path = is_feasible_route(graph, s, t, edge_lengths[low])
    if feasible:
        final_path = path
    
    return edge_lengths[low], final_path

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list where each edge has a length
    graph = {
        'A': [('B', 14), ('C', 12)],
        'B': [('A', 14), ('C', 11), ('D', 15)],
        'C': [('A', 12), ('B', 11), ('D', 18), ('E', 10)],
        'D': [('B', 15), ('C', 18), ('E', 12)],
        'E': [('C', 10), ('D', 12)]
    }
    s = 'B'
    t = 'A'
    
    # Determine the minimum fuel capacity required to travel from s to t
    min_capacity, route = minimum_fuel_capacity_with_route(graph, s, t)
    print(f"The minimum fuel tank capacity needed to travel from {s} to {t} is {min_capacity} miles.")
    print(f"The route taken is: {' -> '.join(route)}")
