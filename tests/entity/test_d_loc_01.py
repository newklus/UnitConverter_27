import random

from entity.constants import GRID_SIZE, GRID_WIDTH
from entity.locate import locate_value


def test_d_loc_01_random_number_input(grid_g1):
    # Given — 랜덤숫자입력; grid_g1 row-major 4×4, 비빈칸(0)에서 샘플
    assert len(grid_g1) == GRID_SIZE
    non_blank = [v for v in grid_g1 if v != 0]
    random.seed(0)
    user_input = random.choice(non_blank)
    expected_index = grid_g1.index(user_input)
    expected_row = expected_index // GRID_WIDTH
    expected_col = expected_index % GRID_WIDTH

    # When — grid에서 user_input 위치(row-major)
    result = locate_value(grid_g1, user_input)

    # Then
    assert result == {"row": expected_row, "col": expected_col}
