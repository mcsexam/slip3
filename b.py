def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []  # Initialize visited as an empty list
    visited.append(start)
    print(start, end=" ")
    
    if start == goal:
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 5, 7],
    5: [2, 4, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

start_node = 2
goal_node = 7

print("Depth First Search Traversal:")
found = dfs(graph, start_node, goal_node)
if found:
    print("\nGoal node", goal_node, "found!")
else:
    print("\nGoal node", goal_node, "not found.")
