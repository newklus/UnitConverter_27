from entity.constants import GRID_WIDTH, MAGIC_SUM


def sum_line(grid, indices):
    return sum(grid[i] for i in indices)


def magic_line_indices():
    """4 rows + 4 cols + 2 diagonals = 10 lines (row-major 4×4)."""
    width = GRID_WIDTH
    lines = []
    for row in range(width):
        lines.append([row * width + col for col in range(width)])
    for col in range(width):
        lines.append([row * width + col for row in range(width)])
    lines.append([i * width + i for i in range(width)])
    lines.append([i * width + (width - 1 - i) for i in range(width)])
    return lines


def all_line_sums(grid):
    return [sum_line(grid, indices) for indices in magic_line_indices()]


def all_lines_match_magic_sum(grid):
    return all(line_sum == MAGIC_SUM for line_sum in all_line_sums(grid))
