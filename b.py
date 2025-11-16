graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 7],
    5: [2, 6, 7],
    6: [5, 7],
    7: [4, 5, 6]
}

def dfs(graph, current, goal, visited):
    print(current, end=" ")
    if current == goal:
        return True

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False

def main():
    start = 2
    goal = 7
    visited = set()

    print("DFS Traversal Path:")
    found = dfs(graph, start, goal, visited)

    if found:
        print("\nGoal node", goal, "found!")
    else:
        print("\nGoal node not found.")

if __name__ == "__main__":
    main()
