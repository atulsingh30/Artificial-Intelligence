import heapq

# A function to calculate the heuristic distance between two nodes (using Euclidean distance)
def heuristic(node1, node2):
    return ((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2) ** 0.5

# A function to reconstruct the path from the start node to the goal node
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# A function to perform A* search
def astar_search(graph, start, goal):
    frontier = [(0, start)]  # (f-score, node)
    came_from = {}  # A dictionary to store the parent of each visited node
    g_score = {start: 0}  # A dictionary to store the cost of the cheapest path to each visited node
    f_score = {start: heuristic(start, goal)}  # A dictionary to store the estimated total cost of the cheapest path to each visited node

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(frontier, (f_score[neighbor], neighbor))
    return None

# Getting the input from the user
n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(n):
    node = tuple(map(int, input(f"Enter the coordinates of node {i}: ").split()))
    graph[node] = []
m = int(input("Enter the number of edges: "))
for i in range(m):
    node1, node2 = tuple(map(int, input(f"Enter the indices of nodes for edge {i}: ").split()))
    graph[list(graph.keys())[node1]].append(list(graph.keys())[node2])
    graph[list(graph.keys())[node2]].append(list(graph.keys())[node1])
start = tuple(map(int, input("Enter the coordinates of the start node: ").split()))
goal = tuple(map(int, input("Enter the coordinates of the goal node: ").split()))

# Running A* search on the input graph
path = astar_search(graph, start, goal)

# Printing the result
if path:
    print("The path found by A* search is:")
    for node in path:
        print(node)
else:
    print("No path found by A* search.")