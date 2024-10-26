from collections import deque

# Graph representation using adjacency list
cities = {
    'Islamabad': ['Rawalpindi', 'Lahore', 'Peshawar'],
    'Rawalpindi': ['Islamabad', 'Peshawar', 'Quetta'],
    'Peshawar': ['Islamabad', 'Rawalpindi', 'Quetta'],
    'Lahore': ['Islamabad', 'Multan', 'Quetta'],
    'Multan': ['Lahore', 'Karachi', 'Quetta'],
    'Quetta': ['Rawalpindi', 'Peshawar', 'Multan', 'Karachi'],
    'Karachi': ['Multan', 'Quetta']
}


# Function to perform BFS and find the shortest path
def bfs_shortest_path(graph, start, goal):
    # Create a queue for BFS and a dictionary to store paths
    queue = deque([[start]])
    visited = set()

    # Perform BFS
    while queue:
        path = queue.popleft()
        city = path[-1]

        # If the goal is reached, return the path
        if city == goal:
            return path
