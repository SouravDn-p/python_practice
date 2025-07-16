class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self):
        self.x_move = [1, -1, 0, 0]  # Down, Up
        self.y_move = [0, 0, 1, -1]  # Right, Left
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_depth = float('inf')

    def initialize(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]

        self.N = len(graph)
        source_x, source_y = 0, 2
        goal_x, goal_y = 4, 4

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_depth)

        self.perform_dfs(graph, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal cannot be reached from the starting point")

    def print_direction(self, direction, x, y):
        directions = ["Down", "Up", "Right", "Left"]
        print(f"Moving {directions[direction]} to ({x}, {y})")

    def perform_dfs(self, graph, current_node):
        if self.found:
            return

        x, y = current_node.x, current_node.y
        graph[x][y] = 0  # Mark as visited

        for i in range(4):
            new_x = x + self.x_move[i]
            new_y = y + self.y_move[i]

            if 0 <= new_x < self.N and 0 <= new_y < self.N and graph[new_x][new_y] == 1:
                new_depth = current_node.depth + 1
                self.print_direction(i, new_x, new_y)

                if new_x == self.goal.x and new_y == self.goal.y:
                    self.found = True
                    self.goal.depth = new_depth
                    return

                child = Node(new_x, new_y, new_depth)
                self.perform_dfs(graph, child)

                if self.found:
                    return

def main():
    dfs = DFS()
    dfs.initialize()

if __name__ == "__main__":
    main()
