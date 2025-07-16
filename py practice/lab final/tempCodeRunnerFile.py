# Python code to color the conflict graph for a 4x4 chessboard with queens
def get_empty_squares(board_size, queens):
    """Return list of empty squares (i, j) not occupied by queens."""
    empty = []
    for i in range(1, board_size + 1):
        for j in range(1, board_size + 1):
            if (i, j) not in queens:
                empty.append((i, j))
    return empty

def conflicts_with_queen(square, queen):
    """Return the conflicts (row, col, diag) of a square with a queen."""
    i, j = square
    r, c = queen
    conflicts = []
    # Row conflict
    if i == r:
        conflicts.append(('row', r))
    # Column conflict
    if j == c:
        conflicts.append(('col', c))
    # Main diagonal: |i - r| = |j - c|
    if abs(i - r) == abs(j - c):
        # Identify diagonal by direction and intercept
        if i - r == j - c:
            conflicts.append(('diag_main', r - c))
        if i - r == -(j - c):
            conflicts.append(('diag_anti', r + c))
    return conflicts

def build_conflict_graph(empty_squares, queens):
    """Construct conflict graph: vertices are empty squares, edges based on shared conflicts."""
    # Adjacency list for the graph
    graph = {square: set() for square in empty_squares}
    
    # For each pair of empty squares, check if they share a conflict with any queen
    for idx1, s1 in enumerate(empty_squares):
        for idx2, s2 in enumerate(empty_squares):
            if idx1 < idx2:  # Avoid self-loops and duplicate edges
                # Get conflicts for both squares
                conflicts1 = set(conflicts_with_queen(s1, q) for q in queens for c in conflicts_with_queen(s1, q))
                conflicts2 = set(conflicts_with_queen(s2, q) for q in queens for c in conflicts_with_queen(s2, q))
                # If they share any conflict, add an edge
                if conflicts1 & conflicts2:
                    graph[s1].add(s2)
                    graph[s2].add(s1)
    
    return graph

def greedy_coloring(graph, vertices):
    """Apply greedy coloring to the graph, return color assignments."""
    colors = {v: -1 for v in vertices}  # -1 means uncolored
    for v in vertices:
        # Get colors of adjacent vertices
        used_colors = set(colors[u] for u in graph[v] if colors[u] != -1)
        # Assign smallest non-negative integer not in used_colors
        color = 0
        while color in used_colors:
            color += 1
        colors[v] = color
    return colors

def main():
    # Demo input: 4x4 chessboard with queens at (1, 2) and (2, 4)
    board_size = 4
    queens = [(1, 2), (2, 4)]
    
    # Step 1: Get empty squares
    empty_squares = get_empty_squares(board_size, queens)
    print("Empty squares:", empty_squares)
    
    # Step 2: Build conflict graph
    conflict_graph = build_conflict_graph(empty_squares, queens)
    print("\nConflict graph (adjacency list):")
    for v, neighbors in conflict_graph.items():
        print(f"{v}: {neighbors}")
    
    # Step 3: Color the conflict graph
    colors = greedy_coloring(conflict_graph, empty_squares)
    
    # Step 4: Output the coloring
    print("\nColor assignments:")
    for square in empty_squares:
        print(f"Square {square}: Color {colors[square]}")
    print(f"Number of colors used: {max(colors.values()) + 1}")

if __name__ == "__main__":
    main()