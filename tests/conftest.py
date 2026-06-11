import pytest


@pytest.fixture
def grid_g1():
    """4×4 row-major, two blanks (0)."""
    return [
        16, 3, 2, 13,
        5, 0, 11, 8,
        9, 6, 7, 12,
        4, 15, 14, 0,
    ]
