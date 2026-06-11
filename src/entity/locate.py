from entity.constants import GRID_WIDTH


def locate_value(grid, value):
    for index, cell in enumerate(grid):
        if cell == value:
            return {"row": index // GRID_WIDTH, "col": index % GRID_WIDTH}
    return {"row": None, "col": None}
