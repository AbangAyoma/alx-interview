#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    
    Args:
    grid (list of list of int): 2D grid representation of the island and water.
    
    Returns:
    int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 edges for a land cell
                perimeter += 4
                
                # Subtract edges shared with adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
