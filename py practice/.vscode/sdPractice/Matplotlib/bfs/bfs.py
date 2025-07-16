from collections import deque

def bfs(graph, start):
    # Set to keep track of visited nodes
    visited = set()
    # Queue for BFS
    queue = deque([start])
    # Mark the starting node as visited
    visited.add(start)
    
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex, end=' ')  # Process the vertex (here we just print it)
        
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # If not visited, mark it as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("BFS starting from vertex 'A':")
    bfs(graph, 'A')